# AI 宠物热梗视频工具包

[English](README.md) | 中文

把你家狗狗或猫咪放进 TikTok、Instagram Reels、YouTube Shorts 宠物热梗视频的一套东西：一个原片准备脚本、一个给 AI 编程助手用的 skill、一份当前宠物热梗模板清单，还有一份如实写的 AI 宠物视频工具对比。

> 由 [MyPetDance](https://mypetdance.com/zh) 团队制作，下面对比表里也有我们自己的产品。脚本和 skill 不依赖我们的网站，单独就能用。

- **[`petclip.py`](petclip.py)**：贴一个 TikTok / Reels / Shorts 链接，拿到 9:16 720p 的原片、一段干净的 6 秒短版（不会停在刚切到新镜头的那一下）、原声 MP3、每个镜头的切换时间，还有一张逐帧预览图。它还能在你上传之前检查宠物照片的尺寸、格式和清晰度。
- **[`skills/pet-trend-video`](skills/pet-trend-video/SKILL.md)**：给 Claude Code、Codex 等 AI 编程助手用的 skill。跟它说「把我家猫放进跳舞小猫的视频」，它会去找原片、跑 `petclip`、告诉你是什么声音、检查你的照片，再给出最省事的做法。
- **[宠物热梗模板](#宠物热梗模板)**：14 个当前的宠物热梗，每个讲清楚发生什么、多长、哪些宠物能用，还有 **[每个怎么做](#每个宠物热梗视频怎么做)**。
- **[AI 宠物视频工具对比](#ai-宠物视频工具对比)**，价格取自各家自己的页面。

## 宠物热梗模板

截至 2026 年 11 月 16 日，MyPetDance 上所有现成的宠物热梗模板。上传一张狗狗或猫咪的照片，拿到换成你家宠物、带原声的热梗视频。日期、播放量、歌名都是各页面上写的，页面上也注明了核实日期。

| 热梗 | 片子里发生什么 | 时长（短版 / 完整版） | 能用的宠物 | 页面 |
|---|---|---|---|---|
| Left Right 狗狗舞 | 狗狗头上裹着白毛巾，站在淋浴间里左右扭。原片 @jonnyslife_（2026 年 5 月 14 日，1,040 万播放），声音「Follow The Leader」。 | 6 秒 / 15 秒 | 1 只狗（猫还没测过） | [mypetdance.com](https://mypetdance.com/zh) |
| It's Time 圣诞小猫 | 戴圣诞帽和发光眼镜的小猫在雪地路上大喊「It's time!」，后面又冒出两只小猫。出自 @meowtakeover，2026 年 11 月 13 日。 | 6 秒 / 10 秒 | 1–3 只猫或狗 | [/its-time-cat-meme](https://mypetdance.com/zh/its-time-cat-meme) |
| 宠物圣诞老人装 | 宠物穿着红色圣诞老人衣服、戴着帽子坐在亮灯的圣诞树旁，歪头、挥爪，窗外下着雪。 | 6 秒 / 8 秒 | 1 只狗或猫 | [/pet-santa-costume-ai](https://mypetdance.com/zh/pet-santa-costume-ai) |
| 猫咪出租车 | 你家宠物变得巨大，夜里跑到路边，一个穿西装的男人爬上去骑着它回家。出自 Instagram @cat_vlog365，2026 年 11 月 10 日。 | 6 秒 / 12 秒 | 1 只狗或猫 | [/cat-taxi-ai](https://mypetdance.com/zh/cat-taxi-ai) |
| 唱歌的狗 | 宠物在超市货架间仰头唱那首自动调音的「唱歌狗」。截至 2026 年 11 月 14 日，这段声音被 21,665 条 TikTok 视频用过。 | 6 秒 / 13 秒 | 1 只狗或猫 | [/singing-dog-ai](https://mypetdance.com/zh/singing-dog-ai) |
| Suave 小猫舞 | 三只小猫夜里在水边湿沙滩上跟着 El Alfa 的「Suave」跳舞。出自 @meowtakeover，2026 年 10 月 29 日。 | 6 秒 / 24 秒 | 1–2 只猫（狗也行） | [/suave-cat-dance](https://mypetdance.com/zh/suave-cat-dance) |
| Hit the Road Dude | 宠物戴着迷彩帽坐在白色皮卡里，指着让你离开它的地盘，配的是这个梗的原声「hit the road, dude」。 | 6 秒 / 15 秒 | 1 只狗或猫 | [/hit-the-road-dude-pet](https://mypetdance.com/zh/hit-the-road-dude-pet) |
| 跳舞巴哥（狗狗泳池派对） | 宠物戴着粉色泳镜和臂圈，在夜里的泳池派对上跳舞。出自 @lucasthepuglife，2026 年 11 月 8 日。 | 只有 6 秒 | 1 只狗或猫 | [/dancing-pug-ai](https://mypetdance.com/zh/dancing-pug-ai) |
| It's My Life 开车狗 | 宠物开车上高速，唱 Bon Jovi 的「It's My Life」，盯着镜头不说话，最后一句戴上墨镜。 | 6 秒 / 15 秒 | 1 只狗或猫 | [/its-my-life-dog-ai](https://mypetdance.com/zh/its-my-life-dog-ai) |
| 猫骑 Surron | 猫戴着金链子，骑紫色 Surron 款电动越野车在公路上翘头。出自 @ridefx__，2026 年 11 月 7 日。 | 6 秒 / 13 秒 | 1 只猫（狗也行，只测过猫） | [/cat-riding-surron-ai](https://mypetdance.com/zh/cat-riding-surron-ai) |
| 小猫游行 | 雪夜里，你家猫带着一队小猫从低机位镜头前走过，配「Kiat Jud Dai」，最后回来舔镜头。出自 @memescreens，2026 年 11 月 6 日。 | 6 秒 / 13 秒 | 1 只猫（柴犬也测过能用） | [/kitten-parade](https://mypetdance.com/zh/kitten-parade) |
| Grinch 宠物滤镜 | 宠物趴在圣诞树前的白地毯上，一阵金光之后变成亮绿色，戴圣诞帽穿红外套。是我们自己做的片子和原创配乐，不是电影里的角色。 | 6 秒 / 9 秒 | 1 只狗或猫 | [/grinch-pet-filter](https://mypetdance.com/zh/grinch-pet-filter) |
| 跳舞小猫 | 三只小猫夜里在路边用后腿站着跟着节奏跳舞。出自 @meowtakeover，2026 年 6 月 29 日，到 11 月 9 日 1.08 亿播放。 | 6 秒 / 11 秒 | 1–3 只猫 | [/kittens-dance-ai](https://mypetdance.com/zh/kittens-dance-ai) |
| Smalltown Boy 猫 | 两只猫在红栅栏前轮流对着镜头尖叫、跳舞，配 Bronski Beat 的「Smalltown Boy」。 | 14 秒 | 1–2 只猫 | [/smalltown-boy-cat](https://mypetdance.com/zh/smalltown-boy-cat) |

简单说：只有一只狗，先试 Left Right 狗狗舞、Hit the Road Dude 或 It's My Life 开车狗。猫多的话，跳舞小猫和 Suave 小猫舞能放不止一只。圣诞节就选 It's Time 圣诞小猫、宠物圣诞老人装和 Grinch 宠物滤镜。

网站上的其他指南：[AI 狗狗跳舞是怎么火起来的](https://mypetdance.com/zh/ai-dog-dancing-trend) · [怎么用 AI 让狗狗跳舞](https://mypetdance.com/zh/how-to-make-your-dog-dance-ai) · [跳舞狗表情包](https://mypetdance.com/zh/dancing-dog-meme) · [跳舞猫表情包](https://mypetdance.com/zh/dancing-cat-meme) · [AI 猫咪跳舞](https://mypetdance.com/zh/ai-cat-dance) · [狗狗跳舞 App](https://mypetdance.com/zh/dog-dancing-app) · [AI 狗狗跳舞 GIF](https://mypetdance.com/zh/ai-dog-dancing-gif) · [AI 猫咪跳舞 GIF](https://mypetdance.com/zh/ai-cat-dance-gif) · [全部模板](https://mypetdance.com/zh/templates)

## 每个宠物热梗视频怎么做

步骤都一样：

1. 拍或挑一张清楚的宠物照片：正对镜头，脸和耳朵露出来，画面里没有别人。帽子和衣服先摘掉，热梗里的装扮会自动加上。不确定够不够清楚？跑一下 `python3 petclip.py photo 你家宠物.jpg`。
2. 打开对应热梗的页面，传照片，选短版或完整版。
3. 短版大约 8 分钟，完整版 12 到 15 分钟，做好了会发邮件给你。
4. 发的时候用视频里自带的声音，并打开平台的 AI 标签。

每个热梗不一样的地方：

### Left Right 狗狗舞怎么做

一张狗狗正脸照。萨摩耶、博美这种毛特别蓬的狗，脸可能会软一些。6 秒版尝个鲜，15 秒版有每一下扭和转身。在 [MyPetDance 首页](https://mypetdance.com/zh) 就能做。

### It's Time 圣诞小猫怎么做

第 1 张照片是前面戴圣诞帽的小猫，第 2、3 张是后面戴精灵帽和驯鹿帽的两只。后面两只 4.5 秒才出现，想换它们就选完整的 10 秒。后排位置猫和小型犬效果最好。[去做 It's Time 圣诞小猫](https://mypetdance.com/zh/its-time-cat-meme)。

### 宠物圣诞老人装怎么做

宠物不用穿任何东西，普通照片就行，衣服和帽子在视频里加。照片里有项圈、领巾会保留。完整 8 秒能把旋律放完，做圣诞贺卡选它。[去做宠物圣诞老人装](https://mypetdance.com/zh/pet-santa-costume-ai)。

### 猫咪出租车怎么做

宠物跑起来时会露出侧面和背面，所以全身照更好。完整 12 秒从男人招手叫「车」开始，6 秒版从宠物已经到路边开始。[去做猫咪出租车](https://mypetdance.com/zh/cat-taxi-ai)。

### 唱歌的狗怎么做

这是特写，脸比身体重要。视频不带字，你可以在 TikTok、Instagram 或剪映里自己加一句（比如「车里放到我的歌时的我」）。[去做唱歌的狗](https://mypetdance.com/zh/singing-dog-ai)。

### Suave 小猫舞怎么做

第 1 张照片换中间戴项圈的小猫，第 2 张换左边奶油色的那只，右边的灰色虎斑保持原样。这是夜景，浅色毛的宠物最显眼。[去做 Suave 小猫舞](https://mypetdance.com/zh/suave-cat-dance)。

### Hit the Road Dude 宠物版怎么做

两只耳朵都清楚的照片，迷彩帽戴上最自然。6 秒版只有最后那句笑点，15 秒版前面还有「这是私人领地」的铺垫。[去做 Hit the Road Dude](https://mypetdance.com/zh/hit-the-road-dude-pet)。

### 跳舞巴哥泳池派对怎么做

不一定是巴哥，什么狗和猫都行。只有 6 秒，是因为原片后半段巴哥会背对镜头，测试时狗在那一下会变回原来的巴哥。[去做跳舞巴哥](https://mypetdance.com/zh/dancing-pug-ai)。

### It's My Life 开车狗怎么做

用眼睛睁开、嘴没被挡住的照片：最后墨镜要戴在眼睛上，宠物还要张嘴唱。6 秒版是盯镜头、戴墨镜和最后一句。[去做 It's My Life 开车狗](https://mypetdance.com/zh/its-my-life-dog-ai)。

### 猫骑 Surron 怎么做

不用剪映模板，也不用剪辑：传一张猫的照片，拿到 MP4。一只看起来懒洋洋的猫翘头骑车最好笑。[去做猫骑 Surron](https://mypetdance.com/zh/cat-riding-surron-ai)。

### 小猫游行怎么做

你家猫带队开场，最后一秒回来舔镜头，想要这个笑点就选完整 13 秒。浅色毛在雪地里最显眼。[去做小猫游行](https://mypetdance.com/zh/kitten-parade)。

### Grinch 宠物滤镜怎么做

不用剪映滤镜。变绿以后还是你家宠物：脸、耳朵、毛都一样。毛特别蓬的品种变绿后脸部细节会少一些。[去做 Grinch 宠物视频](https://mypetdance.com/zh/grinch-pet-filter)。

### 跳舞小猫怎么做

最多 3 张照片：第 1 张换中间那只，后两张换两边的。三只毛色不同的猫在夜景里比三只黑猫好认。[去做跳舞小猫](https://mypetdance.com/zh/kittens-dance-ai)。

### Smalltown Boy 猫怎么做

A 照片先尖叫后跳舞，B 照片反过来。想换谁先叫，就调换上传顺序。[去做 Smalltown Boy 猫](https://mypetdance.com/zh/smalltown-boy-cat)。

## petclip：把宠物热梗原片准备好

需要 Python 3.9+、[ffmpeg](https://ffmpeg.org) 和 [yt-dlp](https://github.com/yt-dlp/yt-dlp)，不用装任何 pip 包。

```bash
brew install ffmpeg yt-dlp          # macOS；Linux 用系统的包管理器，或 pip install yt-dlp
git clone https://github.com/ken-fs/ai-pet-trend-video && cd ai-pet-trend-video

python3 petclip.py prep "https://www.tiktok.com/@memescreens/video/7704821004471782663" --out kitten-parade
```

```
720x1280 13.0 s · 2 shots · cuts at 10.37 s
short version 0.0–6.0 s (1 shot, clean). Pick another with --start
crop 720x1280 at (0,0) → 720x1280. Look at kitten-parade/sheet.jpg to check your pet's ears and tail aren't cut off
wrote kitten-parade/SHOTS.md and shots.json
```

输出文件夹里有这些：

| 文件 | 是什么 |
|---|---|
| `original.mp4` | 下载下来的原片，能拿到的最高画质 |
| `clip.mp4` / `clip.mp3` | 裁成 9:16、720p 的视频，和原声 |
| `clip-6s.mp4` / `clip-6s.mp3` | 短版 |
| `sheet.jpg` | 每 0.5 秒一帧，用来检查裁切、看每个动作 |
| `SHOTS.md` / `shots.json` | 每个镜头的开始、结束和长度，还有其他可以用的 6 秒片段（[示例](examples/kitten-parade-SHOTS.md)） |

参数：

- `--window 6`（默认）是短版的长度，`--window 0` 不出短版。不加 `--start` 时，petclip 会挑一段开头和结尾都不夹着不到 1 秒的半截镜头的片段，优先从片子开头开始。
- `--start 9` 改用从第 9 秒开始的那段。有些梗的笑点在最后（Hit the Road Dude、It's My Life 开车狗），最后 6 秒才是更好的短版。
- `--ratio 16:9`（或 `1:1`、`4:5`、`3:4`）：原片不是竖屏、裁成 9:16 会裁掉宠物时用。`--x-offset` / `--y-offset` 移动裁切位置。
- `--threshold 0.25` 是多大的画面变化算切镜头。两个镜头长得很像、没检测到时调低（0.15）。

### 其他命令

```bash
python3 petclip.py windows clip.mp4 --length 6     # 最干净的几个 6 秒片段
python3 petclip.py cuts clip.mp4                   # 只看镜头列表
python3 petclip.py frames clip.mp4 --out frames    # 每个镜头存一张图（分镜、封面、首帧）
python3 petclip.py photo biscuit.jpg luna.png      # 这些宠物照片能不能用？
python3 petclip.py match original.mp4 repost.mp4   # 是不是同一段声音？一段在另一段的第几秒开始？
```

`photo` 检查格式（JPG、PNG 或 WebP）、文件大小（很多 App 上限 10 MB）、分辨率和清晰度。清晰度只看照片中间，也就是宠物通常在的地方，所以人像模式拍出的虚化背景不会被算成模糊。2026 年 11 月 16 日我们用 7 张清楚的宠物照片（600–1200 像素）测过：清楚的得分 28–39，轻微模糊后 38–45，明显模糊后 47–50，上限设在 40。所以明显模糊的照片能查出来，稍微有点软的可能会漏过。

```
ok    cat.jpg: 1200x797, 0.1 MB · sharp (softness 31)
check cat-blurry.jpg: 1200x1800, 0.1 MB
      - looks blurry (softness 48, limit 40): take a sharper one in good light
```

`match` 分低音、中音、高音比对两段声音的节奏，所以转发视频重新压缩过、音量变小也能认出来。可以用它找哪条才是真正的原片，或者看你剪的 6 秒在完整原片里从第几秒开始：

```
same sound: score 1.00; clip-6s.mp3 starts 7.00 s into original.mp4
```

**支持的链接：** TikTok、Instagram Reels、YouTube Shorts、Facebook、X，以及 [yt-dlp 支持的大多数网站](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)，本地文件也行。2026 年 11 月 16 日我们测过两条 TikTok 和一条 Instagram Reel。

**如果要求登录：** 加 `--cookies-from-browser chrome`（或 `firefox`、`safari`、`edge`），或者 `--cookies cookies.txt`。

只下载你有权使用的片子，发布时注明原作者。

## pet-trend-video skill

把文件夹复制到你的 AI 助手的 skills 目录：

```bash
# Claude Code
mkdir -p ~/.claude/skills && cp -r skills/pet-trend-video ~/.claude/skills/
# Codex 或其他支持 skill 的助手：把 skills/pet-trend-video 复制到它读取 skill 的位置
```

然后可以问「把我家狗放进 Hit the Road Dude 的视频」「小猫游行是什么歌」，或者贴个链接说「我想让我家猫也来一个」。这个 skill 会让助手先找真正的原片、弄对声音、跑 `petclip`、检查宠物照片，再在自己拍、剪映、AI 模板 App、自己给视频模型写提示词之间给出建议，最后过一遍发布前的检查。

## AI 宠物视频工具对比

2026 年 11 月 16 日在各家自己的页面上核对。价格会变，买之前再看一眼。

| 工具 | 怎么用 | 能免费试吗 | 官网价格 |
|---|---|---|---|
| [MyPetDance](https://mypetdance.com/zh/pricing)（我们的） | 选一个宠物热梗模板，传一张狗狗或猫咪的照片（部分模板可以两三只），拿到换成你家宠物、带原声的热梗原片。720p MP4，无水印。 | 没有免费预览。生成失败自动退积分。 | 积分包，不是订阅：4.99 美元（一条 6 秒短版）、9.99（一条完整版）、19.99、49.99。积分不过期。 |
| [Pet.Video](https://pet.video/pricing) | 用宠物照片做特效和跳舞视频，猫狗之外的动物也行。 | 注册送 30 积分，够做一条 5 秒 480p 视频。 | 订阅最低每月 9 美元（按年付，一年 108 美元），每月 300 积分；视频 25 积分起。积分包 90 天有效，Mega 包除外。 |
| [WigglePet](https://wigglepet.app/pet-video-app-no-subscription) | iOS 和安卓 App：让宠物跳舞、唱歌、说话、拍 vlog，整个身体都会动。 | 可以免费试图片。 | App 内买一次性积分包或订阅，官网没写价格。积分包不过期。 |
| [MakeMeme](https://makememe.video/pricing) | 表情包热梗模板，部分带宠物（比如 [Pet Taxi AI](https://makememe.video/pet-taxi-ai)，要一张你的照片和一张宠物的）。 | 定价页没写免费试用。每个梗生成前会显示价格，失败自动退款。 | 100 积分 9.99 美元、300 积分 26.99、1,000 积分 79.99，也有月付。Pet Taxi AI 10 秒：480p 1.99 美元、720p 3.99、1080p 7.99。 |
| [Jump on the Trend](https://jumponthetrend.app) | 几百个热梗模板，其中有「Starring your pet」宠物分类（我们看的时候 81 个）。 | 不用注册就能免费预览。 | 一条视频 100 积分：100 积分 6.99 美元（限时价，原价 9.90）、300 积分 14.99。积分不过期。 |
| [ViralRemix](https://viralremix.org/pricing) | 热梗表情包视频，同一个梗常有很多场景版本。 | 定价页没写免费试用。失败自动退款。 | 一条 9.90 美元，4 条 29，8 条 49。自动发布套餐每月 69 美元起。 |
| [Viggle](https://viggle.ai/pricing) | 把角色换进视频，或让角色动起来。不是专门做宠物的。 | 免费版每天送积分，免费出的视频带水印。 | Pro 每月 7.99 美元（80 积分，无水印），Live 15.99，Max 63.99，页面上都标着是从 9.99、19.99、79.99 打折来的。 |
| [CapCut（剪映国际版）](https://www.capcut.com/pricing) | 大部分宠物热梗都有用户做的模板：放进自己的照片或视频就能生成。TikTok 上这些梗的帖子大多是这样做的。 | 免费版有免费模板。 | Pro 每月 19.99 美元或每年 179.99。 |

按你要什么来选。想要你家宠物出现在真正的热梗原片里、带原声：MyPetDance 或几个模板站（MakeMeme、Jump on the Trend、ViralRemix）。想付钱前先免费看看：Jump on the Trend 的预览或 Pet.Video 的注册积分。想免费把自己的照片卡点剪成视频：CapCut。想要一个能做很多种宠物视频的手机 App：WigglePet。

## 许可

MIT，见 [LICENSE](LICENSE)。热梗片段、歌曲和画面归原作者所有；这个仓库里只有代码和文字。
