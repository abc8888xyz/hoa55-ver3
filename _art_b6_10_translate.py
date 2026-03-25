# -*- coding: utf-8 -*-
"""Translate _art_b6_10_orig.json CN→VI, output _art_b6_10_trans.json"""
import json, sys, re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art_b6_10_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation map: Chinese text → Vietnamese text
# Rules:
# - Keep English terms, code, URLs, emoji, names as-is
# - Translate Chinese text to natural Vietnamese
# - Keep inline_code content as-is
# - Keep link URLs as-is
# - Add space between adjacent Vietnamese text_runs

TRANS = {
    "教你五步用Telegram创建 OpenClaw 多角色群聊！附邪修大法！（含实操步骤+学不会打我）":
        "Hướng dẫn 5 bước tạo nhóm chat đa vai trò OpenClaw trên Telegram! Kèm chiêu thức cao cấp! (Có hướng dẫn thực hành + không biết thì đánh tui)",
    "🔗 原文链接： ": "🔗 Link bài gốc: ",
    "原创 万万不能的小侠 万万不能的小侠 Berryxia.AI":
        "Nguyên tác: 万万不能的小侠 万万不能的小侠 Berryxia.AI",
    "2026年3月7日 00:08  广东": "Ngày 7 tháng 3 năm 2026, 00:08  Quảng Đông",
    "TIPS：不是人人都需要多个 OpenClaw 龙虾，根据自己的业务需求来创建，并不是越多越好，切记。":
        "TIPS: Không phải ai cũng cần nhiều OpenClaw, hãy tạo theo nhu cầu công việc của mình, không phải càng nhiều càng tốt, hãy nhớ kỹ.",
    "对了，我这个是你默认已经安装好 OpenClaw 了！怎么安装可以看看别人发的教程哈！":
        "À mà, bài này mặc định là bạn đã cài xong OpenClaw rồi nhé! Cách cài đặt thì xem hướng dẫn của người khác nha!",
    "先说结论": "Nói trước kết luận",
    "你以为搭建一个多角色 AI 团队，需要多个机器人账号、多台服务器？":
        "Bạn tưởng để xây dựng một đội AI đa vai trò, cần nhiều tài khoản bot, nhiều máy chủ?",
    "不需要。": "Không cần.",
    "一个 Gateway，一个 Bot，加上几个 Telegram 群组，你就能让产品经理、QA、工程师、内容创作者等多个角色同时在线，互不干扰，还能互相调用。":
        "Một Gateway, một Bot, cộng thêm vài nhóm Telegram, bạn có thể để Product Manager, QA, Kỹ sư, Content Creator và nhiều vai trò khác cùng online, không ảnh hưởng lẫn nhau, còn có thể gọi chéo nhau.",
    "这不是魔法，这是 OpenClaw 的群组路由机制在起作用。":
        "Đây không phải phép thuật, đây là cơ chế định tuyến nhóm của OpenClaw đang hoạt động.",
    "两种架构，按需选择": "Hai kiến trúc, chọn theo nhu cầu",
    "架构一：单 Bot 多群组（推荐入门）": "Kiến trúc 1: Một Bot nhiều nhóm (Khuyến nghị cho người mới)",
    "一个 Bot Token ": "Một Bot Token ",
    "    ├── 群组A → Agent A（产品经理） ": "    ├── Nhóm A → Agent A (Product Manager) ",
    "    ├── 群组B → Agent B（工程师） ": "    ├── Nhóm B → Agent B (Kỹ sư) ",
    "    └── 群组C → Agent C（QA） ": "    └── Nhóm C → Agent C (QA) ",
    "优点： 配置简单，一个 Bot 搞定一切 \n": "Ưu điểm: Cấu hình đơn giản, một Bot xử lý tất cả \n",
    "适用： 个人使用、小团队": "Phù hợp: Sử dụng cá nhân, nhóm nhỏ",
    "架构二：多 Bot 多 Agent（高级玩法）": "Kiến trúc 2: Nhiều Bot nhiều Agent (Cách chơi nâng cao)",
    "Gateway ": "Gateway ",
    "    ├── Bot A (糯糯) → 默认 Agent ": "    ├── Bot A (糯糯) → Agent mặc định ",
    "    ├── Bot B (团团) → life Agent（生活助手） ": "    ├── Bot B (团团) → life Agent (Trợ lý cuộc sống) ",
    "    └── Bot C (爱爱) → ai Agent（技术专家） ": "    └── Bot C (爱爱) → ai Agent (Chuyên gia kỹ thuật) ",
    "优点： 每个 Bot 独立人格，记忆隔离，场景分离 \n":
        "Ưu điểm: Mỗi Bot có tính cách riêng, bộ nhớ cách ly, tình huống tách biệt \n",
    "适用： 多场景、多角色、需要隔离记忆": "Phù hợp: Nhiều tình huống, nhiều vai trò, cần cách ly bộ nhớ",
    "痛点是什么？": "Điểm đau là gì?",
    "你肯定遇到过这种场景：": "Bạn chắc chắn đã gặp tình huống này:",
    "想在 Telegram 里同时跑多个 AI 角色——一个写代码，一个写测试用例，一个做产品分析。但网上的教程告诉你：每个角色都要创建一个 Bot，都要配置一套 Token，都要跑一个 Gateway……":
        "Muốn chạy nhiều vai trò AI đồng thời trên Telegram — một cái viết code, một cái viết test case, một cái phân tích sản phẩm. Nhưng hướng dẫn trên mạng bảo bạn: mỗi vai trò phải tạo một Bot, phải cấu hình một bộ Token, phải chạy một Gateway...",
    "配置到第三个 Bot 的时候，你已经开始怀疑人生了。":
        "Cấu hình đến Bot thứ ba, bạn đã bắt đầu nghi ngờ cuộc đời rồi.",
    "还有一种更隐蔽的坑： 视频教程 。": "Còn có một cái bẫy ẩn giấu hơn: video hướng dẫn.",
    "9 分钟的"保姆级教程"，信息密度极高，你得不停地暂停、倒退、截图。好不容易跟着做完，发现漏了一个步骤，又得重来。":
        "9 phút \"hướng dẫn cầm tay chỉ việc\", mật độ thông tin cực cao, bạn phải liên tục tạm dừng, tua lại, chụp màn hình. Khó khăn lắm mới làm xong theo, phát hiện thiếu một bước, lại phải làm lại.",
    "这篇文章，就是为了解决这个问题而存在的。": "Bài viết này, tồn tại chính là để giải quyết vấn đề đó.",
    "核心原理（一句话讲清楚）": "Nguyên lý cốt lõi (Giải thích trong một câu)",
    "Gateway ：OpenClaw 的"大脑"，负责接收消息、调用 LLM、返回结果。可以理解为 AI 的本地代理服务器。":
        "Gateway: \"Bộ não\" của OpenClaw, chịu trách nhiệm nhận tin nhắn, gọi LLM, trả về kết quả. Có thể hiểu là máy chủ proxy cục bộ của AI.",
    "一个 Gateway 可以托管多个 Agent，每个 Agent 通过"群组路由"绑定到不同的 Telegram 群。":
        "Một Gateway có thể quản lý nhiều Agent, mỗi Agent thông qua \"định tuyến nhóm\" liên kết với các nhóm Telegram khác nhau.",
    "你在群 A 发消息，Gateway 知道该交给"产品经理 Agent"处理；你在群 B 发消息，Gateway 知道该交给"工程师 Agent"处理。":
        "Bạn gửi tin nhắn trong nhóm A, Gateway biết phải giao cho \"Agent Product Manager\" xử lý; bạn gửi tin nhắn trong nhóm B, Gateway biết phải giao cho \"Agent Kỹ sư\" xử lý.",
    "关键在于： 它们共享同一个 Bot 账号，但拥有独立的记忆、权限和工作空间。":
        "Điều quan trọng là: Chúng dùng chung một tài khoản Bot, nhưng có bộ nhớ, quyền hạn và không gian làm việc độc lập.",
    "五步搞定配置": "Năm bước hoàn thành cấu hình",
    "第一步：创建主 Bot（5 分钟）": "Bước 1: Tạo Bot chính (5 phút)",
    "这一步是基础。你需要创建一个"主控 Bot"，它就是所有子 Agent 的"宿主"。":
        "Bước này là nền tảng. Bạn cần tạo một \"Bot chủ\", nó chính là \"máy chủ\" của tất cả Agent con.",
    "在 Telegram 搜索 ": "Trên Telegram tìm kiếm ",
    " ，发送 ": " , gửi ",
    "2。给 Bot 起个名字（比如 ": "2. Đặt tên cho Bot (ví dụ ",
    " ）": " )",
    "3。设置用户名（必须以 ": "3. Đặt username (phải kết thúc bằng ",
    " 结尾，比如 ": " , ví dụ ",
    "复制返回的 Token": "Copy Token được trả về",
    "（长得像 ": "(Trông giống như ",
    "注意：不要泄露此Token 值！": "Lưu ý: Không được tiết lộ giá trị Token này!",
    "然后用这个 Token 把 Bot 接入 OpenClaw：": "Sau đó dùng Token này để kết nối Bot vào OpenClaw:",
    "PS：甚至你可以直接发给 OpenClaw 即可": "PS: Thậm chí bạn có thể gửi trực tiếp cho OpenClaw là được",
    "openclaw config ": "openclaw config ",
    "# 进入 Channels → Telegram → 粘贴 Token ": "# Vào Channels → Telegram → Dán Token ",
    "最后一步配对：": "Bước cuối cùng ghép nối:",
    "# 在 Telegram 与 Bot 私聊，发送 /start 获取 Pairing Code ":
        "# Trên Telegram chat riêng với Bot, gửi /start để lấy Pairing Code ",
    "openclaw pairing approve telegram <你的Pairing Code> ":
        "openclaw pairing approve telegram <Pairing Code của bạn> ",
    "Pairing Code ：类似"验证码"，用于确认你有权限操作这个 Bot。一次配对，永久生效。":
        "Pairing Code: Tương tự \"mã xác nhận\", dùng để xác nhận bạn có quyền thao tác Bot này. Ghép nối một lần, có hiệu lực vĩnh viễn.",
    "PS：这里有一个更简单的办法，就是你可以直接让你现在创建好的这个 OpenClaw 把我的这个内容发给他，让他直接学习操作步骤。":
        "PS: Ở đây có một cách đơn giản hơn, đó là bạn có thể trực tiếp gửi nội dung này cho OpenClaw mà bạn vừa tạo, để nó trực tiếp học các bước thao tác.",
    "创建群聊时，他会引导你一步一步地完成，这是最方便的（如果你不会找这些东西的话）。":
        "Khi tạo nhóm chat, nó sẽ hướng dẫn bạn từng bước hoàn thành, đây là cách tiện nhất (nếu bạn không biết tìm những thứ này).",
    "第二步：开启群组权限（千万别跳过！）": "Bước 2: Bật quyền nhóm (Tuyệt đối đừng bỏ qua!)",
    "这是最容易踩坑的地方。": "Đây là chỗ dễ mắc bẫy nhất.",
    "默认情况下，Bot 开启了"隐私模式"，只能看到 @ 它的消息。如果你不关掉，Bot 在群里就是个"聋子"。":
        "Mặc định, Bot bật \"chế độ riêng tư\", chỉ nhìn thấy tin nhắn @ nó. Nếu bạn không tắt, Bot trong nhóm chỉ là một \"người điếc\".",
    "回到 ": "Quay lại ",
    " ：": " :",
    "设置 BotSetting": "Cài đặt BotSetting",
    "群聊隐私设置": "Cài đặt quyền riêng tư nhóm",
    "关闭隐私模式": "Tắt chế độ riêng tư",
    "/mybots → 选择你的 Bot → Bot Settings ": "/mybots → Chọn Bot của bạn → Bot Settings ",
    "  → Allow Groups: Enable（允许加群） ": "  → Allow Groups: Enable (Cho phép thêm vào nhóm) ",
    "  → Group Privacy: Disable（关闭隐私模式） ": "  → Group Privacy: Disable (Tắt chế độ riêng tư) ",
    "重点：改完之后，必须把 Bot 从群里踢出去，再重新拉进来。":
        "Trọng điểm: Sau khi thay đổi, phải kick Bot ra khỏi nhóm, rồi mời lại vào.",
    "不重新拉，设置不生效。这是很多人配了半天没反应的根本原因。":
        "Không mời lại, cài đặt không có hiệu lực. Đây là nguyên nhân gốc rễ khiến nhiều người cấu hình mãi mà không phản hồi.",
    "第三步：创建群组，拿到 Group ID": "Bước 3: Tạo nhóm, lấy Group ID",
    "每个子 Agent 需要一个专属群组。群组的 ID 就是"路由地址"。":
        "Mỗi Agent con cần một nhóm chuyên dụng. ID của nhóm chính là \"địa chỉ định tuyến\".",
    "新建一个 Telegram 群（建议用角色命名，比如 ":
        "Tạo một nhóm Telegram mới (nên đặt tên theo vai trò, ví dụ ",
    "虾友们": "虾友们",
    "把主 Bot 拉进群": "Mời Bot chính vào nhóm",
    "在群里 @ 你的 Bot，问： ": "Trong nhóm @ Bot của bạn, hỏi: ",
    "当前群组的 ID 是什么？": "ID của nhóm hiện tại là gì?",
    "Bot 会回复一串负数，比如 ": "Bot sẽ trả lời một chuỗi số âm, ví dụ ",
    "-1001234567890": "-1001234567890",
    "把这个 ID 复制保存好，下一步要用。": "Copy lưu ID này lại, bước tiếp theo sẽ dùng.",
    "Group ID ：Telegram 群组的唯一标识符，负数开头。Bot 通过这个 ID 知道消息来自哪个群。":
        "Group ID: Mã định danh duy nhất của nhóm Telegram, bắt đầu bằng số âm. Bot thông qua ID này biết tin nhắn đến từ nhóm nào.",
    "第四步：用 Prompt 自动创建子 Agent（核心步骤）": "Bước 4: Dùng Prompt tự động tạo Agent con (Bước cốt lõi)",
    "这是整个流程最关键的一步。": "Đây là bước quan trọng nhất trong toàn bộ quy trình.",
    "回到 主 Bot 的私聊窗口 ，发送下面这段 Prompt。你只需要把括号里的内容替换成自己的信息：":
        "Quay lại cửa sổ chat riêng của Bot chính, gửi đoạn Prompt bên dưới. Bạn chỉ cần thay thế nội dung trong ngoặc bằng thông tin của mình:",
    "你现在是我的 OpenClaw 主控 Agent，请严格按照以下步骤为我创建一个全新的独立子 Agent： ":
        "Bạn hiện là Agent chủ OpenClaw của tôi, hãy nghiêm túc theo các bước sau để tạo cho tôi một Agent con độc lập hoàn toàn mới: ",
    "1. Agent 基本信息： ": "1. Thông tin cơ bản Agent: ",
    "- Name: 【子 Agent 名称，例如 产品经理】 ": "- Name: 【Tên Agent con, ví dụ Product Manager】 ",
    "- Model: 【模型，例如 gpt-4o 或 claude-3-5-sonnet】 ": "- Model: 【Mô hình, ví dụ gpt-4o hoặc claude-3-5-sonnet】 ",
    "- Workspace: 新建独立 workspace（名称同 Name） ": "- Workspace: Tạo mới workspace độc lập (tên giống Name) ",
    "- Personality: 【角色描述，例如"你是资深产品经理，擅长需求分析、用户研究和产品规划"】 ":
        "- Personality: 【Mô tả vai trò, ví dụ \"Bạn là Product Manager senior, giỏi phân tích yêu cầu, nghiên cứu người dùng và lập kế hoạch sản phẩm\"】 ",
    "2. 配置路由 Bindings： ": "2. Cấu hình định tuyến Bindings: ",
    "- 使用 accountId: \"main\" ": "- Sử dụng accountId: \"main\" ",
    "- 绑定两种 peer 类型： ": "- Liên kết hai loại peer: ",
    "  - peer.kind: \"group\", peer.id: 【你的 Group ID】 ": "  - peer.kind: \"group\", peer.id: 【Group ID của bạn】 ",
    "  - peer.kind: \"channel\", peer.id: 【同上】 ": "  - peer.kind: \"channel\", peer.id: 【Giống trên】 ",
    "- 所有消息路由到这个新 Agent ": "- Tất cả tin nhắn định tuyến đến Agent mới này ",
    "3. 群组策略： ": "3. Chính sách nhóm: ",
    "- requireMention: false（群内无需 @ 就能直接回复） ":
        "- requireMention: false (Trong nhóm không cần @ cũng có thể trả lời trực tiếp) ",
    "- groupPolicy: \"open\"（所有人消息可见） ": "- groupPolicy: \"open\" (Tin nhắn của mọi người đều thấy được) ",
    "- allowFrom: [\"*\"]（开放权限） ": "- allowFrom: [\"*\"] (Mở quyền truy cập) ",
    "4. 防抢消息： ": "4. Chống tranh giành tin nhắn: ",
    "- 为主 Agent 添加 client: \"direct\" + 你的 Telegram 用户 ID 白名单 ":
        "- Thêm cho Agent chính client: \"direct\" + danh sách trắng Telegram user ID của bạn ",
    "请立即执行以上配置，完成后回复确认信息。 ": "Hãy thực hiện ngay cấu hình trên, hoàn thành xong trả lời thông tin xác nhận. ",
    "发送后等待 10-30 秒，主 Agent 会自动创建子 Agent 并返回确认信息。":
        "Sau khi gửi đợi 10-30 giây, Agent chính sẽ tự động tạo Agent con và trả về thông tin xác nhận.",
    "Workspace ：每个 Agent 的"独立办公室"，里面有它自己的记忆、文件、配置。Agent 之间互不干扰。":
        "Workspace: \"Văn phòng độc lập\" của mỗi Agent, bên trong có bộ nhớ, tệp tin, cấu hình riêng. Các Agent không ảnh hưởng lẫn nhau.",
    "第五步：测试，然后加更多角色": "Bước 5: Kiểm thử, sau đó thêm nhiều vai trò hơn",
    "去刚才创建的群组，直接发一条消息：": "Đến nhóm vừa tạo, gửi trực tiếp một tin nhắn:",
    "分别帮我": "Lần lượt giúp tôi",
    "手机": "tìm kiếm",
    "今天的最新AI新闻 ": "tin tức AI mới nhất hôm nay ",
    "如果子 Agent 正常回复了，恭喜你，第一个角色配置成功！":
        "Nếu Agent con trả lời bình thường, xin chúc mừng, vai trò đầu tiên đã cấu hình thành công!",
    "接下来，重复第三步和第四步，创建更多角色：":
        "Tiếp theo, lặp lại bước 3 và bước 4, tạo thêm nhiều vai trò:",
    "QA Agent ：擅长写测试用例、找 Bug": "QA Agent: Giỏi viết test case, tìm Bug",
    "工程师 Agent ：写代码、做架构": "Agent Kỹ sư: Viết code, thiết kế kiến trúc",
    "内容 Agent ：写推文、做文案": "Agent Nội dung: Viết bài đăng, làm copywriting",
    "每个角色一个群，互不干扰。": "Mỗi vai trò một nhóm, không ảnh hưởng lẫn nhau.",
    "更酷的是 ，你可以在主 Bot 私聊里"调度"它们协作：":
        "Tuyệt hơn nữa là, bạn có thể \"điều phối\" chúng cộng tác trong chat riêng với Bot chính:",
    "让产品经理分析需求，QA 写测试用例，工程师给代码实现。 ":
        "Để Product Manager phân tích yêu cầu, QA viết test case, Kỹ sư triển khai code. ",
    "主 Agent 会自动调用对应的子 Agent，把结果汇总给你。":
        "Agent chính sẽ tự động gọi Agent con tương ứng, tổng hợp kết quả cho bạn.",
    "高级玩法：多 Bot 配置": "Cách chơi nâng cao: Cấu hình nhiều Bot",
    "当你需要更清晰的场景分离时，可以配置多个 Bot，每个绑定不同的 Agent。":
        "Khi bạn cần phân tách tình huống rõ ràng hơn, có thể cấu hình nhiều Bot, mỗi cái liên kết Agent khác nhau.",
    "配置示例": "Ví dụ cấu hình",
    "{ ": "{ ",
    "  \"channels\": { ": "  \"channels\": { ",
    "    \"telegram\": { ": "    \"telegram\": { ",
    "      \"accounts\": { ": "      \"accounts\": { ",
    "        \"main\": { ": "        \"main\": { ",
    "          \"botToken\": \"主Bot Token\", ": "          \"botToken\": \"Token Bot chính\", ",
    "          \"groups\": { \"*\": { \"requireMention\": false } } ": "          \"groups\": { \"*\": { \"requireMention\": false } } ",
    "        }, ": "        }, ",
    "        \"life\": { ": "        \"life\": { ",
    "          \"botToken\": \"生活助手Bot Token\", ": "          \"botToken\": \"Token Bot trợ lý cuộc sống\", ",
    "          \"groups\": { \"*\": { \"requireMention\": true } } ": "          \"groups\": { \"*\": { \"requireMention\": true } } ",
    "        \"xiaoxiamiss\": { ": "        \"xiaoxiamiss\": { ",
    "          \"botToken\": \"技术专家Bot Token\", ": "          \"botToken\": \"Token Bot chuyên gia kỹ thuật\", ",
    "      } ": "      } ",
    "    } ": "    } ",
    "  } ": "  } ",
    "} ": "} ",
    "群组响应策略": "Chiến lược phản hồi nhóm",
    "场景：群里有多个 Bot，如何避免混乱？": "Tình huống: Trong nhóm có nhiều Bot, làm sao tránh hỗn loạn?",
    "方案一：默认响应者": "Phương án 1: Người phản hồi mặc định",
    "不指定时 → 糯糯（默认）回答": "Khi không chỉ định → 糯糯 (mặc định) trả lời",
    "@团团 → 团团回答": "@团团 → 团团 trả lời",
    "@爱爱 → 爱爱回答": "@爱爱 → 爱爱 trả lời",
    "方案二：全部需要 @": "Phương án 2: Tất cả đều cần @",
    "所有 Bot 都设置 ": "Tất cả Bot đều cài đặt ",
    "requireMention: true": "requireMention: true",
    "叫谁谁回答": "Gọi ai người đó trả lời",
    "权限管理": "Quản lý quyền hạn",
    "私聊权限": "Quyền chat riêng",
    "{ \n": "{ \n",
    "  \"dmPolicy\": \"pairing\"  // 需要配对码才能私聊 \n":
        "  \"dmPolicy\": \"pairing\"  // Cần mã ghép nối mới có thể chat riêng \n",
    "} \n": "} \n",
    "群组权限": "Quyền nhóm",
    "  \"groupPolicy\": \"allowlist\",  // 白名单模式 \n":
        "  \"groupPolicy\": \"allowlist\",  // Chế độ danh sách trắng \n",
    "  \"allowFrom\": [ \n": "  \"allowFrom\": [ \n",
    "    1867306242,        // 用户ID \n": "    1867306242,        // User ID \n",
    "    -5095174939        // 群组ID \n": "    -5095174939        // Group ID \n",
    "  ] \n": "  ] \n",
    "开放给更多人": "Mở rộng cho nhiều người hơn",
    "场景": "Tình huống",
    "操作": "Thao tác",
    "拉人进现有群": "Mời người vào nhóm hiện có",
    "可以直接拉，bot 会响应该群消息": "Có thể mời trực tiếp, bot sẽ phản hồi tin nhắn nhóm đó",
    "拉 bot 进新群": "Mời bot vào nhóm mới",
    "需要把新群 ID 加到 ": "Cần thêm ID nhóm mới vào ",
    "allowFrom": "allowFrom",
    "其他人与 bot 私聊": "Người khác chat riêng với bot",
    "需要他们的用户 ID 加到 ": "Cần thêm user ID của họ vào ",
    "记忆隔离": "Cách ly bộ nhớ",
    "每个 Agent 有独立的 workspace，记忆互不干扰：":
        "Mỗi Agent có workspace độc lập, bộ nhớ không ảnh hưởng lẫn nhau:",
    "workspace-life/ ": "workspace-life/ ",
    "  ├── IDENTITY.md      # 团团的身份 ": "  ├── IDENTITY.md      # Danh tính của 团团 ",
    "  ├── MEMORY.md        # 团团的长期记忆 ": "  ├── MEMORY.md        # Bộ nhớ dài hạn của 团团 ",
    "  └── memory/          # 团团的日记 ": "  └── memory/          # Nhật ký của 团团 ",
    "workspace-ai/ ": "workspace-ai/ ",
    "  ├── IDENTITY.md      # 爱爱的身份 ": "  ├── IDENTITY.md      # Danh tính của 爱爱 ",
    "  ├── MEMORY.md        # 爱爱的长期记忆 ": "  ├── MEMORY.md        # Bộ nhớ dài hạn của 爱爱 ",
    "  └── memory/          # 爱爱的日记 ": "  └── memory/          # Nhật ký của 爱爱 ",
    "遇到问题怎么办？": "Gặp vấn đề thì làm sao?",
    "群里发消息，Bot 不回复": "Gửi tin nhắn trong nhóm, Bot không trả lời",
    "检查清单：": "Danh sách kiểm tra:",
    "隐私模式关了吗？": "Đã tắt chế độ riêng tư chưa?",
    "BotFather → Group Privacy → Disable": "BotFather → Group Privacy → Disable",
    "改完设置后，重新拉过 Bot 吗？": "Sau khi thay đổi cài đặt, đã mời lại Bot chưa?",
    "必须踢出再重新邀请": "Phải kick ra rồi mời lại",
    "Group ID 复制对了吗？": "Group ID đã copy đúng chưa?",
    "负数开头": "Bắt đầu bằng số âm",
    "Gateway 重启过吗？": "Đã khởi động lại Gateway chưa?",
    "openclaw restart": "openclaw restart",
    "Bot 之间抢消息": "Các Bot tranh giành tin nhắn",
    "检查 ": "Kiểm tra ",
    "requireMention": "requireMention",
    " 配置：": " cấu hình:",
    "false": "false",
    " ：不需要 @也能响应": " : Không cần @ cũng có thể phản hồi",
    "true": "true",
    " ：必须 @才响应": " : Phải @ mới phản hồi",
    "建议： 只让一个 Bot 设为 ": "Khuyến nghị: Chỉ để một Bot cài đặt ",
    " ，其他都 ": " , còn lại đều ",
    "想看详细日志": "Muốn xem nhật ký chi tiết",
    "openclaw logs --follow ": "openclaw logs --follow ",
    "实时查看所有消息路由情况，定位问题很方便。":
        "Xem thời gian thực toàn bộ tình hình định tuyến tin nhắn, định vị vấn đề rất tiện.",
    "不同角色想用不同模型": "Các vai trò khác nhau muốn dùng mô hình khác nhau",
    "在第四步的 Prompt 里，把 ": "Trong Prompt ở bước 4, đổi ",
    "Model": "Model",
    " 改成你想要的：": " thành cái bạn muốn:",
    "gpt-4o": "gpt-4o",
    " ：综合能力强": " : Năng lực tổng hợp mạnh",
    "claude-3-5-sonnet": "claude-3-5-sonnet",
    " ：写代码、推理更强": " : Viết code, suy luận mạnh hơn",
    "gpt-4o-mini": "gpt-4o-mini",
    " ：便宜快速": " : Rẻ và nhanh",
    "常见场景配置": "Cấu hình tình huống thường gặp",
    "场景一：个人助理 + 技术顾问": "Tình huống 1: Trợ lý cá nhân + Cố vấn kỹ thuật",
    "糯糯 （默认）：日常对话、生活助手": "糯糯 (mặc định): Trò chuyện hàng ngày, trợ lý cuộc sống",
    "爱爱 （需 @）：技术问题、代码开发": "爱爱 (cần @): Vấn đề kỹ thuật, phát triển code",
    "场景二：团队协作": "Tình huống 2: Cộng tác nhóm",
    "群 A - 产品经理 ：需求分析、用户研究": "Nhóm A - Product Manager: Phân tích yêu cầu, nghiên cứu người dùng",
    "群 B - 工程师 ：代码实现、架构设计": "Nhóm B - Kỹ sư: Triển khai code, thiết kế kiến trúc",
    "群 C - QA ：测试用例、Bug 分析": "Nhóm C - QA: Test case, phân tích Bug",
    "场景三：多语言服务": "Tình huống 3: Dịch vụ đa ngôn ngữ",
    "Bot A ：中文客服": "Bot A: Chăm sóc khách hàng tiếng Trung",
    "Bot B ：英文客服": "Bot B: Chăm sóc khách hàng tiếng Anh",
    "Bot C ：日文客服": "Bot C: Chăm sóc khách hàng tiếng Nhật",
    "Gateway Token 获取": "Lấy Gateway Token",
    "如果需要通过 API 访问 Gateway：": "Nếu cần truy cập Gateway qua API:",
    "cat ~/.openclaw/openclaw.json | grep -A2 '\"auth\"' ":
        "cat ~/.openclaw/openclaw.json | grep -A2 '\"auth\"' ",
    "Token 用于：": "Token dùng cho:",
    "API 调用": "Gọi API",
    "远程管理": "Quản lý từ xa",
    "第三方集成": "Tích hợp bên thứ ba",
    "写在最后": "Lời kết",
    "AI 时代，一个人就是一个团队。": "Thời đại AI, một người chính là một đội ngũ.",
    "以前，你想同时跑产品经理、QA、工程师，得配三套环境，搞三个 Bot。现在，一个 Gateway 搞定。":
        "Trước đây, muốn chạy đồng thời Product Manager, QA, Kỹ sư, phải cấu hình ba bộ môi trường, tạo ba Bot. Bây giờ, một Gateway là xong.",
    "这不是技术炫耀，这是效率革命。": "Đây không phải khoe kỹ thuật, đây là cuộc cách mạng hiệu suất.",
    "如果你正在用 AI 做产品、写代码、搞内容，这个配置方式值得花 15 分钟试试。配置完成后，你的 Telegram 就变成了一个"AI 作战室"，随时召唤不同角色协同工作。":
        "Nếu bạn đang dùng AI để làm sản phẩm, viết code, làm nội dung, cách cấu hình này đáng để bỏ 15 phút thử. Sau khi cấu hình xong, Telegram của bạn sẽ biến thành một \"phòng tác chiến AI\", bất cứ lúc nào cũng có thể triệu hồi các vai trò khác nhau cùng làm việc.",
    "作者：Berryxia": "Tác giả: Berryxia",
    "欢迎交流：358848136": "Chào mừng trao đổi: 358848136",
}

