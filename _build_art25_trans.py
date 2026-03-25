#!/usr/bin/env python3
"""Build translation for article 25 - CN to VI"""
import json
import re
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Load original
with open('_art25_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation map: Chinese -> Vietnamese
trans = {
    "03-03直播回放 | 卡尔：花10分钟用Obsidian+OpenClaw彻底重构你的AI知识管理体系":
        "03-03 Phát lại livestream | Carl: Dành 10 phút dùng Obsidian+OpenClaw tái cấu trúc hoàn toàn hệ thống quản lý tri thức AI của bạn",
    "\n🎤 特邀嘉宾\n卡尔的AI沃茨：公众号AI自媒体Top10、视频号AI自媒体Top30、前字节大模型算法工程师\n\n💡 直播核心亮点：\n✅ 全程实操｜带你用「Obsidian+OpenClaw」构建高效知识管理体系\n✅ 避坑指南｜拆解各个工具使用痛点与技巧，助你少走弯路快速上手\n":
        "\n🎤 Khách mời đặc biệt\nAI Watts của Carl: Top 10 tài khoản công khai AI tự truyền thông, Top 30 video AI tự truyền thông, cựu kỹ sư thuật toán mô hình lớn tại ByteDance\n\n💡 Điểm nổi bật của buổi livestream:\n✅ Thực hành toàn bộ | Hướng dẫn bạn xây dựng hệ thống quản lý tri thức hiệu quả bằng「Obsidian+OpenClaw」\n✅ Hướng dẫn tránh bẫy | Phân tích điểm đau và mẹo sử dụng từng công cụ, giúp bạn ít đi đường vòng và nhanh chóng bắt đầu\n",
    "WaytoAGI晚8点共学 2026年3月3日":
        "WaytoAGI Học chung lúc 8 giờ tối ngày 3 tháng 3 năm 2026",
    "回放": "Phát lại",
    "🎤 特邀嘉宾": "🎤 Khách mời đặc biệt",
    "卡尔的AI沃茨：公众号AI自媒体Top10、视频号AI自媒体Top30、前字节大模型算法工程师":
        "AI Watts của Carl: Top 10 tài khoản công khai AI tự truyền thông, Top 30 video AI tự truyền thông, cựu kỹ sư thuật toán mô hình lớn tại ByteDance",
    "总结": "Tổng kết",
    "本次会议由 AJ 主持，特别邀请卡尔分享其利用 obsidian 与 openclaw 组合搭建 AI 知识管理体系的经验。卡尔介绍工具选择原因、体系搭建方法、插件使用技巧等内容，并解答参会者疑问。内容如下：":
        "Buổi họp này do AJ chủ trì, đặc biệt mời Carl chia sẻ kinh nghiệm xây dựng hệ thống quản lý tri thức AI bằng cách kết hợp Obsidian và OpenClaw. Carl giới thiệu lý do chọn công cụ, phương pháp xây dựng hệ thống, mẹo sử dụng plugin và giải đáp thắc mắc của người tham dự. Nội dung như sau:",
    "分享背景与目标": "Bối cảnh và mục tiêu chia sẻ",
    "爆文引发关注": "Bài viết viral thu hút sự chú ý",
    "爆文影响力：卡尔近期撰写的几篇文章成为爆文，尤其是关于 obsidian 与小龙虾、Openclaw 组合的文章，详细介绍使用方法与思路，阅读量高，受到广泛好评，引发大家对其知识管理体系的关注。":
        "Sức ảnh hưởng của bài viết viral: Một số bài viết gần đây của Carl đã trở thành bài viral, đặc biệt là bài về sự kết hợp giữa Obsidian và OpenClaw, giới thiệu chi tiết phương pháp sử dụng và ý tưởng, lượng đọc cao, được đánh giá tốt rộng rãi, thu hút sự chú ý của mọi người đến hệ thống quản lý tri thức của anh.",
    "分享目的：为让大家深入了解该体系搭建过程与思路，AJ 邀请卡尔进行本次分享，希望参会者能从中获得启发，提升自身知识管理能力。":
        "Mục đích chia sẻ: Để mọi người hiểu sâu về quá trình xây dựng và ý tưởng của hệ thống này, AJ mời Carl thực hiện buổi chia sẻ, hy vọng người tham dự có thể nhận được cảm hứng và nâng cao khả năng quản lý tri thức của bản thân.",
    "知识管理目标": "Mục tiêu quản lý tri thức",
    "内容产出目标：卡尔作为重度笔记用户，希望实现视频与图文日更。目前图文已能做到日更，但视频更新还存在困难，因此希望通过搭建知识管理体系加速内容产出。":
        "Mục tiêu sản xuất nội dung: Carl là người dùng ghi chú nặng, hy vọng đạt được cập nhật hàng ngày cả video và đồ họa. Hiện tại đồ họa đã có thể cập nhật hàng ngày, nhưng cập nhật video vẫn còn khó khăn, vì vậy hy vọng thông qua xây dựng hệ thống quản lý tri thức để tăng tốc sản xuất nội dung.",
    "信息整合需求：卡尔日常信息来源分散，包括飞书、苹果备忘录、各类网站等，需要一个有效的工具将这些信息整合到一起，便于管理与使用，":
        "Nhu cầu tích hợp thông tin: Nguồn thông tin hàng ngày của Carl phân tán, bao gồm Feishu, Apple Notes, các trang web khác nhau, cần một công cụ hiệu quả để tích hợp các thông tin này lại với nhau, thuận tiện cho việc quản lý và sử dụng,",
    "obsidian 成为他的选择。": "Obsidian trở thành lựa chọn của anh ấy.",
    "工具选择与迁移原因": "Lý do chọn công cụ và di chuyển",
    "笔记软件对比": "So sánh phần mềm ghi chú",
    "多软件使用体验：卡尔曾使用过 ": "Trải nghiệm sử dụng nhiều phần mềm: Carl đã từng sử dụng ",
    "notion、Flomo、滴答、飞书等": "Notion, Flomo, TickTick, Feishu và các phần mềm khác",
    "多种笔记软件，但最终选择将所有内容迁移到 obsidian。他认为这些软件各有特点，但 obsidian 在与 AI 结合以及知识管理方面具有独特优势。":
        "nhiều loại phần mềm ghi chú, nhưng cuối cùng chọn di chuyển tất cả nội dung sang Obsidian. Anh cho rằng các phần mềm này đều có đặc điểm riêng, nhưng Obsidian có ưu thế độc đáo trong việc kết hợp với AI và quản lý tri thức.",
    "obsidian 优势体现：obsidian 发展多年，拥有丰富的插件和主题，即使在没有 AI 之前，也是一款优秀的笔记软件。它能够更好地呈现知识内容，实现内容的关联，与小龙虾等工具共创，为知识管理提供了更多可能性。":
        "Ưu thế của Obsidian: Obsidian phát triển nhiều năm, có plugin và chủ đề phong phú, ngay cả trước khi có AI, nó đã là một phần mềm ghi chú xuất sắc. Nó có thể trình bày nội dung tri thức tốt hơn, thực hiện liên kết nội dung, đồng sáng tạo với các công cụ như OpenClaw, mang lại nhiều khả năng hơn cho quản lý tri thức.",
    "GPT 与 Claude 选择": "Lựa chọn giữa GPT và Claude",
    "GPT 记忆系统局限：卡尔提到 GPT 有较好的记忆系统，但在信息导出方面存在限制，只能导出部分对话记录，不能代表全部信息。而 Claude 虽然可以通过新机制导入对话记录，但信息完整性不足。":
        "Hạn chế của hệ thống bộ nhớ GPT: Carl đề cập GPT có hệ thống bộ nhớ khá tốt, nhưng có hạn chế trong xuất thông tin, chỉ có thể xuất một phần lịch sử hội thoại, không thể đại diện cho toàn bộ thông tin. Còn Claude tuy có thể nhập lịch sử hội thoại thông qua cơ chế mới, nhưng tính toàn vẹn thông tin không đủ.",
    "Claude 安装便利性：Claude 的安装门槛较低，使用 ": "Sự tiện lợi cài đặt Claude: Ngưỡng cài đặt Claude khá thấp, sử dụng ",
    " 输入指令即可完成安装。例如输入"": " nhập lệnh là có thể hoàn thành cài đặt. Ví dụ nhập \"",
    "帮我安装 obsidian，并让我在里面使用 Claude": "Giúp tôi cài đặt Obsidian và cho phép tôi sử dụng Claude trong đó",
    ""，就能轻松完成安装。": "\", là có thể dễ dàng hoàn thành cài đặt.",
    "信息收录与插件安装": "Thu thập thông tin và cài đặt plugin",
    "信息收录思路": "Ý tưởng thu thập thông tin",
    "解决信息分散问题：卡尔面临信息散落在多个平台的问题，他希望将这些信息全部收录到 obsidian 中。为此，他尝试了多种方法，最终确定了一套可行的方案。":
        "Giải quyết vấn đề thông tin phân tán: Carl đối mặt với vấn đề thông tin rải rác trên nhiều nền tảng, anh hy vọng thu thập tất cả thông tin này vào Obsidian. Vì vậy, anh đã thử nhiều phương pháp và cuối cùng xác định được một bộ giải pháp khả thi.",
    "节省 API 使用：在信息收录过程中，卡尔尽量节省 API 的使用，因为每天更新的消息量较大，使用 API 会产生较高成本。他仅将 API 用于翻译标题，以降低成本。":
        "Tiết kiệm sử dụng API: Trong quá trình thu thập thông tin, Carl cố gắng tiết kiệm sử dụng API, vì lượng tin nhắn cập nhật hàng ngày rất lớn, sử dụng API sẽ tạo ra chi phí cao. Anh chỉ dùng API để dịch tiêu đề, nhằm giảm chi phí.",
    "插件安装介绍": "Giới thiệu cài đặt plugin",
    "飞书文档下载插件：该插件可将飞书文档下载为 Markdown 格式，除多维表格外，视频、PDF 等文档均可下载。多维表格由于体系较难替代，卡尔保留了部分在飞书中。":
        "Plugin tải tài liệu Feishu: Plugin này có thể tải tài liệu Feishu về định dạng Markdown, ngoại trừ bảng đa chiều, video, PDF và các tài liệu khác đều có thể tải. Bảng đa chiều do hệ thống khó thay thế nên Carl giữ lại một phần trên Feishu.",
    "obsidian 检藏工具：此工具比直接转发更具优势，它能显示来源，自动打 tag，可自定义规则。但在爬取图片或视频时，若不是图床或在线预览形式，可能会丢失部分视频，仅保留链接。":
        "Công cụ lưu trữ Obsidian: Công cụ này có ưu thế hơn so với chuyển tiếp trực tiếp, nó có thể hiển thị nguồn, tự động gắn tag, có thể tùy chỉnh quy tắc. Nhưng khi thu thập hình ảnh hoặc video, nếu không phải dạng hosting ảnh hoặc xem trước trực tuyến, có thể mất một số video, chỉ giữ lại liên kết.",
    "obsidian AI 视频笔记与截图插件：支持多种平台，可用于处理 Youtube 等平台的视频。卡尔还提到微信助手可解决视频获取难题，也可使用 open API 实现。":
        "Plugin ghi chú video AI và chụp màn hình Obsidian: Hỗ trợ nhiều nền tảng, có thể dùng để xử lý video từ Youtube và các nền tảng khác. Carl cũng đề cập rằng trợ lý WeChat có thể giải quyết vấn đề lấy video, cũng có thể sử dụng open API để thực hiện.",
    "知识管理体系构建": "Xây dựng hệ thống quản lý tri thức",
    "文件结构设计": "Thiết kế cấu trúc tệp",
    "结构层次介绍：卡尔展示的 obsidian 页面从上到下包括收件箱、日记、项目研究知识库、资源管理系统、微信笔记同步助手、日报等。每个部分都有特定的功能，用于存储和管理不同类型的信息。":
        "Giới thiệu các tầng cấu trúc: Trang Obsidian mà Carl trình bày từ trên xuống dưới bao gồm hộp thư đến, nhật ký, kho tri thức nghiên cứu dự án, hệ thống quản lý tài nguyên, trợ lý đồng bộ ghi chú WeChat, báo cáo hàng ngày, v.v. Mỗi phần đều có chức năng cụ thể, dùng để lưu trữ và quản lý các loại thông tin khác nhau.",
    "避免混淆问题：虽然网上有近 5000 种不同的文件结构，但卡尔认为大家可能混淆了概念。只要在 agents 与 cloud、Gemini 等文件中明确写明文件结构，AI 就能自动生成相应的文件，无需人工过多编辑。":
        "Tránh nhầm lẫn: Mặc dù trên mạng có gần 5000 loại cấu trúc tệp khác nhau, nhưng Carl cho rằng mọi người có thể đã nhầm lẫn khái niệm. Chỉ cần ghi rõ cấu trúc tệp trong các tệp agents, cloud, Gemini, v.v., AI có thể tự động tạo các tệp tương ứng, không cần chỉnh sửa thủ công quá nhiều.",
    "初始结构推荐：卡尔推荐大家使用 Github 上的中文版本作为 obsidian 的初始文件结构，该结构与他自己使用的类似，他在其中增加了额外的工作流存储。":
        "Đề xuất cấu trúc ban đầu: Carl khuyến nghị mọi người sử dụng phiên bản tiếng Trung trên Github làm cấu trúc tệp ban đầu cho Obsidian, cấu trúc này tương tự như cấu trúc mà anh sử dụng, anh đã thêm lưu trữ quy trình công việc bổ sung vào đó.",
    "AI 部署选择": "Lựa chọn triển khai AI",
    "code x 优势体现：卡尔选择 code x 而非 call flow 进行 AI 部署，因为 code 存在一次性只能创建三个新建对话、无法管理定时任务、上下文读取信息链条长等缺点。而 code x 已成为他主流的管理 obsidian 的页面，搜索速度较快，能满足复杂需求。":
        "Ưu thế của Code X: Carl chọn Code X thay vì Call Flow để triển khai AI, vì Code có nhược điểm chỉ tạo được ba cuộc hội thoại mới cùng lúc, không thể quản lý tác vụ hẹn giờ, chuỗi đọc thông tin ngữ cảnh dài. Code X đã trở thành trang quản lý Obsidian chính của anh, tốc độ tìm kiếm nhanh, có thể đáp ứng nhu cầu phức tạp.",
    "对话优化策略：为节省 TOKEN，卡尔采用不同项目问题分类检索的方法，先搜项目，其次研究，再是知识库，最后全库扫描。对话结束后，将记录写入当天流水，重大对话记录更新到 memory。":
        "Chiến lược tối ưu hội thoại: Để tiết kiệm TOKEN, Carl áp dụng phương pháp tìm kiếm phân loại theo dự án khác nhau, tìm dự án trước, sau đó nghiên cứu, tiếp theo là kho tri thức, cuối cùng quét toàn bộ kho. Sau khi kết thúc hội thoại, ghi nhận vào nhật ký trong ngày, các bản ghi hội thoại quan trọng được cập nhật vào memory.",
    "遗忘检测方法：卡尔发现与 Claude 对话时，它遗忘速度较快，因此设置指令进行确认。若对话五六十轮后，Claude 能回复"卡尔真棒"，则表示它还能记住信息，否则需开启新的对话记录。":
        "Phương pháp phát hiện quên: Carl phát hiện khi trò chuyện với Claude, nó quên khá nhanh, vì vậy đặt lệnh để xác nhận. Nếu sau năm sáu mươi lượt hội thoại, Claude có thể trả lời \"Carl thật tuyệt\", điều đó cho thấy nó vẫn nhớ thông tin, nếu không thì cần mở bản ghi hội thoại mới.",
    "插件推荐与使用方法": "Đề xuất plugin và phương pháp sử dụng",
    "三方插件推荐": "Đề xuất plugin bên thứ ba",
    "笔记同步助手：在微信中搜索该公众号，设置 TOKEN 后，可将小红书、图文等链接同步到 obsidian，无需复杂设置。":
        "Trợ lý đồng bộ ghi chú: Tìm kiếm tài khoản công khai này trong WeChat, sau khi thiết lập TOKEN, có thể đồng bộ liên kết từ Xiaohongshu, đồ họa, v.v. sang Obsidian, không cần thiết lập phức tạp.",
    "obshare 插件：用于将 obsidian 内容上传到飞书，卡尔因依赖飞书分享内容而安装此插件，但它在同步图片时可能会有一定概率丢失。":
        "Plugin obshare: Dùng để tải nội dung Obsidian lên Feishu, Carl cài đặt plugin này vì phụ thuộc vào Feishu để chia sẻ nội dung, nhưng nó có thể có xác suất mất ảnh khi đồng bộ.",
    "插件下载方法": "Phương pháp tải plugin",
    "code x 辅助安装：对于未使用 call code 的朋友，推荐使用 code x 下载插件。与 code x 对话后可归档项目，项目可直接连接到 obsidian 目录。例如，让 code x 汇总与 open craps 联网搜索相关的项目，它能快速给出结果。":
        "Cài đặt hỗ trợ bằng Code X: Đối với những bạn chưa sử dụng Claude Code, khuyến nghị dùng Code X để tải plugin. Sau khi trò chuyện với Code X có thể lưu trữ dự án, dự án có thể kết nối trực tiếp với thư mục Obsidian. Ví dụ, yêu cầu Code X tổng hợp các dự án liên quan đến tìm kiếm trực tuyến OpenClaw, nó có thể nhanh chóng đưa ra kết quả.",
    "其他安装方式：若找不到插件，可向 code x 或 Calco 说明需求，让它们帮忙查找并安装。如告诉 code x"我 Pixel 想去做一个 obsidian 的同步"，它会自动完成安装。":
        "Các cách cài đặt khác: Nếu không tìm thấy plugin, có thể nói nhu cầu cho Code X hoặc Calco, để chúng giúp tìm và cài đặt. Ví dụ nói với Code X \"Tôi muốn Pixel đồng bộ với Obsidian\", nó sẽ tự động hoàn thành cài đặt.",
    "Openclaw 与 obsidian 连接": "Kết nối OpenClaw với Obsidian",
    "连接平台选择": "Lựa chọn nền tảng kết nối",
    "龙虾与 DISCORD 优势：卡尔将龙虾接入飞书，也可接入 DISCORD。龙虾不同应用可共享 Gateway 与记忆体系，但身份不同，可配置不同 TOOLS；DISCORD 有不同频道，可支持在不同频道与机器人对话，将任务挂后台运行。":
        "Ưu thế của OpenClaw và DISCORD: Carl kết nối OpenClaw với Feishu, cũng có thể kết nối DISCORD. Các ứng dụng OpenClaw khác nhau có thể chia sẻ Gateway và hệ thống bộ nhớ, nhưng danh tính khác nhau, có thể cấu hình TOOLS khác nhau; DISCORD có các kênh khác nhau, hỗ trợ trò chuyện với bot trên các kênh khác nhau, chạy tác vụ ở nền.",
    "信息录入新方法：卡尔研究发现 Openweb 理论上可取代部分插件步骤，完成信息录入。如内置的联网搜索工具，推荐 t 每月有 1000 次免费调用，mediumse search engine 集齐 17 个搜索引擎，无需 API。":
        "Phương pháp nhập thông tin mới: Nghiên cứu của Carl phát hiện Openweb về lý thuyết có thể thay thế một số bước plugin, hoàn thành nhập thông tin. Như công cụ tìm kiếm trực tuyến tích hợp, khuyến nghị Tavily mỗi tháng có 1000 lần gọi miễn phí, MediumSearch Engine tích hợp 17 công cụ tìm kiếm, không cần API.",
    "信息录入工具": "Công cụ nhập thông tin",
    "x reader 与 agent reach：这两个工具能覆盖 YouTube、某站、x 公众号、TG、小红书、Wechat、GitHub、抖音等平台，可爬取评论区内容。但使用时需根据 agent 配置，部分平台需扫码登录获取信息。":
        "X Reader và Agent Reach: Hai công cụ này có thể bao phủ YouTube, Bilibili, X, tài khoản công khai, TG, Xiaohongshu, WeChat, GitHub, Douyin và các nền tảng khác, có thể thu thập nội dung bình luận. Nhưng khi sử dụng cần cấu hình theo agent, một số nền tảng cần quét mã đăng nhập để lấy thông tin.",
    "Gemini 相关应用：有 Gemini 账号的用户，可安装 MOD switch 与 Gemini deep research 等插件，将 CIL 免费额度用于联网搜索，将 Gemini 的 deep research 能力应用到 open crab 中。还可安装 Nobel am 生成 PPT，GOG 连接 Google 邮箱进行总结。":
        "Ứng dụng liên quan Gemini: Người dùng có tài khoản Gemini có thể cài đặt plugin MOD Switch và Gemini Deep Research, sử dụng quota miễn phí CLI cho tìm kiếm trực tuyến, áp dụng khả năng Deep Research của Gemini vào OpenClaw. Cũng có thể cài đặt plugin tạo PPT, kết nối Google Mail để tổng hợp.",
    "联动方式与数据安全": "Phương thức liên kết và bảo mật dữ liệu",
    "联动方式说明": "Giải thích phương thức liên kết",
    "主力模型选择：卡尔建议使用 Claude 作为主网模型，通过中转降低成本，让 open query 自动升级。信息录入时，先将内容录入收件箱，再用 code x 或抄课整理到文件夹。":
        "Lựa chọn mô hình chính: Carl khuyến nghị sử dụng Claude làm mô hình chính, giảm chi phí thông qua trung chuyển, để open query tự động nâng cấp. Khi nhập thông tin, trước tiên nhập nội dung vào hộp thư đến, sau đó dùng Code X hoặc Chao Ke để sắp xếp vào thư mục.",
    "软链接应用：为避免信息录入打乱文件节奏，可建立软链接。通过 collection 或 call code 新建文件夹，将 open crab 的设置和数据存储在其中，修改 agents 的 Markdown 文件，实现从 open crab 直接将笔记录入 obsidian。":
        "Ứng dụng liên kết mềm: Để tránh việc nhập thông tin phá vỡ nhịp tệp, có thể tạo liên kết mềm. Tạo thư mục mới thông qua Collection hoặc Claude Code, lưu trữ cài đặt và dữ liệu của OpenClaw trong đó, chỉnh sửa tệp Markdown của agents, thực hiện ghi chú trực tiếp từ OpenClaw vào Obsidian.",
    "数据安全保障": "Đảm bảo bảo mật dữ liệu",
    "Git 版本备份：为防止 Openai 误删 obsidian 内容，可在 code x 或 Coco 中使用 Git 进行版本备份。设置定时任务，code x 会对修改前后的内容进行版本存储，可实现版本回退。":
        "Sao lưu phiên bản Git: Để ngăn AI xóa nhầm nội dung Obsidian, có thể sử dụng Git trong Code X hoặc Coco để sao lưu phiên bản. Thiết lập tác vụ hẹn giờ, Code X sẽ lưu trữ phiên bản nội dung trước và sau khi sửa đổi, có thể khôi phục phiên bản.",
    "隐私数据处理：将隐私数据存储到 icloud，避免 Mac mini 读取隐私数据。同时，给 openclaw 配置独立的 Google 账号，保障数据安全。":
        "Xử lý dữ liệu riêng tư: Lưu trữ dữ liệu riêng tư vào iCloud, tránh Mac mini đọc dữ liệu riêng tư. Đồng thời, cấu hình tài khoản Google độc lập cho OpenClaw, đảm bảo an toàn dữ liệu.",
    "常见问题解答": "Câu hỏi thường gặp",
    "硬件与配置问题": "Vấn đề phần cứng và cấu hình",
    "电脑配置要求：电脑最低基础配置要求不高，老电脑甚至安卓机都可运行，因为主要依赖模型的 API 能力。":
        "Yêu cầu cấu hình máy tính: Yêu cầu cấu hình cơ bản tối thiểu không cao, máy tính cũ thậm chí điện thoại Android cũng có thể chạy, vì chủ yếu dựa vào khả năng API của mô hình.",
    "内存需求：16G 内存足够使用，对硬件要求较低。":
        "Yêu cầu bộ nhớ: RAM 16G đủ để sử dụng, yêu cầu phần cứng khá thấp.",
    "工具使用问题": "Vấn đề sử dụng công cụ",
    "code x 与 Claude code 选择：二者二选一即可，卡尔将 code x 用于复杂任务，它的运行时间比之前的版本更长，使用效果较好。":
        "Lựa chọn giữa Code X và Claude Code: Chọn một trong hai là đủ, Carl dùng Code X cho các tác vụ phức tạp, thời gian chạy lâu hơn phiên bản trước, hiệu quả sử dụng khá tốt.",
    "文件管理与分类：按工作流分类可让 AI 读懂文件，若还需按类型查找，可让 Collins 或 Coco 为文件做软链接或目录。":
        "Quản lý và phân loại tệp: Phân loại theo quy trình công việc giúp AI đọc hiểu tệp, nếu cần tìm theo loại, có thể để Collins hoặc Coco tạo liên kết mềm hoặc thư mục cho tệp.",
    "视频处理方式：推荐记录视频链接后续人工处理，若要先生成字幕和摘要，可使用相关插件收录视频笔记。":
        "Phương pháp xử lý video: Khuyến nghị ghi lại liên kết video rồi xử lý thủ công sau, nếu muốn tạo phụ đề và tóm tắt trước, có thể sử dụng plugin liên quan để thu thập ghi chú video.",
    "数据获取与安全问题": "Vấn đề thu thập dữ liệu và bảo mật",
    "权威网站数据获取：推荐使用 code x 自行开发脚本获取权威网站数据，目前大部分网站可通过 AI 直接爬取，无需额外消耗 TOKEN。":
        "Thu thập dữ liệu trang web uy tín: Khuyến nghị sử dụng Code X tự phát triển script để thu thập dữ liệu từ trang web uy tín, hiện tại hầu hết trang web có thể được AI trực tiếp thu thập, không cần tiêu tốn TOKEN thêm.",
    "微信聊天记录处理：卡尔记得有成熟的处理方法，但目前处理微信聊天记录较少。":
        "Xử lý lịch sử chat WeChat: Carl nhớ có phương pháp xử lý hoàn thiện, nhưng hiện tại ít xử lý lịch sử chat WeChat.",
    "任务分配原则：优先将任务交给额度最大、最好用的工具，如卡尔优先将任务交给 code x，解决不了再依次交给 CC、openclaw。":
        "Nguyên tắc phân bổ tác vụ: Ưu tiên giao tác vụ cho công cụ có quota lớn nhất, dễ dùng nhất, ví dụ Carl ưu tiên giao tác vụ cho Code X, không giải quyết được thì lần lượt giao cho CC, OpenClaw.",
    "总结与展望": "Tổng kết và triển vọng",
    "分享总结": "Tổng kết chia sẻ",
    "体系优势强调：卡尔总结了 obsidian 与 openclaw 组合搭建的知识管理体系的优势，包括信息整合、知识关联、自动化处理等方面，认为该体系能有效提升知识管理效率。":
        "Nhấn mạnh ưu thế hệ thống: Carl tổng kết các ưu thế của hệ thống quản lý tri thức được xây dựng bằng sự kết hợp Obsidian và OpenClaw, bao gồm tích hợp thông tin, liên kết tri thức, xử lý tự động, cho rằng hệ thống này có thể nâng cao hiệu quả quản lý tri thức.",
    "工具使用建议：再次强调了插件的使用方法和注意事项，以及不同工具的适用场景和任务分配原则，帮助参会者更好地掌握和运用这些工具。":
        "Khuyến nghị sử dụng công cụ: Nhấn mạnh lại phương pháp sử dụng và lưu ý khi dùng plugin, cũng như các tình huống áp dụng và nguyên tắc phân bổ tác vụ cho các công cụ khác nhau, giúp người tham dự nắm vững và vận dụng các công cụ này tốt hơn.",
    "后续交流期望": "Kỳ vọng trao đổi tiếp theo",
    "玩法交流邀请：卡尔邀请大家分享更多 obsidian 的玩法，认为该工具具有很高的可玩性，通过交流可以发现更多的应用场景和创新方法。":
        "Lời mời trao đổi cách chơi: Carl mời mọi người chia sẻ thêm các cách sử dụng Obsidian, cho rằng công cụ này có khả năng khám phá cao, thông qua trao đổi có thể phát hiện thêm nhiều kịch bản ứng dụng và phương pháp sáng tạo.",
    "持续学习与分享：AJ 表示后续有新的内容和研究，将再次邀请卡尔进行分享，鼓励大家持续学习和探索 AI 知识管理领域的新方法和新技巧。":
        "Học tập và chia sẻ liên tục: AJ cho biết sẽ mời Carl chia sẻ lại khi có nội dung và nghiên cứu mới, khuyến khích mọi người tiếp tục học tập và khám phá các phương pháp và kỹ thuật mới trong lĩnh vực quản lý tri thức AI.",
    "Gemini 总结：": "Tổng kết bởi Gemini:",
    "💡 总结速览": "💡 Tổng quan nhanh",
    "本次分享由卡尔（Carl）主讲，深入探讨了如何利用 ": "Buổi chia sẻ này do Carl chủ giảng, thảo luận sâu về cách sử dụng ",
    " 结合 ": " kết hợp ",
    "OpenClaw（小龙虾）": "OpenClaw",
    " 和 ": " và ",
    " 构建一套"活"的知识管理体系。核心在于打破笔记的静态存储，利用 ": " xây dựng một hệ thống quản lý tri thức \"sống\". Cốt lõi là phá vỡ lưu trữ tĩnh của ghi chú, sử dụng ",
    " 的能力，将信息的采集、整理、归档自动化。": " để tự động hóa việc thu thập, sắp xếp và lưu trữ thông tin.",
    "内容涵盖了从飞书、微信、网页等渠道高效": "Nội dung bao gồm việc hiệu quả",
    "捕获信息": "thu thập thông tin",
    "的流派，利用 ": " từ các kênh như Feishu, WeChat, trang web, sử dụng ",
    " 进行本地与云端的智能调度，以及通过 ": " để điều phối thông minh giữa local và cloud, cũng như thông qua ",
    "Soft Link（软链接）": "Soft Link (liên kết mềm)",
    " 实现 Agent 与笔记仓库的无缝交互。本质上，这是一场关于将"第二大脑"从存储器升级为处理器的技术实操，旨在解决信息过载与知识僵化的问题，实现知识的动态增值。":
        " thực hiện tương tác liền mạch giữa Agent và kho ghi chú. Về bản chất, đây là một thực hành kỹ thuật về việc nâng cấp \"bộ não thứ hai\" từ bộ nhớ thành bộ xử lý, nhằm giải quyết vấn đề quá tải thông tin và tri thức cứng nhắc, thực hiện gia tăng giá trị tri thức động.",
    "🚀 核心：知识容器与智能引擎的耦合": "🚀 Cốt lõi: Kết hợp giữa bộ chứa tri thức và engine thông minh",
    "为什么要重构？": "Tại sao phải tái cấu trúc?",
    "传统的笔记软件（如 Notion、Flomo、飞书）往往成为信息的"填埋场"。GPT 的记忆机制虽然强大，但依然受限于其封闭的生态系统。":
        "Phần mềm ghi chú truyền thống (như Notion, Flomo, Feishu) thường trở thành \"bãi chôn lấp\" thông tin. Cơ chế bộ nhớ của GPT tuy mạnh mẽ, nhưng vẫn bị hạn chế bởi hệ sinh thái đóng của nó.",
    "Obsidian 的不可替代性": "Tính không thể thay thế của Obsidian",
    "：作为本地 Markdown 编辑器，Obsidian 提供了数据的主权和极高的可扩展性。它不仅是笔记，更是 AI Agent 可以直接读写的文件系统。":
        ": Với tư cách là trình soạn thảo Markdown cục bộ, Obsidian cung cấp quyền sở hữu dữ liệu và khả năng mở rộng cực cao. Nó không chỉ là ghi chú, mà còn là hệ thống tệp mà AI Agent có thể trực tiếp đọc ghi.",
    "流动的哲学": "Triết lý dòng chảy",
    "：目标不是单纯的"记"，而是让散落在微信、网页、视频中的信息流，自动汇入 Obsidian，经过 AI 提炼后形成知识网络。":
        ": Mục tiêu không chỉ đơn giản là \"ghi\", mà là để dòng thông tin rải rác trong WeChat, trang web, video tự động chảy vào Obsidian, sau khi được AI tinh lọc sẽ hình thành mạng tri thức.",
    "信息的"无感"捕获（Input Layer）": "Thu thập thông tin \"không cảm nhận\" (Input Layer)",
    "构建体系的第一步是解决信息输入的摩擦力。卡尔推荐了一套高效的"采集插件组合拳"：":
        "Bước đầu tiên xây dựng hệ thống là giải quyết ma sát nhập thông tin. Carl khuyến nghị một bộ \"combo plugin thu thập\" hiệu quả:",
    "全能剪藏": "Lưu trữ toàn năng",
    "：使用 ": ": Sử dụng ",
    " 或类似简藏工具。相比简单的复制粘贴，它能保留": " hoặc công cụ lưu trữ tương tự. So với copy paste đơn giản, nó có thể giữ lại",
    "来源链接 (Source)": "liên kết nguồn (Source)",
    " 和自动打上 ": " và tự động gắn ",
    "，为 AI 后续的整理提供元数据。": ", cung cấp metadata cho AI sắp xếp sau này.",
    "视频转文案": "Video sang văn bản",
    "：利用 ": ": Sử dụng ",
    " 或 ": " hoặc ",
    "元宝小程序": "Mini Program Yuanbao",
    "，提取 YouTube、B站、视频号的字幕和文案。对于未看过的长视频，建议先保存链接或生成摘要，而非盲目全文收录。":
        ", trích xuất phụ đề và văn bản từ YouTube, Bilibili, Video Account. Đối với video dài chưa xem, khuyến nghị lưu liên kết hoặc tạo tóm tắt trước, thay vì thu thập toàn bộ một cách mù quáng.",
    "移动端同步": "Đồng bộ di động",
    "：痛点在于手机到电脑的割裂。解决方案是使用": ": Điểm đau nằm ở sự rời rạc giữa điện thoại và máy tính. Giải pháp là sử dụng",
    "微信笔记同步助手": "Trợ lý đồng bộ ghi chú WeChat",
    "（或类似服务），将微信中的图片、链接直接同步至 Obsidian，打通移动端孤岛。":
        " (hoặc dịch vụ tương tự), đồng bộ trực tiếp hình ảnh, liên kết trong WeChat sang Obsidian, xóa bỏ ốc đảo di động.",
    "构建"活"的文件系统（Structure Layer）": "Xây dựng hệ thống tệp \"sống\" (Structure Layer)",
    "不必迷信完美的分类树，让 AI 理解你的工作流才是关键。":
        "Không cần mê tín cây phân loại hoàn hảo, để AI hiểu quy trình công việc của bạn mới là chìa khóa.",
    "目录即指令": "Thư mục chính là lệnh",
    "00 Inbox (收件箱)": "00 Inbox (Hộp thư đến)",
    "：所有采集的原始素材入口。": ": Đầu vào tất cả nguyên liệu thô thu thập được.",
    "Projects (项目)": "Projects (Dự án)",
    "Research (研究)": "Research (Nghiên cứu)",
    "：动态工作的区域。": ": Khu vực làm việc động.",
    "Archive (归档)": "Archive (Lưu trữ)",
    "：历史沉淀。": ": Tích lũy lịch sử.",
    "AI 的介入": "Sự can thiệp của AI",
    "：不需手动整理，通过 ": ": Không cần sắp xếp thủ công, thông qua ",
    "，让 AI 根据预设的 ": ", để AI theo ",
    "提示词": "prompt",
    "，自动将收件箱的内容分发到对应目录。": " đã thiết lập trước, tự động phân phối nội dung hộp thư đến vào thư mục tương ứng.",
    "软链接（Soft Link）的妙用": "Công dụng tuyệt vời của liên kết mềm (Soft Link)",
    "：在操作系统层面建立软链接，让部署在本地的 Agent（如 OpenClaw）能直接访问 Obsidian 的特定文件夹。这样既保证了数据安全（只暴露部分权限），又实现了 Agent 对笔记的实时读写。":
        ": Tạo liên kết mềm ở cấp hệ điều hành, cho phép Agent được triển khai cục bộ (như OpenClaw) truy cập trực tiếp các thư mục cụ thể của Obsidian. Điều này vừa đảm bảo an toàn dữ liệu (chỉ mở một phần quyền), vừa thực hiện đọc ghi ghi chú theo thời gian thực của Agent.",
    "智能引擎的配置（Agent Layer）": "Cấu hình engine thông minh (Agent Layer)",
    "这是整个体系的"大脑"，利用 AI 自动化处理信息。":
        "Đây là \"bộ não\" của toàn bộ hệ thống, sử dụng AI để tự động hóa xử lý thông tin.",
    "主力模型选择": "Lựa chọn mô hình chính",
    "：适合处理复杂的编程和文件重构任务，作为主力的"执行官"。":
        ": Phù hợp xử lý các tác vụ lập trình và tái cấu trúc tệp phức tạp, đóng vai \"giám đốc điều hành\" chính.",
    "：用于管理日常文件结构，处理较复杂的指令规划。":
        ": Dùng để quản lý cấu trúc tệp hàng ngày, xử lý lập kế hoạch lệnh phức tạp hơn.",
    "OpenClaw (小龙虾)": "OpenClaw",
    "：作为全天候在线的 ": ": Với tư cách là ",
    "，挂载在本地服务器（如 Mac Mini）或云端。它可以执行定时任务（Cron），如每天凌晨整理日报、拉取新闻。":
        " trực tuyến 24/7, được gắn trên máy chủ cục bộ (như Mac Mini) hoặc cloud. Nó có thể thực thi tác vụ hẹn giờ (Cron), như sắp xếp báo cáo hàng ngày, lấy tin tức vào mỗi đêm.",
    "记忆增强 (Memory)": "Tăng cường bộ nhớ (Memory)",
    "不要让 Agent 裸奔。通过 ": "Đừng để Agent chạy trần. Thông qua ",
    " 记录 AI 的长期记忆。": " ghi lại bộ nhớ dài hạn của AI.",
    "心跳机制": "Cơ chế heartbeat",
    "：为了防止长对话后 AI 变"笨"，可以设置检测指令（如"卡尔真棒"），一旦 AI 遗忘上下文或 Skill，立即重启对话或重载记忆。":
        ": Để ngăn AI trở nên \"đần\" sau cuộc hội thoại dài, có thể thiết lập lệnh phát hiện (như \"Carl thật tuyệt\"), một khi AI quên ngữ cảnh hoặc Skill, lập tức khởi động lại hội thoại hoặc tải lại bộ nhớ.",
    "降低成本的策略": "Chiến lược giảm chi phí",
    " 切换模型，或者通过 ": " chuyển đổi mô hình, hoặc thông qua ",
    " 薅取各家大模型（如 DeepSeek、Gemini、Claude）的免费或低价额度。":
        " tận dụng quota miễn phí hoặc giá rẻ của các mô hình lớn (như DeepSeek, Gemini, Claude).",
    "进阶玩法与避坑": "Cách chơi nâng cao và tránh bẫy",
    "：这不仅是阅读器，更是一套通过 ": ": Đây không chỉ là trình đọc, mà còn là một framework thu thập chạy thông qua ",
    " 运行的采集框架。它能覆盖小红书、公众号、GitHub 等多个平台，将内容结构化为 Markdown。":
        ". Nó có thể bao phủ nhiều nền tảng như Xiaohongshu, tài khoản công khai, GitHub, cấu trúc hóa nội dung thành Markdown.",
    "硬件部署": "Triển khai phần cứng",
    "推荐 ": "Khuyến nghị ",
    " 作为 Always-on 的服务器，跑 OpenClaw 和定时任务。":
        " làm máy chủ Always-on, chạy OpenClaw và tác vụ hẹn giờ.",
    "iCloud 同步": "Đồng bộ iCloud",
    "：虽然方便但需谨慎，建议结合 ": ": Tuy tiện lợi nhưng cần thận trọng, khuyến nghị kết hợp ",
    " 做私有版本控制，防止 AI"发疯"误删文件。":
        " để kiểm soát phiên bản riêng tư, ngăn AI \"phát điên\" xóa nhầm tệp.",
    "双向同步": "Đồng bộ hai chiều",
    "：Obsidian 的双向链接（Backlinks）结合 AI 的语义理解，可以涌现出意想不到的知识关联。":
        ": Liên kết hai chiều (Backlinks) của Obsidian kết hợp với hiểu ngữ nghĩa của AI, có thể tạo ra các liên kết tri thức bất ngờ.",
    "🧗 对个人发展的实操建议": "🧗 Khuyến nghị thực hành cho phát triển cá nhân",
    "2026年，AI 已从"聊天机器人"进化为"操作系统"的一部分。对于职场人和创业者，竞争的核心不再是掌握了多少工具，而是构建了多自动化的":
        "Năm 2026, AI đã tiến hóa từ \"chatbot\" thành một phần của \"hệ điều hành\". Đối với người đi làm và khởi nghiệp, cốt lõi cạnh tranh không còn là nắm bao nhiêu công cụ, mà là đã xây dựng được bao nhiêu tự động hóa cho",
    "知识复利系统": "hệ thống lãi kép tri thức",
    "面向 知识工作者 / 咨询顾问 / 内容创作者": "Dành cho người lao động tri thức / tư vấn viên / nhà sáng tạo nội dung",
    "打造"AI 驱动的自动化情报局"。": "Xây dựng \"cơ quan tình báo tự động hóa do AI điều khiển\".",
    "思路": "Ý tưởng",
    "：你的时间不应浪费在 copy-paste 和基础整理上。如果你每天还在手动将微信文件转存到电脑，或者手动总结长视频，你就在做 AI 的工作。":
        ": Thời gian của bạn không nên lãng phí vào copy-paste và sắp xếp cơ bản. Nếu bạn vẫn đang thủ công chuyển tệp WeChat sang máy tính hàng ngày, hoặc thủ công tóm tắt video dài, bạn đang làm công việc của AI.",
    "方法论": "Phương pháp luận",
    "部署私人情报员": "Triển khai nhân viên tình báo riêng",
    "：模仿卡尔的 ": ": Mô phỏng phương án ",
    " 方案。搭建一套自动化的信息流：": " của Carl. Xây dựng một luồng thông tin tự động:",
    "监控特定行业关键词 -> 自动抓取文章/视频 -> AI 自动总结 -> 自动归档至 Obsidian -> 发送日报到微信":
        "Giám sát từ khóa ngành cụ thể -> Tự động thu thập bài viết/video -> AI tự động tóm tắt -> Tự động lưu trữ vào Obsidian -> Gửi báo cáo hàng ngày đến WeChat",
    "建立垂直知识库": "Xây dựng kho tri thức chuyên sâu",
    "：不要追求大而全，利用 ": ": Đừng theo đuổi lớn và toàn diện, hãy tận dụng ",
    "RAG (检索增强生成)": "RAG (Retrieval-Augmented Generation)",
    " 技术。将你所在领域（如"新能源汽车出海"、"跨境电商SaaS"）的高质量报告喂给本地 Obsidian。":
        ". Đưa các báo cáo chất lượng cao trong lĩnh vực của bạn (như \"xe năng lượng mới ra nước ngoài\", \"SaaS thương mại điện tử xuyên biên giới\") vào Obsidian cục bộ.",
    "搞钱方案": "Phương án kiếm tiền",
    "：封装你的"信息流"。许多企业没有能力筛选海量信息。你可以提供 ":
        ": Đóng gói \"luồng thông tin\" của bạn. Nhiều doanh nghiệp không có khả năng sàng lọc thông tin khổng lồ. Bạn có thể cung cấp ",
    ""行业定制情报服务"": "\"dịch vụ tình báo tùy chỉnh theo ngành\"",
    "。不仅仅是卖报告，而是卖"经过筛选和结构化的实时知识库"。":
        ". Không chỉ bán báo cáo, mà bán \"kho tri thức thời gian thực đã được sàng lọc và cấu trúc hóa\".",
    "面向 程序员 / AI 工程师": "Dành cho lập trình viên / kỹ sư AI",
    "成为"个人知识库(PKM) 架构师"或"Agent 甚至 AgentOps 专家"。":
        "Trở thành \"kiến trúc sư kho tri thức cá nhân (PKM)\" hoặc \"chuyên gia Agent thậm chí AgentOps\".",
    "：Obsidian 和 Agent 的结合门槛依然很高（终端、Docker、API 配置）。普通用户即使想要"第二大脑"，也会被技术细节劝退。":
        ": Ngưỡng kết hợp Obsidian và Agent vẫn rất cao (terminal, Docker, cấu hình API). Người dùng bình thường dù muốn \"bộ não thứ hai\" cũng sẽ bị chi tiết kỹ thuật làm nản lòng.",
    "开发中间件": "Phát triển middleware",
    "：目前 Obsidian 与各家 Agent（如 OpenInterpreter、OpenWebUI）的连接还需要复杂的配置。开发一款":
        ": Hiện tại kết nối giữa Obsidian với các Agent (như OpenInterpreter, OpenWebUI) vẫn cần cấu hình phức tạp. Phát triển một",
    ""一键部署包"": "\"gói triển khai một chạm\"",
    "，集成好 Environment、Prompt Template 和 API 转发，让小白也能用上这套系统。":
        ", tích hợp sẵn Environment, Prompt Template và chuyển tiếp API, cho phép người mới cũng có thể sử dụng hệ thống này.",
    "插件开发": "Phát triển plugin",
    "：针对 Obsidian 开发更深度的 AI 插件。例如，不仅是聊天，而是能根据笔记内容自动生成":
        ": Phát triển plugin AI chuyên sâu hơn cho Obsidian. Ví dụ, không chỉ chat, mà còn có thể tự động tạo",
    "思维导图、PPT大纲": "sơ đồ tư duy, dàn ý PPT",
    "甚至": "thậm chí",
    "可执行代码": "mã có thể thực thi",
    "的 Agent 插件。": " plugin Agent.",
    "：提供 ": ": Cung cấp ",
    ""数字化大脑搭建咨询"": "\"tư vấn xây dựng bộ não số hóa\"",
    "。为企业高管或研究团队搭建私有化、离线的 AI 知识管理系统，解决他们的数据隐私焦虑（Privacy-First AI Setup）。":
        ". Xây dựng hệ thống quản lý tri thức AI tư nhân hóa, offline cho lãnh đạo doanh nghiệp hoặc nhóm nghiên cứu, giải quyết lo lắng về quyền riêng tư dữ liệu (Privacy-First AI Setup).",
    "面向 自由职业者 / 学生": "Dành cho freelancer / sinh viên",
    "利用"套利模型"降维打击。": "Sử dụng \"mô hình chênh lệch giá\" để tấn công giảm chiều.",
    "：利用信息差和工具效率差。大部分人还在用百度搜索和手动做笔记时，你已经拥有了一支 AI 团队。":
        ": Tận dụng chênh lệch thông tin và hiệu quả công cụ. Khi hầu hết mọi người vẫn đang tìm kiếm trên Baidu và ghi chú thủ công, bạn đã có một đội ngũ AI.",
    "学术/研报降维": "Giảm chiều học thuật/báo cáo nghiên cứu",
    "：用 ": ": Dùng ",
    " 批量爬取外文核心期刊或长视频，利用 ": " thu thập hàng loạt tạp chí lõi ngoại ngữ hoặc video dài, sử dụng ",
    " 进行深度翻译和逻辑重构，将晦涩的专业内容转化为通俗易懂的短视频脚本或图文笔记。":
        " để dịch sâu và tái cấu trúc logic, chuyển đổi nội dung chuyên ngành khó hiểu thành kịch bản video ngắn hoặc ghi chú đồ họa dễ hiểu.",
    "低成本算力组合": "Tổ hợp sức mạnh tính toán chi phí thấp",
    "：学习卡尔提到的 ": ": Học hỏi kỹ thuật ",
    " 技巧，组合各家大模型的免费/低价额度，极低成本地完成高质量内容生产。":
        " mà Carl đề cập, kết hợp quota miễn phí/giá rẻ của các mô hình lớn, hoàn thành sản xuất nội dung chất lượng cao với chi phí cực thấp.",
    "：做 ": ": Làm ",
    ""超级个体"": "\"siêu cá thể\"",
    " 的运营。一人运营多个矩阵账号，后台用这一套 Obsidian+OpenClaw 系统作为内容中央厨房，实现内容的流水线生产与分发。":
        " vận hành. Một người vận hành nhiều tài khoản ma trận, hậu đài sử dụng hệ thống Obsidian+OpenClaw này làm \"bếp trung tâm\" nội dung, thực hiện sản xuất và phân phối nội dung dạng dây chuyền.",
    "Claude 总结：": "Tổng kết bởi Claude:",
    "总结速览": "Tổng quan nhanh",
    "本次直播由 AI 自媒体创作者卡尔主讲，核心主题是如何用 ":
        "Buổi livestream này do nhà sáng tạo AI tự truyền thông Carl chủ giảng, chủ đề cốt lõi là cách sử dụng ",
    " 在约10分钟内完成个人 AI 知识管理体系的彻底重构。OpenClaw 是一个开源的本地 AI Agent 框架，所有数据完全保留在本地、不上传任何云端。卡尔从自身从大厂离职、转型独立创作者的实际经历出发，分享了他为何放弃 Notion、Flomo、飞书等工具，最终选择 Obsidian 作为核心知识库，并通过插件体系与 OpenClaw 打通，实现信息的自动聚合、关联与激活。":
        " để hoàn thành việc tái cấu trúc hoàn toàn hệ thống quản lý tri thức AI cá nhân trong khoảng 10 phút. OpenClaw là một framework AI Agent cục bộ mã nguồn mở, tất cả dữ liệu được giữ hoàn toàn tại máy, không tải lên bất kỳ cloud nào. Carl từ kinh nghiệm thực tế rời công ty lớn và chuyển đổi thành nhà sáng tạo độc lập, chia sẻ lý do từ bỏ các công cụ như Notion, Flomo, Feishu và cuối cùng chọn Obsidian làm kho tri thức cốt lõi, kết nối thông qua hệ sinh thái plugin với OpenClaw, thực hiện tự động tổng hợp, liên kết và kích hoạt thông tin.",
    "为什么选择 Obsidian？从痛点出发": "Tại sao chọn Obsidian? Xuất phát từ điểm đau",
    "卡尔坦言，他并非 Obsidian 的早期用户，真正下定决心全面迁移，是三周前才做出的决定。此前他用过几乎所有主流笔记工具：Notion、Flomo、滴答清单、飞书，但始终有一个未被满足的核心需求——":
        "Carl thừa nhận, anh không phải người dùng sớm của Obsidian, quyết định di chuyển toàn diện thực sự mới được đưa ra ba tuần trước. Trước đó anh đã dùng hầu như tất cả công cụ ghi chú chính thống: Notion, Flomo, TickTick, Feishu, nhưng luôn có một nhu cầu cốt lõi chưa được đáp ứng —",
    "让 AI 真正\"认识\"自己": "Để AI thực sự \"nhận biết\" bản thân",
    "他以 ChatGPT 的记忆系统为例说明：之所以迟迟没有完全转向 Claude，是因为 GPT 积累了一个\"非常懂他\"的记忆体系。这种记忆不是简单的对话导出，而是长期交互沉淀下来的个人化上下文。他意识到，与其依赖某个平台的私有记忆，不如自己构建一套":
        "Anh lấy hệ thống bộ nhớ của ChatGPT làm ví dụ: Lý do chần chừ chưa chuyển hoàn toàn sang Claude là vì GPT đã tích lũy một hệ thống bộ nhớ \"rất hiểu anh\". Loại bộ nhớ này không phải là xuất hội thoại đơn giản, mà là ngữ cảnh cá nhân hóa được lắng đọng qua tương tác lâu dài. Anh nhận ra, thay vì phụ thuộc vào bộ nhớ riêng của một nền tảng, tốt hơn nên tự xây dựng một bộ",
    "可控的、结构化的个人知识库": "kho tri thức cá nhân có thể kiểm soát, cấu trúc hóa",
    "，再通过 AI 工具赋予它\"活的\"能力。": ", rồi thông qua công cụ AI trao cho nó khả năng \"sống\".",
    "与此同时，他观察到一个行业信号：越来越多的新创业项目开始以\"Obsidian 形态\"为原型，原因在于 Obsidian 的底层逻辑——":
        "Đồng thời, anh quan sát thấy một tín hiệu ngành: Ngày càng nhiều dự án khởi nghiệp mới bắt đầu lấy \"hình thái Obsidian\" làm nguyên mẫu, nguyên nhân nằm ở logic nền tảng của Obsidian —",
    "让知识内容更好地呈现、更好地关联": "Trình bày nội dung tri thức tốt hơn, liên kết tốt hơn",
    "——与 AI Agent 的工作方式天然契合。Obsidian 的 CEO 在产品理念上也高度重视本地数据主权与知识图谱，这在 AI 时代显得格外有远见。":
        "— khớp tự nhiên với phương thức làm việc của AI Agent. CEO của Obsidian cũng rất coi trọng quyền sở hữu dữ liệu cục bộ và đồ thị tri thức trong lý niệm sản phẩm, điều này đặc biệt có tầm nhìn xa trong kỷ nguyên AI.",
    "第一步：信息的全面收录": "Bước một: Thu thập thông tin toàn diện",
    "重构体系的第一步，不是 AI，而是": "Bước đầu tiên tái cấu trúc hệ thống, không phải AI, mà là",
    "解决信息的\"入口\"问题": "giải quyết vấn đề \"đầu vào\" thông tin",
    "——如何把散落在各处的内容统一汇聚到 Obsidian。": "— làm thế nào để tập hợp nội dung rải rác khắp nơi vào Obsidian.",
    "卡尔每天需要处理的信息量极大，仅每日更新的消息就有五六千条，分散在飞书、苹果备忘录、各类网站和订阅源中。他的解法是安装三个关键插件，其中一个核心插件可以将飞书文档（包括普通文档、视频、PDF 等格式）批量下载为 ":
        "Lượng thông tin Carl cần xử lý hàng ngày cực lớn, chỉ riêng tin nhắn cập nhật hàng ngày đã có năm sáu nghìn tin, phân tán trên Feishu, Apple Notes, các trang web và nguồn đăng ký khác nhau. Giải pháp của anh là cài đặt ba plugin quan trọng, trong đó một plugin cốt lõi có thể tải hàng loạt tài liệu Feishu (bao gồm tài liệu thông thường, video, PDF, v.v.) về định dạng ",
    "Markdown 格式": "Markdown",
    "，直接导入 Obsidian。唯一的例外是飞书多维表格，由于其结构特殊性难以完全替代，他选择保留这一部分。":
        ", nhập trực tiếp vào Obsidian. Ngoại lệ duy nhất là bảng đa chiều Feishu, do tính đặc thù cấu trúc khó thay thế hoàn toàn, anh chọn giữ lại phần này.",
    "这里有一个重要的观念：": "Ở đây có một quan niệm quan trọng:",
    "彻底迁移并不意味着抛弃一切现有工具": "Di chuyển triệt để không có nghĩa là bỏ đi tất cả công cụ hiện có",
    "，而是以 Obsidian 为核心枢纽，让其他工具各司其职，只是将\"知识沉淀\"这件事交给 Obsidian 来主导。":
        ", mà lấy Obsidian làm trung tâm, để các công cụ khác đảm nhận vai trò riêng, chỉ giao việc \"lắng đọng tri thức\" cho Obsidian chủ đạo.",
    "在 API 使用策略上，卡尔也分享了一个务实的思路：他尽量避免将 API 用于大批量的信息处理（如每天五六千条消息的全量翻译），而是":
        "Về chiến lược sử dụng API, Carl cũng chia sẻ một ý tưởng thực tế: Anh cố gắng tránh sử dụng API cho xử lý thông tin hàng loạt lớn (như dịch toàn bộ năm sáu nghìn tin nhắn hàng ngày), mà",
    "只用 API 做标题翻译": "chỉ dùng API để dịch tiêu đề",
    "等轻量任务，以此控制成本。这对独立创作者和个人开发者来说是一个值得借鉴的成本管理意识。":
        " và các tác vụ nhẹ, để kiểm soát chi phí. Đây là ý thức quản lý chi phí đáng tham khảo cho nhà sáng tạo độc lập và nhà phát triển cá nhân.",
    "Obsidian 的安装门槛：比你想象的低": "Ngưỡng cài đặt Obsidian: Thấp hơn bạn tưởng",
    "卡尔特别强调，Obsidian 结合 AI 工具的安装门槛几乎为零。他的说法是：随便安装一个 Claude Code（或类似的 AI 编程助手），输入一句\"帮我安装 Obsidian\"，配合 Cursor 即可完成整个安装流程。":
        "Carl đặc biệt nhấn mạnh, ngưỡng cài đặt Obsidian kết hợp công cụ AI gần như bằng không. Cách nói của anh là: Cài đặt bất kỳ Claude Code (hoặc trợ lý lập trình AI tương tự), nhập một câu \"Giúp tôi cài đặt Obsidian\", kết hợp Cursor là hoàn thành toàn bộ quy trình cài đặt.",
    "真正的门槛不在于安装，而在于": "Ngưỡng thực sự không nằm ở cài đặt, mà ở",
    "建立正确的使用心态": "xây dựng tâm thế sử dụng đúng đắn",
    "。很多人把 Obsidian 当成高级备忘录来用，但这与真正发挥其潜力的状态相差甚远。卡尔提到，社群中的\"向阳乔木\"和\"小七姐\"都是深度 Obsidian 用户，后者甚至基于 Obsidian 构建了完整的\"第二大脑\"体系，与 AI Agent 对话时拥有极为丰富的个人上下文，这种体验被描述为\"另一个世界的大门\"。":
        ". Nhiều người dùng Obsidian như một ghi chú cao cấp, nhưng điều này cách xa trạng thái phát huy hết tiềm năng của nó. Carl đề cập, \"Hướng Dương Kiều Mộc\" và \"Tiểu Thất Tỷ\" trong cộng đồng đều là người dùng Obsidian sâu, người sau thậm chí đã xây dựng hệ thống \"bộ não thứ hai\" hoàn chỉnh dựa trên Obsidian, có ngữ cảnh cá nhân cực kỳ phong phú khi đối thoại với AI Agent, trải nghiệm này được mô tả là \"cánh cửa đến thế giới khác\".",
    "Obsidian 本身已有超过五六年的发展历史（2020年发布第一个版本），拥有庞大的插件和主题生态，即便在 AI 出现之前，它就已经是一款极为优秀的笔记软件。":
        "Bản thân Obsidian đã có hơn năm sáu năm lịch sử phát triển (phát hành phiên bản đầu tiên năm 2020), có hệ sinh thái plugin và chủ đề khổng lồ, ngay cả trước khi AI xuất hiện, nó đã là một phần mềm ghi chú cực kỳ xuất sắc.",
    "OpenClaw 与 Obsidian 的协同：让知识\"活\"起来": "Sự phối hợp giữa OpenClaw và Obsidian: Làm cho tri thức \"sống\" dậy",
    "OpenClaw 是一个": "OpenClaw là một",
    "开源的本地 AI Agent 框架": "framework AI Agent cục bộ mã nguồn mở",
    "，核心设计哲学是\"简单、直接、可靠\"——所有数据完全保留在本地机器上，零网络请求，不上传任何云端服务。它与 Obsidian 的结合之所以天然契合，是因为 Obsidian 的知识库（vault）本质上就是一个普通文件夹，里面全是标准的 Markdown 文件。OpenClaw 无需任何专属 API，直接通过文件系统操作读写 ":
        ", triết lý thiết kế cốt lõi là \"đơn giản, trực tiếp, đáng tin cậy\" — tất cả dữ liệu được giữ hoàn toàn trên máy cục bộ, không có yêu cầu mạng, không tải lên bất kỳ dịch vụ cloud nào. Sự kết hợp với Obsidian khớp tự nhiên vì kho tri thức (vault) của Obsidian về bản chất chỉ là một thư mục thông thường, bên trong toàn là tệp Markdown tiêu chuẩn. OpenClaw không cần API riêng, trực tiếp đọc ghi ",
    " 文件，用 ": " tệp thông qua hệ thống tệp, dùng ",
    " 等 Shell 命令扫描和检索内容，这使得整套方案": " và các lệnh Shell khác để quét và tìm kiếm nội dung, điều này giúp toàn bộ giải pháp",
    "零依赖、高性能、不受 Obsidian 版本更新影响": "không phụ thuộc, hiệu suất cao, không bị ảnh hưởng bởi cập nhật phiên bản Obsidian",
    "在具体能力上，OpenClaw 可以用自然语言查询笔记内容（如\"找出所有提到 AI Agent 的笔记\"）、自动创建或更新笔记、分析笔记间的关联并建议双向链接，还能自动整理杂乱结构、修复损坏链接、清理重复内容。":
        "Về khả năng cụ thể, OpenClaw có thể dùng ngôn ngữ tự nhiên truy vấn nội dung ghi chú (như \"tìm tất cả ghi chú đề cập AI Agent\"), tự động tạo hoặc cập nhật ghi chú, phân tích liên kết giữa các ghi chú và đề xuất liên kết hai chiều, còn có thể tự động sắp xếp cấu trúc lộn xộn, sửa liên kết hỏng, dọn dẹp nội dung trùng lặp.",
    "直播中提到的两个关键机制，使整个知识体系从\"静态存储\"跃迁为\"动态激活\"：":
        "Hai cơ chế quan trọng được đề cập trong livestream, giúp toàn bộ hệ thống tri thức chuyển từ \"lưu trữ tĩnh\" sang \"kích hoạt động\":",
    "心跳机制（Heartbeat）​": "Cơ chế heartbeat (Heartbeat)",
    "：让 AI Agent 可以定期主动\"感知\"知识库状态，而不是被动等待查询。例如每天自动扫描新增笔记、生成知识图谱摘要、发现潜在的笔记关联。":
        ": Cho phép AI Agent định kỳ chủ động \"cảm nhận\" trạng thái kho tri thức, thay vì thụ động chờ truy vấn. Ví dụ mỗi ngày tự động quét ghi chú mới, tạo tóm tắt đồ thị tri thức, phát hiện liên kết ghi chú tiềm năng.",
    "Cron 机制": "Cơ chế Cron",
    "：允许设定定时任务，让 Agent 按计划自动执行特定操作，例如定时整理新增笔记、生成摘要、更新知识图谱，甚至定期备份重要内容。":
        ": Cho phép thiết lập tác vụ hẹn giờ, để Agent tự động thực thi các thao tác cụ thể theo lịch, ví dụ định kỳ sắp xếp ghi chú mới, tạo tóm tắt, cập nhật đồ thị tri thức, thậm chí sao lưu định kỳ nội dung quan trọng.",
    "这两个机制的结合，使得整个知识体系不再是死板的文档堆积，而是一个":
        "Sự kết hợp của hai cơ chế này giúp toàn bộ hệ thống tri thức không còn là đống tài liệu cứng nhắc, mà là một",
    "有节律、会自我更新的活体系统": "hệ thống sống có nhịp điệu, tự cập nhật",
    "。结合当前开源社区对 AI 记忆（Memory）机制的持续改进，以及大模型上下文窗口的不断扩展，个人知识库与 AI 的协同效率正在以指数级速度提升。":
        ". Kết hợp với việc cộng đồng mã nguồn mở liên tục cải tiến cơ chế bộ nhớ (Memory) AI, cũng như cửa sổ ngữ cảnh của mô hình lớn không ngừng mở rộng, hiệu quả phối hợp giữa kho tri thức cá nhân và AI đang tăng với tốc độ theo cấp số nhân.",
    "总结与当下环境中的实操建议": "Tổng kết và khuyến nghị thực hành trong bối cảnh hiện tại",
    "2026年，中国 AI 应用层的竞争已从\"谁有模型\"转向\"谁有数据和上下文\"。海外市场同样如此——个人品牌和独立创作者的核心壁垒，越来越依赖于":
        "Năm 2026, cạnh tranh tầng ứng dụng AI ở Trung Quốc đã chuyển từ \"ai có mô hình\" sang \"ai có dữ liệu và ngữ cảnh\". Thị trường quốc tế cũng vậy — rào cản cốt lõi của thương hiệu cá nhân và nhà sáng tạo độc lập ngày càng phụ thuộc vào",
    "可被 AI 调用的结构化个人知识": "tri thức cá nhân cấu trúc hóa có thể được AI gọi dùng",
    "。卡尔的这套方法论，本质上是在回答一个时代命题：在信息爆炸和 AI 普及的双重背景下，":
        ". Phương pháp luận của Carl, về bản chất đang trả lời một mệnh đề thời đại: Trong bối cảnh kép của bùng nổ thông tin và phổ cập AI,",
    "个体如何构建不可替代的认知护城河": "cá nhân làm thế nào để xây dựng hào bảo vệ nhận thức không thể thay thế",
    "对个人发展的举一反三与实操建议": "Áp dụng linh hoạt và khuyến nghị thực hành cho phát triển cá nhân",
    "面对这场由 AI 重塑知识生产方式的浪潮，个人和小型团队与其焦虑，不如找准自己的\"上升流\"。以下是从不同职业角度出发的落地方法论：":
        "Đối mặt với làn sóng AI tái định hình phương thức sản xuất tri thức, cá nhân và nhóm nhỏ thay vì lo lắng, tốt hơn hãy tìm đúng \"dòng đi lên\" của mình. Sau đây là phương pháp luận triển khai từ góc độ nghề nghiệp khác nhau:",
    "面向 AI 自媒体创作者 / 内容博主的建议": "Khuyến nghị cho nhà sáng tạo AI tự truyền thông / blogger nội dung",
    "打造\"知识飞轮\"，让内容自我繁殖。": "Tạo \"bánh đà tri thức\", để nội dung tự sinh sôi.",
    "思路：卡尔能够实现图文日更，核心不是勤奋，而是他构建了一套": "Ý tưởng: Carl có thể cập nhật đồ họa hàng ngày, cốt lõi không phải siêng năng, mà là anh đã xây dựng một bộ",
    "信息自动流入、AI 辅助加工、Obsidian 沉淀输出": "thông tin tự động chảy vào, AI hỗ trợ xử lý, Obsidian lắng đọng đầu ra",
    "的流水线。对于内容创作者而言，这套体系的价值在于：每一篇文章、每一条笔记，都在为下一篇内容提供素材。":
        " dạng dây chuyền. Đối với nhà sáng tạo nội dung, giá trị của hệ thống này là: mỗi bài viết, mỗi ghi chú, đều đang cung cấp tư liệu cho nội dung tiếp theo.",
    "方法论一：在 Obsidian 中建立\"选题库\"插件联动机制。将每日订阅的 RSS 源（推荐使用 ":
        "Phương pháp luận 1: Thiết lập cơ chế liên kết plugin \"kho đề tài\" trong Obsidian. Đồng bộ nguồn RSS đăng ký hàng ngày (khuyến nghị sử dụng ",
    "，国内可用 ": ", trong nước có thể dùng ",
    "Feedly 镜像或竹白": "Feedly mirror hoặc Zhubai",
    "）自动同步到 Obsidian，配合 OpenClaw 的 Cron 任务，每天自动生成一份\"今日可写选题清单\"，彻底解决选题焦虑。出海方向可接入 ":
        ") tự động vào Obsidian, kết hợp tác vụ Cron của OpenClaw, mỗi ngày tự động tạo \"danh sách đề tài có thể viết hôm nay\", giải quyết triệt để lo lắng chọn đề tài. Hướng ra nước ngoài có thể kết nối API của ",
    " 的 API 做英文内容聚合。": " để tổng hợp nội dung tiếng Anh.",
    "方法论二：建立\"读后即资产\"的工作流。每读完一篇文章或看完一个视频，强制输出一段100字以内的\"个人观点备注\"存入 Obsidian，并打上标签。三个月后，这些碎片将自动聚合成可直接发布的深度文章。国内可用 ":
        "Phương pháp luận 2: Thiết lập quy trình \"đọc xong thành tài sản\". Mỗi khi đọc xong một bài viết hoặc xem xong một video, bắt buộc đưa ra một đoạn \"ghi chú quan điểm cá nhân\" dưới 100 từ lưu vào Obsidian, và gắn thẻ. Sau ba tháng, những mảnh ghép này sẽ tự động tổng hợp thành bài viết chuyên sâu có thể xuất bản trực tiếp. Trong nước có thể dùng ",
    "微信读书 + 笔记导出插件": "WeRead + plugin xuất ghi chú",
    "，海外可用 ": ", nước ngoài có thể dùng ",
    "Readwise + Obsidian 官方插件": "Readwise + plugin chính thức Obsidian",
    "实现全自动同步。": "thực hiện đồng bộ hoàn toàn tự động.",
    "面向独立开发者 / 个人产品经理的建议": "Khuyến nghị cho nhà phát triển độc lập / quản lý sản phẩm cá nhân",
    "把自己的知识库变成产品的\"原型机\"。": "Biến kho tri thức của bạn thành \"nguyên mẫu\" sản phẩm.",
    "思路：卡尔提到他正在开发自己的小产品，而他的 Obsidian 体系本身就是产品需求的孵化器。独立开发者最大的浪费，是把大量时间花在\"想清楚做什么\"上，而不是\"快速验证\"上。":
        "Ý tưởng: Carl đề cập anh đang phát triển sản phẩm nhỏ của mình, và hệ thống Obsidian của anh chính là vườn ươm nhu cầu sản phẩm. Lãng phí lớn nhất của nhà phát triển độc lập là dành nhiều thời gian cho \"nghĩ rõ làm gì\" thay vì \"xác minh nhanh\".",
    "方法论一：用 Obsidian 的": "Phương pháp luận 1: Dùng",
    "双向链接（Backlinks）+ Dataview 插件": "liên kết hai chiều (Backlinks) + plugin Dataview",
    "构建\"用户痛点数据库\"。每次在社群、评论区、微博看到用户抱怨某个问题，立刻记录并打标签。用 Dataview 插件自动统计高频痛点，这就是你的":
        " của Obsidian xây dựng \"cơ sở dữ liệu điểm đau người dùng\". Mỗi khi thấy người dùng phàn nàn về vấn đề nào đó trong cộng đồng, phần bình luận, Weibo, lập tức ghi lại và gắn thẻ. Dùng plugin Dataview tự động thống kê điểm đau tần suất cao, đó chính là",
    "最小可行产品（MVP）需求文档": "tài liệu yêu cầu sản phẩm khả thi tối thiểu (MVP)",
    "，比任何用户调研表格都真实。国内可结合": " của bạn, chân thực hơn bất kỳ biểu mẫu khảo sát người dùng nào. Trong nước có thể kết hợp",
    "飞书多维表格": "bảng đa chiều Feishu",
    "做结构化管理，海外可用 ": " để quản lý cấu trúc, nước ngoài có thể dùng ",
    " 双轨并行。": " song hành hai đường.",
    "方法论二：以\"AI 知识管理工具定制服务\"切入 B 端市场。当前大量中小企业有知识沉淀需求但缺乏技术能力，独立开发者可以提供 ":
        "Phương pháp luận 2: Tiếp cận thị trường B2B bằng \"dịch vụ tùy chỉnh công cụ quản lý tri thức AI\". Hiện tại nhiều doanh nghiệp vừa và nhỏ có nhu cầu lắng đọng tri thức nhưng thiếu năng lực kỹ thuật, nhà phát triển độc lập có thể cung cấp ",
    "Obsidian 企业知识库搭建 + OpenClaw 私有化部署": "xây dựng kho tri thức doanh nghiệp Obsidian + triển khai tư nhân hóa OpenClaw",
    "的一站式服务包，按项目收费。在国内，可以重点面向": " gói dịch vụ một cửa, thu phí theo dự án. Trong nước, có thể tập trung hướng đến",
    "律所、咨询公司、教培机构": "văn phòng luật, công ty tư vấn, tổ chức giáo dục đào tạo",
    "等知识密集型行业；出海方向可在 ": " và các ngành thâm dụng tri thức khác; hướng ra nước ngoài có thể trên ",
    "Fiverr 或 Contra": "Fiverr hoặc Contra",
    " 上发布服务，面向中小型 SaaS 团队。": " đăng dịch vụ, hướng đến các nhóm SaaS vừa và nhỏ.",
    "面向职场知识工作者（产品、运营、咨询、教育等）的建议": "Khuyến nghị cho người lao động tri thức tại nơi làm việc (sản phẩm, vận hành, tư vấn, giáo dục, v.v.)",
    "把\"工作记录\"升级为\"职业资产\"。": "Nâng cấp \"bản ghi công việc\" thành \"tài sản nghề nghiệp\".",
    "思路：大多数职场人的工作记录停留在飞书文档或微信收藏里，换工作时归零。Obsidian 的价值在于，它让你的每一次工作经验都成为":
        "Ý tưởng: Bản ghi công việc của hầu hết người đi làm dừng lại ở tài liệu Feishu hoặc mục yêu thích WeChat, khi đổi việc thì về số không. Giá trị của Obsidian là nó biến mỗi kinh nghiệm làm việc của bạn thành",
    "可被 AI 检索和调用的结构化资产": "tài sản cấu trúc hóa có thể được AI tìm kiếm và gọi dùng",
    "，是真正属于个人的职业护城河。": ", là hào bảo vệ nghề nghiệp thực sự thuộc về cá nhân.",
    "方法论一：建立\"项目复盘 → 方法论提炼 → 可复用模板\"的三层结构。每完成一个项目，在 Obsidian 中写一篇结构化复盘（背景、决策、结果、反思），然后让 OpenClaw 帮你提炼出":
        "Phương pháp luận 1: Thiết lập cấu trúc ba tầng \"đánh giá dự án → tinh lọc phương pháp luận → mẫu có thể tái sử dụng\". Mỗi khi hoàn thành một dự án, viết một bài đánh giá cấu trúc trong Obsidian (bối cảnh, quyết định, kết quả, phản ánh), sau đó để OpenClaw giúp bạn tinh lọc ra",
    "可复用的方法论卡片": "thẻ phương pháp luận có thể tái sử dụng",
    "。一年后，你将拥有一套完全个人化的\"职业方法论手册\"，可直接用于面试、接单或开课变现。国内可在":
        ". Sau một năm, bạn sẽ có một bộ \"sổ tay phương pháp luận nghề nghiệp\" hoàn toàn cá nhân hóa, có thể dùng trực tiếp cho phỏng vấn, nhận đơn hoặc mở khóa học kiếm tiền. Trong nước có thể trên",
    "小红书、知识星球": "Xiaohongshu, Knowledge Planet",
    "上以此为内容基础做付费社群；出海可在 ": " lấy đây làm nền tảng nội dung xây dựng cộng đồng trả phí; ra nước ngoài có thể trên ",
    "Gumroad 或 Lemon Squeezy": "Gumroad hoặc Lemon Squeezy",
    " 上出售方法论电子书。": " bán ebook phương pháp luận.",
    "方法论二：用 Obsidian + OpenClaw 构建": "Phương pháp luận 2: Dùng Obsidian + OpenClaw xây dựng",
    "个人\"AI 助理\"": "\"trợ lý AI\" cá nhân",
    "，专门服务于本职工作。例如运营人员可以将历史活动数据、竞品分析报告全部导入 Obsidian，配置 OpenClaw 的 RAG（检索增强生成）功能，让 AI 在每次策划新活动时自动调取历史经验。这不仅提升工作效率，更重要的是在团队中建立":
        ", chuyên phục vụ công việc chính. Ví dụ nhân viên vận hành có thể nhập toàn bộ dữ liệu hoạt động lịch sử, báo cáo phân tích đối thủ vào Obsidian, cấu hình chức năng RAG (Retrieval-Augmented Generation) của OpenClaw, để AI tự động truy xuất kinh nghiệm lịch sử mỗi khi lên kế hoạch hoạt động mới. Điều này không chỉ nâng cao hiệu suất, quan trọng hơn là thiết lập trong nhóm",
    "不可替代的\"活记忆\"角色": "vai trò \"bộ nhớ sống\" không thể thay thế",
    "，是最稳固的职场护城河之一。": ", là một trong những hào bảo vệ nghề nghiệp vững chắc nhất.",
    "面向自由职业者 / 知识付费从业者的建议": "Khuyến nghị cho freelancer / người làm tri thức trả phí",
    "把知识管理体系本身变成可销售的产品。": "Biến bản thân hệ thống quản lý tri thức thành sản phẩm có thể bán.",
    "思路：卡尔的这套方法论本身就是一篇爆款文章的来源。对于自由职业者而言，":
        "Ý tưởng: Phương pháp luận này của Carl chính là nguồn cho một bài viết viral. Đối với freelancer,",
    "方法论即产品": "phương pháp luận chính là sản phẩm",
    "，你用这套体系解决了自己的问题，就意味着你有能力帮别人解决同样的问题。":
        ", bạn dùng hệ thống này giải quyết vấn đề của mình, nghĩa là bạn có khả năng giúp người khác giải quyết vấn đề tương tự.",
    "方法论一：开发\"AI 知识管理体系搭建\"课程或陪跑服务。当前市场上 Obsidian 的中文教程良莠不齐，而结合 OpenClaw 的实操内容几乎是空白地带。可以在":
        "Phương pháp luận 1: Phát triển khóa học hoặc dịch vụ đồng hành \"xây dựng hệ thống quản lý tri thức AI\". Hiện tại trên thị trường, các hướng dẫn tiếng Trung về Obsidian chất lượng không đồng đều, còn nội dung thực hành kết hợp OpenClaw gần như là vùng trống. Có thể trên",
    "小鹅通、得到": "Xiaoetong, Dedao",
    "等平台上线付费课程，或在": " và các nền tảng khác ra mắt khóa học trả phí, hoặc trên",
    "即刻、微信私域": "Jike, miền riêng WeChat",
    "中提供一对一陪跑服务。定价策略上，课程可以走低价引流（99~199元），陪跑服务走高客单价（1000元以上/月），形成漏斗。":
        " cung cấp dịch vụ đồng hành một-một. Về chiến lược định giá, khóa học có thể đi giá thấp thu hút (99~199 tệ), dịch vụ đồng hành đi giá cao (trên 1000 tệ/tháng), tạo phễu.",
    "方法论二：为特定垂直行业输出\"行业定制版知识库模板\"。例如为律师行业定制\"案例管理 + 法规检索\"Obsidian 模板包，为教师群体定制\"备课 + 学生反馈追踪\"模板包。在国内可通过":
        "Phương pháp luận 2: Xuất \"mẫu kho tri thức tùy chỉnh theo ngành\" cho các ngành dọc cụ thể. Ví dụ tùy chỉnh gói mẫu Obsidian \"quản lý án lệ + tra cứu pháp luật\" cho ngành luật, gói mẫu \"soạn bài + theo dõi phản hồi học sinh\" cho giáo viên. Trong nước có thể thông qua",
    "微信生态": "hệ sinh thái WeChat",
    "分发，出海可在 ": " phân phối, ra nước ngoài có thể trên ",
    "Obsidian 官方论坛或 Reddit 的 r/ObsidianMD": "diễn đàn chính thức Obsidian hoặc r/ObsidianMD trên Reddit",
    " 社区免费发布基础版、付费升级版，借助社区流量实现冷启动。": " cộng đồng phát hành miễn phí phiên bản cơ bản, phiên bản nâng cấp trả phí, tận dụng lưu lượng cộng đồng để cold start.",
    "会议中的金句时刻": "Khoảnh khắc câu nói vàng trong cuộc họp",
    "相关链接": "Liên kết liên quan",
    "妙记：": "Ghi chú thông minh:",
    "03-03 | 花10分钟用Obsidian+OpenClaw彻底重构你的AI知识管理体系\n\n🎤 特邀嘉宾\n卡尔的AI沃茨：公众号AI自媒体Top10、视频号AI自媒体Top30、前字节大模型算法工程师\n\n💡 直播核心亮点：\n✅ 全程实操｜带你用「Obsidian+OpenClaw」构建高效知识管理体系\n✅ 避坑指南｜拆解各个工具使用痛点与技巧，助你少走弯路快速上手\n":
        "03-03 | Dành 10 phút dùng Obsidian+OpenClaw tái cấu trúc hoàn toàn hệ thống quản lý tri thức AI của bạn\n\n🎤 Khách mời đặc biệt\nAI Watts của Carl: Top 10 tài khoản công khai AI tự truyền thông, Top 30 video AI tự truyền thông, cựu kỹ sư thuật toán mô hình lớn tại ByteDance\n\n💡 Điểm nổi bật của buổi livestream:\n✅ Thực hành toàn bộ | Hướng dẫn bạn xây dựng hệ thống quản lý tri thức hiệu quả bằng「Obsidian+OpenClaw」\n✅ Hướng dẫn tránh bẫy | Phân tích điểm đau và mẹo sử dụng từng công cụ, giúp bạn ít đi đường vòng và nhanh chóng bắt đầu\n",
    "WaytoAGI晚8点共学": "WaytoAGI Học chung lúc 8 giờ tối",
    "文字记录": "Bản ghi văn bản",
    "相关会议纪要": "Biên bản họp liên quan",
}

# Now handle the remaining "智能纪要" entries - these are meeting minutes titles
# Most of them are mixed CN/EN and should be translated
remaining_texts = []

with open('_art25_cn_texts.json', 'r', encoding='utf-8') as f:
    all_cn_texts = json.load(f)

for t in all_cn_texts:
    if t not in trans:
        remaining_texts.append(t)

print(f"Translated: {len(trans)}")
print(f"Remaining: {len(remaining_texts)}")

# Save remaining for inspection
with open('_art25_remaining.json', 'w', encoding='utf-8') as f:
    json.dump(remaining_texts, f, ensure_ascii=False, indent=2)

print("Saved remaining texts to _art25_remaining.json")
