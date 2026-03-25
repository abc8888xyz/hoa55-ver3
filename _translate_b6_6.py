# -*- coding: utf-8 -*-
"""Translate _art_b6_6_orig.json CN->VI, preserve style/URL/code/emoji, add space between adjacent VI text_runs"""
import json, sys, re, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art_b6_6_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation map: Chinese text -> Vietnamese text
# For text_runs with links or inline_code, keep content as-is
# For pure URLs, keep as-is
# For model names, technical terms, keep as-is

CN_VI = {
    "Openclaw一周烧掉我14亿Token后，我总结了这10条血泪教训": "Sau khi Openclaw đốt 1,4 tỷ Token của tôi trong một tuần, tôi đã rút ra 10 bài học xương máu này",
    "🔗 原文链接： ": "🔗 Link bài gốc: ",
    "原创 DracoVibeCoding DracoVibeCoding Draco正在VibeCoding": "Nguyên tác DracoVibeCoding DracoVibeCoding Draco đang VibeCoding",
    "2026年2月22日 16:49  澳大利亚": "22/02/2026 16:49  Australia",
    "小伙伴们也可以通过阿里云百炼": "Các bạn cũng có thể triển khai thông qua Alibaba Cloud Bailian",
    "来部署": " để triển khai",
    "：": ":",
    "首购低至 7.9 元，续费 5 折起，支持Qwen3.5、Qwen3-max、Qwen3-coder、GLM-5、GLM-4.7、Kimi-k2.5等模型": "Mua lần đầu chỉ từ 7,9 tệ, gia hạn từ 5 折, hỗ trợ Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 và nhiều mô hình khác",
    "👉戳链接直达：": "👉 Nhấn link truy cập ngay:",
    "👉查看详细部署教程：": "👉 Xem hướng dẫn triển khai chi tiết:",
    "最多三步，即可拥有 7x 24小时在线、随时响应的AI助手": "Chỉ tối đa ba bước, bạn có thể sở hữu trợ lý AI trực tuyến 7x24 giờ, phản hồi mọi lúc",
    "原文：I Burned 1.4B Codex Tokens in a Week Running OpenClaw. Here's What I'd Tell Myself on Day One.": "Bài gốc: I Burned 1.4B Codex Tokens in a Week Running OpenClaw. Here's What I'd Tell Myself on Day One.",
    "作者：legendaryy (@legendaryy)": "Tác giả: legendaryy (@legendaryy)",
    "日期：20 Feb 2026": "Ngày: 20 Feb 2026",
    "一开始我以为，装个OpenClaw，丢给它几个任务，然后让它自己跑就完事了。演示视频里就是这么讲的。但前两周根本不是这么回事。": "Ban đầu tôi nghĩ, cài OpenClaw, giao cho nó vài nhiệm vụ, rồi để nó tự chạy là xong. Video demo nói vậy mà. Nhưng hai tuần đầu hoàn toàn không phải như vậy.",
    "前两周简直就是\"带娃\"——盯着它烧token，看着它在同一个答案上循环八次，看着Codex任务在那儿空转。我布置个任务，走开一会儿，回来发现它要么只做了一件事就罢工了，要么陷入和自己关于用tab还是space的无限对话里。": 'Hai tuần đầu đúng nghĩa là "trông trẻ" -- theo dõi nó đốt token, nhìn nó lặp cùng một câu trả lời tám lần, nhìn task Codex chạy không. Tôi giao một nhiệm vụ, đi ra ngoài một lát, quay lại phát hiện nó hoặc chỉ làm một việc rồi đình công, hoặc rơi vào cuộc tranh luận bất tận với chính nó về dùng tab hay space.',
    "经过大量试错，现在它终于能稳定运行，真的在干正事了。从\"这玩意儿就是个玩具\"到\"我睡觉的时候它把功能都上线了\"，这个差距是真实存在的。关键就在于，你得停止把它当聊天机器人，开始把它当基础设施来看待。": 'Sau rất nhiều thử sai, giờ nó cuối cùng đã chạy ổn định, thực sự làm việc nghiêm túc. Từ "cái này chỉ là đồ chơi" đến "tôi ngủ dậy thì nó đã deploy hết feature rồi", khoảng cách này là có thật. Chìa khóa là bạn phải ngừng coi nó như chatbot, bắt đầu coi nó như hạ tầng.',
    "下面是真正起作用的东西。10个我想告诉每个今天刚开始的人的事。": "Dưới đây là những thứ thực sự có tác dụng. 10 điều tôi muốn nói với mọi người mới bắt đầu hôm nay.",
    "1. 模型路由决定一切（别用Opus去跑心跳）": "1. Định tuyến mô hình quyết định tất cả (đừng dùng Opus để chạy heartbeat)",
    "这是最关键的决策，也是我14亿token主要烧在哪儿的原因。我把所有东西都往Opus或Codex上怼——心跳、定时检查、状态ping、普通聊天，全都在用最贵的模型。": "Đây là quyết định quan trọng nhất, cũng là lý do 1,4 tỷ token của tôi bị đốt ở đâu. Tôi đẩy mọi thứ lên Opus hoặc Codex -- heartbeat, kiểm tra định kỳ, status ping, chat thông thường, tất cả đều chạy trên mô hình đắt nhất.",
    "这周开始，Sonnet 4.6是日常使用的最佳选择。刚发布，基本上有Opus级别的智商，但只需要五分之一的成本。输入/输出每百万token只要$3/$15美元，而Opus是15/75美元。它在OSWorld上得分72.5%，几乎追平Opus 4.6的72.7%。性格也很好。这是我用过最适合做agent工作的模型，质量够硬还不会让你大出血。": "Từ tuần này, Sonnet 4.6 là lựa chọn tốt nhất cho sử dụng hàng ngày. Vừa ra mắt, về cơ bản có IQ ngang Opus, nhưng chỉ cần một phần năm chi phí. Input/output mỗi triệu token chỉ $3/$15, trong khi Opus là $15/$75. Nó đạt 72.5% trên OSWorld, gần bằng 72.7% của Opus 4.6. Tính cách cũng tốt. Đây là mô hình phù hợp nhất để làm agent mà tôi từng dùng, chất lượng đủ cứng mà không làm bạn chảy máu.",
    "如果Sonnet的价格对你的配置来说还是太贵，那就降级到Kimi K2.5，通过OpenRouter调用。大约$0.60/$2美元每百万token，工具调用也很稳定。把Opus预算留到真正需要深度推理或长上下文作的时候。": "Nếu giá Sonnet vẫn quá đắt cho cấu hình của bạn, thì hạ xuống Kimi K2.5, gọi qua OpenRouter. Khoảng $0.60/$2 mỗi triệu token, tool calling cũng rất ổn định. Dành ngân sách Opus cho khi thực sự cần suy luận sâu hoặc xử lý context dài.",
    "设置一个分层配置。好模型做主引擎处理日常任务，强力模型做后备处理复杂工作。": "Thiết lập cấu hình phân tầng. Mô hình tốt làm engine chính xử lý task hàng ngày, mô hình mạnh làm dự phòng xử lý công việc phức tạp.",
    "你可以在聊天中用/model随时切换模型。需要Opus处理复杂任务？切换。回到常规工作？切回Sonnet。上面的配置会自动处理后备方案，如果主模型碰到速率限制的话。": "Bạn có thể dùng /model trong chat để chuyển mô hình bất kỳ lúc nào. Cần Opus xử lý task phức tạp? Chuyển. Quay lại công việc thường? Chuyển về Sonnet. Cấu hình trên sẽ tự động xử lý phương án dự phòng nếu mô hình chính bị rate limit.",
    "2. 不写Skill文件，你的agent就是个智障": "2. Không viết file Skill, agent của bạn sẽ chỉ là đồ ngốc",
    "刚开箱的时候，你的OpenClaw agent会做一些让人叹为观止的蠢事。在同一个失败的方法上循环六次。编辑它根本没资格碰的配置文件。跳过文档自己瞎编解决方案，结果把整个项目搞崩。模型是聪明的，agent行为不是。这是两回事。": "Lúc mới mở hộp, OpenClaw agent của bạn sẽ làm những điều ngu ngốc đến kinh ngạc. Lặp lại cùng một phương pháp thất bại sáu lần. Chỉnh sửa file cấu hình mà nó không có quyền đụng vào. Bỏ qua tài liệu tự bịa giải pháp, kết quả là đổ sập cả project. Mô hình thì thông minh, hành vi agent thì không. Đây là hai chuyện khác nhau.",
    "解决办法是Skill文件。": "Giải pháp là file Skill.",
    "这些文件放在你的workspace/skills/文件夹里，告诉agent具体该怎么表现。把它们想象成防止你的agent越野脱缰的护栏。": "Những file này nằm trong thư mục workspace/skills/ của bạn, cho agent biết cụ thể phải hành xử thế nào. Hãy coi chúng như lan can ngăn agent của bạn chạy lạc đường.",
    "这是大多数人跳过的部分": "Đây là phần mà hầu hết mọi người bỏ qua",
    "你得自己写这些规则。没人知道你的技术栈、你的偏好，或者你的agent具体会以什么方式搞砸。你是在为一个能力很强但非常死板的员工写操作手册。没有它，你就只能祈祷。": "Bạn phải tự viết những quy tắc này. Không ai biết tech stack của bạn, sở thích của bạn, hay agent của bạn cụ thể sẽ phá hỏng theo cách nào. Bạn đang viết sổ tay vận hành cho một nhân viên rất giỏi nhưng cực kỳ cứng nhắc. Không có nó, bạn chỉ còn cách cầu nguyện.",
    "让我错误率直接砍半的一条规则：做任何改动之前，先读文档。Agent喜欢即兴发挥，它们会硬刚那些文档里早就有的优雅解决方案。我做了个叫DocClaw的Skill，强制\"先读再做\"的工作流，在任何代码改动前必须有个侦察阶段。已经在ClawHub上了。": 'Một quy tắc giúp tôi giảm tỷ lệ lỗi ngay lập tức 50%: đọc tài liệu trước khi làm bất kỳ thay đổi nào. Agent thích ngẫu hứng, chúng sẽ cứng đầu cố giải quyết những vấn đề mà tài liệu đã có giải pháp thanh lịch từ lâu. Tôi đã tạo một Skill tên DocClaw, bắt buộc workflow "đọc trước làm sau", phải có giai đoạn trinh sát trước mọi thay đổi code. Đã có trên ClawHub.',
    "没有这些文件，你的agent干完一件事就卡住了。没有后续，没有迭代。只有一个昂贵的光标在凌晨3点等你告诉它该干嘛。": "Không có những file này, agent của bạn làm xong một việc rồi treo. Không có bước tiếp theo, không có lặp lại. Chỉ có một con trỏ đắt đỏ lúc 3 giờ sáng chờ bạn bảo nó phải làm gì.",
    "3. Soul.md是你的大脑，不是你的待办清单": "3. Soul.md là bộ não của bạn, không phải danh sách việc cần làm",
    "构建 → 测试 → 记录 → 决策 → 循环": "Xây dựng → Kiểm thử → Ghi chép → Quyết định → Lặp lại",
    "4. Todo.md = 自动扩展的任务清单": "4. Todo.md = Danh sách task tự mở rộng",
    "自扩展任务列表。": "Danh sách task tự mở rộng.",
    "睡前给agent一个大任务。它会分解成子任务，工作时更新状态，发现后续工作时生成新任务。午夜的一个任务，到早上可能变成三四个。": "Trước khi đi ngủ giao cho agent một task lớn. Nó sẽ phân tách thành các task con, cập nhật trạng thái khi làm việc, tạo task mới khi phát hiện công việc tiếp theo. Một task lúc nửa đêm, đến sáng có thể thành ba bốn task.",
    "5. ProgressLog.md = 你的晨间简报": "5. ProgressLog.md = Bản tin buổi sáng của bạn",
    "每轮构建-测试循环都要记录。它试了什么，通过还是失败，学到了什么。边喝咖啡边打开这个，不用看会话记录就知道昨晚发生了什么。": "Mỗi vòng build-test đều phải ghi lại. Nó đã thử gì, pass hay fail, học được gì. Vừa uống cà phê vừa mở cái này, không cần xem lịch sử hội thoại cũng biết đêm qua xảy ra chuyện gì.",
    "6. Cron job > 长会话": "6. Cron job > Phiên làm việc dài",
    "你不能布置个任务就合上笔记本。会话只有在开着的时候才有状态。窗口一关，agent就全忘了。真正的后台工作需要定时任务，按计划唤醒agent。": "Bạn không thể giao task rồi gập laptop lại. Session chỉ có trạng thái khi đang mở. Đóng cửa sổ, agent quên hết. Công việc nền thực sự cần task định kỳ, đánh thức agent theo lịch trình.",
    "我跑了三个定时任务：凌晨2点、4点、6点。每个都会唤醒agent，让它检查Todo.md里的剩余任务。有活就接着干，干完了就写个总结然后继续睡觉。": "Tôi chạy ba task định kỳ: 2 giờ sáng, 4 giờ, 6 giờ. Mỗi task đều đánh thức agent, bảo nó kiểm tra các task còn lại trong Todo.md. Còn việc thì làm tiếp, xong rồi thì viết tóm tắt rồi ngủ tiếp.",
    "在这些定时任务之前，agent会在任务中途卡住，然后闲置几小时直到我注意到。定时任务就像闹钟。最坏情况下，它闲置两小时就会被戳醒继续干活。": "Trước khi có những task định kỳ này, agent sẽ bị kẹt giữa chừng, rồi nằm không mấy tiếng cho đến khi tôi phát hiện. Task định kỳ giống như đồng hồ báo thức. Trường hợp xấu nhất, nó nằm không hai tiếng là bị gọi dậy làm tiếp.",
    "7. 文件就是记忆": "7. File chính là bộ nhớ",
    "长会话会被压缩。这意味着你的agent会悄悄丢失上下文。它之前做的决策、跟踪的状态、已经搞清楚的东西，全没了。然后它从头开始重新推导一遍，烧token做已经做过的工作，有时候第二次还会得出不同结论。": "Phiên dài sẽ bị nén. Điều này có nghĩa agent của bạn sẽ âm thầm mất context. Những quyết định nó đã đưa ra, trạng thái nó đang theo dõi, những thứ nó đã tìm hiểu xong, tất cả biến mất. Rồi nó bắt đầu lại từ đầu, đốt token làm lại công việc đã làm, đôi khi lần thứ hai còn đưa ra kết luận khác.",
    "解决办法是把所有重要的东西都写到workspace的markdown文件里。想象一下，就像给一个每天早上失忆的员工写入职文档。你写得越多，它需要从头搞清楚的就越少。": "Giải pháp là ghi tất cả những thứ quan trọng vào file markdown trong workspace. Hãy tưởng tượng, giống như viết tài liệu onboarding cho một nhân viên mất trí nhớ mỗi sáng. Bạn viết càng nhiều, nó cần tìm hiểu lại từ đầu càng ít.",
    "8. 模型质量 ≠ Agent质量": "8. Chất lượng mô hình ≠ Chất lượng Agent",
    "大部分挫败感不是来自OpenClaw，而是来自那些不会调工具的模型。聊天质量和agent质量是完全不同的两件事。一个模型能写诗，但在需要调用函数、解析结果、决定下一步做什么的时候可能直接卡死。": "Phần lớn sự thất vọng không đến từ OpenClaw, mà đến từ những mô hình không biết gọi tool. Chất lượng chat và chất lượng agent là hai thứ hoàn toàn khác nhau. Một mô hình có thể viết thơ, nhưng khi cần gọi hàm, parse kết quả, quyết định bước tiếp theo thì có thể đứng hình luôn.",
    "这是我从实际使用中发现的东西，都是2026年2月中旬的最新数据：": "Đây là những gì tôi phát hiện từ sử dụng thực tế, toàn bộ là dữ liệu mới nhất từ giữa tháng 2/2026:",
    "模型": "Mô hình",
    "Agent质量": "Chất lượng Agent",
    "工具调用": "Tool calling",
    "成本": "Chi phí",
    "优秀": "Xuất sắc",
    "可靠": "Đáng tin cậy",
    "不错": "Khá tốt",
    "Pro订阅": "Gói Pro",
    "尚可": "Tạm được",
    "稳定": "Ổn định",
    "我的日常配置：Sonnet 4.6作为OpenClaw的日常主力。刚发布，基本上是Opus级别的办公任务能力，但只需要五分之一的价格。OSWorld上72.5%，几乎追平Opus 4.6的72.7%。目前做agent工作性价比最高的模型。": "Cấu hình hàng ngày của tôi: Sonnet 4.6 làm lực lượng chính hàng ngày cho OpenClaw. Vừa ra mắt, cơ bản có năng lực ngang Opus cho tác vụ văn phòng, nhưng chỉ cần một phần năm giá. 72.5% trên OSWorld, gần bằng 72.7% của Opus 4.6. Hiện tại là mô hình có tỷ lệ chất lượng/giá tốt nhất cho agent.",
    "Opus 4.6留给需要严肃推理或长上下文的工作。100万token上下文窗口。最强大脑，只是你不想让心跳任务跑在上面。": "Opus 4.6 dành cho công việc cần suy luận nghiêm túc hoặc context dài. Cửa sổ context 1 triệu token. Bộ não mạnh nhất, chỉ là bạn không muốn chạy task heartbeat trên đó.",
    "GPT-5.3-Codex专门用来写代码。比5.2快25%，在SWE-Bench Pro和Terminal-Bench 2.0上都是最顶尖的。我在Codex app/CLI里用它做开发工作，和OpenClaw运维分开。": "GPT-5.3-Codex chuyên dùng để viết code. Nhanh hơn 5.2 25%, đứng đầu trên cả SWE-Bench Pro và Terminal-Bench 2.0. Tôi dùng nó trong Codex app/CLI cho công việc phát triển, tách biệt với vận hành OpenClaw.",
    "Agent苦力活的预算模型：Kimi K2.5通过OpenRouter或NVIDIA调用依然便宜得离谱。MiniMax M2.5是预算之王：SWE-Bench上80.2%，开源，MIT协议，输入每百万token只要0.30美元。GLM-5做重推理任务很稳。这三个工具调用都很可靠，这才是agent工作最重要的。": "Mô hình ngân sách cho việc nặng nhọc của Agent: Kimi K2.5 gọi qua OpenRouter hoặc NVIDIA vẫn rẻ bất ngờ. MiniMax M2.5 là vua ngân sách: 80.2% trên SWE-Bench, mã nguồn mở, giấy phép MIT, input chỉ $0.30 mỗi triệu token. GLM-5 làm task suy luận nặng rất ổn. Cả ba đều tool calling đáng tin cậy, đây mới là điều quan trọng nhất cho agent.",
    "9. 一次只加一个新集成": "9. Mỗi lần chỉ thêm một tích hợp mới",
    "别试图一次性把邮件+日历+Telegram+网页爬虫+定时任务全配上。每个集成都是一个独立的故障点。每个渠道都是一个新的出错表面。": "Đừng cố gắng cấu hình email + lịch + Telegram + web crawler + task định kỳ cùng một lúc. Mỗi tích hợp là một điểm lỗi độc lập. Mỗi kênh là một bề mặt lỗi mới.",
    "我从一个简单的晨间简报定时任务开始。稳定跑了一周后，才加下一个。然后再下一个。每个都搞稳了再往前走。出问题了就跑 ": "Tôi bắt đầu từ một task định kỳ tin tức buổi sáng đơn giản. Chạy ổn định một tuần rồi mới thêm cái tiếp theo. Rồi cái tiếp theo nữa. Mỗi cái đều ổn rồi mới đi tiếp. Có vấn đề thì chạy ",
    " 。": ".",
    "专业提示": "Mẹo chuyên nghiệp",
    "一旦某个工作流稳定了，让你的agent学习它。让它读Skill文件、定时任务配置、成功运行的日志。当它理解你这套配置的\"正常状态\"是什么样子后，它会更擅长保持系统运行，在问题级联之前发现它们。": 'Khi một workflow đã ổn định, hãy để agent học nó. Cho nó đọc file Skill, cấu hình task định kỳ, log chạy thành công. Khi nó hiểu "trạng thái bình thường" của cấu hình này trông như thế nào, nó sẽ giỏi hơn trong việc giữ hệ thống chạy, phát hiện vấn đề trước khi chúng lan rộng.',
    "10. 分开你的Dev和Ops Agent": "10. Tách biệt Dev Agent và Ops Agent của bạn",
    "Codex / Claude Code 做开发 写代码、调试、上线功能。": "Codex / Claude Code làm phát triển - viết code, debug, deploy feature.",
    "有时候Codex会卡住。换Claude。有时候反过来。不同工作用不同模型。都指向一个有干净git结构的私有GitHub仓库。Agent在组织良好的代码里很擅长识别模式。": "Đôi khi Codex bị kẹt. Chuyển sang Claude. Đôi khi ngược lại. Công việc khác nhau dùng mô hình khác nhau. Tất cả đều trỏ đến một repo GitHub private có cấu trúc git sạch sẽ. Agent rất giỏi nhận diện pattern trong code được tổ chức tốt.",
    "OpenClaw 做运维 监控、调度、通信、自动化。": "OpenClaw làm vận hành - giám sát, điều phối, giao tiếp, tự động hóa.",
    "定时任务、心跳、消息路由、任务管理。把开发和运维分开，这样它们不会互相污染上下文。": "Task định kỳ, heartbeat, định tuyến tin nhắn, quản lý task. Tách phát triển và vận hành ra, để chúng không làm nhiễm context của nhau.",
    "关于记忆系统的补充": "Bổ sung về hệ thống bộ nhớ",
    "最好的agent是不会每次会话都从零开始的。OpenClaw有内置的向量记忆： ": "Agent tốt nhất là agent không bắt đầu từ số 0 mỗi phiên. OpenClaw có bộ nhớ vector tích hợp: ",
    " 和 ": " và ",
    " 。还有Claw Vault和Supermemory可以做更高级的设置。": ". Ngoài ra còn có Claw Vault và Supermemory để thiết lập nâng cao hơn.",
    "我自己在搭一个记忆系统（Gigabrain），目前已经索引了911+条记忆。每次对话、每个决策、每个偏好都被存储并可搜索。Agent记得上次什么有效、什么坏了、我喜欢什么。这个上下文让一切都更快更可靠。": "Bản thân tôi đang xây một hệ thống bộ nhớ (Gigabrain), hiện đã index 911+ bản ghi nhớ. Mỗi cuộc hội thoại, mỗi quyết định, mỗi sở thích đều được lưu trữ và có thể tìm kiếm. Agent nhớ lần trước cái gì hiệu quả, cái gì hỏng, tôi thích gì. Context này khiến mọi thứ nhanh hơn và đáng tin cậy hơn.",
    "关键洞察": "Insight quan trọng",
    "透明度和可审计性比单纯的回忆更重要。你得能看到agent\"知道\"关于你和项目的什么。否则你就是在信任一个有shell访问权限的黑盒子。": 'Tính minh bạch và khả năng kiểm toán quan trọng hơn việc đơn thuần ghi nhớ. Bạn phải có thể xem agent "biết" gì về bạn và project. Nếu không, bạn đang tin tưởng một hộp đen có quyền truy cập shell.',
    "关于安全的补充": "Bổ sung về bảo mật",
    "OpenClaw出过真实的安全事故。多个CVE，包括一个CVSS 8.8的远程代码执行漏洞，Bitsight和Censys的扫描团队发现了超过3万个暴露实例，ClawHub还有大规模的供应链投毒活动。你的agent有shell访问权限、浏览器控制权，还能以你的名义发消息。在循环里运行。不需要问你就执行。": "OpenClaw đã từng xảy ra sự cố bảo mật thực tế. Nhiều CVE, bao gồm một lỗ hổng thực thi mã từ xa CVSS 8.8, đội quét của Bitsight và Censys phát hiện hơn 30.000 instance bị lộ, ClawHub còn có chiến dịch đầu độc chuỗi cung ứng quy mô lớn. Agent của bạn có quyền truy cập shell, quyền điều khiển trình duyệt, còn có thể gửi tin nhắn nhân danh bạn. Chạy trong vòng lặp. Không cần hỏi bạn mà vẫn thực thi.",
    "安全审计会标记暴露的网关认证、浏览器控制暴露、提升的允许列表、文件系统权限。光是ClawHavoc活动就在ClawHub上种植了1,184+个恶意Skill，当时占了整个注册表的约12%。这些可不是什么 subtle 的东西：加密货币窃取器、反向shell、伪装成交易机器人和生产力工具的凭证外泄。CrowdStrike、Cisco和Kaspersky都发布了警告。": "Kiểm toán bảo mật sẽ đánh dấu xác thực gateway bị lộ, điều khiển trình duyệt bị lộ, allowlist được nâng cấp, quyền file system. Riêng chiến dịch ClawHavoc đã cài 1.184+ Skill độc hại trên ClawHub, chiếm khoảng 12% toàn bộ registry lúc đó. Đây không phải thứ tinh vi gì: trình đánh cắp tiền mã hóa, reverse shell, rò rỉ credentials giả dạng bot giao dịch và công cụ năng suất. CrowdStrike, Cisco và Kaspersky đều đã phát cảnh báo.",
    "最后": "Cuối cùng",
    "你不是不擅长这个。这事儿现在就是很难。那些发\"我的agent一晚上做了个完整应用\"的人，已经调了几周了。他们烧了token，写了几十页规则，调试了你正在经历的同样卡顿。": 'Không phải bạn không giỏi cái này. Nó bây giờ đúng là rất khó. Những người đăng "agent của tôi làm xong app hoàn chỉnh trong một đêm", đã tinh chỉnh nhiều tuần rồi. Họ đã đốt token, viết hàng chục trang quy tắc, debug cùng những vấn đề mà bạn đang trải qua.',
    "对我有帮助的是：接受这个事实——配置本身就是工作。写**就是产品工作。调整模型路由是基础设施工作。定时任务是运维工作。你不是在用一个工具，你是在搭建一个系统。": "Điều giúp ích cho tôi là: chấp nhận sự thật rằng cấu hình chính là công việc. Viết Skill chính là công việc sản phẩm. Điều chỉnh định tuyến mô hình là công việc hạ tầng. Task định kỳ là công việc vận hành. Bạn không phải đang dùng một công cụ, bạn đang xây dựng một hệ thống.",
    "14亿token之后，agent在我睡觉的时候真的在产出成果。配置就是护城河。大部分人在到达这里之前就放弃了。": "Sau 1,4 tỷ token, agent thực sự đang tạo ra kết quả khi tôi ngủ. Cấu hình chính là con hào. Phần lớn mọi người bỏ cuộc trước khi đến được đây.",
    "存好这篇。发给你的bot。等它在晚上自动产出成果的时候再回来看看。": "Lưu lại bài này. Gửi cho bot của bạn. Chờ đến khi nó tự động tạo ra kết quả vào ban đêm rồi quay lại xem.",
}