# Stats
translated_count = 0
kept_count = 0
total_text = 0

for block in data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run':
            content = el['content']
            total_text += 1

            # Skip empty/whitespace only
            if not content.strip():
                kept_count += 1
                continue

            # Skip if it's a URL
            if content.startswith('http://') or content.startswith('https://'):
                kept_count += 1
                continue

            # Skip if inline_code and is technical content (code, commands)
            if el.get('style', {}).get('inline_code'):
                kept_count += 1
                continue

            # Check if has link - keep URLs as-is
            if el.get('style', {}).get('link'):
                kept_count += 1
                continue

            # Look up in translation map
            if content in TRANS:
                el['content'] = TRANS[content]
                translated_count += 1
            else:
                # Check if content is purely non-Chinese (English, numbers, symbols)
                has_chinese = bool(re.search(r'[\u4e00-\u9fff]', content))
                if has_chinese:
                    print(f"UNTRANSLATED: [{content[:80]}]")
                    kept_count += 1
                else:
                    kept_count += 1

# Add spaces between adjacent Vietnamese text_runs
for block in data['blocks']:
    elements = block['elements']
    for i in range(len(elements) - 1):
        el = elements[i]
        next_el = elements[i + 1]
        if el['type'] == 'text_run' and next_el['type'] == 'text_run':
            # Check if current ends without space and next starts without space
            curr = el['content']
            nxt = next_el['content']
            if curr and nxt:
                # If current doesn't end with space/punctuation and next doesn't start with space
                if not curr[-1] in ' \n\t' and not nxt[0] in ' \n\t':
                    # Check if they're Vietnamese text (not code blocks)
                    curr_is_code = el.get('style', {}).get('inline_code', False)
                    next_is_code = next_el.get('style', {}).get('inline_code', False)
                    if not curr_is_code and not next_is_code:
                        # Add trailing space to current element
                        el['content'] = curr + ' '

# Update title
data['title'] = "Hướng dẫn 5 bước tạo nhóm chat đa vai trò OpenClaw trên Telegram! Kèm chiêu thức cao cấp! (Có hướng dẫn thực hành + không biết thì đánh tui)"

with open('_art_b6_10_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total text elements: {total_text}")
print(f"Translated: {translated_count}")
print(f"Kept as-is: {kept_count}")
print(f"Done! Saved to _art_b6_10_trans.json")
