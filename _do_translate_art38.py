# -*- coding: utf-8 -*-
"""Translate art38: 智谱AutoClaw新人1分钟部署指南"""
import json, sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art38_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# CN -> VI translation map (exact text_run content matching)
trans = {
    # Block 0 - page title
    '智谱AutoClaw（澳洲龙虾🦞）来了！新人1分钟部署指南': 'Zhipu AutoClaw (Tôm Hùm Úc 🦞) đã đến! Hướng dẫn triển khai 1 phút cho người mới',
    # Block 1 - quote
    '智谱出品，1分钟极速开养你的专属 AI 助手。体验智谱专为OpenClaw场景深度优化的龙虾专属模型——Pony-Alpha-2（内测代号）。': 'Sản phẩm của Zhipu, khởi tạo trợ lý AI chuyên dụng của bạn siêu tốc trong 1 phút. Trải nghiệm mô hình chuyên dụng Tôm Hùm được Zhipu tối ưu hóa sâu cho kịch bản OpenClaw — Pony-Alpha-2 (mã nội bộ thử nghiệm).',
    # Block 2
    '📖 什么是 AutoClaw？': '📖 AutoClaw là gì?',
    # Block 3 - multi text_run
    'AutoClaw（澳龙）是智谱官方出品的': 'AutoClaw (Tôm Hùm Úc) là sản phẩm chính thức của Zhipu, ',
    '一键本地安装版满血 OpenClaw': 'phiên bản cài đặt cục bộ một chạm OpenClaw đầy đủ tính năng',
    '，目前适配的是OpenClaw 2026.2.6版，国内首个真正意义上让普通用户也能轻松上手的本地 AI 助手。本地安装的含金量懂的都懂，不需要买服务器，内置智谱官方龙虾专用大模型，像安装app一样点击【下一步】即可完成养虾。': ', hiện đang tương thích với phiên bản OpenClaw 2026.2.6, là trợ lý AI cục bộ đầu tiên trong nước thực sự cho phép người dùng bình thường cũng có thể dễ dàng sử dụng. Giá trị của việc cài đặt cục bộ ai hiểu thì hiểu, không cần mua máy chủ, tích hợp sẵn mô hình AI lớn chuyên dụng Tôm Hùm chính thức của Zhipu, chỉ cần nhấn [Tiếp theo] như cài đặt app là hoàn thành việc nuôi tôm.',
    # Block 4
    '核心特点': 'Đặc điểm cốt lõi',
    # Block 5 - emoji + bold + text
    '🚀 ': '🚀 ',
    '一键安装': 'Cài đặt một chạm',
    '：win10 + /macos 11 +（仅支持苹果芯片，不支持intel芯片），下载即用': ': win10+ / macOS 11+ (chỉ hỗ trợ chip Apple, không hỗ trợ chip Intel), tải về là dùng ngay',
    # Block 6
    '📦 ': '📦 ',
    '预置 90+ Skills': 'Tích hợp sẵn 90+ Skills',
    '：无需配置，开箱即用': ': không cần cấu hình, sử dụng ngay',
    # Block 7
    '💬 ': '💬 ',
    '飞书深度集成': 'Tích hợp sâu với Lark',
    '：直接在聊天框给龙虾派活': ': trực tiếp giao việc cho Tôm Hùm trong khung chat',
    # Block 8
    '🤖 ': '🤖 ',
    '多模型支持': 'Hỗ trợ đa mô hình',
    '：内置 Pony-Alpha-2，支持 DeepSeek、Kimi、MiniMax、GLM 等': ': tích hợp sẵn Pony-Alpha-2, hỗ trợ DeepSeek, Kimi, MiniMax, GLM v.v.',
    # Block 9
    '🌐 ': '🌐 ',
    '浏览器自动化': 'Tự động hóa trình duyệt',
    '：集成 AutoGLM Browser-Use，完成复杂网页任务': ': tích hợp AutoGLM Browser-Use, hoàn thành các tác vụ web phức tạp',
    # Block 10
    '💰 ': '💰 ',
    '免费额度 + 灵活付费': 'Hạn mức miễn phí + thanh toán linh hoạt',
    '：0成本体验，按需购买积分包': ': trải nghiệm 0 chi phí, mua gói điểm theo nhu cầu',
    # Block 11
    '为什么选择 AutoClaw？': 'Tại sao chọn AutoClaw?',
    # Block 12
    '传统 OpenClaw 需要配置 Node.js、安装依赖、手动添加 Skills……技术门槛极高，把99%的人挡在门外。': 'OpenClaw truyền thống cần cấu hình Node.js, cài đặt dependencies, thêm Skills thủ công... rào cản kỹ thuật cực cao, chặn 99% người dùng bên ngoài.',
    # Block 13
    'AutoClaw 把这些全部打包好了': 'AutoClaw đã đóng gói tất cả những thứ này',
    '——你只需要下载、安装、连接飞书，即可拥有一个7×24小时专属干活助理。': ' — bạn chỉ cần tải về, cài đặt, kết nối Lark, là có ngay một trợ lý làm việc chuyên dụng 7×24 giờ.',
    # Block 14
    '💻 系统要求': '💻 Yêu cầu hệ thống',
    # Block 15
    '最低配置': 'Cấu hình tối thiểu',
    # Block 16
    '操作系统': 'Hệ điều hành',
    '：win10 + /macos 11 +（仅支持苹果芯片，不支持intel芯片）': ': win10+ / macOS 11+ (chỉ hỗ trợ chip Apple, không hỗ trợ chip Intel)',
    # Block 17
    '内存': 'Bộ nhớ',
    '：至少 4GB RAM（推荐 8GB+）': ': ít nhất 4GB RAM (khuyến nghị 8GB+)',
    # Block 18
    '磁盘空间': 'Dung lượng ổ đĩa',
    '：至少 5GB 可用空间': ': ít nhất 5GB dung lượng trống',
    # Block 19
    '网络': 'Mạng',
    '：稳定的互联网连接': ': kết nối internet ổn định',
    # Block 20
    '推荐配置': 'Cấu hình khuyến nghị',
    # Block 21-23
    '：macOS 12+ / Windows 11': ': macOS 12+ / Windows 11',
    '：8GB+ RAM': ': 8GB+ RAM',
    '：10GB+ 可用空间': ': 10GB+ dung lượng trống',
    # Block 24
    '🚀 快速开始（3步搞定）': '🚀 Bắt đầu nhanh (3 bước hoàn thành)',
    # Block 25
    '第一步：下载 AutoClaw': 'Bước 1: Tải AutoClaw',
    # Block 26
    '访问官网下载页面，选择你的操作系统版本：': 'Truy cập trang tải về trên website chính thức, chọn phiên bản hệ điều hành của bạn:',
    # Block 27 - split: emoji + bold + text
    '🔗 ': '🔗 ',
    '下载地址': 'Địa chỉ tải về',
    # Block 28 - macOS用户: bold + text + code + text
    'macOS 用户': 'Người dùng macOS',
    '：下载 ': ': tải ',
    ' 安装包': ' gói cài đặt',
    # Block 29
    'Windows 用户': 'Người dùng Windows',
    ' 安装程序': ' trình cài đặt',
    # Block 30
    '第二步：安装': 'Bước 2: Cài đặt',
    # Block 31-32-33-34-35
    '双击下载的 ': 'Nhấp đúp vào file ',
    ' 文件': ' đã tải',
    '将 AutoClaw 图标拖入 ': 'Kéo biểu tượng AutoClaw vào thư mục ',
    ' 文件夹': '',
    '在"应用程序"中找到并启动 AutoClaw': 'Tìm và khởi động AutoClaw trong "Ứng dụng"',
    '首次启动时，如果出现安全提示，在"系统设置 → 隐私与安全性"中允许': 'Khi khởi động lần đầu, nếu xuất hiện cảnh báo bảo mật, cho phép trong "Cài đặt hệ thống \u2192 Quyền riêng tư & Bảo mật"',
    # Block 36-39
    '按照"安装向导"点击"下一步"（默认选项即可）': 'Theo "Trình hướng dẫn cài đặt" nhấn "Tiếp theo" (giữ tùy chọn mặc định)',
    '安装完成后，从桌面或开始菜单启动 AutoClaw': 'Sau khi cài đặt xong, khởi động AutoClaw từ desktop hoặc menu Start',
    # Block 40 - split with bold
    'AutoClaw 为每个新用户提供了': 'AutoClaw cung cấp cho mỗi người dùng mới ',
    '免费额度': 'hạn mức miễn phí',
    '，让你 0 成本体验龙虾的全部能力。【AutoClaw首发，限时赠送2000积分】': ', cho phép bạn trải nghiệm 0 chi phí toàn bộ khả năng của Tôm Hùm. [AutoClaw ra mắt, tặng giới hạn thời gian 2000 điểm]',
    # Block 41 - split with link
    '通过邀请注册：': 'Đăng ký qua lời mời: ',
    '，可额外多享500积分。': ', được hưởng thêm 500 điểm.',
    # Block 42
    '注册完，登录账户，即可直接享用龙虾专属模型——Pony-Alpha-2': 'Sau khi đăng ký, đăng nhập tài khoản, có thể trực tiếp sử dụng mô hình chuyên dụng Tôm Hùm — Pony-Alpha-2',
    # Block 43
    '实测每次调用大模型，消耗12-13积分。': 'Thực tế mỗi lần gọi mô hình AI lớn, tiêu tốn 12-13 điểm.',
    # Block 44
    '第三步：连接飞书': 'Bước 3: Kết nối Lark',
    # Block 45
    '首次启动后，AutoClaw 会引导你完成飞书接入：': 'Sau khi khởi động lần đầu, AutoClaw sẽ hướng dẫn bạn hoàn thành kết nối Lark:',
    # Block 46-49
    '登录刚刚注册的账号': 'Đăng nhập tài khoản vừa đăng ký',
    '点击"接入飞书"按钮': 'Nhấn nút "Kết nối Lark"',
    '按提示完成飞书机器人创建和设置。': 'Theo hướng dẫn hoàn thành việc tạo và cài đặt bot Lark.',
    '返回 AutoClaw，确认连接成功': 'Quay lại AutoClaw, xác nhận kết nối thành công',
    # Block 50 - split: text + link
    '详见官方配置说明': 'Xem chi tiết hướng dẫn cấu hình chính thức ',
    '【对外】0基础小白手把手版-飞书bot配置': '[Công khai] Phiên bản hướng dẫn tay từng bước cho người mới - Cấu hình bot Lark',
    # Block 51 - split: emoji + bold + text
    '✅ ': '✅ ',
    '完成！': 'Hoàn thành!',
    ' 现在你可以在飞书对话框中直接和龙虾对话了。': ' Bây giờ bạn có thể trò chuyện trực tiếp với Tôm Hùm trong hộp thoại Lark.',
    # Block 52
    '🎯 第一次对话': '🎯 Cuộc trò chuyện đầu tiên',
    # Block 53
    '在飞书中打开与 AutoClaw 的对话，试试这些指令：': 'Mở cuộc trò chuyện với AutoClaw trong Lark, thử các lệnh sau:',
    # Block 54-58
    '基础对话': 'Hội thoại cơ bản',
    '内容创作': 'Sáng tạo nội dung',
    '信息搜索': 'Tìm kiếm thông tin',
    '代码任务': 'Tác vụ lập trình',
    '文档处理': 'Xử lý tài liệu',
    # Block 59
    '🎁 免费额度与付费': '🎁 Hạn mức miễn phí và thanh toán',
    # Block 60 (heading)
    # Block 61 - split
    '，让你 0 成本体验龙虾的全部能力。': ', cho phép bạn trải nghiệm 0 chi phí toàn bộ khả năng của Tôm Hùm.',
    # Block 62 - split
    '走邀请注册：': 'Đăng ký qua lời mời: ',
    # Block 63
    '付费积分包': 'Gói điểm trả phí',
    # Block 64
    '当免费额度用完后，可选择购买积分包：': 'Khi hạn mức miễn phí đã hết, có thể chọn mua gói điểm:',
    # Block 65-67
    '入门包': 'Gói cơ bản',
    '：适合轻度使用': ': phù hợp sử dụng nhẹ',
    '专业包': 'Gói chuyên nghiệp',
    '：适合日常办公': ': phù hợp công việc văn phòng hàng ngày',
    '企业包': 'Gói doanh nghiệp',
    '：适合团队协作': ': phù hợp làm việc nhóm',
    # Block 68
    '也可以配置自己的大模型API，支持标准的OpenAI和Anthropic两种协议。': 'Cũng có thể cấu hình API mô hình AI lớn của riêng bạn, hỗ trợ hai giao thức tiêu chuẩn OpenAI và Anthropic.',
    # Block 69
    '🤖 模型接入': '🤖 Kết nối mô hình',
    # Block 70
    '内置模型：Pony-Alpha-2（内测）': 'Mô hình tích hợp: Pony-Alpha-2 (thử nghiệm nội bộ)',
    # Block 71 - split
    'AutoClaw 内置智谱专为 OpenClaw 场景深度优化的': 'AutoClaw tích hợp sẵn ',
    '龙虾专属模型': 'mô hình chuyên dụng Tôm Hùm',
    '——Pony-Alpha-2。': ' được Zhipu tối ưu hóa sâu cho kịch bản OpenClaw — Pony-Alpha-2.',
    # Block 72
    '核心优势：': 'Ưu điểm cốt lõi:',
    # Block 73-76
    '✅ 工具调用更稳': '✅ Gọi công cụ ổn định hơn',
    '✅ 任务推进更强': '✅ Thúc đẩy tác vụ mạnh hơn',
    '✅ 响应速度更快': '✅ Tốc độ phản hồi nhanh hơn',
    '✅ 更适合 Skill 调用、定时任务、持续执行等真实工作流': '✅ Phù hợp hơn cho quy trình làm việc thực tế như gọi Skill, tác vụ định thời, thực thi liên tục',
    # Block 77
    '目前 Pony-Alpha-2 内测版本已面向 AutoClaw 用户开放试用。': 'Hiện tại phiên bản thử nghiệm nội bộ Pony-Alpha-2 đã mở dùng thử cho người dùng AutoClaw.',
    # Block 78
    '开放模型接入': 'Kết nối mô hình mở',
    # Block 79 - split
    'AutoClaw 完全开放模型接入，支持任意模型的 ': 'AutoClaw hoàn toàn mở kết nối mô hình, hỗ trợ ',
    ' 或 ': ' hoặc ',
    '，推荐以下模型：': ' của bất kỳ mô hình nào, khuyến nghị các mô hình sau:',
    # Block 80-94 table cells
    '模型': 'Mô hình',
    '特点': 'Đặc điểm',
    '适用场景': 'Kịch bản áp dụng',
    '智谱自研，中文能力强': 'Tự phát triển bởi Zhipu, khả năng tiếng Trung mạnh',
    '日常对话、内容创作': 'Hội thoại hàng ngày, sáng tạo nội dung',
    '性价比高，代码能力强': 'Hiệu quả chi phí cao, khả năng lập trình mạnh',
    '编程任务、逻辑推理': 'Tác vụ lập trình, suy luận logic',
    '长文本处理优秀': 'Xử lý văn bản dài xuất sắc',
    '文档阅读、长篇分析': 'Đọc tài liệu, phân tích dài',
    '多模态能力强': 'Khả năng đa phương thức mạnh',
    '图文生成、创意设计': 'Tạo hình ảnh & văn bản, thiết kế sáng tạo',
    # Block 95
    '🌐 浏览器自动化能力': '🌐 Khả năng tự động hóa trình duyệt',
    # Block 96 - split
    'AutoClaw 集成了智谱自研的 ': 'AutoClaw tích hợp ',
    ' 能力，补齐了 OpenClaw 在执行复杂浏览器任务上的短板。': ' do Zhipu tự phát triển, bổ sung điểm yếu của OpenClaw trong việc thực thi tác vụ trình duyệt phức tạp.',
    # Block 97
    '能做什么？': 'Có thể làm gì?',
    # Block 98-102
    '✅ 自动搜索信息': '✅ Tự động tìm kiếm thông tin',
    '✅ 自动填表提交': '✅ Tự động điền biểu mẫu và gửi',
    '✅ 跨页面操作': '✅ Thao tác xuyên trang',
    '✅ 数据抓取': '✅ Thu thập dữ liệu',
    '✅ 自动化测试': '✅ Kiểm thử tự động',
    # Block 103
    '示例任务': 'Tác vụ mẫu',
    # Block 104
    'AutoClaw 会：': 'AutoClaw sẽ:',
    # Block 105-110
    '自动打开浏览器': 'Tự động mở trình duyệt',
    '访问京东首页': 'Truy cập trang chủ JD.com',
    '搜索 "iPhone 15"': 'Tìm kiếm "iPhone 15"',
    '识别商品卡片': 'Nhận diện thẻ sản phẩm',
    '提取价格信息': 'Trích xuất thông tin giá',
    '回传结果到飞书': 'Gửi kết quả về Lark',
    # Block 111
    '📦 50+ 预置 Skills': '📦 50+ Skills tích hợp sẵn',
    # Block 112 - split
    'AutoClaw 封装了 50+ 主流 Skills 与 API，普通用户': 'AutoClaw đã đóng gói 50+ Skills và API phổ biến, người dùng bình thường ',
    '无需单独配置搜索 API、生图 API 等各类接口': 'không cần cấu hình riêng từng API tìm kiếm, API tạo hình ảnh v.v.',
    '，从安装完成到真正上手几乎没有门槛。': ', từ cài đặt xong đến thực sự sử dụng hầu như không có rào cản.',
    # Block 113
    'Skills 覆盖场景': 'Các kịch bản Skills bao phủ',
    # Block 114-127 table cells
    '类别': 'Danh mục',
    '示例 Skills': 'Skills mẫu',
    '小红书笔记、公众号文章、短视频脚本': 'Bài viết Xiaohongshu, bài công chúng hào, kịch bản video ngắn',
    '办公效率': 'Hiệu suất văn phòng',
    '文档处理、PPT 生成、邮件撰写': 'Xử lý tài liệu, tạo PPT, soạn email',
    '代码开发': 'Phát triển mã',
    '代码生成、代码审查、项目搭建': 'Tạo mã, đánh giá mã, xây dựng dự án',
    '营销推广': 'Marketing quảng bá',
    '竞品分析、用户画像、营销文案': 'Phân tích đối thủ, chân dung người dùng, bài viết marketing',
    '金融投研': 'Nghiên cứu đầu tư tài chính',
    '行研报告、数据分析、财报解读': 'Báo cáo nghiên cứu ngành, phân tích dữ liệu, giải đọc báo cáo tài chính',
    '日常助手': 'Trợ lý hàng ngày',
    '天气查询、日程管理、待办事项': 'Tra cứu thời tiết, quản lý lịch trình, danh sách công việc',
    # Block 128
    '实用案例': 'Ví dụ thực tế',
    # Block 129
    '案例一：社交媒体内容一键生成': 'Ví dụ 1: Tạo nội dung mạng xã hội một chạm',
    # Block 130-134
    '生成多条创意标题': 'Tạo nhiều tiêu đề sáng tạo',
    '撰写正文内容': 'Viết nội dung chính',
    '推荐话题标签': 'Gợi ý hashtag chủ đề',
    '输出排版建议': 'Đưa ra gợi ý bố cục',
    # Block 135
    '案例二：从 PRD 到网站': 'Ví dụ 2: Từ PRD đến website',
    # Block 136-141
    '分析 PRD 需求': 'Phân tích yêu cầu PRD',
    '设计页面结构': 'Thiết kế cấu trúc trang',
    '生成前端代码': 'Tạo mã frontend',
    '搭建基础功能': 'Xây dựng chức năng cơ bản',
    '输出可运行的项目': 'Xuất dự án có thể chạy được',
    # Block 142
    '案例三：金融投研': 'Ví dụ 3: Nghiên cứu đầu tư tài chính',
    # Block 143-147
    '搜索行业数据': 'Tìm kiếm dữ liệu ngành',
    '分析市场趋势': 'Phân tích xu hướng thị trường',
    '识别投资标的': 'Nhận diện mục tiêu đầu tư',
    '输出研究报告': 'Xuất báo cáo nghiên cứu',
    # Block 148
    '⚙️ 进阶配置': '⚙️ Cấu hình nâng cao',
    # Block 149
    '切换模型': 'Chuyển đổi mô hình',
    # Block 150
    '在 AutoClaw 设置中：': 'Trong cài đặt AutoClaw:',
    # Block 151-154
    '点击"模型配置"': 'Nhấn "Cấu hình mô hình"',
    '选择你偏好的模型': 'Chọn mô hình bạn ưa thích',
    '输入 API Key（如需）': 'Nhập API Key (nếu cần)',
    '保存并应用': 'Lưu và áp dụng',
    # Block 155
    '管理技能': 'Quản lý kỹ năng',
    # Block 156-158
    '查看"已安装 Skills"列表': 'Xem danh sách "Skills đã cài đặt"',
    '启用/禁用特定技能': 'Bật/tắt kỹ năng cụ thể',
    '调整技能优先级': 'Điều chỉnh độ ưu tiên kỹ năng',
    # Block 159
    '自动化任务': 'Tác vụ tự động hóa',
    # Block 160
    '设置定时任务或触发规则：': 'Thiết lập tác vụ định thời hoặc quy tắc kích hoạt:',
    # Block 161-163
    '每日晨间简报': 'Bản tin buổi sáng hàng ngày',
    '定期数据监控': 'Giám sát dữ liệu định kỳ',
    '消息自动回复': 'Tự động trả lời tin nhắn',
    # Block 164
    '❓ 常见问题': '❓ Câu hỏi thường gặp',
    # Block 165
    'Q1: AutoClaw 和开源 OpenClaw 有什么区别？': 'Q1: AutoClaw và OpenClaw mã nguồn mở có gì khác nhau?',
    # Block 166 - split: bold "A:" + text
    'A:': 'A:',
    ' AutoClaw 是智谱官方的商业化版本，提供一键安装、预置 Skills、内置模型、浏览器自动化等增强功能，大幅降低了使用门槛。': ' AutoClaw là phiên bản thương mại chính thức của Zhipu, cung cấp cài đặt một chạm, Skills tích hợp sẵn, mô hình tích hợp, tự động hóa trình duyệt và các tính năng nâng cao khác, giảm đáng kể rào cản sử dụng.',
    # Block 167
    'Q2: 免费额度能用来做什么？': 'Q2: Hạn mức miễn phí có thể dùng để làm gì?',
    # Block 168
    ' 免费额度可以体验 AutoClaw 的全部核心功能，包括日常对话、内容创作、信息查询等，足够评估是否适合你。': ' Hạn mức miễn phí có thể trải nghiệm toàn bộ tính năng cốt lõi của AutoClaw, bao gồm hội thoại hàng ngày, sáng tạo nội dung, tra cứu thông tin v.v., đủ để đánh giá xem có phù hợp với bạn không.',
    # Block 169
    'Q3: 隐私和数据安全如何保障？': 'Q3: Quyền riêng tư và bảo mật dữ liệu được đảm bảo như thế nào?',
    # Block 170
    ' AutoClaw 本地执行，你的数据主要保存在本地。只有调用云端模型时才会上传必要信息。': ' AutoClaw thực thi cục bộ, dữ liệu của bạn chủ yếu được lưu trữ tại máy. Chỉ khi gọi mô hình đám mây mới tải lên thông tin cần thiết.',
    # Block 171
    'Q4: 可以同时接入多个飞书账号吗？': 'Q4: Có thể kết nối nhiều tài khoản Lark cùng lúc không?',
    # Block 172
    ' 目前一个 AutoClaw 实例支持接入一个飞书账号。如需多账号，可运行多个 AutoClaw 实例。': ' Hiện tại một instance AutoClaw hỗ trợ kết nối một tài khoản Lark. Nếu cần nhiều tài khoản, có thể chạy nhiều instance AutoClaw.',
    # Block 173
    'Q5: 如何获取 Pony-Alpha-2 内测资格？': 'Q5: Làm thế nào để nhận tư cách thử nghiệm nội bộ Pony-Alpha-2?',
    # Block 174
    ' AutoClaw 用户自动获得 Pony-Alpha-2 内测资格，无需额外申请。': ' Người dùng AutoClaw tự động nhận tư cách thử nghiệm nội bộ Pony-Alpha-2, không cần đăng ký thêm.',
    # Block 175
    '📚 使用技巧': '📚 Mẹo sử dụng',
    # Block 176
    '高效沟通': 'Giao tiếp hiệu quả',
    # Block 177
    '明确目标': 'Mục tiêu rõ ràng',
    '：直接说出想要的结果，而非步骤': ': nói trực tiếp kết quả mong muốn, không phải các bước',
    # Block 178-179
    '✅ "帮我写一篇关于 AI 的文章"': '✅ "Viết giúp tôi một bài về AI"',
    '❌ "帮我思考一下关于 AI 的文章怎么写"': '❌ "Giúp tôi suy nghĩ xem bài viết về AI nên viết thế nào"',
    # Block 180
    '提供上下文': 'Cung cấp ngữ cảnh',
    '：先给背景，再提任务': ': đưa bối cảnh trước, rồi mới giao nhiệm vụ',
    # Block 181-182
    '✅ "我是一名产品经理，需要..."': '✅ "Tôi là một product manager, cần..."',
    '❌ "帮我写个文档"': '❌ "Viết giúp tôi một tài liệu"',
    # Block 183
    '分阶段反馈': 'Phản hồi theo giai đoạn',
    '：复杂任务可分步确认': ': tác vụ phức tạp có thể xác nhận từng bước',
    # Block 184
    '"先写个大纲，我确认后再展开"': '"Viết dàn ý trước, tôi xác nhận rồi mới triển khai"',
    # Block 185
    '典型工作流': 'Quy trình làm việc điển hình',
    # Block 186
    '场景：小红书运营': 'Kịch bản: Vận hành Xiaohongshu',
    # Block 187
    '🆘 需要帮助？': '🆘 Cần trợ giúp?',
    # Block 188 - split: bold + text
    '官网': 'Website chính thức',
    # Block 189 - split: bold + text + link
    '官微': 'WeChat chính thức',
    '：': ': ',
    # Block 190 - split: bold + link
    '用户手册：': 'Sổ tay người dùng: ',
    '📢AutoClaw 产品使用说明书': '📢 Hướng dẫn sử dụng sản phẩm AutoClaw',
    # Block 191 - split: bold + link + text + link
    '澳龙急诊：': 'Cấp cứu Tôm Hùm: ',
    'AutoClaw Windows 10 安装后无法启动问题排查': 'Xử lý sự cố không khởi động được sau khi cài đặt AutoClaw trên Windows 10',
    # Block 192 - split: bold + link
    '飞书配置：': 'Cấu hình Lark: ',
    # Block 193
    '🔮 百虾大战时代来了': '🔮 Thời đại trăm tôm tranh đấu đã đến',
    # Block 194
    '我们正在步入一个「Agent 自主做事」的时代。': 'Chúng ta đang bước vào thời đại "Agent tự chủ làm việc".',
    # Block 195
    '国家队AutoClaw参战，进一步推动了 AI 平权，真正实现了"人人养龙虾"的愿景。': 'Đội tuyển quốc gia AutoClaw tham chiến, thúc đẩy hơn nữa sự bình đẳng AI, thực sự hiện thực hóa tầm nhìn "mọi người đều nuôi tôm hùm".',
    # Block 196
    '现在就开始养你的小澳龙吧！🦞': 'Hãy bắt đầu nuôi Tôm Hùm Úc nhỏ của bạn ngay bây giờ! 🦞',
}

# Apply translations
translated_count = 0
kept_count = 0
missed_cn = []

def has_chinese(s):
    return any(0x4e00 <= ord(c) <= 0x9fff for c in s)

for block in data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run':
            content = el['content']
            if content in trans:
                el['content'] = trans[content]
                translated_count += 1
            else:
                kept_count += 1
                if has_chinese(content):
                    missed_cn.append(content[:120])

print(f'Translated: {translated_count}, Kept: {kept_count}')
if missed_cn:
    print(f'\nMISSED Chinese texts ({len(missed_cn)}):')
    for t in missed_cn:
        print(f'  - {repr(t)}')
else:
    print('All Chinese texts translated!')

# Count total text elements for stats
total_text = 0
translated_text = 0
for block in data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run' and el['content'].strip():
            total_text += 1
            if not has_chinese(el['content']):
                translated_text += 1

print(f'\nStats: {total_text} total text elements, {translated_text} translated/non-CN, {total_text - translated_text} still CN')

with open('_art38_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('\nSaved _art38_trans.json')
