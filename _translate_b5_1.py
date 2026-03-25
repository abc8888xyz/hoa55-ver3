# -*- coding: utf-8 -*-
"""Translate _art_b5_1_orig.json from Chinese to Vietnamese"""
import json
import re
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art_b5_1_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation map: Chinese -> Vietnamese
# We'll translate each text_run content
# Rules: keep URLs, code, emoji, proper nouns (product names like Clawdbot, GitHub, etc.)

def is_url(text):
    return text.startswith('http://') or text.startswith('https://')

def has_only_special(text):
    """Check if text is only punctuation, numbers, spaces, URLs"""
    cleaned = re.sub(r'https?://\S+', '', text)
    cleaned = re.sub(r'[0-9\s\.\,\;\:\!\?\-\+\*\/\=\(\)\[\]\{\}\<\>\@\#\$\%\^\&\_\~\`\"\'\|\\]', '', cleaned)
    cleaned = re.sub(r'[a-zA-Z]', '', cleaned)
    # Remove emoji
    cleaned = re.sub(r'[\U0001F300-\U0001F9FF\U00002702-\U000027B0\U0000FE00-\U0000FEFF]', '', cleaned)
    return len(cleaned.strip()) == 0

# Build translation dictionary for all text segments
translations = {
    # Page title
    "Clawdbot一夜爆火，GitHub已狂飙 64k Star！附最新部署使用教程": "Clawdbot bùng nổ chỉ sau một đêm, GitHub đã vọt lên 64k Star! Kèm hướng dẫn triển khai và sử dụng mới nhất",

    # Quote - original link
    "🔗 原文链接： ": "🔗 Link bài gốc: ",

    # Author info
    "原创 苍何 苍何 苍何": "Nguyên tác: Thương Hà",
    "2026年1月28日 10:40  北京": "28/01/2026 10:40 Bắc Kinh",

    # Intro paragraphs
    "小伙伴们也可以通过阿里云百炼": "Các bạn cũng có thể thông qua Alibaba Cloud Bailian",
    "Coding Plan ": "Coding Plan ",
    "来部署": " để triển khai",
    "：": ":",
    "首购低至 7.9 元，续费 5 折起，支持Qwen3.5、Qwen3-max、Qwen3-coder、GLM-5、GLM-4.7、Kimi-k2.5等模型": "Mua lần đầu chỉ từ 7.9 tệ, gia hạn giảm từ 50%, hỗ trợ Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 và các mô hình khác",
    "👉戳链接直达：": "👉 Bấm link trực tiếp:",
    "👉查看详细部署教程：": "👉 Xem hướng dẫn triển khai chi tiết:",
    "最多三步，即可拥有 7x 24小时在线、随时响应的AI助手": "Chỉ cần tối đa ba bước, bạn đã có trợ lý AI trực tuyến 7x24 giờ, phản hồi mọi lúc",

    "这是苍何的第 477 篇原创！": "Đây là bài viết gốc thứ 477 của Thương Hà!",
    "大家好，我是苍何。": "Xin chào mọi người, mình là Thương Hà.",
    "这两天 Clawdbot 火出来天际，我的 X 时间线上全部都是这玩意。": "Hai ngày nay Clawdbot nổi đình nổi đám, timeline X của mình toàn là thứ này.",
    "这是一个 AI 开源项目，主打的是 AI 私人助理，他能自行处理你电脑里面的任何需求，能帮你整理文件，能为你回复消息，能帮你写周报，写文章，甚至还能帮你购物。": "Đây là một dự án AI mã nguồn mở, chuyên về trợ lý AI cá nhân. Nó có thể tự xử lý mọi nhu cầu trên máy tính của bạn, giúp bạn sắp xếp tệp, trả lời tin nhắn, viết báo cáo tuần, viết bài, thậm chí còn giúp bạn mua sắm.",
    "开源地址如下：https://github.com/moltbot/moltbot": "Địa chỉ mã nguồn mở: https://github.com/moltbot/moltbot",
    "截止当下，已狂飙 64 k Star，而这个增长实际只花了几天时间。": "Tính đến thời điểm hiện tại, đã vọt lên 64k Star, và sự tăng trưởng này thực tế chỉ mất vài ngày.",
    "可笑的是，原本 Clawdbot 作者为了致敬 Claude 而取了这个名字，现在却被 Anthropic 要求改名，现在 Clawdbot正式改名为 Moltbot。": "Buồn cười là ban đầu tác giả Clawdbot đặt tên này để tôn vinh Claude, giờ lại bị Anthropic yêu cầu đổi tên. Hiện tại Clawdbot đã chính thức đổi tên thành Moltbot.",
    "他和传统的通用 Agent 不同，这是一个本地的完全开源的 Agent，他完全运行在你自己的电脑上。": "Nó khác với các Agent thông dụng truyền thống - đây là một Agent mã nguồn mở hoàn toàn chạy trên máy tính cá nhân của bạn.",
    "而且还可以远程指挥，做到 7* 24 小时为你工作。而且记忆永久保存在本地，理论上拥有永久的记忆能力。": "Hơn nữa còn có thể điều khiển từ xa, làm việc cho bạn 7x24 giờ. Bộ nhớ được lưu vĩnh viễn trên máy cục bộ, về lý thuyết có khả năng ghi nhớ vĩnh viễn.",
    "比如，我远程操控 Clawdbot 帮我搜索关于他自己的资料及教程案例，他很好的就帮我完成了任务，并直接给我结果。": "Ví dụ, mình điều khiển từ xa Clawdbot tìm kiếm tài liệu và hướng dẫn về chính nó, nó đã hoàn thành nhiệm vụ rất tốt và đưa ra kết quả trực tiếp cho mình.",
    "然后我用手机也能操控他帮我把这个结果保存在电脑上的指定文件夹。": "Sau đó mình dùng điện thoại cũng có thể điều khiển nó lưu kết quả vào thư mục chỉ định trên máy tính.",
    "他可以很出色的完成任务，真的🐂🍺，而且这个过程他完全是在我自己的服务器电脑上执行的。": "Nó có thể hoàn thành nhiệm vụ rất xuất sắc, thật sự 🐂🍺, và toàn bộ quá trình đều được thực thi trên máy chủ của mình.",
    "其实能操控 Clawdbot 的平台还非常多，国外的你能想到的几乎都可以，国内也很快支持飞书、企微等。": "Thực ra có rất nhiều nền tảng có thể điều khiển Clawdbot, hầu hết các nền tảng quốc tế bạn nghĩ đến đều được hỗ trợ, trong nước cũng sắp hỗ trợ Feishu, WeCom, v.v.",
    "Clawdbot 的爆火绝非偶然，AI Agent 发展至今，我们都太急切需要一个属于我们自己的 AI 助理，他能全天帮我们干活，不知疲倦的为我们打工。": "Sự bùng nổ của Clawdbot không phải ngẫu nhiên. AI Agent phát triển đến nay, chúng ta đều quá cần một trợ lý AI thuộc về riêng mình, có thể làm việc cả ngày, không biết mệt mỏi.",
    "但是 Clawdbot 能操控电脑权限太高了，现在体验的话要么整个不用的电脑，要么就整个便宜的云服务器玩。": "Nhưng Clawdbot có quyền điều khiển máy tính quá cao, hiện tại muốn trải nghiệm thì hoặc dùng máy tính không sử dụng, hoặc thuê một máy chủ đám mây giá rẻ để chơi.",
    "光这一点，就把 Mac Mini 给卖爆了。": "Chỉ riêng điều này đã khiến Mac Mini bán chạy đột biến.",
    "这个东西部署也没那么简单，特别是涉及到自定义 API，以及不同的平台设置，对非开发者还不是很友好。": "Việc triển khai thứ này cũng không đơn giản lắm, đặc biệt khi liên quan đến tùy chỉnh API và cài đặt trên các nền tảng khác nhau, không thân thiện lắm với người không phải lập trình viên.",
    "所以，也就有了这一篇教程，可以自信的说，这篇文章主打最新最全，包含部署、配置、自定义 API 设置、使用等。": "Vì vậy mới có bài hướng dẫn này. Có thể tự tin nói rằng bài viết này cung cấp đầy đủ và mới nhất, bao gồm triển khai, cấu hình, thiết lập API tùy chỉnh, sử dụng, v.v.",
    "文章会显得有些长，熬夜写到了凌晨 5 点，如果对你有帮助，感谢你的点赞转发支持。": "Bài viết có vẻ hơi dài, thức khuya viết đến 5 giờ sáng. Nếu có ích cho bạn, cảm ơn bạn đã like và chia sẻ ủng hộ.",
    "废话不多说，直接进入教程。": "Không nói nhiều nữa, vào thẳng hướng dẫn.",

    # Heading 1: 准备服务器
    "准备服务器": "Chuẩn bị máy chủ",

    "目前用云服务是性价比最优的方式，买个电脑好几千，一台云服务器先租个一个也也才二三十。": "Hiện tại sử dụng dịch vụ đám mây là cách có hiệu quả chi phí tốt nhất. Mua máy tính mất vài nghìn tệ, thuê một máy chủ đám mây chỉ hai ba chục tệ.",
    "选个 2 核 2 G 就差不多了，像阿里云/腾讯云或者任意 VPS 都可以支持。": "Chọn cấu hình 2 nhân 2GB là đủ, như Alibaba Cloud/Tencent Cloud hoặc bất kỳ VPS nào đều được hỗ trợ.",
    "我为了图省事，用的腾讯云新出的 Lighthouse，免去安装环境和依赖，直接就有 Clawdbot 模板。": "Mình chọn Lighthouse mới ra của Tencent Cloud cho tiện, không cần cài đặt môi trường và phụ thuộc, trực tiếp đã có template Clawdbot.",
    "地区选择硅谷，选择最便宜的套餐。": "Khu vực chọn Silicon Valley, chọn gói rẻ nhất.",
    "你可以选择关闭自动续费。": "Bạn có thể chọn tắt tự động gia hạn.",
    "在站内信中找到服务器 IP、用户名、密码，然后用 SSH 客户端连接服务器，我这里用的是 Xterminal。": "Trong tin nhắn hệ thống tìm IP máy chủ, tên người dùng, mật khẩu, rồi dùng SSH client kết nối máy chủ. Mình dùng Xterminal.",
    "没有 SSH 客户端也可以直接点击页面这里的登录进去。": "Không có SSH client cũng có thể trực tiếp nhấn nút đăng nhập trên trang.",

    # Heading 1: 一键安装
    "一键安装": "Cài đặt một chạm",

    "因为这里是内置了应用模板，理论上就是不用再重新安装 Clawdbot 了，当然如果你不是通过应用模板的方式，也可以自行执行以下指令：": "Vì ở đây đã tích hợp sẵn template ứng dụng, về lý thuyết không cần cài lại Clawdbot nữa. Tất nhiên nếu bạn không dùng template, cũng có thể tự chạy các lệnh sau:",
    "这里我用了应用模板就不需要再安装了，他已经装好了环境和依赖。": "Ở đây mình dùng template ứng dụng nên không cần cài lại, môi trường và phụ thuộc đã được cài sẵn.",
    "安装好之后输入如下命令查看 Clawdbot 版本：": "Sau khi cài xong, nhập lệnh sau để xem phiên bản Clawdbot:",
    "安装好后，下一步就可以直接进入配置环节。需要配置模型和 Bot。": "Sau khi cài xong, bước tiếp theo là vào phần cấu hình. Cần cấu hình mô hình và Bot.",
    "Bot 就是可以操控 Clawdbot 的端侧，比如 telegram 发消息操控 Clawdbot 远程工作。": "Bot là phía client có thể điều khiển Clawdbot, ví dụ gửi tin nhắn qua Telegram để điều khiển Clawdbot làm việc từ xa.",
    "配置模型和 Bot一共需要准备以下 2 个东西：API key、Bot token，下面详细说一说。": "Cấu hình mô hình và Bot cần chuẩn bị 2 thứ sau: API key, Bot token. Dưới đây sẽ nói chi tiết.",

    # Heading 1: 配置模型
    "配置模型": "Cấu hình mô hình",

    "Clawdbot 支持非常多的 API 模型，比如 OpenAI、Anthropic、kimi、GLM 都是内置支持的。": "Clawdbot hỗ trợ rất nhiều mô hình API, ví dụ OpenAI, Anthropic, Kimi, GLM đều được hỗ trợ sẵn.",
    "当然除了内置的，还支持自定义 API，这里充分考虑灵活性，我用的自定义 API 的方式，模型选择性也多和更灵活一些。": "Ngoài các mô hình tích hợp sẵn, còn hỗ trợ API tùy chỉnh. Ở đây mình chọn dùng API tùy chỉnh để linh hoạt hơn trong việc chọn mô hình.",
    "如果你希望稳定，性价比高的 API 平台，可以试试之前给大家推荐过的 Atlas Cloud。": "Nếu bạn muốn nền tảng API ổn định, hiệu quả chi phí cao, có thể thử Atlas Cloud mà trước đây mình đã giới thiệu.",
    "地址：https://www.atlascloud.ai?ref=AXZ9S7": "Địa chỉ: https://www.atlascloud.ai?ref=AXZ9S7",
    "毕竟它主打的是企业级 API 聚合，拥有 300+ 知名大模型， ": "Xét cho cùng, nó chuyên về tích hợp API cấp doanh nghiệp, sở hữu hơn 300 mô hình AI nổi tiếng, ",
    "Qwen、DeepSeek、Kimi、MiniMax等知名大模型一网打尽。 总结下来是： ": "tập hợp đầy đủ các mô hình lớn nổi tiếng như Qwen, DeepSeek, Kimi, MiniMax. Tóm lại là: ",
    "稳定、易用、低价。 ": "Ổn định, dễ dùng, giá rẻ. ",
    "那该如何使用呢？注册登录后，打开控制台，新建 API 密钥。": "Vậy sử dụng như thế nào? Sau khi đăng ký đăng nhập, mở bảng điều khiển, tạo API key mới.",
    "多说一嘴，Atlas Cloud 目前注册绑卡即可白嫖 1 美元使用额度，用我的邀请码注册首充还能送 25% bonus。可以先免费白嫖起🐶。": "Nói thêm chút, Atlas Cloud hiện tại đăng ký liên kết thẻ là được miễn phí 1 USD. Dùng mã mời của mình đăng ký nạp lần đầu còn tặng thêm 25% bonus. Có thể dùng miễn phí trước 🐶.",
    "填写名称后，点击创建：": "Điền tên xong, nhấn tạo:",
    "然后点击复制这个 API：": "Sau đó nhấn sao chép API này:",
    "这个 API Key 在第四步的时候需要填入的参数：": "API Key này là tham số cần điền ở bước thứ tư:",

    # Heading 1: 配置 Bot
    "配置 Bot": "Cấu hình Bot",

    "这个实际配置的是和 Clawdbot 进行交互的软件，支持挺多国外软件的，比如 Telegram、Discord 等。": "Thực tế đây là cấu hình phần mềm tương tác với Clawdbot, hỗ trợ khá nhiều phần mềm quốc tế như Telegram, Discord, v.v.",
    "国内的企微、飞书或者微信，我估计也会很快支持了，毕竟开源生态发展太快了。": "Các ứng dụng trong nước như WeCom, Feishu hay WeChat, mình ước tính cũng sẽ sớm được hỗ trợ, xét cho cùng hệ sinh thái mã nguồn mở phát triển quá nhanh.",
    "这里以 Discord 为例（我使用的多一些）。": "Ở đây lấy Discord làm ví dụ (mình dùng nhiều hơn).",
    "1、前往 Discord Developer Portal > Application > New Application": "1. Truy cập Discord Developer Portal > Application > New Application",
    "2、创建好应用后，选择 Bot> Reset Token > copy token": "2. Sau khi tạo ứng dụng xong, chọn Bot > Reset Token > copy token",
    "3、打开 Message Content Intent的选项并保存": "3. Bật tùy chọn Message Content Intent và lưu",
    "4、OAuth2 页面配置": "4. Cấu hình trang OAuth2",
    "在 OAuth2 URL Generator中选择 bot": "Trong OAuth2 URL Generator chọn bot",
    "在 Bot Permissions 中勾选 Send Messages 和 Read Message History。": "Trong Bot Permissions tick chọn Send Messages và Read Message History.",
    "同样这个页面往下滑，复制 bot 邀请链接。": "Cũng trên trang này kéo xuống, sao chép link mời bot.",
    "在浏览器中打开这个链接，然后选择一个自己的服务器，相当于把机器人 bot 加入到 server 中。": "Mở link này trong trình duyệt, sau đó chọn một server của bạn, tương đương với việc thêm bot vào server.",
    "这时候确认下刚才我们给 bot 的 2 个权限。": "Lúc này xác nhận lại 2 quyền vừa cấp cho bot.",
    "打开 Discord，然后输入框中@就可以看到刚才添加的机器人 bot。": "Mở Discord, rồi gõ @ trong ô nhập liệu sẽ thấy bot vừa thêm.",

    # Heading 1: Clawdbot配置
    "Clawdbot配置": "Cấu hình Clawdbot",

    "先在服务器执行以下命令，直接修改Clawdbot 配置，如果需要自定义 API，需要自行按照如下配置修改。": "Trước tiên chạy lệnh sau trên máy chủ để sửa trực tiếp cấu hình Clawdbot. Nếu cần tùy chỉnh API, hãy tự sửa theo cấu hình dưới đây.",
    "当然如果不需要自定义 API，也可以用自带的就可以直接在页面中操作，需要提前准备好对应官方的 API。": "Tất nhiên nếu không cần tùy chỉnh API, cũng có thể dùng API có sẵn và thao tác trực tiếp trên giao diện. Cần chuẩn bị trước API chính thức tương ứng.",
    "如果没用云服务模板自己安装的话，安装好后会弹窗让配置，选择 QuickStart。": "Nếu không dùng template dịch vụ đám mây mà tự cài, sau khi cài sẽ hiện cửa sổ yêu cầu cấu hình, chọn QuickStart.",
    "如果是用的腾讯云的模板，就输入如下命令进入配置：": "Nếu dùng template của Tencent Cloud, nhập lệnh sau để vào cấu hình:",
    "接下来配置的操作直接使用键盘来操作，这里先选择 yes 知晓风险。": "Các bước cấu hình tiếp theo thao tác trực tiếp bằng bàn phím, ở đây chọn yes xác nhận đã biết rủi ro.",
    "然后选择默认的 QuickStart。": "Sau đó chọn QuickStart mặc định.",
    "接着是选择模型供应商的配置，如果上一步已经配置了第三方 API 就不用再配了": "Tiếp theo là chọn cấu hình nhà cung cấp mô hình, nếu bước trước đã cấu hình API bên thứ ba thì không cần cấu hình lại",
    "也可以选择自带的 API：": "Cũng có thể chọn API có sẵn:",
    "比如选 GLM 4.7, 输入 key，只需要选择默认模型就好了。": "Ví dụ chọn GLM 4.7, nhập key, chỉ cần chọn mô hình mặc định là được.",
    "接下来是选择 channel，这里选择 Discord": "Tiếp theo là chọn channel, ở đây chọn Discord",
    "还挺贴心的，把如何获取 token 也做了说明。": "Khá chu đáo, cũng có hướng dẫn cách lấy token.",
    "把之前我们创建的 bot 的 token 复制进来。": "Dán token của bot đã tạo trước đó vào.",
    "然后页面按照这个做选择：": "Sau đó chọn theo hướng dẫn trên trang:",
    "这里可以自定义安装很多依赖，可以先不装。": "Ở đây có thể tùy chỉnh cài nhiều phụ thuộc, có thể bỏ qua trước.",
    "这些 key 也可以先不配置：": "Các key này cũng có thể chưa cần cấu hình:",
    "注意 Enable hooks 的选项选择 session-memory：": "Lưu ý chọn tùy chọn Enable hooks là session-memory:",
    "接下来你就可以在服务器中和 Clawdbot 对话了：": "Tiếp theo bạn có thể trò chuyện với Clawdbot trên máy chủ:",
    "但这并没结束，因为我们要通过 discord 来指挥 Clawdbot。": "Nhưng chưa xong đâu, vì chúng ta cần điều khiển Clawdbot qua Discord.",
    "先退出 Clawdbot，然后在服务器停止服务：": "Thoát Clawdbot trước, rồi dừng dịch vụ trên máy chủ:",
    "然后重新启动：": "Sau đó khởi động lại:",
    "启动成功后，返回 Discord，与 bot 进行对话后拿到配对码。": "Sau khi khởi động thành công, quay lại Discord, trò chuyện với bot để lấy mã ghép nối.",
    "是点击 bot 进行私聊，而不是@聊天。": "Là nhấn vào bot để nhắn tin riêng, không phải @ trong chat.",
    "紧接着返回服务器命令行，你需要按下Ctrl+C（Windows）或者Command+C（MacOS）终止 Gateway 服务。": "Tiếp theo quay lại dòng lệnh máy chủ, bạn cần nhấn Ctrl+C (Windows) hoặc Command+C (MacOS) để dừng dịch vụ Gateway.",
    "然后粘贴并运行如下命令进行配对，把 Pairing code 替换为上面的\"Pairing code\"后面的内容。": "Sau đó dán và chạy lệnh sau để ghép nối, thay thế Pairing code bằng nội dung phía sau \"Pairing code\" ở trên.",
    "然后粘贴并运行如下命令进行配对，把 Pairing code 替换为上面的\u201cPairing code\u201d后面的内容。": "Sau đó dán và chạy lệnh sau để ghép nối, thay thế Pairing code bằng nội dung phía sau \"Pairing code\" ở trên.",
    "然后再次启动 Gateway": "Sau đó khởi động lại Gateway",
    "如果你想要让它在服务器中静默启动，而不是关闭终端就停止服务了，你可以输入以下命令：": "Nếu bạn muốn nó chạy nền trên máy chủ thay vì dừng dịch vụ khi đóng terminal, có thể nhập lệnh sau:",
    "在 discord 中@机器人，可以看到有回复了：": "Trong Discord @ bot, có thể thấy đã có phản hồi:",
    "然后服务器也能看到有回复了：": "Máy chủ cũng thấy có phản hồi:",
    "自此，Clawdbot 就完成了安装和配置，以及能通过在 discord 中和 bot 对话的方式操控服务器上的 Clawdbot。": "Đến đây, Clawdbot đã hoàn tất cài đặt và cấu hình, đồng thời có thể điều khiển Clawdbot trên máy chủ thông qua trò chuyện với bot trong Discord.",

    # Heading 1: 使用 Clawdbot
    "使用 Clawdbot": "Sử dụng Clawdbot",

    "配置好后就可以直接在 discord 中@bot 的方式来远程指挥 Clawdbot 干活。": "Sau khi cấu hình xong có thể trực tiếp @ bot trong Discord để điều khiển Clawdbot làm việc từ xa.",
    "直接来一个问题：": "Thử ngay một câu hỏi:",
    "我录了一个视频，大家可以感受一下，非常刺激：": "Mình đã quay một video, mọi người có thể cảm nhận, rất thú vị:",
    "可以看到 Clawdbot 会自行去搜索，并且给到我想要的信息，最牛 X 的是，这家伙居然给我推荐了相关的 discord 社区，我靠，真贴心。": "Có thể thấy Clawdbot tự tìm kiếm và đưa ra thông tin mình cần. Điều tuyệt vời nhất là nó còn giới thiệu cộng đồng Discord liên quan, quá chu đáo.",
    "然后我又直接在手机上，让 Clawdbot 帮我把刚刚找到的结果保存在电脑指定的文件夹，我的要求如下：": "Sau đó mình trực tiếp trên điện thoại, yêu cầu Clawdbot lưu kết quả vừa tìm được vào thư mục chỉ định trên máy tính, yêu cầu như sau:",
    "我喝了几口水的功夫，Clawdbot 就已经帮我把事情做好了。": "Mới uống vài ngụm nước, Clawdbot đã hoàn thành xong việc cho mình.",
    "这也太爽了，他真的能做，这种远程指挥的感觉，太让人兴奋了。": "Quá đã, nó thực sự làm được. Cảm giác điều khiển từ xa này thật sự rất phấn khích.",

    # Heading 1: Clawdbot 优缺点
    "Clawdbot 优缺点": "Ưu nhược điểm của Clawdbot",

    "Clawdbot 也并非完美无瑕，优缺点，我自己也做了个总结：": "Clawdbot cũng không hoàn hảo. Về ưu nhược điểm, mình cũng tự tổng kết:",
    "1、 Clawdbot 优点": "1. Ưu điểm của Clawdbot",

    # Bullet points - advantages
    "本地优先，数据隐私安全": "Ưu tiên cục bộ, bảo mật dữ liệu riêng tư",
    "— 所有数据运行在你自己的设备上，无需担心第三方访问或数据泄露": "— Toàn bộ dữ liệu chạy trên thiết bị của bạn, không lo bên thứ ba truy cập hay rò rỉ dữ liệu",
    "多平台支持": "Hỗ trợ đa nền tảng",
    "— 支持 WhatsApp、Telegram、Discord、Slack、Google Chat、Signal、iMessage 等十余个通讯平台，一个助手打通所有渠道": "— Hỗ trợ hơn 10 nền tảng nhắn tin như WhatsApp, Telegram, Discord, Slack, Google Chat, Signal, iMessage, một trợ lý kết nối tất cả kênh",
    "高度可定制": "Khả năng tùy chỉnh cao",
    "— 支持多种 AI 模型（Anthropic、OpenAI），可通过技能系统扩展功能，配置灵活": "— Hỗ trợ nhiều mô hình AI (Anthropic, OpenAI), có thể mở rộng chức năng qua hệ thống kỹ năng, cấu hình linh hoạt",
    "功能丰富强大": "Chức năng phong phú và mạnh mẽ",
    "— 内置浏览器自动化、Cron 定时任务、设备节点控制、Canvas 画布等高级工具": "— Tích hợp sẵn tự động hóa trình duyệt, tác vụ định thời Cron, điều khiển thiết bị, Canvas và các công cụ nâng cao khác",

    "2、Clawdbot 缺点": "2. Nhược điểm của Clawdbot",

    # Bullet points - disadvantages
    "技术门槛较高": "Rào cản kỹ thuật khá cao",
    "— 需要 Node.js 环境、配置文件编辑、命令行操作，对非技术用户不够友好": "— Cần môi trường Node.js, chỉnh sửa tệp cấu hình, thao tác dòng lệnh, không thân thiện với người dùng phi kỹ thuật",
    "需要自行承担成本": "Phải tự chịu chi phí",
    "— AI 模型的 API 调用费用和订阅费用需用户自己承担，长期使用成本较高": "— Chi phí gọi API mô hình AI và phí đăng ký do người dùng tự chịu, chi phí sử dụng lâu dài khá cao",
    "需维护服务器": "Cần bảo trì máy chủ",
    "— Gateway 守护进程需要持续运行，用户需要自己管理和维护服务器或本地机器": "— Tiến trình daemon Gateway cần chạy liên tục, người dùng cần tự quản lý và bảo trì máy chủ hoặc máy cục bộ",
    "安全风险": "Rủi ro bảo mật",
    "— 权限太高，大家都不敢在主电脑上玩": "— Quyền hạn quá cao, ai cũng ngại chạy trên máy tính chính",

    # Heading 1: 写在最后
    "写在最后": "Lời kết",

    "说实话，Clawdbot 并不完美。": "Nói thật, Clawdbot không hoàn hảo.",
    "门槛高，还费钱。": "Rào cản cao, lại tốn tiền.",
    "但它代表了一种未来。": "Nhưng nó đại diện cho một tương lai.",
    "一种 AI 真正属于你的未来。": "Một tương lai AI thực sự thuộc về bạn.",
    "不再是冷冰冰的网页框。": "Không còn là khung trang web lạnh lẽo.",
    "而是实实在在的私人助理。": "Mà là trợ lý cá nhân thực thụ.",
    "它住你的电脑里。": "Nó ở trong máy tính của bạn.",
    "只听你一个人的话。": "Chỉ nghe lời một mình bạn.",
    "帮干活，帮省心。": "Giúp làm việc, giúp tiết kiệm lo lắng.",
    "这才是我们想要的 AI，对吧？": "Đây mới là AI mà chúng ta muốn, phải không?",
    "虽然现在它还很稚嫩。": "Dù hiện tại nó vẫn còn non trẻ.",
    "但未来已来，值得一试。": "Nhưng tương lai đã đến, đáng để thử.",
    "折腾一下，总有收获。": "Thử nghiệm một chút, luôn có thu hoạch.",
    "如果教程对你有用。": "Nếu hướng dẫn có ích cho bạn.",
    "记得点个赞，转给需要的人。": "Nhớ bấm thích, chia sẻ cho người cần.",
    "咱们下期见。": "Hẹn gặp lại kỳ sau.",

    # Space-only text - keep as is
    " ": " ",
}

# Apply translations
translated_count = 0
kept_count = 0

for block in data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run':
            content = el['content']
            if content in translations:
                new_content = translations[content]
                if new_content != content:
                    el['content'] = new_content
                    if content.strip():
                        translated_count += 1
                else:
                    if content.strip():
                        kept_count += 1
            else:
                # Check if it's a URL or non-translatable
                if is_url(content.strip()) or has_only_special(content) or not content.strip():
                    kept_count += 1
                else:
                    print(f"WARNING: Untranslated text: {content[:80]}")
                    kept_count += 1

# Add spaces between adjacent Vietnamese text_runs
for block in data['blocks']:
    elements = block['elements']
    new_elements = []
    for i, el in enumerate(elements):
        new_elements.append(el)
    block['elements'] = new_elements

print(f"\nTranslation stats:")
print(f"  Translated: {translated_count}")
print(f"  Kept as-is: {kept_count}")
print(f"  Total text segments: {translated_count + kept_count}")

# Save translated file
with open('_art_b5_1_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nSaved to _art_b5_1_trans.json")
