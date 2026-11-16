#!/usr/bin/env python3
"""petclip: get a viral pet TikTok / Reels clip ready to remake with your own dog or cat.

Give it a link (or a video file) and it will:
  1. download the original clip (yt-dlp: TikTok, Instagram Reels, YouTube Shorts, Facebook, X and more)
  2. find every camera cut (ffmpeg scene detection)
  3. pick the best 6-second window (one that starts and ends on a cut, so it loops cleanly)
  4. crop it to 9:16 at 720p and export the original sound as MP3
  5. save a contact sheet (one frame every half second) and a shot list

It also checks pet photos before you upload them anywhere (size, format, blur).

Needs ffmpeg / ffprobe on PATH, and yt-dlp if you pass a URL. Python standard library only.

  python3 petclip.py prep "https://www.tiktok.com/@user/video/123" --out kittens
  python3 petclip.py prep my_clip.mp4 --window 6 --start 9 --out its-my-life
  python3 petclip.py cuts my_clip.mp4                 # only print the shot list
  python3 petclip.py windows my_clip.mp4 --length 6   # the best 6 s windows to cut
  python3 petclip.py frames my_clip.mp4               # one still per shot
  python3 petclip.py photo biscuit.jpg luna.png       # are these pet photos good enough?
  python3 petclip.py match original.mp4 repost.mp4    # same sound? at what offset?

Made by MyPetDance (https://mypetdance.com). MIT license.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import shutil
import subprocess
import sys

RATIOS = {"9:16": (9, 16), "16:9": (16, 9), "1:1": (1, 1), "4:5": (4, 5), "3:4": (3, 4)}


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, text=True, capture_output=True, **kw)


def need(tool: str) -> None:
    if not shutil.which(tool):
        sys.exit(f"petclip: '{tool}' not found. Install it first (macOS: brew install {tool}).")


def probe(path: str) -> dict:
    out = run(["ffprobe", "-v", "error", "-show_entries",
               "stream=codec_type,codec_name,width,height,r_frame_rate:format=duration,format_name", "-of", "json", path]).stdout
    data = json.loads(out)
    video = next((s for s in data["streams"] if s["codec_type"] == "video"), None)
    if not video:
        sys.exit(f"petclip: no video or image in {path}")
    num, den = (video.get("r_frame_rate") or "30/1").split("/")
    return {
        "width": int(video["width"]),
        "height": int(video["height"]),
        "fps": round(int(num) / max(int(den), 1), 2),
        "duration": round(float(data["format"].get("duration") or 0), 2),
        "has_audio": any(s["codec_type"] == "audio" for s in data["streams"]),
        "codec": video.get("codec_name", ""),
    }


def download(url: str, out_dir: str, cookies_from: str | None, cookies_file: str | None = None) -> str:
    need("yt-dlp")
    target = os.path.join(out_dir, "original.%(ext)s")
    # best picture first, preferring H.264 + AAC so every editor opens it; merged into one MP4
    cmd = ["yt-dlp", "-q", "--no-playlist", "-f", "bv*+ba/b", "-S", "res,vcodec:h264,acodec:m4a",
           "--merge-output-format", "mp4", "-o", target, url]
    if cookies_from:
        cmd[1:1] = ["--cookies-from-browser", cookies_from]
    if cookies_file:
        cmd[1:1] = ["--cookies", cookies_file]
    try:
        run(cmd)
    except subprocess.CalledProcessError as e:
        hint = "" if cookies_from or cookies_file else (
            "\nSome posts need a logged-in browser (Instagram often does, private or age-gated posts too): "
            "add --cookies-from-browser chrome (or firefox / safari / edge)")
        sys.exit(f"petclip: download failed.\n{e.stderr.strip()}{hint}")
    for name in os.listdir(out_dir):
        if name.startswith("original."):
            return os.path.join(out_dir, name)
    sys.exit("petclip: yt-dlp finished but no file was written")


def find_cuts(path: str, threshold: float) -> list[float]:
    """Times (seconds) where the picture changes enough to count as a camera cut."""
    proc = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-vf", f"select='gt(scene,{threshold})',showinfo",
                           "-an", "-f", "null", "-"], text=True, capture_output=True)
    times = [float(t) for t in re.findall(r"pts_time:([0-9.]+)", proc.stderr)]
    cuts: list[float] = []
    for t in times:  # drop flashes that fire twice within half a second
        if not cuts or t - cuts[-1] > 0.5:
            cuts.append(round(t, 2))
    return cuts


def shot_list(cuts: list[float], duration: float) -> list[dict]:
    edges = [0.0] + [c for c in cuts if 0 < c < duration] + [duration]
    return [{"shot": i + 1, "start": round(a, 2), "end": round(b, 2), "length": round(b - a, 2)}
            for i, (a, b) in enumerate(zip(edges, edges[1:]))]


def describe_window(start: float, end: float, cuts: list[float]) -> dict:
    """A window of the clip: how many shots it has, and whether it starts or ends on a sliver of a shot.

    A pet clip that ends less than a second into a new shot (or opens on the last frames of the previous one)
    looks like a mistake. Ending in the middle of one long take is fine.
    """
    inner = [c for c in cuts if start + 0.05 < c < end - 0.05]
    problems = []
    if inner:
        head, tail = inner[0] - start, end - inner[-1]
        if head < 1:
            problems.append(f"opens with only {head:.2f} s of the shot before the cut at {inner[0]} s")
        if tail < 1:
            problems.append(f"ends {tail:.2f} s into the shot that starts at {inner[-1]} s")
    return {"start": round(start, 2), "end": round(end, 2), "shots": len(inner) + 1, "problems": problems}


def best_windows(cuts: list[float], duration: float, length: float, top: int = 3) -> list[dict]:
    """Windows of `length` seconds that start or end on a cut (or the clip's start / end), cleanest first.

    Clean = no sliver of a shot at either end. Among clean ones, the window that starts at 0 wins (the opening is
    usually the hook people know), then the earliest one.
    """
    if duration <= length:
        return [describe_window(0.0, duration, cuts)]
    edges = [0.0] + [c for c in cuts if 0 < c < duration] + [duration]
    seen, out = set(), []
    for e in edges:
        for start in (e, e - length):  # start on this edge, or end on it
            start = round(start, 2)
            if start < 0 or start + length > duration + 0.01 or start in seen:
                continue
            seen.add(start)
            out.append(describe_window(start, min(start + length, duration), cuts))
    out.sort(key=lambda w: (len(w["problems"]), w["start"] > 0, w["start"]))
    return out[:top]


def crop_box(w: int, h: int, ratio: tuple[int, int]) -> tuple[int, int, int, int]:
    """Largest centred crop with the target ratio. Returns (cw, ch, x, y), all even numbers."""
    rw, rh = ratio
    if w * rh > h * rw:  # source is wider than target: cut the sides
        ch, cw = h, int(h * rw / rh)
    else:  # source is taller than target: cut top and bottom
        cw, ch = w, int(w * rh / rw)
    cw, ch = cw - cw % 2, ch - ch % 2
    return cw, ch, (w - cw) // 2 // 2 * 2, (h - ch) // 2 // 2 * 2


def target_size(ratio: tuple[int, int]) -> tuple[int, int]:
    rw, rh = ratio
    if rw >= rh:  # landscape / square: 720 tall
        return int(720 * rw / rh) // 2 * 2, 720
    return 720, int(720 * rh / rw) // 2 * 2


def export(src: str, dst_mp4: str, dst_mp3: str | None, vf: str, start: float = 0, seconds: float | None = None) -> None:
    cut = (["-ss", f"{start}"] if start else []) + (["-t", f"{seconds}"] if seconds else [])
    run(["ffmpeg", "-v", "error", "-y", "-i", src] + cut + ["-vf", vf, "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", dst_mp4])
    if dst_mp3:
        run(["ffmpeg", "-v", "error", "-y", "-i", src] + cut + ["-vn", "-c:a", "libmp3lame", "-b:a", "192k", dst_mp3])


def contact_sheet(src: str, dst: str, duration: float, every: float = 0.5, cols: int = 6) -> None:
    frames = max(1, math.ceil(duration / every))
    rows = math.ceil(frames / cols)
    run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf",
         f"fps={1 / every},scale=320:-2,tile={cols}x{rows}", "-frames:v", "1", "-q:v", "3", dst])


def label(source: str) -> str:
    return source if re.match(r"https?://", source) else os.path.basename(source)


def write_report(out_dir: str, source: str, info: dict, ratio: str, cuts: list[float], window: dict | None,
                 options: list[dict]) -> None:
    shots = shot_list(cuts, info["duration"])
    with open(os.path.join(out_dir, "shots.json"), "w") as f:
        json.dump({"source": label(source), "original": info, "ratio": ratio, "cuts": cuts, "shots": shots,
                   "window": window, "window_options": options}, f, indent=2)
    lines = [f"# Shot list: {label(source)}", "",
             f"Original: {info['width']}x{info['height']}, {info['fps']} fps, {info['duration']} s, "
             f"{'with' if info['has_audio'] else 'no'} sound. Exported as {ratio} at 720p.", "",
             "| Shot | Start | End | Length |", "|---|---|---|---|"]
    lines += [f"| {s['shot']} | {s['start']} s | {s['end']} s | {s['length']} s |" for s in shots]
    if window:
        w = window
        lines += ["", f"Short version: {w['start']}–{w['end']} s ({round(w['end'] - w['start'], 2)} s, {w['shots']} shot"
                  f"{'s' if w['shots'] > 1 else ''}). "
                  + ("No sliver of a shot at either end." if not w["problems"] else
                     "It " + " and ".join(w["problems"]) + ", which looks like a mistake: try another window below.")]
        if len(options) > 1:
            lines += ["", "Other windows of the same length:", ""]
            lines += [f"- {o['start']}–{o['end']} s ({o['shots']} shot{'s' if o['shots'] > 1 else ''}"
                      + (f", {'; '.join(o['problems'])}" if o["problems"] else ", clean") + ")" for o in options if o != w]
    lines += ["", "Files: `clip.mp4` / `clip.mp3` (full length)"
              + (f", `clip-{window['end'] - window['start']:g}s.mp4` / `.mp3` (short version)" if window else "")
              + ", `sheet.jpg` (one frame every 0.5 s).",
              "", "Want your own pet in it without editing? Many pet trends are ready as templates on https://mypetdance.com "
              "(upload one photo of your dog or cat, get the clip back with your pet and the original sound)."]
    with open(os.path.join(out_dir, "SHOTS.md"), "w") as f:
        f.write("\n".join(lines) + "\n")


def cmd_prep(args: argparse.Namespace) -> None:
    need("ffmpeg"), need("ffprobe")
    os.makedirs(args.out, exist_ok=True)
    src = args.source if os.path.exists(args.source) else download(args.source, args.out, args.cookies_from_browser, args.cookies)
    info = probe(src)
    ratio = RATIOS.get(args.ratio)
    if not ratio:
        sys.exit(f"petclip: --ratio must be one of {', '.join(RATIOS)}")
    cw, ch, x, y = crop_box(info["width"], info["height"], ratio)
    if args.y_offset is not None:
        y = max(0, min(info["height"] - ch, args.y_offset)) // 2 * 2
    if args.x_offset is not None:
        x = max(0, min(info["width"] - cw, args.x_offset)) // 2 * 2
    tw, th = target_size(ratio)
    vf = f"crop={cw}:{ch}:{x}:{y},scale={tw}:{th},setsar=1"
    cuts = find_cuts(src, args.threshold)
    audio = info["has_audio"]
    export(src, os.path.join(args.out, "clip.mp4"), os.path.join(args.out, "clip.mp3") if audio else None, vf)
    window, options = None, []
    if args.window:
        options = best_windows(cuts, info["duration"], args.window)
        if args.start is not None:
            start = max(0.0, min(args.start, info["duration"] - args.window))
            window = describe_window(start, min(start + args.window, info["duration"]), cuts)
        else:
            window = options[0]
        name = f"clip-{window['end'] - window['start']:g}s"
        export(src, os.path.join(args.out, f"{name}.mp4"), os.path.join(args.out, f"{name}.mp3") if audio else None,
               vf, window["start"], round(window["end"] - window["start"], 2))
    contact_sheet(os.path.join(args.out, "clip.mp4"), os.path.join(args.out, "sheet.jpg"), info["duration"])
    write_report(args.out, args.source, info, args.ratio, cuts, window, options)
    print(f"{info['width']}x{info['height']} {info['duration']} s · {len(cuts) + 1} shot{'s' if cuts else ''} · cuts at "
          f"{', '.join(f'{c} s' for c in cuts) or 'none'}")
    if window:
        print(f"short version {window['start']}–{window['end']} s ({window['shots']} shot{'s' if window['shots'] > 1 else ''}, "
              + ("clean" if not window["problems"] else "; ".join(window["problems"])) + ")"
              + ("" if args.start is not None else ". Pick another with --start"))
    print(f"crop {cw}x{ch} at ({x},{y}) → {tw}x{th}. Look at {args.out}/sheet.jpg to check your pet's ears and tail "
          f"aren't cut off (move the crop with --x-offset / --y-offset).")
    print(f"wrote {args.out}/SHOTS.md and shots.json")


def cmd_cuts(args: argparse.Namespace) -> None:
    need("ffmpeg"), need("ffprobe")
    info = probe(args.source)
    for s in shot_list(find_cuts(args.source, args.threshold), info["duration"]):
        print(f"shot {s['shot']}: {s['start']:>6} – {s['end']:>6} s  ({s['length']} s)")


def cmd_windows(args: argparse.Namespace) -> None:
    need("ffmpeg"), need("ffprobe")
    info = probe(args.source)
    cuts = find_cuts(args.source, args.threshold)
    for w in best_windows(cuts, info["duration"], args.length, args.top):
        note = "clean" if not w["problems"] else "; ".join(w["problems"])
        print(f"{w['start']:>6} – {w['end']:>6} s  {w['shots']} shot{'s' if w['shots'] > 1 else ''}, {note}")


def cmd_frames(args: argparse.Namespace) -> None:
    """One still per shot, taken just after each cut (for image-to-video tools, thumbnails or a storyboard)."""
    need("ffmpeg"), need("ffprobe")
    info = probe(args.source)
    os.makedirs(args.out, exist_ok=True)
    for s in shot_list(find_cuts(args.source, args.threshold), info["duration"]):
        t = s["start"] + min(0.2, s["length"] / 3)  # a moment after the cut, so it isn't a blend of two shots
        dst = os.path.join(args.out, f"shot-{s['shot']:02d}.jpg")
        run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", args.source, "-frames:v", "1", "-q:v", "2", dst])
        print(f"{dst}  shot {s['shot']} at {t:.2f} s ({s['start']}–{s['end']} s)")


def softness(path: str) -> float | None:
    """How little the photo changes when we blur it a bit more (PSNR in dB, centre half of the photo, 384 px wide).

    A sharp photo has fine detail (fur, whiskers), so a light blur changes it a lot: a low number. A photo that is
    already blurry barely changes: a high number. The centre is where the pet usually is, so a blurred background
    (portrait mode) doesn't count against it.
    """
    graph = "[0:v]crop=iw/2:ih/2,scale='min(384,iw)':-2,format=gray,split[a][b];[b]gblur=sigma=1.2[bb];[a][bb]psnr"
    proc = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-filter_complex", graph, "-f", "null", "-"],
                          text=True, capture_output=True)
    m = re.findall(r"average:([0-9.]+|inf)", proc.stderr)
    return None if not m or m[-1] == "inf" else float(m[-1])


def cmd_photo(args: argparse.Namespace) -> None:
    """Check pet photos before uploading them to an AI pet video app."""
    need("ffmpeg"), need("ffprobe")
    bad = 0
    for path in args.photos:
        problems, notes = [], []
        size_mb = os.path.getsize(path) / 1_000_000
        ext = os.path.splitext(path)[1].lower()
        info = probe(path)
        w, h = info["width"], info["height"]
        if ext not in (".jpg", ".jpeg", ".png", ".webp"):
            problems.append(f"{ext or 'no extension'}: most apps want JPG, PNG or WebP (iPhone HEIC: export as JPG)")
        if size_mb > 10:
            problems.append(f"{size_mb:.1f} MB: many apps stop at 10 MB")
        if min(w, h) < 400:
            problems.append(f"{w}x{h} is small: the face will come out soft. Use the original photo, not a screenshot or a chat copy")
        elif min(w, h) < 720:
            notes.append(f"{w}x{h} is on the small side, the original from your phone is better")
        if max(w, h) > 3 * min(w, h):
            problems.append("very long and thin: crop it so your pet fills most of the frame")
        soft = softness(path)
        # 16 Nov 2026 tests on 7 sharp pet photos (600–1200 px): 28–39. The same photos with a light blur (gblur 1.5): 38–45,
        # a heavy one (gblur 4): 47–50. So it catches clearly blurry photos; a slightly soft one can still pass
        if soft is not None:
            if soft >= args.soft_limit:
                problems.append(f"looks blurry (softness {soft:.0f}, limit {args.soft_limit:g}): take a sharper one in good light")
            elif soft >= args.soft_limit - 3:
                notes.append(f"a little soft (softness {soft:.0f})")
            else:
                notes.append(f"sharp (softness {soft:.0f})")
        verdict = "check" if problems else "ok"
        bad += bool(problems)
        print(f"{verdict:5} {path}: {w}x{h}, {size_mb:.1f} MB" + ("" if not notes else " · " + "; ".join(notes)))
        for p in problems:
            print(f"      - {p}")
    print("\nThings a script can't check: one pet per photo, facing the camera, face and ears in view, no hat or costume.")
    sys.exit(1 if bad else 0)


ENV_RATE = 50  # loudness samples per second for match (one every 20 ms)
BANDS = ["lowpass=f=250", "bandpass=f=1200:width_type=o:w=2", "highpass=f=3500"]  # bass, mids (voice), highs (hats, claps)


def onset_envelopes(path: str, max_seconds: float) -> list[list[float]]:
    """For each band: how much louder each 20 ms gets than the one before. Robust to volume and voice-over level."""
    import array
    out = []
    step = 8000 // ENV_RATE
    for band in BANDS:
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-t", f"{max_seconds}", "-vn", "-ac", "1", "-af", band,
                              "-ar", "8000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
        pcm = array.array("h")
        pcm.frombytes(raw[: len(raw) // 2 * 2])
        energy = [math.log1p(sum(abs(v) for v in pcm[i:i + step]) / step) for i in range(0, len(pcm) - step + 1, step)]
        out.append([max(0.0, e - p) for p, e in zip([energy[0]] + energy, energy)] if energy else [])
    return out


def pearson(xa: list[float], xb: list[float]) -> float | None:
    n = len(xa)
    ma, mb = sum(xa) / n, sum(xb) / n
    va = sum((x - ma) ** 2 for x in xa)
    vb = sum((y - mb) ** 2 for y in xb)
    if va <= 0 or vb <= 0:
        return None
    return sum((x - ma) * (y - mb) for x, y in zip(xa, xb)) / math.sqrt(va * vb)


def correlate(a: list[list[float]], b: list[list[float]], min_overlap: int) -> tuple[float, int]:
    """Slide b against a; score = mean correlation over the bands. Returns (score, offset): b[0] lines up with a[offset]."""
    la, lb = len(a[0]), len(b[0])
    best = (-1.0, 0)
    for off in range(-(lb - min_overlap), la - min_overlap + 1):
        sa, sb = max(0, off), max(0, -off)
        n = min(la - sa, lb - sb)
        if n < min_overlap:
            continue
        rs = [pearson(ba[sa:sa + n], bb[sb:sb + n]) for ba, bb in zip(a, b)]
        rs = [r for r in rs if r is not None]
        if rs and sum(rs) / len(rs) > best[0]:
            best = (sum(rs) / len(rs), off)
    return best


def cmd_match(args: argparse.Namespace) -> None:
    """Do two videos use the same sound, and where does one start inside the other?"""
    need("ffmpeg")
    a = onset_envelopes(args.a, args.max_seconds)
    b = onset_envelopes(args.b, args.max_seconds)
    if not a[0] or not b[0]:
        sys.exit("petclip: one of the files has no sound")
    score, off = correlate(a, b, min(len(a[0]), len(b[0]), ENV_RATE * 3))
    sec = off / ENV_RATE
    verdict = "same sound" if score >= 0.65 else "maybe the same sound (check by ear)" if score >= 0.5 else "different sound"
    na, nb = os.path.basename(args.a), os.path.basename(args.b)
    if na == nb:
        na, nb = args.a, args.b
    where = f"{nb} starts {sec:.2f} s into {na}" if sec >= 0 else f"{na} starts {-sec:.2f} s into {nb}"
    print(f"{verdict}: score {score:.2f}" + (f"; {where}" if score >= 0.5 else ""))


def main() -> None:
    p = argparse.ArgumentParser(prog="petclip", description="Get a viral pet clip ready to remake: download, find cuts, "
                                "pick a clean 6 s window, crop, export the sound, check pet photos.")
    sub = p.add_subparsers(dest="cmd", required=True)
    prep = sub.add_parser("prep", help="download (or read) a clip and export everything")
    prep.add_argument("source", help="TikTok, Instagram Reels, YouTube Shorts, Facebook, X… URL, or a local video file")
    prep.add_argument("--window", type=float, default=6, help="length of the short version in seconds (default 6; 0 = none)")
    prep.add_argument("--start", type=float, help="where the short version starts (default: the cleanest window)")
    prep.add_argument("--ratio", default="9:16", help="output ratio: 9:16 (default), 16:9, 1:1, 4:5, 3:4")
    prep.add_argument("--out", default="petclip-out", help="output folder (default: petclip-out)")
    prep.add_argument("--threshold", type=float, default=0.25, help="scene-cut sensitivity, 0–1 (default 0.25; lower finds more cuts)")
    prep.add_argument("--y-offset", type=int, help="top edge of the crop in pixels (when ears or paws get cut)")
    prep.add_argument("--x-offset", type=int, help="left edge of the crop in pixels (when a pet at the side gets cut)")
    prep.add_argument("--cookies-from-browser", help="for posts that need a login, e.g. chrome")
    prep.add_argument("--cookies", help="a cookies.txt file (Netscape format)")
    prep.set_defaults(func=cmd_prep)
    cuts = sub.add_parser("cuts", help="print the shot list of a local file")
    cuts.add_argument("source")
    cuts.add_argument("--threshold", type=float, default=0.25)
    cuts.set_defaults(func=cmd_cuts)
    win = sub.add_parser("windows", help="list the cleanest short windows (start and end on a cut)")
    win.add_argument("source")
    win.add_argument("--length", type=float, default=6)
    win.add_argument("--top", type=int, default=3)
    win.add_argument("--threshold", type=float, default=0.25)
    win.set_defaults(func=cmd_windows)
    fr = sub.add_parser("frames", help="save one still per shot")
    fr.add_argument("source")
    fr.add_argument("--out", default="frames")
    fr.add_argument("--threshold", type=float, default=0.25)
    fr.set_defaults(func=cmd_frames)
    ph = sub.add_parser("photo", help="check pet photos (size, format, blur) before uploading them")
    ph.add_argument("photos", nargs="+")
    ph.add_argument("--soft-limit", type=float, default=40, help="softness that counts as blurry (default 40; sharp photos are about 28–39)")
    ph.set_defaults(func=cmd_photo)
    ma = sub.add_parser("match", help="check whether two videos use the same sound, and the offset between them")
    ma.add_argument("a", help="usually the longer one (the original post, or the full song)")
    ma.add_argument("b", help="the clip to look for in it (a repost, a remake, your edit)")
    ma.add_argument("--max-seconds", type=float, default=120, help="only read this much of each file (default 120)")
    ma.set_defaults(func=cmd_match)
    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
