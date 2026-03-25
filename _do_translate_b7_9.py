"""Translate article b7_9 from Chinese to Vietnamese"""
import json, sys, re, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art_b7_9_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def is_url(text):
    t = text.strip()
    return t.startswith('http://') or t.startswith('https://') or t.startswith('www.')

# CN -> VI translation for each text_run content
# Only translate text_run with Chinese characters
# Keep URLs, code, emoji, brand/tech names intact

cn2vi = {
    # Block 0 - title
    "把 AI 助手Moltbot 装进聊天软件，一行命令就够了":
        "Cài đặt trợ lý AI Moltbot vào phần mềm nhắn tin, chỉ cần một dòng lệnh",
    # Block 1
    "小伙伴们可以通过阿里云百炼":
        "Các bạn có thể triển khai thông qua Alibaba Cloud Bailian ",
    "来部署": " để triển khai",
    "：": ":",
    # Block 2
    "首购低至 7.9 元，续费 5 折起，支持Qwen3.5、Qwen3-max、Qwen3-coder、GLM-5、GLM-4.7、Kimi-k2.5等模型":
        "Mua lần đầu chỉ từ 7.9 NDT, gia hạn giảm 50%, hỗ trợ Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 và các mô hình khác",
    # Block 3
    "👉戳链接直达：": "👉 Truy cập trực tiếp: ",
    # Block 4
    "👉查看详细部署教程：": "👉 Xem hướng dẫn triển khai chi tiết: ",
    # Block 5
    "最多三步，即可拥有 7x 24小时在线、随时响应的AI助手":
        "Chỉ tối đa ba bước, bạn sẽ có trợ lý AI trực tuyến 7x24 giờ, phản hồi bất cứ lúc nào",
    # Block 6
    "如果你每天都在用 AI，但每次都要打开网页、登录、复制粘贴，那你该试试 ":
        "Nếu bạn dùng AI mỗi ngày, nhưng mỗi lần đều phải mở trình duyệt, đăng nhập, sao chép dán, thì bạn nên thử ",
    " 了。": ".",
    # Block 7
    "有机大橘子说：": "Hữu Cơ Đại Quất Tử nói:",
    # Block 8
    "ClawdBot/MoltBot 最大的意义在于把大众对通用 Agent 的想象进一步打开了。":
        "Ý nghĩa lớn nhất của ClawdBot/MoltBot là mở rộng thêm trí tưởng tượng của mọi người về Agent đa năng.",
    # Block 9
    "即便已经有了 Manus 这样能自己上网调研的\"通用 Agent\"":
        "Dù đã có \"Agent đa năng\" như Manus có thể tự lên mạng nghiên cứu",
    '即便已经有了 Manus 这样能自己上网调研的\u201c通用 Agent\u201d':
        'Dù đã có "Agent đa năng" như Manus có thể tự lên mạng nghiên cứu',
    # Block 10
    "即便有了 Claude Code 这样能用 Coding 解决一切开放问题的\"通用Agent\"":
        "Dù đã có \"Agent đa năng\" như Claude Code có thể dùng Coding giải quyết mọi vấn đề mở",
    '即便有了 Claude Code 这样能用 Coding 解决一切开放问题的\u201c通用Agent\u201d':
        'Dù đã có "Agent đa năng" như Claude Code có thể dùng Coding giải quyết mọi vấn đề mở',
    # Block 11
    "在这个赛道依然有巨大的想象空间和可能性":
        "Trong đường đua này vẫn còn không gian tưởng tượng và khả năng to lớn",
    # Block 12
    "垂直和通用，其实是个观测视角的问题":
        "Chuyên biệt và đa năng, thực ra là vấn đề góc nhìn quan sát",
    # Block 13
    "在通用 Agent 赛道里，大厂的创新不如个人开发者":
        "Trong đường đua Agent đa năng, sự đổi mới của các công ty lớn không bằng lập trình viên cá nhân",
    # Block 14
    "也是值得深思的": "cũng là điều đáng suy ngẫm",
    # Block 15
    "这个开源项目在 72 小时内斩获 60,000+ GitHub Stars，被开发者称为\"最接近 JARVIS 的东西\"。它能让你在 Telegram、Discord、WhatsApp 里直接@机器人对话。不只是聊天，它还能帮你整理文件、查资料、写代码、甚至主动提醒你。":
        "Dự án mã nguồn mở này đạt hơn 60.000 GitHub Stars trong 72 giờ, được các lập trình viên gọi là \"thứ gần nhất với JARVIS\". Nó cho phép bạn trực tiếp @ bot trò chuyện trong Telegram, Discord, WhatsApp. Không chỉ chat, nó còn giúp bạn sắp xếp tệp, tra cứu tài liệu, viết code, thậm chí chủ động nhắc nhở bạn.",
    # Block 16
    "你在群里发句\"把 Downloads 的 PDF 按月份分类\"，它真的会去干活。":
        "Bạn gửi một tin trong nhóm \"Phân loại PDF trong Downloads theo tháng\", nó thực sự sẽ làm luôn.",
    # Block 17
    "项目背景：从 Clawdbot 到 Moltbot 的\"大蜕壳\"":
        "Bối cảnh dự án: Cuộc \"lột xác vĩ đại\" từ Clawdbot sang Moltbot",
    # Block 18
    "2026 年 1 月 27 日，Anthropic 发了律师函，说\"Clawdbot\"跟\"Claude\"太像了。创始人 Peter Steinberger（PSPDFKit 创始人）连夜组织社区投票，在 2 小时内决定改名为 ":
        "Ngày 27 tháng 1 năm 2026, Anthropic gửi thư luật sư, nói \"Clawdbot\" quá giống \"Claude\". Nhà sáng lập Peter Steinberger (người sáng lập PSPDFKit) kết nối tổ chức bình chọn cộng đồng trong đêm, quyết định đổi tên thành ",
    "——取\"蜕壳\"之意，龙虾蜕去旧壳迎来新生。社区把这次事件称为 ":
        " — lấy ý nghĩa \"lột xác\", tôm hùm lột bỏ vỏ cũ để tái sinh. Cộng đồng gọi sự kiện này là ",
    "\"The Great Molt\"（大蜕壳）": "\"The Great Molt\" (Cuộc lột xác vĩ đại)",
    "。": ".",
    # Block 19
    "戏剧性的是，改名公告发布仅 10 秒后，骗子机器人就抢注了原 Twitter 账号发布虚假加密货币钱包地址，差点酿成 1600 万美元的诈骗事件。这也从侧面说明了这个项目有多火。":
        "Điều kịch tính là chỉ 10 giây sau khi công bố đổi tên, bot lừa đảo đã chiếm tài khoản Twitter gốc để đăng địa chỉ ví tiền điện tử giả, suýt gây ra vụ lừa đảo 16 triệu đô la. Điều này cũng cho thấy dự án này hot đến mức nào.",
    # Block 20
    "它能干什么：不只是聊天，是真的在干活":
        "Nó làm được gì: Không chỉ chat, mà thực sự đang làm việc",
    # Block 21
    "大多数人用 AI 的方式是这样的：打开浏览器 → 输入问题 → 等回答 → 复制粘贴 → 关闭网页。这个流程就像你每次想跟朋友说话，都要先坐飞机去他家。":
        "Cách hầu hết mọi người dùng AI là thế này: mở trình duyệt → nhập câu hỏi → đợi trả lời → sao chép dán → đóng trang web. Quy trình này giống như mỗi lần bạn muốn nói chuyện với bạn bè, đều phải bay máy bay đến nhà họ trước.",
    # Block 22
    "Moltbot 做的事情很简单：": "Điều Moltbot làm rất đơn giản: ",
    "把 AI 装进你每天都在用的聊天软件里":
        "đưa AI vào phần mềm nhắn tin bạn dùng hàng ngày",
    # Block 23
    "真实使用场景": "Tình huống sử dụng thực tế",
    # Block 24
    "场景": "Tình huống",
    # Block 25
    "你说的话": "Bạn nói gì",
    # Block 26
    "它做的事": "Nó làm gì",
    # Block 27
    "文件整理": "Sắp xếp tệp",
    # Block 28
    "\"把 Downloads 里的 PDF 按日期分类\"":
        "\"Phân loại PDF trong Downloads theo ngày\"",
    # Block 29
    "创建文件夹，自动归类，发报告给你":
        "Tạo thư mục, tự động phân loại, gửi báo cáo cho bạn",
    # Block 30
    "收据处理": "Xử lý hóa đơn",
    # Block 31
    "\"把这张购物小票录入表格\"":
        "\"Nhập hóa đơn mua sắm này vào bảng tính\"",
    # Block 32
    "OCR 识别，提取商品信息，生成 Excel 文件":
        "Nhận dạng OCR, trích xuất thông tin sản phẩm, tạo file Excel",
    # Block 33
    "资料查询": "Tra cứu tài liệu",
    # Block 34 (two text_runs)
    "\"React 19 新": "\"React 19 có tính năng mới ",
    "特性有哪些\"": "nào\"",
    # Block 35
    "打开浏览器搜索，筛选权威来源，总结发给你":
        "Mở trình duyệt tìm kiếm, lọc nguồn uy tín, tổng hợp gửi cho bạn",
    # Block 36
    "日程管理": "Quản lý lịch trình",
    # Block 37
    "\"提醒我明天 3 点开会\"": "\"Nhắc tôi họp lúc 3 giờ ngày mai\"",
    # Block 38
    "设置提醒，到点主动发消息":
        "Cài đặt nhắc nhở, đến giờ chủ động gửi tin nhắn",
    # Block 39
    "代码审查": "Kiểm tra code",
    # Block 40
    "\"检查一下今天的 GitHub 提交\"":
        "\"Kiểm tra các commit GitHub hôm nay\"",
    # Block 41
    "拉取代码，分析变更，输出审查意见":
        "Pull code, phân tích thay đổi, xuất ý kiến review",
    # Block 42
    "主动简报": "Bản tin chủ động",
    # Block 43
    "每天早上 7 点自动发送": "Tự động gửi lúc 7 giờ sáng mỗi ngày",
    # Block 44
    "天气、日程、重要邮件摘要，无需你问":
        "Thời tiết, lịch trình, tóm tắt email quan trọng, không cần bạn hỏi",
    # Block 45
    "浏览器自动化": "Tự động hóa trình duyệt",
    # Block 46
    "\"帮我在亚马逊上找这款商品\"":
        "\"Giúp tôi tìm sản phẩm này trên Amazon\"",
    # Block 47
    "打开网页、搜索、比价、返回结果":
        "Mở trang web, tìm kiếm, so sánh giá, trả về kết quả",
    # Block 48
    "核心能力": "Năng lực cốt lõi",
    # Block 49
    "1. 持久记忆": "1. Bộ nhớ lâu dài",
    # Block 50
    "不像普通 AI 每次对话都\"失忆\"，Moltbot 会记住你的偏好。你说过一次\"我喜欢 Markdown 格式的邮件\"，以后它都会自动这么处理。所有记忆以 Markdown 文件存储在你本地，随时可以查看和修改。":
        "Không giống AI thông thường \"mất trí nhớ\" sau mỗi cuộc trò chuyện, Moltbot sẽ nhớ sở thích của bạn. Bạn chỉ cần nói một lần \"Tôi thích email định dạng Markdown\", sau đó nó sẽ tự động xử lý như vậy. Toàn bộ bộ nhớ được lưu dưới dạng file Markdown trên máy bạn, có thể xem và chỉnh sửa bất cứ lúc nào.",
    # Block 51
    "2. 主动通知": "2. Thông báo chủ động",
    # Block 52
    "设置\"心跳\"（Heartbeat）让它每 30 分钟检查一次：有没有紧急邮件？今天有什么日程？如果它发现需要你关注的事情，会主动发消息给你。":
        "Cài đặt \"nhịp tim\" (Heartbeat) để nó kiểm tra mỗi 30 phút: có email khẩn cấp không? Hôm nay có lịch trình gì? Nếu nó phát hiện điều cần bạn chú ý, sẽ chủ động gửi tin nhắn cho bạn.",
    # Block 53
    "3. 真实执行": "3. Thực thi thực tế",
    # Block 54
    "它能执行 Shell 命令、操作文件系统、控制浏览器、发送邮件。失败了还会自己反思哪里错了，改完再试。":
        "Nó có thể thực thi lệnh Shell, thao tác hệ thống tệp, điều khiển trình duyệt, gửi email. Thất bại thì tự suy ngẫm sai ở đâu, sửa xong thử lại.",
    # Block 55
    "安装只需要一行命令": "Cài đặt chỉ cần một dòng lệnh",
    # Block 56
    "我见过太多\"保姆级教程\"最后把人劝退的。什么\"首先安装 Node.js，然后配置环境变量，接着修改系统路径\"——看到这种开头，大部分人已经关掉网页了。":
        "Tôi đã thấy quá nhiều \"hướng dẫn siêu chi tiết\" cuối cùng khiến người ta bỏ cuộc. Nào là \"trước hết cài Node.js, rồi cấu hình biến môi trường, tiếp theo sửa đường dẫn hệ thống\" — thấy mở đầu kiểu này, hầu hết mọi người đã đóng trang web rồi.",
    # Block 57
    "Moltbot 的安装方式只有一行命令。":
        "Cách cài đặt Moltbot chỉ có một dòng lệnh.",
    # Block 58
    "macOS / Linux:": "macOS / Linux:",
    # Block 59
    "Windows PowerShell:": "Windows PowerShell:",
    # Block 60
    "脚本会自动检测系统，装好所有依赖（包括 Node.js 22+），然后弹出配置向导。":
        "Script sẽ tự động phát hiện hệ thống, cài đầy đủ các phụ thuộc (bao gồm Node.js 22+), sau đó hiển thị trình hướng dẫn cấu hình.",
    # Block 61
    "装完之后运行：": "Sau khi cài xong, chạy:",
    # Block 62
    "就这么多。": "Chỉ vậy thôi.",
    # Block 63
    "注意：本地电脑安全问题需要注意，建议开VPS虚拟机":
        "Lưu ý: Cần chú ý vấn đề bảo mật máy tính cục bộ, khuyến nghị dùng VPS hoặc máy ảo",
    # Block 64
    "配置向导：回答三个问题":
        "Trình hướng dẫn cấu hình: Trả lời ba câu hỏi",
    # Block 65
    "第一个问题：本地用还是云端用？":
        "Câu hỏi thứ nhất: Dùng cục bộ hay trên cloud?",
    # Block 66
    "：装在自己电脑上，适合个人使用（安全性需要重点注意，可以操控你的电脑，甚至格式化）":
        ": Cài trên máy tính cá nhân, phù hợp sử dụng cá nhân (cần đặc biệt chú ý bảo mật, có thể điều khiển máy tính của bạn, thậm chí format)",
    # Block 67
    "：扔到服务器上 24 小时跑，适合团队协作":
        ": Đưa lên server chạy 24 giờ, phù hợp làm việc nhóm",
    # Block 68
    "熟悉后再考虑云服务器（腾讯云 Lighthouse、阿里云等月租几十块就能跑）。":
        "Khi đã quen thì hãy cân nhắc cloud server (Tencent Cloud Lighthouse, Alibaba Cloud... thuê tháng vài chục nghìn đồng là chạy được).",
    # Block 69
    "第二个问题：用哪家的 AI？":
        "Câu hỏi thứ hai: Dùng AI của hãng nào?",
    # Block 70
    "Anthropic 的 Claude": "Anthropic Claude",
    "推荐 ": "Khuyên dùng ",
    # Block 71
    "模型选 ": "Chọn mô hình ",
    " 最强，或者 ": " mạnh nhất, hoặc ",
    " 性价比高": " có hiệu suất chi phí cao",
    # Block 72
    "API Key 在 ": "Lấy API Key tại ",
    " 获取": "",
    # Block 73
    "也可以选：": "Cũng có thể chọn:",
    # Block 74
    "：在 ": ": Lấy API Key tại ",
    " 获取 API Key": "",
    # Block 75
    "本地模型": "Mô hình cục bộ",
    "：用 Ollama 运行 Llama、Mistral 等，完全免费":
        ": Dùng Ollama chạy Llama, Mistral..., hoàn toàn miễn phí",
    # Block 76
    "当然性价比最高的还是国产模型：\n":
        "Tất nhiên hiệu suất chi phí cao nhất vẫn là các mô hình nội địa Trung Quốc:\n",
    # Block 77
    "GLM 4.7 因为 coding plan 性价比太高，直接卖脱销了":
        "GLM 4.7 vì coding plan hiệu suất chi phí quá cao, bán hết sạch luôn",
    # Block 78
    "MiniMax m2.1 因为 Agent 能力强被 clawdbot 御用也被拉爆了":
        "MiniMax m2.1 vì khả năng Agent mạnh được clawdbot chọn dùng nên cũng quá tải",
    # Block 79
    "Kimi K2.5 发布，多模态加持的 coding，前端能力顶上来了":
        "Kimi K2.5 ra mắt, coding được tăng cường đa phương thức, năng lực frontend đã được nâng tầm",
    # Block 80
    "第三个问题：在哪个聊天软件里用？":
        "Câu hỏi thứ ba: Dùng trên phần mềm nhắn tin nào?",
    # Block 81
    "Telegram（最简单）：": "Telegram (đơn giản nhất):",
    # Block 82
    "找 @BotFather，发送 ": "Tìm @BotFather, gửi ",
    # Block 83
    "按提示设置名称": "Đặt tên theo hướng dẫn",
    # Block 84
    "拿到 token（一串数字和字母）": "Nhận token (một chuỗi số và chữ cái)",
    # Block 85
    "粘贴到配置里": "Dán vào cấu hình",
    # Block 86
    "Discord：": "Discord:",
    # Block 87
    "去 ": "Truy cập ",
    "Discord 开发者后台": "Discord Developer Portal",
    # Block 88
    "创建新应用 → Bot → 获取 Token":
        "Tạo ứng dụng mới → Bot → Lấy Token",
    # Block 89
    "WhatsApp：": "WhatsApp:",
    # Block 90
    "运行 ": "Chạy ",
    # Block 91
    "扫描二维码完成配对": "Quét mã QR để hoàn tất kết nối",
    # Block 92
    "配置完成后，在聊天软件里给机器人发条消息，它回复了就说明成功了。":
        "Sau khi cấu hình xong, gửi một tin nhắn cho bot trong phần mềm nhắn tin, nếu nó trả lời thì nghĩa là đã thành công.",
    # Block 93
    "如果有问题随时问AI": "Nếu có vấn đề gì cứ hỏi AI bất cứ lúc nào",
    # Block 94
    "进阶配置：让它主动为你工作":
        "Cấu hình nâng cao: Để nó chủ động làm việc cho bạn",
    # Block 95
    "设置每日简报（Cron 任务）": "Cài đặt bản tin hàng ngày (Cron Task)",
    # Block 96
    "设置心跳监控": "Cài đặt giám sát nhịp tim",
    # Block 97
    "编辑 ": "Chỉnh sửa ",
    # Block 98
    "在配置文件中设置：": "Cài đặt trong file cấu hình:",
    # Block 99
    "但这玩意儿有风险": "Nhưng thứ này có rủi ro",
    # Block 100
    "装完之后我没有立刻开始用。因为 Moltbot 要求的权限很高。":
        "Sau khi cài xong tôi không dùng ngay. Vì Moltbot yêu cầu quyền hạn rất cao.",
    # Block 101
    "它能访问你的文件系统，能执行 Shell 命令，能读写任何文件。这意味着什么？意味着如果 AI 误判了你的指令，或者有人通过提示词注入攻击控制了你的机器人，它可以删掉你硬盘上的所有东西。":
        "Nó có thể truy cập hệ thống tệp của bạn, thực thi lệnh Shell, đọc ghi bất kỳ file nào. Điều này có nghĩa gì? Nghĩa là nếu AI hiểu sai lệnh của bạn, hoặc ai đó thông qua tấn công prompt injection chiếm quyền điều khiển bot của bạn, nó có thể xóa mọi thứ trên ổ cứng của bạn.",
    # Block 102
    "这不是危言耸听。AI 不是人，它没有常识，它只会按照概率最高的方式理解你的话。你说\"清理一下桌面\"，它可能真的把 Desktop 文件夹清空了。":
        "Đây không phải nói quá. AI không phải người, nó không có nhận thức thường thức, nó chỉ hiểu lời bạn theo cách xác suất cao nhất. Bạn nói \"Dọn dẹp màn hình desktop\", nó có thể thực sự xóa sạch thư mục Desktop.",
    # Block 103
    "开发者在文档里写得很清楚：":
        "Nhà phát triển đã viết rất rõ trong tài liệu: ",
    "不要把它装在存有钱包、私钥、重要账号的电脑上":
        "Không cài nó trên máy tính chứa ví, private key, tài khoản quan trọng",
    # Block 104
    "安全建议": "Khuyến nghị bảo mật",
    # Block 105
    "✅ 推荐做法": "✅ Nên làm",
    # Block 106
    "❌ 避免做法": "❌ Nên tránh",
    # Block 107
    "装在云服务器上（隔离环境）":
        "Cài trên cloud server (môi trường cách ly)",
    # Block 108
    "装在主力工作机上": "Cài trên máy làm việc chính",
    # Block 109
    "装在虚拟机里": "Cài trong máy ảo",
    # Block 110
    "处理敏感财务数据": "Xử lý dữ liệu tài chính nhạy cảm",
    # Block 111
    "用闲置的旧电脑": "Dùng máy tính cũ không dùng",
    # Block 112
    "给予不必要的系统权限": "Cấp quyền hệ thống không cần thiết",
    # Block 113
    "定期备份重要数据": "Sao lưu dữ liệu quan trọng định kỳ",
    # Block 114
    "在公共网络暴露 Gateway": "Để lộ Gateway trên mạng công cộng",
    # Block 115
    "更多实战案例": "Thêm các ví dụ thực tế",
    # Block 116
    "案例 1：自动整理发票": "Ví dụ 1: Tự động sắp xếp hóa đơn",
    # Block 117
    "用户 @dev_john 分享：每个月底让 Moltbot 扫描 ":
        "Người dùng @dev_john chia sẻ: Cuối mỗi tháng cho Moltbot quét thư mục ",
    " 文件夹，按公司名称分类，生成月度支出汇总表，发送到 Slack。":
        ", phân loại theo tên công ty, tạo bảng tổng hợp chi tiêu hàng tháng, gửi đến Slack.",
    # Block 118
    "案例 2：代码审查助手": "Ví dụ 2: Trợ lý review code",
    # Block 119
    "开发团队把 Moltbot 接入 Discord，每天早上自动拉取前一天的 GitHub PR，用 Claude 分析代码变更，输出审查意见发到频道。":
        "Đội phát triển kết nối Moltbot vào Discord, mỗi sáng tự động pull các GitHub PR của ngày hôm trước, dùng Claude phân tích thay đổi code, xuất ý kiến review gửi vào kênh.",
    # Block 120
    "案例 3：智能购物比价": "Ví dụ 3: So sánh giá mua sắm thông minh",
    # Block 121
    "用户 @sarah_tech 设置：看到想买的商品，把链接发给 Moltbot，它会自动打开浏览器，在 Amazon、京东、淘宝比价，返回最低价和历史价格走势。":
        "Người dùng @sarah_tech thiết lập: Thấy sản phẩm muốn mua, gửi link cho Moltbot, nó sẽ tự mở trình duyệt, so sánh giá trên Amazon, JD.com, Taobao, trả về giá thấp nhất và xu hướng giá lịch sử.",
    # Block 122
    "案例 4：语音笔记转录": "Ví dụ 4: Chuyển đổi ghi chú thoại",
    # Block 123
    "收到 Telegram 语音消息后，Moltbot 自动转录成文字，提取待办事项，添加到 Todoist。":
        "Sau khi nhận tin nhắn thoại Telegram, Moltbot tự động chuyển thành văn bản, trích xuất công việc cần làm, thêm vào Todoist.",
    # Block 124
    "关于隐私": "Về quyền riêng tư",
    # Block 125
    "有人会问：这东西会不会偷我的数据？":
        "Có người sẽ hỏi: Thứ này có đánh cắp dữ liệu của tôi không?",
    # Block 126
    "Moltbot 的设计是": "Thiết kế của Moltbot là ",
    "\"本地优先\"": "\"ưu tiên cục bộ\"",
    " ：": ":",
    # Block 127
    "对话记录存在你自己的设备上，Markdown 格式，随时可以打开看":
        "Lịch sử trò chuyện lưu trên thiết bị của bạn, định dạng Markdown, bất cứ lúc nào cũng có thể mở xem",
    # Block 128
    "Gateway 服务运行在 localhost，不会暴露到公网":
        "Dịch vụ Gateway chạy trên localhost, không bị lộ ra mạng công cộng",
    # Block 129
    "唯一需要联网的是调用 AI 模型的时候，但那是你自己的 API 密钥，数据直接发给 Anthropic 或 OpenAI，不经过第三方":
        "Lần duy nhất cần kết nối mạng là khi gọi mô hình AI, nhưng đó là API key của chính bạn, dữ liệu gửi trực tiếp đến Anthropic hoặc OpenAI, không qua bên thứ ba",
    # Block 130
    "换句话说，": "Nói cách khác, ",
    "除了 AI 供应商，没人能看到你的对话内容":
        "ngoài nhà cung cấp AI, không ai có thể xem nội dung trò chuyện của bạn",
    # Block 131
    "当然，前提是你别把它部署在不可信的云服务器上，别用来处理真正敏感的信息。":
        "Tất nhiên, tiền đề là bạn không triển khai nó trên cloud server không đáng tin, không dùng để xử lý thông tin thực sự nhạy cảm.",
    # Block 132
    "总结": "Tổng kết",
    # Block 133
    "这个时代的 AI 工具太多了，多到让人麻木。但真正有用的不多。大部分都是套壳产品，换个界面，改个名字，本质上还是那套东西。":
        "Công cụ AI thời đại này quá nhiều, nhiều đến mức tê liệt. Nhưng thực sự hữu ích thì không nhiều. Phần lớn là sản phẩm bọc lại, đổi giao diện, đổi tên, bản chất vẫn là thứ cũ.",
    # Block 134
    "Moltbot 不一样。它不是在教你怎么用 AI，而是":
        "Moltbot thì khác. Nó không dạy bạn cách dùng AI, mà là ",
    "让 AI 融入你的日常工具里，变成一个随时待命的助手":
        "để AI hòa nhập vào công cụ hàng ngày của bạn, trở thành trợ lý luôn sẵn sàng",
    # Block 135
    "适合使用的人": "Đối tượng phù hợp",
    # Block 136
    "频繁使用 AI 助手的开发者和效率党":
        "Lập trình viên và người yêu hiệu suất thường xuyên dùng trợ lý AI",
    # Block 137
    "需要 AI 自动化处理任务的用户":
        "Người dùng cần AI tự động xử lý tác vụ",
    # Block 138
    "有独立设备（云服务器/虚拟机）可以部署的用户":
        "Người dùng có thiết bị riêng (cloud server/máy ảo) để triển khai",
    # Block 139
    "想体验\"未来个人助理\"的早期尝鲜者":
        "Người muốn trải nghiệm \"trợ lý cá nhân tương lai\" sớm nhất",
    # Block 140
    "不适合的人": "Đối tượng không phù hợp",
    # Block 141
    "完全不熟悉命令行的小白":
        "Người mới hoàn toàn không quen với dòng lệnh",
    # Block 142
    "只能在主力机上使用的用户":
        "Người dùng chỉ có thể sử dụng trên máy làm việc chính",
    # Block 143
    "对安全风险零容忍的场景":
        "Tình huống không chấp nhận bất kỳ rủi ro bảo mật nào",
    # Block 144
    "没有 API 预算（Claude API 每月约 $20）":
        "Không có ngân sách API (Claude API khoảng $20/tháng)",
    # Block 145
    "它不完美，有风险，需要折腾，但它是真的在解决问题。这就够了。":
        "Nó không hoàn hảo, có rủi ro, cần mày mò, nhưng nó thực sự đang giải quyết vấn đề. Vậy là đủ.",
    # Block 146
    "参考资源": "Tài liệu tham khảo",
    # Block 147
    "GitHub 仓库": "Kho GitHub",
    # Block 148
    "官方网站": "Website chính thức",
    # Block 149
    "社区 Discord": "Discord cộng đồng",
}

