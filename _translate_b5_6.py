# -*- coding: utf-8 -*-
"""Translate _art_b5_6_orig.json Chinese -> Vietnamese"""
import json, sys, re, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Chinese character detection
def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def is_url(text):
    return bool(re.match(r'https?://', text.strip()))

def is_only_emoji_or_punctuation(text):
    """Check if text is only emoji/punctuation/whitespace"""
    cleaned = re.sub(r'[\s\u200b\ufeff]', '', text)
    if not cleaned:
        return True
    # Remove emoji and common punctuation
    cleaned = re.sub(r'[^\u4e00-\u9fff\u3400-\u4dbfa-zA-Z0-9]', '', cleaned)
    return len(cleaned) == 0

# Translation dictionary - comprehensive mapping
TRANSLATIONS = {
    # Page title
    "林月半子：Cloudflare官方出手!OpenClaw 云端部署保姆级教程": "Linyuebanzai: Cloudflare chính thức ra tay! Hướng dẫn triển khai OpenClaw trên đám mây chi tiết từ A-Z",

    # Quote block
    "🔗 原文链接： ": "🔗 Link bài gốc: ",

    # Author info
    "原创 林月半子聊AI 林月半子聊AI 林月半子的AI笔记": "Bài gốc: Linyuebanzai nói về AI - Ghi chép AI của Linyuebanzai",
    "2026年2月3日 18:26  浙江": "Ngày 3 tháng 2 năm 2026, 18:26 - Chiết Giang",

    # Intro paragraphs
    "小伙伴们也可以通过阿里云百炼": "Các bạn cũng có thể thông qua Alibaba Cloud Bailian",
    "来部署": " để triển khai",
    "首购低至 7.9 元，续费 5 折起，支持Qwen3.5、Qwen3-max、Qwen3-coder、GLM-5、GLM-4.7、Kimi-k2.5等模型": "Mua lần đầu chỉ từ 7.9 NDT, gia hạn giảm từ 50%, hỗ trợ các model Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 v.v.",
    "👉戳链接直达：": "👉 Bấm link truy cập trực tiếp:",
    "👉查看详细部署教程：": "👉 Xem hướng dẫn triển khai chi tiết:",
    "最多三步，即可拥有 7x 24小时在线、随时响应的AI助手": "Chỉ cần tối đa ba bước, bạn sẽ có trợ lý AI online 24/7, phản hồi mọi lúc",

    # Main content
    "前几天看到，Cloudflare 也加入了 OpenClaw 的热度之中。": "Mấy hôm trước tôi thấy Cloudflare cũng nhảy vào làn sóng OpenClaw.",
    "他们技术团队开源了，一个叫 Moltworker 的项目，让我们能快速地把 OpenClaw 部署到云端。": "Đội ngũ kỹ thuật của họ đã mã nguồn mở một dự án tên Moltworker, cho phép chúng ta triển khai OpenClaw lên đám mây một cách nhanh chóng.",
    "项目地址 ": "Địa chỉ dự án ",
    "这可不是简单套壳，它内置了浏览器自动化(cloudflare-browser)，可以执行网页截图，还能抓取数据，更支持 R2 存储，实现数据持久化，因此，哪怕容器重启，你的对话历史，和设备配对信息，也不会丢。": "Đây không phải là đơn giản bọc vỏ, nó tích hợp sẵn tự động hóa trình duyệt (cloudflare-browser), có thể chụp ảnh trang web, thu thập dữ liệu, còn hỗ trợ lưu trữ R2, thực hiện lưu trữ dữ liệu bền vững, do đó, ngay cả khi container khởi động lại, lịch sử trò chuyện và thông tin ghép nối thiết bị của bạn cũng không bị mất.",
    "它甚至提供了，完整的管理界面，可以查看 R2 备份状态，审批设备配对请求，还能重启网关进程，并集成 Cloudflare Access，做身份认证保护，安全感拉满。": "Nó thậm chí còn cung cấp giao diện quản trị đầy đủ, có thể xem trạng thái sao lưu R2, phê duyệt yêu cầu ghép nối thiết bị, khởi động lại tiến trình gateway, và tích hợp Cloudflare Access để bảo vệ xác thực danh tính, an toàn tuyệt đối.",
    "最重要的是，它可以直接访问外网，且 24 小时开机。": "Quan trọng nhất là nó có thể truy cập internet trực tiếp và hoạt động 24 giờ.",
    "我顺便把 OpenClaw 的 Channel，接到了 Discord，现在体验下来，Discord 的体验，真的比其他几个好太多，非常丝滑。": "Nhân tiện tôi đã kết nối Channel của OpenClaw vào Discord, trải nghiệm thực tế cho thấy Discord thực sự tốt hơn nhiều so với các nền tảng khác, cực kỳ mượt mà.",

    # Section 1: Why Cloudflare
    "一、为什么选择Cloudflare": "Một, Tại sao chọn Cloudflare",
    "一句话总结，这是一个把 OpenClaw AI 助手，部署到 Cloudflare Workers 的，开箱即用方案，不用买服务器。": "Tóm lại trong một câu, đây là giải pháp dùng ngay không cần cấu hình để triển khai trợ lý AI OpenClaw lên Cloudflare Workers, không cần mua server.",
    "三个关键技术点": "Ba điểm kỹ thuật quan trọng",

    # Subsection: Sandbox
    "一）第一点，Sandbox容器替代传统服务器": "1) Điểm thứ nhất, Container Sandbox thay thế server truyền thống",
    "传统方案要买 VPS，装 Docker，还得维护系统，心累，": "Phương án truyền thống phải mua VPS, cài Docker, còn phải bảo trì hệ thống, thật mệt mỏi,",
    "而 Moltworker 直接用，Cloudflare Workers，类似轻量容器,": "Còn Moltworker sử dụng trực tiếp Cloudflare Workers, tương tự container nhẹ,",
    "好处是自动扩缩容，冷启动后常驻，成本极低，Workers Paid 订阅仅需 $5/月起步。": "Ưu điểm là tự động mở rộng/thu hẹp, thường trú sau cold start, chi phí cực thấp, đăng ký Workers Paid chỉ từ $5/tháng.",

    # Subsection: Triple auth
    "二）第二点，三重认证": "2) Điểm thứ hai, Xác thực ba lớp",
    "流程是这样的： 用户请求 → CF Access 登录 → 验证 Gateway Token → 设备配对批准 → 聊天 。": "Quy trình như sau: Yêu cầu người dùng → Đăng nhập CF Access → Xác thực Gateway Token → Phê duyệt ghép nối thiết bị → Trò chuyện.",
    "这不是简单的一个密码，而是三层把关，防止陌生人白嫖你的 AI。": "Đây không đơn giản chỉ là một mật khẩu, mà là ba lớp kiểm soát, ngăn chặn người lạ dùng chùa AI của bạn.",

    # Subsection: R2 backup
    "三）第三点，R2备份还原方案": "3) Điểm thứ ba, Phương án sao lưu phục hồi R2",
    "容器重启通常会丢失数据，但 Moltworker 会，每5分钟自动备份到R2，也就是对象存储，并在启动时从 R2 恢复，简单但有效，比改代码适配 R2 数据库，更直接。": "Container khởi động lại thường sẽ mất dữ liệu, nhưng Moltworker sẽ tự động sao lưu vào R2 mỗi 5 phút, tức là object storage, và phục hồi từ R2 khi khởi động, đơn giản nhưng hiệu quả, trực tiếp hơn so với việc sửa code để tương thích database R2.",

    # Section 2: How to install
    "二、如何安装": "Hai, Cách cài đặt",
    "一）准备工作": "1) Công việc chuẩn bị",
    "想要丝滑部署，这几样东西缺一不可，请大家逐一核对：": "Muốn triển khai mượt mà, những thứ sau đây không thể thiếu, mời các bạn kiểm tra từng mục:",

    "首先是 ": "Đầu tiên là ",
    "硬性门槛 ": "điều kiện bắt buộc ",
    "：你需要开通 Cloudflare 的 ": ": bạn cần kích hoạt ",
    "Workers Paid 订阅 ": "gói đăng ký Workers Paid ",
    "（$5/月）。没办法，免费版不支持 Sandbox 容器技术，但这 5 刀绝对花得值。": "($5/tháng). Không có cách nào khác, bản miễn phí không hỗ trợ công nghệ container Sandbox, nhưng 5 đô này hoàn toàn xứng đáng.",

    "其次是 ": "Tiếp theo là ",
    "本地环境 ": "môi trường local ",
    "：你的电脑上需要安装 ": ": máy tính của bạn cần cài đặt ",
    "和 ": "và ",
    "。因为 Moltworker 的部署脚本需要在本地打包容器，没有 Docker 是跑不通的。": ". Vì script triển khai của Moltworker cần đóng gói container ở local, không có Docker thì không chạy được.",

    "最后是 ": "Cuối cùng là ",
    "粮草弹药 ": "\"lương thực đạn dược\" ",
    "：注册好 Cloudflare 账号，并准备好你常用的 AI 模型 ": ": đăng ký tài khoản Cloudflare, và chuẩn bị sẵn ",
    "（DeepSeek、OpenRouter 等均可），我们马上就要用到。": "(DeepSeek, OpenRouter đều được), chúng ta sẽ dùng ngay.",

    # Wrangler section
    "二）Wrangler是什么": "2) Wrangler là gì",
    "简单来说，Wrangler 是 Cloudflare Workers 的遥控器。": "Nói đơn giản, Wrangler là điều khiển từ xa của Cloudflare Workers.",
    "Moltworker 涉及大量敏感配置，比如 Anthropic API Key，Discord或Telegram Bot Token，R2存储密钥，Gateway认证 Token，这些东西绝对不能写在代码里，必须通过 Wrangler，以加密形式注入到 Worker 环境，这是 Cloudflare 推荐的安全实践。": "Moltworker liên quan đến nhiều cấu hình nhạy cảm, ví dụ Anthropic API Key, Discord hoặc Telegram Bot Token, khóa lưu trữ R2, Gateway Token xác thực, những thứ này tuyệt đối không được viết trong code, phải thông qua Wrangler, tiêm vào môi trường Worker dưới dạng mã hóa, đây là thực hành bảo mật được Cloudflare khuyến nghị.",
    "安装非常简单，先运行": "Cài đặt rất đơn giản, trước tiên chạy",
    "然后登录账号，运行": "Sau đó đăng nhập tài khoản, chạy",
    "它会打开浏览器，点击允许授权即可": "Nó sẽ mở trình duyệt, bấm cho phép ủy quyền là xong",
    "登录成功后，你就具备了，在终端控制 Cloudflare 的能力，接下来的部署、配密钥、看日志，全部通过它完成。": "Sau khi đăng nhập thành công, bạn đã có khả năng điều khiển Cloudflare từ terminal, việc triển khai, cấu hình khóa bí mật, xem log tiếp theo, tất cả đều thông qua nó.",

    # Clone project
    "三）克隆项目并安装依赖": "3) Clone dự án và cài đặt dependencies",
    "Moltworker 官方提供了，一个 GitHub 代码仓库，我们首先克隆它，并安装依赖。": "Moltworker chính thức cung cấp một kho mã nguồn GitHub, trước tiên chúng ta clone nó và cài đặt dependencies.",

    # AI Gateway
    "四）创建AI Gateway": "4) Tạo AI Gateway",
    "按照官方 Quick Start，接下来要配置 AI 模型。": "Theo Quick Start chính thức, tiếp theo cần cấu hình model AI.",
    "我们可以看到它最快的方式就是使用 ANTHROPIC_API_KEY。": "Chúng ta có thể thấy cách nhanh nhất là sử dụng ANTHROPIC_API_KEY.",
    "如果大家有 Anthropic API Key 的话，直接使用 ": "Nếu các bạn có Anthropic API Key, sử dụng trực tiếp ",
    "是最简单的，可以跳过这个小章节。": " là đơn giản nhất, có thể bỏ qua phần nhỏ này.",
    "我没有 Anthropic API Key，所以我选择使用 Cloudflare 的 AI Gateway。": "Tôi không có Anthropic API Key, nên tôi chọn sử dụng AI Gateway của Cloudflare.",
    "原因很简单，省心且可观测，能看到具体的 Token 消耗日志。": "Lý do rất đơn giản, tiết kiệm công sức và có thể quan sát được, xem được log tiêu thụ Token cụ thể.",

    # Create gateway steps
    "1、第一步创建新网关": "1. Bước đầu tiên tạo gateway mới",
    "在 Cloudflare 后台的计算和AI菜单里，找到 AI Gateway 入口": "Trong menu Compute và AI ở bảng điều khiển Cloudflare, tìm mục AI Gateway",
    "点击创建，随便起个名字": "Bấm tạo, đặt tên tùy ý",
    "Cloudflare 提供了很多提供商，这里我选择大家比较熟悉的 DeepSeek。": "Cloudflare cung cấp nhiều nhà cung cấp, ở đây tôi chọn DeepSeek mà mọi người quen thuộc.",

    "2、第二步添加提供程序密钥": "2. Bước hai thêm khóa nhà cung cấp",
    "点击 Add，填入你的 DeepSeek API Key，注意，Gateway 只是中间商，最终调用的还是 DeepSeek，所以必须填你自己的 Key。": "Bấm Add, điền DeepSeek API Key của bạn, lưu ý, Gateway chỉ là trung gian, cuối cùng vẫn gọi đến DeepSeek, nên phải điền Key của chính bạn.",

    "3、第三步获取 Gateway 专属Token": "3. Bước ba lấy Token chuyên dụng của Gateway",
    "我们看右侧的 Create a token": "Chúng ta xem Create a token ở bên phải",
    "输入名称，创建 API 令牌，生成 Token": "Nhập tên, tạo API token, sinh Token",
    "注意，这个 Token 是 Cloudflare Gateway 的认证，不是 DeepSeek 的，复制生成的 Token，马上要用。": "Lưu ý, Token này là xác thực của Cloudflare Gateway, không phải của DeepSeek, copy Token đã sinh, sắp dùng ngay.",

    "4、第四步部署时填入 Secret": "4. Bước bốn điền Secret khi triển khai",
    "回到终端，执行命令，填入 Gateway 的Token": "Quay lại terminal, thực thi lệnh, điền Token của Gateway",
    "用于 Worker 连接 Cloudflare AI Gateway，此时系统会自动在 Cloudflare上创建一个名为 moltbot-sandbox的Worker": "Dùng để Worker kết nối Cloudflare AI Gateway, lúc này hệ thống sẽ tự động tạo một Worker có tên moltbot-sandbox trên Cloudflare",
    "我们可以看到在平台上创建了一个新的 Worker": "Chúng ta có thể thấy một Worker mới đã được tạo trên nền tảng",

    "接下来设置 Gateway 的 Base URL，这取决于你选择的模型，具体格式规则如下": "Tiếp theo cài đặt Base URL của Gateway, điều này phụ thuộc vào model bạn chọn, quy tắc định dạng cụ thể như sau",
    "Gateway 是\"二传手\"：它用你的 DeepSeek Key 去调模型，但给你加了缓存、限流、统计。": "Gateway là \"người chuyền bóng\": nó dùng DeepSeek Key của bạn để gọi model, nhưng thêm cho bạn cache, giới hạn tốc độ, thống kê.",

    # Access token section
    "五）设置访问令牌": "5) Cài đặt token truy cập",
    "注意，这是最重要的安全凭证，泄露等于，别人能控制你的AI助手。": "Lưu ý, đây là thông tin xác thực bảo mật quan trọng nhất, rò rỉ đồng nghĩa với người khác có thể điều khiển trợ lý AI của bạn.",
    "1、生成并设置 Token": "1. Sinh và cài đặt Token",
    "别用简单密码，直接生成一个高强度随机字符串，显示出来给你看，赶紧复制保存好，然后设置到 Cloudflare": "Đừng dùng mật khẩu đơn giản, trực tiếp sinh một chuỗi ký tự ngẫu nhiên cường độ cao, hiển thị cho bạn xem, nhanh chóng copy lưu lại, sau đó cài đặt vào Cloudflare",
    "2、和 AI Gateway Token 区分开": "2. Phân biệt với AI Gateway Token",

    # Token table
    "Token": "Token",
    "用途": "Mục đích",
    "MOLTBOT_GATEWAY_TOKEN": "MOLTBOT_GATEWAY_TOKEN",
    "登录你的 AI 助手控制界面": "Đăng nhập giao diện điều khiển trợ lý AI của bạn",
    "AI_GATEWAY_API_KEY": "AI_GATEWAY_API_KEY",
    "连接 Cloudflare AI Gateway": "Kết nối Cloudflare AI Gateway",

    "3、使用方式": "3. Cách sử dụng",
    "部署成功后，访问你的 URL，必须带上 token 参数。": "Sau khi triển khai thành công, truy cập URL của bạn, phải kèm theo tham số token.",

    # Cloudflare Access section
    "六）设置 Cloudflare Access 密钥": "6) Cài đặt khóa Cloudflare Access",
    "1、在后台开启 Access 开关": "1. Bật Access trong bảng điều khiển",
    "回到 ": "Quay lại ",
    "，进入 ": ", vào ",
    "。": ".",
    "点进刚才创建的 worker（比如 moltbot-sandbox ）": "Bấm vào worker vừa tạo (ví dụ moltbot-sandbox)",
    "点击顶部的 ": "Bấm vào ",
    "设置 (Settings) ": "Cài đặt (Settings) ",
    "-> ": "-> ",
    "域和路由 (Domains & Routes)": "Tên miền và Tuyến đường (Domains & Routes)",
    "找到 workers.dev 这一行，点击右侧的 ": "Tìm dòng workers.dev, bấm vào ",
    "三个点图标 (...)， ": "biểu tượng ba chấm (...), ",
    "三个点 (...) ": "ba chấm (...) ",
    "点击 ": " bấm ",
    "（启用 Access）": "(kích hoạt Access)",

    "2、获取并设置 Access 密钥": "2. Lấy và cài đặt khóa Access",
    '保护开启了，现在要告诉 Worker 怎么去验证\u201c通行证\u201d。': 'Bảo vệ đã được bật, bây giờ cần cho Worker biết cách xác thực "thẻ thông hành".',
    "我们需要两个值：一个是 Team Domain，另一个是 Access 应用的 AUD 标签。": "Chúng ta cần hai giá trị: một là Team Domain, hai là nhãn AUD của ứng dụng Access.",
    "当你启用 Cloudflare Access 后，访问 /_admin/ 后台时。": "Khi bạn kích hoạt Cloudflare Access, truy cập trang quản trị /_admin/.",
    "浏览器跳转到 Access 登录页，你输入邮箱登录，登录成功，Access 发给你一个通行证，也就是 JWT Token。": "Trình duyệt chuyển hướng đến trang đăng nhập Access, bạn nhập email đăng nhập, đăng nhập thành công, Access cấp cho bạn một thẻ thông hành, tức là JWT Token.",
    "问题来了，Worker 怎么知道，这个通行证是真的，还是黑客伪造的，这就需要 TEAM_DOMAIN 和 AUD 来验证。": "Vấn đề là, Worker làm sao biết thẻ thông hành này là thật hay hacker giả mạo, đây là lúc cần TEAM_DOMAIN và AUD để xác thực.",

    "3、两个变量的作用": "3. Tác dụng của hai biến",
    "变量": "Biến",
    "是什么": "Là gì",
    "作用": "Tác dụng",
    "CF_ACCESS_TEAM_DOMAIN": "CF_ACCESS_TEAM_DOMAIN",
    "你的 Cloudflare 团队域名": "Tên miền nhóm Cloudflare của bạn",
    "告诉 Worker \"去哪个认证中心校验\"": "Cho Worker biết \"đến trung tâm xác thực nào để kiểm tra\"",
    "CF_ACCESS_AUD": "CF_ACCESS_AUD",
    "Access 应用的 AUD 标签": "Nhãn AUD của ứng dụng Access",
    "告诉 Worker \"这个通行证是不是发给我的\"": "Cho Worker biết \"thẻ thông hành này có phải cấp cho tôi không\"",
    "通俗类比，TEAM_DOMAIN相当于公安局总部地址，去哪验证身份证，AUD 相当于你的身份证号,验证这张证，是不是发给你的，两个凑齐，Worker才能确认，登录成功的那个人确实是你。": "Ví dụ dễ hiểu, TEAM_DOMAIN tương đương địa chỉ trụ sở công an, đến đâu để xác minh CMND, AUD tương đương số CMND của bạn, xác minh tấm thẻ này có phải cấp cho bạn không, hai cái đủ cả, Worker mới xác nhận được người đăng nhập thành công chính là bạn.",

    "4、去哪找这两个值": "4. Tìm hai giá trị này ở đâu",
    "CF_ACCESS_TEAM_DOMAIN ": "CF_ACCESS_TEAM_DOMAIN ",
    "：Zero Trust Dashboard -> ": ": Zero Trust Dashboard -> ",
    "Team domain ": "Team domain ",
    "CF_ACCESS_AUD ": "CF_ACCESS_AUD ",
    "：Zero Trust Dashboard -> Access -> Applications": ": Zero Trust Dashboard -> Access -> Applications",
    "点进你的应用，复制那串 UUID。": "Bấm vào ứng dụng của bạn, copy chuỗi UUID đó.",

    # R2 persistent storage
    "七）配置 R2 持久存储": "7) Cấu hình lưu trữ bền vững R2",
    "默认情况下，Cloudflare Workers 是无状态的。这意味着容器重启后，你的 ": "Mặc định, Cloudflare Workers là không trạng thái (stateless). Điều này có nghĩa là sau khi container khởi động lại, ",
    "对话历史 ": "lịch sử trò chuyện ",
    "设备配对信息 ": "thông tin ghép nối thiết bị ",
    "都会丢失。": " của bạn đều sẽ bị mất.",
    '想要让你的 AI 助手拥有\u201c长期记忆\u201d，必须配置 R2 存储。': 'Muốn trợ lý AI của bạn có "bộ nhớ dài hạn", phải cấu hình lưu trữ R2.',
    "在部署过程中，系统通常会自动创建一个名为 moltbot-data 的存储桶（Bucket），我们需要给 Worker 授权去读写它。": "Trong quá trình triển khai, hệ thống thường tự động tạo một bucket lưu trữ tên moltbot-data, chúng ta cần cấp quyền cho Worker đọc ghi nó.",

    "1、创建 R2 API Token": "1. Tạo R2 API Token",
    "回到 Cloudflare Dashboard，点击左侧菜单的 ": "Quay lại Cloudflare Dashboard, bấm vào menu bên trái ",
    "。在右侧找到并点击 ": ". Ở bên phải tìm và bấm ",
    "点击创建 User API 令牌。": "Bấm tạo User API token.",
    "权限（关键） ": "Quyền hạn (quan trọng) ",
    "：选择 ": ": chọn ",
    "（读写权限）。": "(quyền đọc ghi).",
    "范围（关键） ": "Phạm vi (quan trọng) ",
    "：为了安全，建议指定 Bucket。选择 ": ": để an toàn, khuyến nghị chỉ định Bucket. Chọn ",
    "，然后选中 moltbot-data 。": ", sau đó chọn moltbot-data.",
    "然后我们拿到这里两个信息，这两个值只显示一次，请务必复制保存好！": "Sau đó chúng ta lấy được hai thông tin ở đây, hai giá trị này chỉ hiển thị một lần, nhất định phải copy lưu lại!",

    "2、配置存储密钥": "2. Cấu hình khóa lưu trữ",
    "回到终端，我们需要设置 3 个密钥：": "Quay lại terminal, chúng ta cần cài đặt 3 khóa bí mật:",
    "设置 Access Key ID：": "Cài đặt Access Key ID:",
    "设置 Secret Access Key：": "Cài đặt Secret Access Key:",
    "设置 Cloudflare Account ID：": "Cài đặt Cloudflare Account ID:",
    "这个 ID 哪里找？ 回到 Cloudflare 首页，点击右侧的 ": "ID này tìm ở đâu? Quay lại trang chủ Cloudflare, bấm vào ",
    "下面的 ": " phía dưới ",
    "，选择 ": ", chọn ",
    "复制账户ID ": "Copy Account ID ",
    "然后执行命令：": "Sau đó thực thi lệnh:",
    '这样，你的 AI 助手就拥有了永久记忆，再也不怕重启\u201c失忆\u201d了！': 'Như vậy, trợ lý AI của bạn đã có bộ nhớ vĩnh viễn, không còn sợ khởi động lại "mất trí nhớ" nữa!',
    "配置完成，开始部署，运行": "Cấu hình hoàn tất, bắt đầu triển khai, chạy",
    "部署成功后，你会看到终端输出了，OpenClaw 的访问地址。": "Sau khi triển khai thành công, bạn sẽ thấy terminal xuất ra địa chỉ truy cập OpenClaw.",

    # Access and login
    "八）访问与登录": "8) Truy cập và đăng nhập",
    "拼接你的访问地址和 Token，格式如下。": "Ghép địa chỉ truy cập và Token của bạn, định dạng như sau.",
    "访问时会提醒你输入邮箱，这个email 必须是你允许列表里的。": "Khi truy cập sẽ yêu cầu bạn nhập email, email này phải nằm trong danh sách cho phép của bạn.",
    "输入验证码后，会跳转到登录页面。": "Sau khi nhập mã xác thực, sẽ chuyển hướng đến trang đăng nhập.",
    "注意，因为是首次访问，通常需要1到2分钟，容器冷启动时间，请耐心等待。": "Lưu ý, vì là lần truy cập đầu tiên, thường cần 1 đến 2 phút cho thời gian cold start của container, xin hãy kiên nhẫn chờ.",
    "进入后就能看到，熟悉的 OpenClaw 界面了，但别急，先根据提示进入 Moltbot Admin 界面": "Sau khi vào bạn sẽ thấy giao diện OpenClaw quen thuộc, nhưng đừng vội, trước tiên theo hướng dẫn vào giao diện Moltbot Admin",
    "审批设备，在 Admin 界面，批准设备通过": "Phê duyệt thiết bị, trong giao diện Admin, phê duyệt thiết bị",
    "接下来就可以愉快地玩耍了。": "Tiếp theo bạn có thể thoải mái sử dụng rồi.",

    # Section 3: Model configuration
    "三、如何配置模型": "Ba, Cách cấu hình model",
    "因为接触不到命令行，我们没法通过 CLI 去修改配置，不过没关系，直接在平台网页里改，也是一样的。": "Vì không truy cập được command line, chúng ta không thể sửa cấu hình qua CLI, nhưng không sao, sửa trực tiếp trên trang web nền tảng cũng vậy.",
    "点击左侧的 Config， ": "Bấm vào Config ở bên trái, ",
    "切换到 Raw 模式 ": "chuyển sang chế độ Raw ",
    "，就可以直接修改配置文件了， ": ", là có thể sửa trực tiếp file cấu hình, ",
    "默认的配置通常是错的 ": "cấu hình mặc định thường sai ",
    "，我们需要手动修正成，DeepSeek 的配置。": ", chúng ta cần sửa thủ công thành cấu hình của DeepSeek.",

    # DeepSeek subsection
    "一）DeepSeek": "1) DeepSeek",
    "记得替换成你的信息，baseUrl 填你的网关地址，apiKey 填 Cloudflare AI Gateway的Token，注意这里填的是Gateway Token，不是DeepSeek的Key。": "Nhớ thay thế bằng thông tin của bạn, baseUrl điền địa chỉ gateway của bạn, apiKey điền Token của Cloudflare AI Gateway, lưu ý ở đây điền Gateway Token, không phải Key của DeepSeek.",
    "另外别忘了设置 Primary Model，也就是主模型。": "Ngoài ra đừng quên cài đặt Primary Model, tức là model chính.",
    "改完后点击 Apply，立马生效。": "Sau khi sửa xong bấm Apply, có hiệu lực ngay lập tức.",
    "因为我们走的是 AI Gateway，回到 Cloudflare 后台，能看到每一次对话的，Token 消耗记录，强迫症表示极其舒适。": "Vì chúng ta đi qua AI Gateway, quay lại bảng điều khiển Cloudflare, có thể thấy bản ghi tiêu thụ Token của mỗi cuộc trò chuyện, người có OCD sẽ thấy cực kỳ thỏa mãn.",

    # OpenRouter subsection
    "二、OpenRouter": "2) OpenRouter",
    "如果你连 DeepSeek 的钱，都不想花，或者想同时白嫖 Gemini、Kimi 等多个免费模型，这里有个白嫖方案，那就是OpenRouter。": "Nếu bạn không muốn tốn tiền cho cả DeepSeek, hoặc muốn dùng miễn phí nhiều model như Gemini, Kimi, ở đây có phương án miễn phí, đó là OpenRouter.",
    "OpenRouter 最近推出了，一个聚合网关，可以自动路由到，各种免费模型，也就是 Free Tier。": "OpenRouter gần đây đã ra mắt một gateway tổng hợp, có thể tự động định tuyến đến các model miễn phí khác nhau, tức là Free Tier.",

    "1、第 1 步：配置网关": "1. Bước 1: Cấu hình gateway",
    "回到 Cloudflare AI Gateway 界面，找到 ": "Quay lại giao diện Cloudflare AI Gateway, tìm ",
    "找到 ": "Tìm ",
    "，点击 ": ", bấm ",
    "，填入你的 OpenRouter API Key ( sk-or-xxxx )。": ", điền OpenRouter API Key của bạn (sk-or-xxxx).",
    "这样 Cloudflare 才有权限代表你去调用 OpenRouter": "Như vậy Cloudflare mới có quyền thay mặt bạn gọi đến OpenRouter",

    "2、 第 2 步：修改配置": "2. Bước 2: Sửa cấu hình",
    "回到 OpenClaw 的 ": "Quay lại ",
    "界面，在 providers 字段里，追加 OpenRouter 的配置。": " của OpenClaw, trong trường providers, thêm cấu hình OpenRouter.",
    "注意： ": "Lưu ý: ",
    "这里的 apiKey 依然填你的 ": "apiKey ở đây vẫn điền ",
    "（就是配置 DeepSeek 时用的那个），而不是 OpenRouter 的 Key。": "(chính là cái đã dùng khi cấu hình DeepSeek), chứ không phải Key của OpenRouter.",
    "这样你的AI助手，就会自动在各种免费模型之间，反复横跳，彻底0成本运行。": "Như vậy trợ lý AI của bạn sẽ tự động nhảy qua lại giữa các model miễn phí, hoàn toàn chạy với chi phí 0 đồng.",

    # Section 4: Chat Channel
    "四、如何配置 Chat Channel": "Bốn, Cách cấu hình Chat Channel",
    "官方文档说要用，wrangler cli 来配置 Channel。": "Tài liệu chính thức nói phải dùng wrangler CLI để cấu hình Channel.",
    "但我发现了一个更懒的方法，直接在 Chat 对话框里，让机器人自己去配。": "Nhưng tôi phát hiện ra một cách lười hơn, trực tiếp trong hộp thoại Chat, để robot tự cấu hình.",
    "比如配置 Discord，你只需要拿到 Token，然后直接对它说，请帮我配置 Discord渠道，Token 是多少": "Ví dụ cấu hình Discord, bạn chỉ cần lấy Token, rồi nói trực tiếp với nó, hãy giúp tôi cấu hình kênh Discord, Token là bao nhiêu",
    "等一会它就自动配置好了。": "Chờ một lát nó sẽ tự cấu hình xong.",
    "甚至连 Clawdbot Pairing 操作，也可以直接在这里完成，不需要去后台点": "Thậm chí cả thao tác Clawdbot Pairing cũng có thể hoàn thành trực tiếp ở đây, không cần vào bảng điều khiển bấm",
    "最后直接在 Discord 里，享受你的AI助手吧。": "Cuối cùng hãy tận hưởng trợ lý AI của bạn trực tiếp trên Discord.",

    # Closing
    "感谢看到这里 👏": "Cảm ơn bạn đã đọc đến đây 👏",
    "觉得有用的话，点赞 👍 / 在看 👀 / 转发 🫱 / 评论 📣": "Nếu thấy hữu ích, hãy thả like 👍 / đang xem 👀 / chia sẻ 🫱 / bình luận 📣",
    "星标 ⭐ 一下，下次更新不迷路": "Đánh dấu sao ⭐, lần cập nhật sau không bị lạc",

    # Misc single characters/short phrases that appear as separate text_runs
    "： ": ": ",
    "：": ":",
}