def translate_content(text):
    """Translate text, return translated text or original if no translation needed"""
    if text in CN_VI:
        return CN_VI[text]
    # If it's a URL, keep as-is
    if text.startswith("http://") or text.startswith("https://"):
        return text
    # If it's a model name or technical term, keep as-is
    tech_terms = ["Claude Sonnet 4.6", "Claude Opus 4.6", "GPT-5.3-Codex", "Kimi K2.5",
                  "MiniMax M2.5", "GLM-5", "Coding Plan ", "$3/$15 per 1M", "$15/$75 per 1M",
                  "～$0.6-$2", "per 1M", "$0.3-$1.20 per 1M", "$0.75-$2.55 per 1M",
                  "openclaw doctor --fix", "openclaw memory status", "openclaw memory search",
                  "2.9"]
    if text in tech_terms or text.strip() in tech_terms:
        return text
    # Return original if no match
    return text

def is_chinese(text):
    """Check if text contains Chinese characters"""
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def needs_space_between(prev_text, next_text):
    """Check if space needed between two adjacent Vietnamese text_runs"""
    if not prev_text or not next_text:
        return False
    last_char = prev_text[-1]
    first_char = next_text[0]
    # No space if either side is punctuation or already has space
    if last_char in ' \n\t.:,;!?()[]{}' or first_char in ' \n\t.:,;!?()[]{}':
        return False
    # Add space between text content
    if last_char.isalnum() or ord(last_char) > 127:
        if first_char.isalnum() or ord(first_char) > 127:
            return True
    return False