# Process the data
translated = copy.deepcopy(data)
stats = {"total": 0, "translated": 0, "kept": 0}

for block in translated["blocks"]:
    for el in block["elements"]:
        if el["type"] != "text_run":
            continue
        stats["total"] += 1
        content = el["content"]

        # Skip URLs
        if is_url(content):
            stats["kept"] += 1
            continue

        # Skip code-only elements (inline_code style)
        if el.get("style", {}).get("inline_code", False) and not has_chinese(content):
            stats["kept"] += 1
            continue

        # Try exact match first
        if content in cn2vi:
            el["content"] = cn2vi[content]
            stats["translated"] += 1
        elif has_chinese(content):
            # Mark untranslated Chinese
            print(f"WARNING: Untranslated Chinese text: {content[:80]}")
            stats["kept"] += 1
        else:
            stats["kept"] += 1

# Add space between adjacent Vietnamese text_runs where needed
for block in translated["blocks"]:
    elements = block["elements"]
    for i in range(len(elements) - 1):
        el = elements[i]
        next_el = elements[i + 1]
        if el["type"] == "text_run" and next_el["type"] == "text_run":
            curr = el["content"]
            nxt = next_el["content"]
            # Add space if current doesn't end with space/punctuation and next doesn't start with space/punctuation
            if (curr and nxt and
                not curr[-1] in ' \n\t:.,;!?、，。；！？：' and
                not nxt[0] in ' \n\t:.,;!?、，。；！？：' and
                not is_url(curr) and not is_url(nxt)):
                # Check if both are Vietnamese text (not code)
                if not el.get("style", {}).get("inline_code", False) and not next_el.get("style", {}).get("inline_code", False):
                    # Only add if looks like it needs it
                    if re.search(r'[a-zA-ZÀ-ỹ0-9\)\"\']$', curr) and re.search(r'^[a-zA-ZÀ-ỹ0-9\(\"\']', nxt):
                        el["content"] = curr + " "

# Save
with open('_art_b7_9_trans.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f"\nStats:")
print(f"  Total text_runs: {stats['total']}")
print(f"  Translated: {stats['translated']}")
print(f"  Kept as-is: {stats['kept']}")
print(f"\nSaved to _art_b7_9_trans.json")