def translate_content(text):
    """Translate a text_run content from Chinese to Vietnamese"""
    # Don't translate URLs
    if is_url(text):
        return text, False

    # Don't translate if only emoji/punctuation
    if is_only_emoji_or_punctuation(text):
        return text, False

    # Don't translate if no Chinese
    if not has_chinese(text):
        return text, False

    # Exact match in dictionary
    if text in TRANSLATIONS:
        return TRANSLATIONS[text], True

    # If not found in dictionary, return original (should not happen if dict is complete)
    print(f"  WARNING: No translation for: [{text}]")
    return text, False

def main():
    with open('_art_b5_6_orig.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    translated = copy.deepcopy(data)

    total_text_runs = 0
    translated_count = 0
    kept_count = 0

    for block in translated['blocks']:
        for el in block['elements']:
            if el['type'] == 'text_run':
                total_text_runs += 1
                original = el['content']
                new_text, was_translated = translate_content(original)
                if was_translated:
                    el['content'] = new_text
                    translated_count += 1
                else:
                    kept_count += 1

    # Save translated file
    with open('_art_b5_6_trans.json', 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)

    print(f"\n=== Translation Summary ===")
    print(f"Total blocks: {len(translated['blocks'])}")
    print(f"Total text_runs: {total_text_runs}")
    print(f"Translated: {translated_count}")
    print(f"Kept as-is: {kept_count}")
    print(f"Saved to _art_b5_6_trans.json")

if __name__ == '__main__':
    main()