# Process blocks
trans_data = copy.deepcopy(data)
stats = {"total_text": 0, "translated": 0, "kept": 0}

for block in trans_data["blocks"]:
    elements = block["elements"]
    new_elements = []

    for i, el in enumerate(elements):
        if el["type"] == "text_run":
            stats["total_text"] += 1
            original = el["content"]

            # Check if has link or inline_code - keep content for links, translate for inline_code only if Chinese
            has_link = el.get("style", {}).get("link")
            has_inline_code = el.get("style", {}).get("inline_code")

            if has_link:
                # Keep URL text as-is
                translated = original
            elif has_inline_code:
                # Keep code as-is
                translated = original
            else:
                translated = translate_content(original)

            if translated != original:
                stats["translated"] += 1
            else:
                stats["kept"] += 1

            el["content"] = translated
        new_elements.append(el)

    # Add spaces between adjacent Vietnamese text_runs
    final_elements = []
    for i, el in enumerate(new_elements):
        final_elements.append(el)
        # Check if we need to add space between this and next text_run
        if el["type"] == "text_run" and i + 1 < len(new_elements):
            next_el = new_elements[i + 1]
            if next_el["type"] == "text_run":
                curr_text = el["content"]
                next_text = next_el["content"]
                if needs_space_between(curr_text, next_text):
                    # Add space to end of current text_run
                    el["content"] = curr_text + " "

    block["elements"] = final_elements

# Save
with open('_art_b6_6_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans_data, f, ensure_ascii=False, indent=2)

print(f"Total text_runs: {stats['total_text']}")
print(f"Translated: {stats['translated']}")
print(f"Kept as-is: {stats['kept']}")
print(f"Saved to _art_b6_6_trans.json")
