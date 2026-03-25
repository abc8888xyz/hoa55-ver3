# -*- coding: utf-8 -*-
"""Build art22 translation using direct full-text mapping for every element"""
import json, re, sys, copy
sys.stdout.reconfigure(encoding='utf-8')

CN_PAT = re.compile(r'[\u4e00-\u9fff]')

with open('_art22_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build COMPLETE translation map: original text -> translated text
# Every single Chinese-containing text element gets an exact entry
FULL_MAP = {
    # === BLOCK 0: Page title ===
    "02-25直播回放 | 今晚是自习室 WaytoAGI晚8点共学 2026年2月25日":
        "02-25 Phát lại livestream | Tối nay là phòng tự học WaytoAGI học chung lúc 8 giờ tối ngày 25 tháng 2 năm 2026",

    # === BLOCK 1-2: Meeting info ===
    "会议主题：02-25 | 今晚是自习室 WaytoAGI晚8点共学":
        "Chủ đề cuộc họp: 02-25 | Tối nay là phòng tự học WaytoAGI học chung lúc 8 giờ tối",
    "会议时间：2026年2月25日（周三） 19:59 - 21:53 （GMT+08）":
        "Thời gian họp: Ngày 25 tháng 2 năm 2026 (Thứ Tư) 19:59 - 21:53 (GMT+08)",

    # === BLOCK 3: AI disclaimer ===
    "智能会议纪要由 AI 生成，可能不准确，请谨慎甄别后使用":
        "Biên bản họp thông minh được AI tạo ra, có thể không chính xác, vui lòng cân nhắc trước khi sử dụng",

    # === BLOCK 4-5: Summary header ===
    "总结": "Tóm tắt",
    "本次会议由 AJ 主持，参会人员围绕小龙虾（Openclaw）的部署、使用、应用案例以及即将开展的训练营等内容进行了深入交流和讨论，分享了各自的经验和见解，内容如下：":
        "Cuộc họp lần này do AJ chủ trì, các thành viên tham gia đã trao đổi và thảo luận chuyên sâu về việc triển khai, sử dụng, các trường hợp ứng dụng của Tôm hùm (Openclaw) cũng như khóa đào tạo sắp tới, chia sẻ kinh nghiệm và quan điểm của mỗi người, nội dung như sau:",

    # === BLOCKS 6-29: Summary bullet points ===
    "小龙虾部署与配置": "Triển khai và cấu hình Tôm hùm",
    "安装流程": "Quy trình cài đặt",
    "CC 优先：AJ 提出安装小龙虾的建议流程是先安装 CC（cloud code），再由 CC 安装 Openclaw。因为 Openclaw 不稳定且版本变更频繁，而 CC 相对稳定。":
        "Ưu tiên CC: AJ đề xuất quy trình cài đặt Tôm hùm nên cài CC (cloud code) trước, sau đó CC sẽ cài Openclaw. Vì Openclaw không ổn định và phiên bản thay đổi thường xuyên, trong khi CC tương đối ổn định.",
    "云端部署：可选择火山引擎、阿里云、腾讯云等云服务器进行部署。以火山引擎为例，进入首页的 Openclaw 云上部署页面，购买实例，建议选择海外（如雅加达）的实例，部分实例有促销优惠。":
        "Triển khai đám mây: Có thể chọn các máy chủ đám mây như Volcano Engine, Alibaba Cloud, Tencent Cloud để triển khai. Lấy Volcano Engine làm ví dụ, vào trang triển khai đám mây Openclaw trên trang chủ, mua instance, nên chọn instance ở nước ngoài (như Jakarta), một số instance có ưu đãi khuyến mãi.",
    "本地部署：对于小白来说，在自己电脑端部署是最快、最方便的方式，可使用 IDE 工具；有一定技术背景的人可按官方教程部署。":
        "Triển khai cục bộ: Đối với người mới, triển khai trên máy tính cá nhân là cách nhanh nhất và tiện lợi nhất, có thể sử dụng công cụ IDE; người có nền tảng kỹ thuật có thể triển khai theo hướng dẫn chính thức.",
    "配置要点": "Điểm cấu hình quan trọng",
    "Claude code 安装：安装 Claude code 需先有 nodejs 的 22 版本，通过 AI 协助安装，输入相关命令即可开始安装，安装完成后输入 claude 即可开启。":
        "Cài đặt Claude code: Cài đặt Claude code cần có trước nodejs phiên bản 22, thông qua AI hỗ trợ cài đặt, nhập lệnh liên quan là có thể bắt đầu cài đặt, sau khi cài xong nhập claude là có thể khởi động.",
    "API key 配置：不同模型的 API key 配置方式不同，需注意接口协议（如 Anthropic 或 open AI）和 base URL。配置时可参考官方文档，将 key 和模型信息填入相应位置。":
        "Cấu hình API key: Cách cấu hình API key của các mô hình khác nhau thì khác nhau, cần chú ý giao thức giao diện (như Anthropic hoặc OpenAI) và base URL. Khi cấu hình có thể tham khảo tài liệu chính thức, điền key và thông tin mô hình vào vị trí tương ứng.",
    "环境变量配置：ENV 文件用于保存 API key 等信息，模型本身无法获取 key 的明文。可使用 CC switch 工具在电脑端切换不同模型。":
        "Cấu hình biến môi trường: File ENV dùng để lưu thông tin API key, bản thân mô hình không thể lấy được bản rõ của key. Có thể sử dụng công cụ CC switch để chuyển đổi giữa các mô hình khác nhau trên máy tính.",
    "小龙虾应用案例分享": "Chia sẻ các trường hợp ứng dụng Tôm hùm",
    "枫子的案例": "Trường hợp của Phong Tử",
    "自我进化：枫子作为产品技术小白，使用 Claude code 部署小龙虾后，让其自我学习和安装，包括 scale、安全配置、记忆系统等，小龙虾能自动总结全网知识并完成任务。":
        "Tự tiến hóa: Phong Tử là người mới về công nghệ sản phẩm, sau khi sử dụng Claude code triển khai Tôm hùm, cho phép nó tự học và cài đặt, bao gồm scale, cấu hình bảo mật, hệ thống bộ nhớ, v.v., Tôm hùm có thể tự động tổng hợp kiến thức toàn mạng và hoàn thành nhiệm vụ.",
    "功能应用：小龙虾可实现自动推送新闻、规划使用方式、更新记忆系统等功能，还能根据用户需求部署和执行任务。":
        "Ứng dụng chức năng: Tôm hùm có thể thực hiện tự động đẩy tin tức, lập kế hoạch sử dụng, cập nhật hệ thống bộ nhớ và các chức năng khác, còn có thể triển khai và thực thi nhiệm vụ theo nhu cầu người dùng.",
    "遇到的问题：在拉小龙虾进群时遇到困难，原因是飞书机器人部署需企业认证，通过创建自建应用并选中对外共享选项可解决。":
        "Vấn đề gặp phải: Gặp khó khăn khi kéo Tôm hùm vào nhóm, nguyên nhân là triển khai robot Feishu cần xác thực doanh nghiệp, có thể giải quyết bằng cách tạo ứng dụng tự xây dựng và chọn tùy chọn chia sẻ bên ngoài.",
    "W 的案例": "Trường hợp của W",
    "跨境电商应用：W 所在团队主要做韩国跨境电商服装业务，使用 Web coding 能力搭建了分布式抓取数据系统，包括数据面板、抓数据和抓销量工具等，还基于此做了数据分析工具。":
        "Ứng dụng thương mại điện tử xuyên biên giới: Nhóm của W chủ yếu kinh doanh quần áo thương mại điện tử xuyên biên giới Hàn Quốc, sử dụng khả năng Web coding xây dựng hệ thống thu thập dữ liệu phân tán, bao gồm bảng điều khiển dữ liệu, công cụ thu thập dữ liệu và doanh số, còn dựa trên đó phát triển công cụ phân tích dữ liệu.",
    "团队协作：使用小龙虾的代理机制创建了 agent 团队，设定不同角色和任务，通过管家进行任务分配和管理。":
        "Hợp tác nhóm: Sử dụng cơ chế đại lý của Tôm hùm tạo ra nhóm agent, thiết lập các vai trò và nhiệm vụ khác nhau, thông qua quản gia để phân công và quản lý nhiệm vụ.",
    "技能与应用技巧": "Kỹ năng và thủ thuật ứng dụng",
    "生图技能": "Kỹ năng tạo ảnh",
    "prompt 分享：AJ 分享了生图的 skills prompt，强调使用 nanobanana Pro 4K 来生图可保证信息密度大且图像清晰，有人使用后涨粉率较高。":
        "Chia sẻ prompt: AJ chia sẻ skills prompt tạo ảnh, nhấn mạnh sử dụng nanobanana Pro 4K để tạo ảnh có thể đảm bảo mật độ thông tin lớn và hình ảnh rõ nét, có người sử dụng sau đó tỷ lệ tăng follower khá cao.",
    "技能制作：可将 prompt 写成 skill，把 API 要求等信息写入其中，小龙虾可根据 skill 生成图片。":
        "Tạo kỹ năng: Có thể viết prompt thành skill, đưa các yêu cầu API và thông tin khác vào trong đó, Tôm hùm có thể tạo ảnh dựa trên skill.",
    "飞书文档配置": "Cấu hình tài liệu Feishu",
    "问题解决：孔立刚指出飞书文档配置需分两步，先写标题，再写正文，还提供了相关文档链接，帮助解决小龙虾写飞书文档空白的问题。":
        "Giải quyết vấn đề: Khổng Lập Cương chỉ ra cấu hình tài liệu Feishu cần chia hai bước, viết tiêu đề trước, sau đó viết nội dung, còn cung cấp liên kết tài liệu liên quan, giúp giải quyết vấn đề Tôm hùm viết tài liệu Feishu bị trống.",
    "文档读取：小龙虾自带的飞书 read doc 技能可读取分享出来的文档内容并转为 Markdown，但图片不行。":
        "Đọc tài liệu: Kỹ năng read doc Feishu tích hợp sẵn của Tôm hùm có thể đọc nội dung tài liệu được chia sẻ và chuyển thành Markdown, nhưng ảnh thì không được.",
    "训练营预告": "Thông báo trước về khóa đào tạo",
    "训练营内容": "Nội dung khóa đào tạo",
    "：即将开展 Openclaw 训练营，由崟海和 CY 担任主讲，教大家小龙虾的从头部署到安装，以及在多维表格等各种端操作使用，CY 还会教如何将其部署在硬件上面。":
        ": Sắp triển khai khóa đào tạo Openclaw, do Ngân Hải và CY làm giảng viên chính, dạy mọi người từ triển khai đến cài đặt Tôm hùm, cũng như thao tác sử dụng trên các nền tảng như bảng đa chiều, CY còn sẽ dạy cách triển khai trên phần cứng.",
    "时间安排": "Sắp xếp thời gian",
    "：具体开营日期待定，待小鱿鱼通知。": ": Ngày khai giảng cụ thể chưa xác định, chờ thông báo từ Tiểu Mực.",
    "后续工作计划": "Kế hoạch công việc tiếp theo",
    "分享与交流": "Chia sẻ và giao lưu",
    "：欢迎大家随时联系 AJ 进行分享，可加其飞书并担任嘉宾。": ": Chào mừng mọi người liên hệ AJ bất cứ lúc nào để chia sẻ, có thể thêm Feishu của AJ và làm khách mời.",
    "训练营准备": "Chuẩn bị khóa đào tạo",
    "：等待小鱿鱼通知 Openclaw 训练营的具体开营日期，做好参加准备。": ": Chờ đợi thông báo từ Tiểu Mực về ngày khai giảng cụ thể của khóa đào tạo Openclaw, chuẩn bị sẵn sàng tham gia.",
    "技能应用": "Ứng dụng kỹ năng",
    "：大家可尝试将 AJ 分享的生图 skills prompt 制作成技能，应用到实际工作中。": ": Mọi người có thể thử chuyển skills prompt tạo ảnh mà AJ chia sẻ thành kỹ năng, ứng dụng vào công việc thực tế.",
    "问题解决": "Giải quyết vấn đề",
    "：针对使用小龙虾过程中遇到的问题，如飞书文档配置、上下文污染等，可参考会议中分享的解决方法进行尝试。":
        ": Đối với các vấn đề gặp phải trong quá trình sử dụng Tôm hùm, như cấu hình tài liệu Feishu, ô nhiễm ngữ cảnh, v.v., có thể tham khảo các phương pháp giải quyết được chia sẻ trong cuộc họp để thử.",
    "待办": "Công việc cần làm",
    "模型配置研究：研究不同角色使用不同模型的配置，参考 yyds 老师的说法进行操作":
        "Nghiên cứu cấu hình mô hình: Nghiên cứu cấu hình sử dụng mô hình khác nhau cho các vai trò khác nhau, tham khảo lời thầy yyds để thực hiện",
    "会议回放发送：将本次会议的回放发送到小龙虾群里":
        "Gửi bản phát lại cuộc họp: Gửi bản phát lại cuộc họp lần này vào nhóm Tôm hùm",

    # === BLOCKS 41-85: Smart chapters ===
    "智能章节": "Chương thông minh",
    "  自习室交流龙虾部署、模型及训练营情况": "  Phòng tự học trao đổi về triển khai Tôm hùm, mô hình và tình hình khóa đào tạo",
    "本章节AJ称今晚未开视频号直播，改为自习室，大家可交流问题，询问部署相关知识。介绍小龙虾安装流程，先装CC再由其安装Openclaw。提及近期变革大，有人做龙虾套壳且硅谷多家获融资。还回应了装CC接模型养龙虾、飞书机器人部署等问题，透露将举办AI训练营，由崟海带队。":
        "Trong chương này AJ cho biết tối nay không livestream trên kênh video, chuyển sang phòng tự học, mọi người có thể trao đổi vấn đề, hỏi kiến thức liên quan đến triển khai. Giới thiệu quy trình cài đặt Tôm hùm, cài CC trước rồi CC cài Openclaw. Đề cập gần đây thay đổi lớn, có người làm vỏ bọc Tôm hùm và nhiều công ty Silicon Valley nhận được vốn đầu tư. Còn trả lời các vấn đề về cài CC kết nối mô hình nuôi Tôm hùm, triển khai robot Feishu, tiết lộ sẽ tổ chức khóa đào tạo AI, do Ngân Hải dẫn đầu.",
    "  飞书应用权限设置与多维表格数据自动写入计划": "  Thiết lập quyền ứng dụng Feishu và kế hoạch tự động ghi dữ liệu vào bảng đa chiều",
    "本章节主要是 AJ 分享工作进展。他创建了飞书应用，开启外部文档多维表格的读写权限，将 Openclaw 应用添加到指定多维表格中。还提到添加文档应用，可尝试让多维表格包含相关内容，数据能自动写入输出。此外，他搞了个人小秘书，打算参照其操作自己做的内容。":
        "Chương này chủ yếu là AJ chia sẻ tiến độ công việc. Anh ấy đã tạo ứng dụng Feishu, mở quyền đọc ghi bảng đa chiều tài liệu bên ngoài, thêm ứng dụng Openclaw vào bảng đa chiều chỉ định. Còn đề cập thêm ứng dụng tài liệu, có thể thử cho bảng đa chiều chứa nội dung liên quan, dữ liệu có thể tự động ghi và xuất. Ngoài ra, anh ấy đã làm trợ lý cá nhân nhỏ, định tham khảo thao tác đó để tự làm nội dung.",
    "  多维表格推送、绘图技巧及Openclaw分享": "  Đẩy bảng đa chiều, kỹ thuật vẽ và chia sẻ Openclaw",
    "本章节中 AJ 分享做图相关内容，建议先进行 skills 安装，结合多维表格推送并可直接发小红书。提到宝玉老师分享文章后自己用其做图，还介绍操作流程，可通过飞书剪存或复制内容，用分享的 skills prompt 制作大图，提及 open cloud agent 开发者指南，强调用大图加 Nano Banana 的 4K 生成，询问是否学不过来。":
        "Trong chương này AJ chia sẻ nội dung liên quan đến làm ảnh, đề xuất cài đặt skills trước, kết hợp đẩy bảng đa chiều và có thể đăng trực tiếp lên Xiaohongshu. Đề cập đến việc sau khi thầy Bảo Ngọc chia sẻ bài viết thì tự dùng để làm ảnh, còn giới thiệu quy trình thao tác, có thể cắt lưu hoặc sao chép nội dung qua Feishu, dùng skills prompt được chia sẻ để tạo ảnh lớn, đề cập đến hướng dẫn nhà phát triển open cloud agent, nhấn mạnh dùng ảnh lớn cộng Nano Banana 4K để tạo, hỏi có học không kịp không.",
    "  Claude风格测试效果及信息密度反馈": "  Hiệu quả thử nghiệm phong cách Claude và phản hồi về mật độ thông tin",
    "本章节中，AJ表示自己这两天疯狂做各种测试，包括复古彩票小票风格、手帐风格、Claude风格等，将直播共学的文字版内容丢给Claude能出不错效果，如胶囊概念图就画得很好。不过有人认为生成内容信息密度太大，字看不过来，AJ觉得这因人而异，若想字少些告知Claude即可。":
        "Trong chương này, AJ cho biết hai ngày qua đã điên cuồng thử nghiệm các loại, bao gồm phong cách vé số cổ điển, phong cách sổ tay, phong cách Claude, v.v., đưa nội dung bản văn bản của livestream học chung cho Claude có thể ra hiệu quả không tệ, như sơ đồ khái niệm viên nang thì vẽ rất đẹp. Tuy nhiên có người cho rằng nội dung tạo ra mật độ thông tin quá lớn, chữ đọc không kịp, AJ cảm thấy điều này tùy người, nếu muốn ít chữ hơn thì báo Claude là được.",
    "  风格尝试、软件安装及平台关注建议交流": "  Thử nghiệm phong cách, cài đặt phần mềm và trao đổi gợi ý theo dõi nền tảng",
    "本章节中，AJ表示可按个人喜好来选择，今日尝试了多种风格，如票据、文件夹风格，还提及相关图片很大，4K图达20多兆。他指出UMAN里没有关注机制，建议给Openclaw安装UMAN，可安装其skills，但自己昨晚没装好，还看了AJ小虾的安装情况，显示还可以安装。":
        "Trong chương này, AJ cho biết có thể chọn theo sở thích cá nhân, hôm nay đã thử nhiều phong cách, như phong cách hóa đơn, thư mục, còn đề cập ảnh liên quan rất lớn, ảnh 4K đạt hơn 20 MB. Anh ấy chỉ ra UMAN không có cơ chế theo dõi, đề xuất cài UMAN cho Openclaw, có thể cài skills của nó, nhưng tối qua chưa cài xong, còn xem tình hình cài đặt của AJ Tôm hùm nhỏ, hiển thị vẫn có thể cài đặt.",
    "  OpenClaw技能安装建议及网页搜索问题探讨": "  Đề xuất cài đặt kỹ năng OpenClaw và thảo luận vấn đề tìm kiếm web",
    "本章节主要由 AJ 分享小盖老师在小红书所发内容，建议装完 openclaw 后不要一下装几百个技能，并推荐了网页搜索这一技能。AJ 还谈到很多人对网页搜索有执念以及其搜索效果有时不佳、需爬虫能力等问题，之后提到自己有文档要发但找不到，最后表示要多发推文。":
        "Chương này chủ yếu do AJ chia sẻ nội dung thầy Tiểu Cái đăng trên Xiaohongshu, khuyên sau khi cài openclaw xong không nên cài hàng trăm kỹ năng cùng lúc, và đã giới thiệu kỹ năng tìm kiếm web. AJ còn nói đến việc nhiều người ám ảnh với tìm kiếm web cũng như hiệu quả tìm kiếm đôi khi không tốt, cần khả năng crawl, v.v., sau đó đề cập mình có tài liệu cần gửi nhưng tìm không thấy, cuối cùng cho biết sẽ đăng nhiều tweet hơn.",
    "  Claude code及Openclaw安装配置与使用交流": "  Trao đổi về cài đặt cấu hình và sử dụng Claude code và Openclaw",
    "本章节中，AJ介绍了软件安装与配置相关内容，包括CC、Claude code、Openclaw等的安装，提及在不同云平台购买实例及coding plan，演示了Claude code配置过程，还说了在Vscode里的配置方法。最后发起调研，询问小龙虾使用案例、使用者背景及使用方向，邀请大家分享部署方式和使用原因。":
        "Trong chương này, AJ giới thiệu nội dung liên quan đến cài đặt và cấu hình phần mềm, bao gồm cài đặt CC, Claude code, Openclaw, đề cập mua instance trên các nền tảng đám mây khác nhau và coding plan, trình diễn quá trình cấu hình Claude code, còn nói về cách cấu hình trong VSCode. Cuối cùng phát động khảo sát, hỏi về trường hợp sử dụng Tôm hùm, nền tảng người dùng và hướng sử dụng, mời mọi người chia sẻ cách triển khai và lý do sử dụng.",
    "  Opencloud使用经验分享及多agent协作探讨": "  Chia sẻ kinh nghiệm sử dụng Opencloud và thảo luận về hợp tác đa agent",
    "本章节主要是枫子分享使用体验，他让技术小白自主学习安装Opencloud相关内容，展现出良好的自我进化能力。也提到部署方法，小白可用IDE工具。还交流了将机器人拉进飞书群的操作问题，需企业认证。此外，预告了Openclaw训练营，枫子还谈及多agent集群协作的研究情况。":
        "Chương này chủ yếu là Phong Tử chia sẻ trải nghiệm sử dụng, anh ấy cho người mới về kỹ thuật tự học cài đặt nội dung liên quan Opencloud, thể hiện khả năng tự tiến hóa tốt. Cũng đề cập phương pháp triển khai, người mới có thể dùng công cụ IDE. Còn trao đổi vấn đề thao tác kéo robot vào nhóm Feishu, cần xác thực doanh nghiệp. Ngoài ra, thông báo trước về khóa đào tạo Openclaw, Phong Tử còn nói đến tình hình nghiên cứu hợp tác cụm đa agent.",
    "  小龙虾工具使用体验及配置、成本问题分享": "  Chia sẻ trải nghiệm sử dụng công cụ Tôm hùm và vấn đề cấu hình, chi phí",
    "本章节孔立刚分享使用小龙虾的感受。部署方面，本机部署更方便，建议全局安装；升级时可在对话框对话完成自我升级。使用时要配置搜索和技能，还介绍了相关配置文件。此外，使用中存在 API 消耗大、GLM 有限制和多模态能力不足等问题，推荐使用 Minimax 模型，最后分享了开发小手机 UI 的经历。":
        "Chương này Khổng Lập Cương chia sẻ cảm nhận khi sử dụng Tôm hùm. Về mặt triển khai, triển khai trên máy local tiện hơn, khuyến nghị cài đặt toàn cục; khi nâng cấp có thể đối thoại trong hộp thoại để hoàn thành tự nâng cấp. Khi sử dụng cần cấu hình tìm kiếm và kỹ năng, còn giới thiệu các file cấu hình liên quan. Ngoài ra, trong quá trình sử dụng có vấn đề tiêu hao API lớn, GLM có giới hạn và khả năng đa phương thức không đủ, khuyến nghị sử dụng mô hình Minimax, cuối cùng chia sẻ trải nghiệm phát triển UI điện thoại nhỏ.",
    "  火山coding plan配置及Claude code安装使用介绍": "  Giới thiệu cấu hình Volcano coding plan và cài đặt sử dụng Claude code",
    "本章节主要介绍火山coding plan使用方法。遇到问题可复制全文让其帮忙配置，配置时要注意将key、model放入指定段，base URL后应为coding，避免扣其他费用。还提及接口协议，如open AI和Anthropic协议。安装Claude code较简单，装好后在窗口输入相关指令可让其干活，有问题在群窗口说可在远程服务器安装。":
        "Chương này chủ yếu giới thiệu cách sử dụng Volcano coding plan. Gặp vấn đề có thể sao chép toàn bộ văn bản cho nó giúp cấu hình, khi cấu hình cần chú ý đặt key, model vào đoạn chỉ định, sau base URL nên là coding, tránh trừ các phí khác. Còn đề cập giao thức giao diện, như giao thức OpenAI và Anthropic. Cài đặt Claude code khá đơn giản, sau khi cài xong nhập lệnh liên quan vào cửa sổ là có thể cho nó làm việc, có vấn đề nói trong cửa sổ nhóm có thể cài trên server từ xa.",
    "  分享阿里iFlow获取API key方法及公众号": "  Chia sẻ phương pháp lấy API key từ Alibaba iFlow và tài khoản công chúng",
    "本章节中孔立刚补充关于API的问题，提到阿里的AI flow可带出GLM 2.5或Minimax 2.5等最新模型，额度比谷歌高。大家讨论其网址应为.cn，它是永久免费的，类似逆向模式，有点像Claude code CLI模式，登录网页拿下cookie，用软件可获取API key使用，孔立刚会发公众号供参考，AJ将收录相关内容。":
        "Trong chương này Khổng Lập Cương bổ sung về vấn đề API, đề cập AI flow của Alibaba có thể kéo ra các mô hình mới nhất như GLM 2.5 hoặc Minimax 2.5, hạn mức cao hơn Google. Mọi người thảo luận địa chỉ web nên là .cn, nó miễn phí vĩnh viễn, tương tự chế độ đảo ngược, hơi giống chế độ CLI của Claude code, đăng nhập web lấy cookie, dùng phần mềm có thể lấy API key sử dụng, Khổng Lập Cương sẽ đăng trên tài khoản công chúng để tham khảo, AJ sẽ thu thập nội dung liên quan.",
    "  Claude code 退出后恢复安装 openclaw": "  Khôi phục cài đặt openclaw sau khi thoát Claude code",
    "本章节主要围绕AJ安装中断后能否找回上次任务展开讨论。AJ表示安装到一半退出，看不到上一任务。孔立刚告知退出来有\"resume\"，给出\"Claude code -- resume\"的操作方法，还让AJ选上次对话，称在对应位置填\"-- resume\"是一样的。最后AJ找到相关内容，决定让其安装openclaw。":
        "Chương này chủ yếu thảo luận xoay quanh việc AJ có thể tìm lại nhiệm vụ trước sau khi cài đặt bị gián đoạn hay không. AJ cho biết cài được nửa thì thoát ra, không thấy nhiệm vụ trước. Khổng Lập Cương thông báo thoát ra có \"resume\", đưa ra phương pháp thao tác \"Claude code -- resume\", còn bảo AJ chọn cuộc trò chuyện trước, nói điền \"-- resume\" vào vị trí tương ứng cũng giống nhau. Cuối cùng AJ tìm được nội dung liên quan, quyết định cho nó cài openclaw.",
    "  AJ反馈飞书文档创建空白问题及解决办法探讨": "  AJ phản hồi vấn đề tạo tài liệu Feishu bị trống và thảo luận giải pháp",
    "本章节中，AJ 提出使用时让工具在 GitHub 安装东西、写飞书文档，但文档为空的问题并询问解决办法。孔立刚表示是配置问题，飞书文档升级后分写标题和正文两步，需分步操作，还称会找出相关链接发给 AJ，认为问题在于不清楚文档配置格式。":
        "Trong chương này, AJ nêu ra vấn đề khi sử dụng cho công cụ cài đặt thứ trên GitHub, viết tài liệu Feishu nhưng tài liệu bị trống và hỏi cách giải quyết. Khổng Lập Cương cho biết đó là vấn đề cấu hình, sau khi tài liệu Feishu nâng cấp chia thành hai bước viết tiêu đề và nội dung, cần thao tác từng bước, còn nói sẽ tìm liên kết liên quan gửi cho AJ, cho rằng vấn đề là không rõ định dạng cấu hình tài liệu.",
    "  MD文件查看难题及带域名下载链接解决办法": "  Khó khăn xem file MD và giải pháp liên kết tải xuống có tên miền",
    "本章节主要围绕AJ生成的MD文件展开讨论。AJ提到文件存于远程机器，预览不便，只能让对方打包发送。孔立刚建议可在服务器路径找文件，若有域名，配置好证书后能生成可下载的链接。AJ表示自己有多个域名，询问能否生成带域名的链接，得到肯定答复并表示认可。":
        "Chương này chủ yếu thảo luận xoay quanh file MD do AJ tạo ra. AJ đề cập file lưu trên máy từ xa, xem trước không tiện, chỉ có thể nhờ đối phương đóng gói gửi. Khổng Lập Cương gợi ý có thể tìm file trong đường dẫn server, nếu có tên miền, sau khi cấu hình chứng chỉ có thể tạo liên kết tải xuống được. AJ cho biết mình có nhiều tên miền, hỏi có thể tạo liên kết có tên miền không, nhận được câu trả lời khẳng định và bày tỏ đồng ý.",
    "  云端助手权限不足，建议本地或全局安装": "  Quyền trợ lý đám mây không đủ, khuyến nghị cài đặt cục bộ hoặc toàn cục",
    "本章节中，🌈AJ 称自己被拒绝回答，怀疑被拉黑名单，还表示与助手说话没权限，一只\"虾\"死机。孔立刚解释是因在云端安装且权限未开足，若自己使用权限较大，可访问服务器其他配置。建议🌈AJ 本地或在单独服务器全局安装，以获得更多权限和更大操作空间。":
        "Trong chương này, AJ cho biết mình bị từ chối trả lời, nghi ngờ bị đưa vào danh sách đen, còn nói nói chuyện với trợ lý không có quyền, một con \"tôm\" bị treo máy. Khổng Lập Cương giải thích là do cài trên đám mây và quyền chưa mở đủ, nếu tự sử dụng quyền lớn hơn, có thể truy cập các cấu hình khác trên server. Khuyến nghị AJ cài cục bộ hoặc cài toàn cục trên server riêng, để có nhiều quyền hơn và không gian thao tác lớn hơn.",
    "  飞书文档使用、API 权限及项目部署交流": "  Trao đổi về sử dụng tài liệu Feishu, quyền API và triển khai dự án",
    "本章节主要围绕文档操作和技术应用展开。孔立刚将文档发至群里，告知可让他人配文档并答疑，还介绍飞书文档有读取分享文档内容转 Markdown 的技能。🌈AJ 提到小龙虾访问微推 API 没权限是因飞书反爬策略，还分享让项目学习 Github 文件后生成 html、部署到 Github 和 vercel 形成网页的经历。":
        "Chương này chủ yếu xoay quanh thao tác tài liệu và ứng dụng kỹ thuật. Khổng Lập Cương gửi tài liệu vào nhóm, thông báo có thể nhờ người khác cấu hình tài liệu và giải đáp, còn giới thiệu tài liệu Feishu có kỹ năng đọc nội dung tài liệu chia sẻ chuyển thành Markdown. AJ đề cập Tôm hùm truy cập API vi đẩy không có quyền là do chiến lược chống crawl của Feishu, còn chia sẻ trải nghiệm cho dự án học file Github rồi tạo html, triển khai lên Github và vercel thành trang web.",
    "  上下文问题解决思路及多角色对话模式探讨": "  Hướng giải quyết vấn đề ngữ cảnh và thảo luận chế độ đối thoại đa vai trò",
    "本章节主要围绕上下文问题展开讨论。孔立刚表示上下文问题与模型上下文窗口有关，可换窗口长的模型。🌈AJ提出上下文可做插件，如存到obsidian上。枫子担心插件上下文压缩及污染问题，孔立刚指出可分角色解决。还探讨多角色模式，一种是指挥官接收分配任务，另一种是创建多个BOT指定不同角色。":
        "Chương này chủ yếu thảo luận xoay quanh vấn đề ngữ cảnh. Khổng Lập Cương cho biết vấn đề ngữ cảnh liên quan đến cửa sổ ngữ cảnh của mô hình, có thể đổi sang mô hình có cửa sổ dài hơn. AJ đề xuất ngữ cảnh có thể làm plugin, như lưu vào Obsidian. Phong Tử lo ngại vấn đề nén ngữ cảnh plugin và ô nhiễm, Khổng Lập Cương chỉ ra có thể giải quyết bằng cách phân vai trò. Còn thảo luận chế độ đa vai trò, một loại là chỉ huy tiếp nhận phân công nhiệm vụ, loại khác là tạo nhiều BOT chỉ định vai trò khác nhau.",
    "  小龙虾agent团队框架搭建及任务分配交流": "  Xây dựng framework nhóm agent Tôm hùm và trao đổi phân công nhiệm vụ",
    "本章节主要围绕小龙虾 agent 团队能力胶囊展开讨论。枫子看到评论区同学发的内容，W 介绍有三个独立框架的能力胶囊，使用第二个和第一个框架配合创建 agent 团队并设定角色任务等。还谈及分配机制、部署位置及权限问题，W 让角色自动赚积分，后续准备按老师建议本地再部署一套继续研究。":
        "Chương này chủ yếu thảo luận xoay quanh viên năng lực nhóm agent Tôm hùm. Phong Tử thấy nội dung bạn đăng trong phần bình luận, W giới thiệu có ba viên năng lực framework độc lập, sử dụng framework thứ hai và thứ nhất phối hợp tạo nhóm agent và thiết lập vai trò nhiệm vụ, v.v. Còn nói đến cơ chế phân công, vị trí triển khai và vấn đề quyền, W cho vai trò tự động kiếm điểm, tiếp theo chuẩn bị theo đề xuất của thầy triển khai thêm một bộ cục bộ để tiếp tục nghiên cứu.",
    "  W分享跨境电商运营及数据抓取系统搭建经验": "  W chia sẻ kinh nghiệm vận hành thương mại điện tử xuyên biên giới và xây dựng hệ thống thu thập dữ liệu",
    "本章节中W介绍自己背景，其加入跨境电商运营与AI团队，主攻Web coding。他用相关能力搭建了分布式抓取数据系统，能更新产品流量、销量数据，还做了数据分析工具用于选品。数据有t减一和实时两种。团队在东北，因人力便宜，做韩国跨境服装生意，直接找厂生产，成本较低。":
        "Trong chương này W giới thiệu nền tảng bản thân, anh ấy tham gia nhóm vận hành thương mại điện tử xuyên biên giới và AI, chuyên về Web coding. Anh ấy dùng năng lực liên quan xây dựng hệ thống thu thập dữ liệu phân tán, có thể cập nhật lưu lượng sản phẩm, dữ liệu doanh số, còn làm công cụ phân tích dữ liệu dùng cho chọn sản phẩm. Dữ liệu có hai loại t-1 và thời gian thực. Nhóm ở Đông Bắc, vì nhân công rẻ, làm kinh doanh quần áo xuyên biên giới Hàn Quốc, trực tiếp tìm nhà máy sản xuất, chi phí khá thấp.",
    "  画图技能分享、案例展示及文档使用交流": "  Chia sẻ kỹ năng vẽ, trình bày trường hợp và trao đổi sử dụng tài liệu",
    "本章节会议中，AJ先提及龙虾聚会及群里小龙虾发言多、自己发API key调查一事，之后与枫子、孔立刚等交流画图技能相关内容。AJ表示会分享并更新画图内容，强调生图用nanobanana Pro 4K更清晰且涨粉率高，还将文档设为可编辑，让大家把做的案例贴图放最下面。":
        "Trong phiên họp chương này, AJ đầu tiên đề cập buổi họp mặt Tôm hùm và việc Tôm hùm phát biểu nhiều trong nhóm, việc mình phát khảo sát API key, sau đó trao đổi với Phong Tử, Khổng Lập Cương và những người khác về nội dung liên quan đến kỹ năng vẽ. AJ cho biết sẽ chia sẻ và cập nhật nội dung vẽ, nhấn mạnh tạo ảnh dùng nanobanana Pro 4K rõ hơn và tỷ lệ tăng follower cao, còn đặt tài liệu thành có thể chỉnh sửa, để mọi người đặt ảnh trường hợp đã làm xuống cuối cùng.",
    "  分享学习工具，邀人入群及嘉宾分享": "  Chia sẻ công cụ học tập, mời người vào nhóm và khách mời chia sẻ",
    "本章节中，AJ将学习包转发到群里，介绍了knowledge SE的set Creator，称其能一句话生成任何领域学习网站，还可直接在vercel上部署。AJ鼓励大家举例制作并分享，提及要凑满2000人，让大家拉人进群，提到小龙虾人数较少。今日自习结束，欢迎想做分享者加其飞书，也欢迎来当嘉宾。":
        "Trong chương này, AJ chuyển tiếp gói học tập vào nhóm, giới thiệu set Creator của knowledge SE, nói nó có thể tạo trang web học tập bất kỳ lĩnh vực nào chỉ với một câu, còn có thể triển khai trực tiếp trên vercel. AJ khuyến khích mọi người làm ví dụ và chia sẻ, đề cập cần đủ 2000 người, nhờ mọi người kéo người vào nhóm, nói số người Tôm hùm còn ít. Hôm nay tự học kết thúc, chào mừng người muốn chia sẻ thêm Feishu của anh ấy, cũng chào mừng đến làm khách mời.",
    "  Openclaw小龙虾训练营相关安排及4K图操作说明": "  Sắp xếp liên quan đến khóa đào tạo Tôm hùm Openclaw và hướng dẫn thao tác ảnh 4K",
    "本章节主要介绍了即将举办的Openclaw（AI小龙虾）训练营相关事宜，主讲人为崟海和CY，还邀请了嘉宾，会教大家小龙虾从头部署到安装、在多维表格等各端的操作使用，CY会教硬件部署。日期未确定，等小鱿鱼通知，欢迎大家过两天关注。此外提到4K图操作看API文档，会议回放会发至小龙虾群。":
        "Chương này chủ yếu giới thiệu các vấn đề liên quan đến khóa đào tạo Openclaw (AI Tôm hùm) sắp tổ chức, giảng viên chính là Ngân Hải và CY, còn mời khách mời, sẽ dạy mọi người từ triển khai đến cài đặt Tôm hùm, thao tác sử dụng trên các nền tảng như bảng đa chiều, CY sẽ dạy triển khai phần cứng. Ngày chưa xác định, chờ Tiểu Mực thông báo, mời mọi người theo dõi trong vài ngày tới. Ngoài ra đề cập thao tác ảnh 4K xem tài liệu API, bản phát lại cuộc họp sẽ gửi vào nhóm Tôm hùm.",

    # === BLOCKS 86-91: Related section headers ===
    "会议中的金句时刻": "Khoảnh khắc câu nói hay trong cuộc họp",
    "相关链接": "Liên kết liên quan",
    "妙记：": "Ghi chép thông minh:",
    "02-25 | 今晚是自习室 WaytoAGI晚8点共学": "02-25 | Tối nay là phòng tự học WaytoAGI học chung lúc 8 giờ tối",
    "文字记录": "Bản ghi văn bản",
    "02-25 | 今晚是自习室 WaytoAGI晚8点共学 2026年2月25日": "02-25 | Tối nay là phòng tự học WaytoAGI học chung lúc 8 giờ tối ngày 25 tháng 2 năm 2026",
    "相关会议纪要": "Biên bản họp liên quan",
}

# Now I'll generate the translation programmatically for blocks 92+
# These are the related meeting minutes links - we translate them using a function
# that handles full-text properly

def translate_minutes_text(text):
    """Full proper translation of meeting minutes titles"""
    import re as _re

    # Work on a copy
    t = text

    # First do exact full-phrase replacements (longest first to avoid conflicts)
    phrases = [
        ("智能纪要：", "Biên bản thông minh: "),
        ("WaytoAGI晚8点共学", "WaytoAGI học chung lúc 8 giờ tối"),
        ("晚8点共学", "học chung lúc 8 giờ tối"),
        # Dates
        ("2026年3月23日", "ngày 23 tháng 3 năm 2026"),
        ("2026年3月18日", "ngày 18 tháng 3 năm 2026"),
        ("2026年3月17日", "ngày 17 tháng 3 năm 2026"),
        ("2026年3月15日", "ngày 15 tháng 3 năm 2026"),
        ("2026年3月13日", "ngày 13 tháng 3 năm 2026"),
        ("2026年3月11日", "ngày 11 tháng 3 năm 2026"),
        ("2026年3月7日", "ngày 7 tháng 3 năm 2026"),
        ("2026年3月5日", "ngày 5 tháng 3 năm 2026"),
        ("2026年3月4日", "ngày 4 tháng 3 năm 2026"),
        ("2026年3月3日", "ngày 3 tháng 3 năm 2026"),
        ("2026年3月1日", "ngày 1 tháng 3 năm 2026"),
        ("2026年2月28日", "ngày 28 tháng 2 năm 2026"),
        ("2026年2月27日", "ngày 27 tháng 2 năm 2026"),
        ("2026年2月26日", "ngày 26 tháng 2 năm 2026"),
        ("2026年2月25日", "ngày 25 tháng 2 năm 2026"),
        ("2026年2月24日", "ngày 24 tháng 2 năm 2026"),
        ("2026年2月13日", "ngày 13 tháng 2 năm 2026"),
        ("2026年2月12日", "ngày 12 tháng 2 năm 2026"),
        ("2026年2月11日", "ngày 11 tháng 2 năm 2026"),
        ("2026年2月10日", "ngày 10 tháng 2 năm 2026"),
        ("2026年2月8日", "ngày 8 tháng 2 năm 2026"),
        ("2026年2月6日", "ngày 6 tháng 2 năm 2026"),
        ("2026年2月5日", "ngày 5 tháng 2 năm 2026"),
        ("2026年2月4日", "ngày 4 tháng 2 năm 2026"),
        ("2026年2月3日", "ngày 3 tháng 2 năm 2026"),
        ("2026年1月30日", "ngày 30 tháng 1 năm 2026"),
        ("2026年1月28日", "ngày 28 tháng 1 năm 2026"),
        ("2026年1月26日", "ngày 26 tháng 1 năm 2026"),
        ("2026年1月25日", "ngày 25 tháng 1 năm 2026"),
        ("2026年1月24日", "ngày 24 tháng 1 năm 2026"),
        ("2026年1月23日", "ngày 23 tháng 1 năm 2026"),
        ("2026年1月20日", "ngày 20 tháng 1 năm 2026"),
        ("2026年1月19日", "ngày 19 tháng 1 năm 2026"),
        ("2026年1月17日", "ngày 17 tháng 1 năm 2026"),
        ("2026年1月13日", "ngày 13 tháng 1 năm 2026"),
        ("2026年1月10日", "ngày 10 tháng 1 năm 2026"),
        ("2026年1月8日", "ngày 8 tháng 1 năm 2026"),
        ("2026年1月3日", "ngày 3 tháng 1 năm 2026"),
        ("2025年12月30日", "ngày 30 tháng 12 năm 2025"),
        ("2025年12月29日", "ngày 29 tháng 12 năm 2025"),
        ("2025年12月28日", "ngày 28 tháng 12 năm 2025"),
        ("2025年12月27日", "ngày 27 tháng 12 năm 2025"),
        ("2025年12月22日", "ngày 22 tháng 12 năm 2025"),
        ("2025年12月20日", "ngày 20 tháng 12 năm 2025"),
        ("2025年12月18日", "ngày 18 tháng 12 năm 2025"),
        ("2025年12月15日", "ngày 15 tháng 12 năm 2025"),
        ("2025年12月13日", "ngày 13 tháng 12 năm 2025"),
        ("2025年12月11日", "ngày 11 tháng 12 năm 2025"),
        ("2025年12月10日", "ngày 10 tháng 12 năm 2025"),
        ("2025年12月9日", "ngày 9 tháng 12 năm 2025"),
        ("2025年12月8日", "ngày 8 tháng 12 năm 2025"),
        ("2025年12月6日", "ngày 6 tháng 12 năm 2025"),
        ("2025年12月5日", "ngày 5 tháng 12 năm 2025"),
        ("2025年12月4日", "ngày 4 tháng 12 năm 2025"),
        ("2025年12月2日", "ngày 2 tháng 12 năm 2025"),
        ("2025年11月29日", "ngày 29 tháng 11 năm 2025"),
        ("2025年11月28日", "ngày 28 tháng 11 năm 2025"),
        ("2025年11月27日", "ngày 27 tháng 11 năm 2025"),
        ("2025年11月26日", "ngày 26 tháng 11 năm 2025"),
        ("2025年11月25日", "ngày 25 tháng 11 năm 2025"),
        ("2025年11月24日", "ngày 24 tháng 11 năm 2025"),
        ("2025年11月23日", "ngày 23 tháng 11 năm 2025"),
        ("2025年11月22日", "ngày 22 tháng 11 năm 2025"),
        ("2025年11月21日", "ngày 21 tháng 11 năm 2025"),
        ("2025年11月20日", "ngày 20 tháng 11 năm 2025"),
        ("2025年11月19日", "ngày 19 tháng 11 năm 2025"),
        ("2025年11月18日", "ngày 18 tháng 11 năm 2025"),
        ("2025年11月17日", "ngày 17 tháng 11 năm 2025"),
        ("2025年11月15日", "ngày 15 tháng 11 năm 2025"),
        ("2025年11月14日", "ngày 14 tháng 11 năm 2025"),
        ("2025年11月13日", "ngày 13 tháng 11 năm 2025"),
        ("2025年11月12日", "ngày 12 tháng 11 năm 2025"),
        ("2025年11月11日", "ngày 11 tháng 11 năm 2025"),
        ("2025年11月9日", "ngày 9 tháng 11 năm 2025"),
        ("2025年11月8日", "ngày 8 tháng 11 năm 2025"),
        ("2025年11月7日", "ngày 7 tháng 11 năm 2025"),
        ("2025年11月5日", "ngày 5 tháng 11 năm 2025"),
        ("2025年11月4日", "ngày 4 tháng 11 năm 2025"),
        ("2025年11月3日", "ngày 3 tháng 11 năm 2025"),
        ("2025年11月2日", "ngày 2 tháng 11 năm 2025"),
        ("2025年11月1日", "ngày 1 tháng 11 năm 2025"),
        ("2025年10月31日", "ngày 31 tháng 10 năm 2025"),
        ("2025年10月30日", "ngày 30 tháng 10 năm 2025"),
        ("2025年10月29日", "ngày 29 tháng 10 năm 2025"),
        ("2025年10月28日", "ngày 28 tháng 10 năm 2025"),
        ("2025年10月24日", "ngày 24 tháng 10 năm 2025"),
        ("2025年10月23日", "ngày 23 tháng 10 năm 2025"),
        ("2025年10月22日", "ngày 22 tháng 10 năm 2025"),
        ("2025年10月21日", "ngày 21 tháng 10 năm 2025"),
        ("2025年10月20日", "ngày 20 tháng 10 năm 2025"),
        ("2025年10月18日", "ngày 18 tháng 10 năm 2025"),
        ("2025年10月17日", "ngày 17 tháng 10 năm 2025"),
        ("2025年10月15日", "ngày 15 tháng 10 năm 2025"),
        ("2025年10月14日", "ngày 14 tháng 10 năm 2025"),
        ("2025年10月13日", "ngày 13 tháng 10 năm 2025"),
        ("2025年10月10日", "ngày 10 tháng 10 năm 2025"),
        ("2025年10月9日", "ngày 9 tháng 10 năm 2025"),
        ("2025年10月7日", "ngày 7 tháng 10 năm 2025"),
        ("2025年10月3日", "ngày 3 tháng 10 năm 2025"),
        ("2025年10月2日", "ngày 2 tháng 10 năm 2025"),
        ("2025年10月1日", "ngày 1 tháng 10 năm 2025"),
        ("2025年9月27日", "ngày 27 tháng 9 năm 2025"),
        ("2025年9月25日", "ngày 25 tháng 9 năm 2025"),
        ("2025年9月24日", "ngày 24 tháng 9 năm 2025"),
        ("2025年9月23日", "ngày 23 tháng 9 năm 2025"),
        ("2025年9月22日", "ngày 22 tháng 9 năm 2025"),
        ("2025年9月20日", "ngày 20 tháng 9 năm 2025"),
        ("2025年9月19日", "ngày 19 tháng 9 năm 2025"),
        ("2025年9月18日", "ngày 18 tháng 9 năm 2025"),
        ("2025年9月17日", "ngày 17 tháng 9 năm 2025"),
        ("2025年9月16日", "ngày 16 tháng 9 năm 2025"),
        ("2025年9月11日", "ngày 11 tháng 9 năm 2025"),
        ("2025年9月10日", "ngày 10 tháng 9 năm 2025"),
        ("2025年9月9日", "ngày 9 tháng 9 năm 2025"),
        ("2025年9月8日", "ngày 8 tháng 9 năm 2025"),
        ("2025年9月7日", "ngày 7 tháng 9 năm 2025"),
        ("2025年9月6日", "ngày 6 tháng 9 năm 2025"),
        ("2025年9月5日", "ngày 5 tháng 9 năm 2025"),
        ("2025年9月4日", "ngày 4 tháng 9 năm 2025"),
        ("2025年9月3日", "ngày 3 tháng 9 năm 2025"),
        ("2025年9月2日", "ngày 2 tháng 9 năm 2025"),
        ("2025年8月29日", "ngày 29 tháng 8 năm 2025"),
        ("2025年8月28日", "ngày 28 tháng 8 năm 2025"),
        ("2025年8月27日", "ngày 27 tháng 8 năm 2025"),
        ("2025年8月26日", "ngày 26 tháng 8 năm 2025"),
        ("2025年8月22日", "ngày 22 tháng 8 năm 2025"),
        ("2025年8月21日", "ngày 21 tháng 8 năm 2025"),
        ("2025年8月19日", "ngày 19 tháng 8 năm 2025"),
        ("2025年8月18日", "ngày 18 tháng 8 năm 2025"),
        ("2025年8月13日", "ngày 13 tháng 8 năm 2025"),
        ("2025年8月11日", "ngày 11 tháng 8 năm 2025"),
        ("2025年8月6日", "ngày 6 tháng 8 năm 2025"),
        ("2025年8月2日", "ngày 2 tháng 8 năm 2025"),
        ("2025年7月31日", "ngày 31 tháng 7 năm 2025"),
        ("2025年7月23日", "ngày 23 tháng 7 năm 2025"),
        ("2025年7月22日", "ngày 22 tháng 7 năm 2025"),
        ("2025年7月16日", "ngày 16 tháng 7 năm 2025"),
        ("2025年7月15日", "ngày 15 tháng 7 năm 2025"),
        ("2025年7月9日", "ngày 9 tháng 7 năm 2025"),
        ("2025年7月7日", "ngày 7 tháng 7 năm 2025"),
        # Chinese words/phrases in the minutes titles - ordered longest first
        ("AI搭子上班记：你思考，DuMate干活", "AI bạn đồng hành đi làm: Bạn suy nghĩ, DuMate làm việc"),
        ("还在自己整理文件、查资料、做表格？", "Vẫn đang tự mình sắp xếp file, tra tài liệu, làm bảng tính?"),
        ("首个国产企业级满血版小龙虾——百度 DuMate 已全量上线！", "Con tôm hùm phiên bản đầy đủ cấp doanh nghiệp nội địa đầu tiên — Baidu DuMate đã ra mắt toàn diện!"),
        ("一个人 + 一个 DuMate = 一个小团队。", "Một người + một DuMate = một nhóm nhỏ."),
        ("直播亮点：", "Điểm nổi bật livestream:"),
        ("磁盘整理 + 资料搜集 + 学习助手，三大办公场景实测", "Sắp xếp ổ đĩa + Thu thập tài liệu + Trợ lý học tập, thử nghiệm thực tế ba kịch bản văn phòng lớn"),
        ("从文件管理到信息汇总，全流程 AI 代劳", "Từ quản lý file đến tổng hợp thông tin, AI làm thay toàn bộ quy trình"),
        ("今晚21:00直播｜「Agent Talk系列第一期」：带你揭秘YC创业者都在用Agent做什么", "Tối nay 21:00 livestream | \"Agent Talk loạt kỳ 1\": Dẫn bạn khám phá các nhà khởi nghiệp YC đang dùng Agent làm gì"),
        ("特邀嘉宾", "Khách mời đặc biệt"),
        ("发起人", "Người sáng lập"),
        ("直播核心亮点：", "Điểm nổi bật cốt lõi livestream:"),
        ("硅谷最火的 Agent 方向拆解", "Phân tích hướng Agent nóng nhất Silicon Valley"),
        ("从 Demo 到赚钱的完整路径", "Con đường hoàn chỉnh từ Demo đến kiếm tiền"),
        ("可规模化Agent的安全兼容性", "Tính bảo mật tương thích của Agent có thể mở rộng quy mô"),
        ("养虾经验谈：我睡觉，虾剪片", "Kinh nghiệm nuôi tôm: Tôi ngủ, tôm cắt phim"),
        ("养虾经验谈：我睡觉，虾赚钱", "Kinh nghiệm nuôi tôm: Tôi ngủ, tôm kiếm tiền"),
        ("广告、产品、品牌片全搞定", "Quảng cáo, sản phẩm, phim thương hiệu đều xử lý hết"),
        ("今天晚上百度千帆开发者带你解锁新姿势：", "Tối nay nhà phát triển Baidu Qianfan dẫn bạn mở khóa tư thế mới:"),
        ("用 OpenClaw 实现全自动 AI 剪辑", "Dùng OpenClaw thực hiện cắt phim AI hoàn toàn tự động"),
        ("你只管放心睡觉，小虾帮你剪片！", "Bạn cứ yên tâm ngủ, tôm nhỏ giúp bạn cắt phim!"),
        ("全自动剪片流程，从脚本→成片一步到位", "Quy trình cắt phim hoàn toàn tự động, từ kịch bản đến thành phẩm một bước hoàn thành"),
        ("爆款视频一键复刻，一只虾就是一个剪辑团队", "Nhân bản video hot một cú nhấp, một con tôm chính là một nhóm biên tập"),
        ("解放双手，大幅提升内容产出效率", "Giải phóng đôi tay, nâng cao đáng kể hiệu quả sản xuất nội dung"),
        ("从概念到实操，手把手教你玩转GEO！", "Từ khái niệm đến thực hành, cầm tay chỉ việc dạy bạn chơi GEO!"),
        ("向阳乔木：前TikTok商业化AI产品经理、AI自媒体人", "Hướng Dương Kiều Mộc: Cựu quản lý sản phẩm AI thương mại hóa TikTok, nhà sáng tạo nội dung AI"),
        ("姚金刚：前好未来学而思网校营销负责人、猎河科技CEO", "Diêu Kim Cương: Cựu trưởng bộ phận marketing Xueersi Online School Good Future, CEO Liehu Tech"),
        ("搜索正在偷走你的流量？来聊聊怎么让 AI 主动引用你！", "Tìm kiếm đang đánh cắp lưu lượng của bạn? Hãy nói về cách để AI chủ động trích dẫn bạn!"),
        ("当用户不再点击链接，而是直接看 AI 给的答案，你的内容还能被看到吗？", "Khi người dùng không còn nhấp vào liên kết mà trực tiếp xem câu trả lời AI đưa ra, nội dung của bạn còn được nhìn thấy không?"),
        ("带你揭秘ALL-IN-ONE 的 Agent 工作空间", "Dẫn bạn khám phá không gian làm việc Agent ALL-IN-ONE"),
        ("少卿", "Thiếu Khanh"),
        ("出国点餐一条龙 Builder", "Builder dịch vụ gọi món khi đi nước ngoài trọn gói"),
        ("社区共创者", "Đồng sáng tạo cộng đồng"),
        ("带你解锁首个为一人公司打造的 AI 工作空间", "Dẫn bạn mở khóa không gian làm việc AI đầu tiên được tạo cho công ty một người"),
        ("一键连接3500+工具，实现本地与云端文件一站式管理", "Kết nối hơn 3500 công cụ một cú nhấp, quản lý file cục bộ và đám mây một cửa"),
        ("参与直播即可领取社区专属积分兑换码", "Tham gia livestream nhận mã đổi điểm độc quyền cộng đồng"),
        ("秒哒全球首发应用生成Skill，🦞帮你做应用", "MiaoDa ra mắt toàn cầu Skill tạo ứng dụng, Tôm hùm giúp bạn làm ứng dụng"),
        ("营销增长与SEO优化全攻略", "Toàn bộ chiến lược tăng trưởng marketing và tối ưu SEO"),
        ("对准科技创始人", "Nhà sáng lập Duizhun Tech"),
        ("增长专家，三年实战经验，服务 100+ 产品", "Chuyên gia tăng trưởng, ba năm kinh nghiệm thực chiến, phục vụ hơn 100 sản phẩm"),
        ("擅长 SEO、内容营销、外链建设和增长策略", "Giỏi về SEO, marketing nội dung, xây dựng liên kết ngoài và chiến lược tăng trưởng"),
        ("掌握144 项Skills，实现精准获客与稳定增长", "Nắm vững 144 Skills, thu hút khách hàng chính xác và tăng trưởng ổn định"),
        ("实战案例复盘，解锁可复用的增长方法论", "Phân tích lại trường hợp thực chiến, mở khóa phương pháp luận tăng trưởng có thể tái sử dụng"),
        ("高玩分享！从扣子养虾到 Vibe Coding大趋势", "Chia sẻ cao thủ! Từ nuôi tôm trên Coze đến xu hướng lớn Vibe Coding"),
        ("跨5城、30+WaytoAGI社区伙伴共创的2026年度AI贺岁片《老马的AI囧途》幕后分享", "Qua 5 thành phố, hơn 30 đối tác cộng đồng WaytoAGI đồng sáng tạo phim Tết AI năm 2026 \"Con đường AI rắc rối của Lão Mã\" chia sẻ hậu trường"),
        ("该上班了！千帆养虾进阶实战", "Đã đến lúc đi làm! Thực chiến nuôi tôm nâng cao trên Qianfan"),
        ("花10分钟用Obsidian+OpenClaw彻底重构你的AI知识管理体系", "Dành 10 phút dùng Obsidian+OpenClaw hoàn toàn tái cấu trúc hệ thống quản lý tri thức AI của bạn"),
        ("卡尔的AI沃茨：公众号AI自媒体Top10、视频号AI自媒体Top30、前字节大模型算法工程师", "Karl's AI Watts: Top 10 tự truyền thông AI tài khoản công chúng, Top 30 tự truyền thông AI kênh video, cựu kỹ sư thuật toán mô hình lớn ByteDance"),
        ("全程实操｜带你用「Obsidian+OpenClaw」构建高效知识管理体系", "Thực hành toàn bộ | Dẫn bạn dùng \"Obsidian+OpenClaw\" xây dựng hệ thống quản lý tri thức hiệu quả"),
        ("避坑指南｜拆解各个工具使用痛点与技巧，助你少走弯路快速上手", "Hướng dẫn tránh bẫy | Phân tích điểm đau và kỹ thuật sử dụng từng công cụ, giúp bạn đi đường tắt nhanh chóng bắt đầu"),
        ("如何突破AI短番量多精品少困局？", "Làm thế nào để vượt qua tình trạng phim ngắn AI nhiều nhưng ít tác phẩm chất lượng?"),
        ("南墙：AIMWISE 技术开发、中国美院 AIGC 特聘讲师，首批国家级数智设计创作先锋", "Nam Tường: Phát triển kỹ thuật AIMWISE, giảng viên đặc biệt AIGC Học viện Mỹ thuật Trung Quốc, tiên phong sáng tạo thiết kế số thông minh cấp quốc gia đầu tiên"),
        ("联合创始人，百万粉丝博主，拥有超 10 年影视特效经验", "Đồng sáng lập, blogger triệu fan, có hơn 10 năm kinh nghiệm kỹ xảo điện ảnh"),
        ("拆解 AI 短番从脚本到成片的高效创作流程", "Phân tích quy trình sáng tạo hiệu quả phim ngắn AI từ kịch bản đến thành phẩm"),
        ("揭秘高质量短番创作的实战技巧与避坑指南", "Tiết lộ kỹ thuật thực chiến sáng tạo phim ngắn chất lượng cao và hướng dẫn tránh bẫy"),
        ("未来硅世界第12期：Claude Code最佳搭档CC Switch背后的故事", "Thế giới Silicon Tương lai kỳ 12: Câu chuyện đằng sau CC Switch - đối tác tốt nhất của Claude Code"),
        ("海辛：我给小龙虾造了一个可视化工作间", "Hải Tân: Tôi đã tạo một không gian làm việc trực quan cho Tôm hùm"),
        ("从文档到生命体，开启文件即软件新纪元", "Từ tài liệu đến thực thể sống, mở ra kỷ nguyên mới file chính là phần mềm"),
        ("特邀嘉宾：", "Khách mời đặc biệt:"),
        ("社区共创者、出国点餐一条龙 Builder", "Đồng sáng tạo cộng đồng, Builder dịch vụ gọi món nước ngoài trọn gói"),
        ("架构师", "Kiến trúc sư"),
        ("直播亮点", "Điểm nổi bật livestream"),
        ('\u62c6\u89e3Self Instance\uff1a\u89e3\u9501\u201c\u6587\u4ef6\u5373\u8f6f\u4ef6\u201d\u7684\u7ec8\u6781\u5f62\u6001', 'Ph\u00e2n t\u00edch Self Instance: M\u1edf kh\u00f3a h\u00ecnh th\u00e1i cu\u1ed1i c\u00f9ng "file ch\u00ednh l\u00e0 ph\u1ea7n m\u1ec1m"'),
        ("架构师面对面：从底层逻辑到实战搭建，全流程打通Selfware", "Kiến trúc sư trực tiếp: Từ logic nền tảng đến xây dựng thực chiến, thông suốt toàn quy trình Selfware"),
        ("来新璐带大家把OpenClaw技术架构拆解，还能手搓一个最小的龙虾", "Lai Xinlu dẫn mọi người phân tích kiến trúc kỹ thuật OpenClaw, còn có thể tự tay làm một con tôm hùm nhỏ nhất"),
        ("系列课：一天消耗10亿token的龙虾养成记", "Loạt bài: Nhật ký nuôi tôm hùm tiêu thụ 1 tỷ token mỗi ngày"),
        ("对谈 EvoMap创始人：10分钟登顶ClawHub榜首的出圈密码", "Đối thoại nhà sáng lập EvoMap: Mật mã vượt vòng lên đỉnh ClawHub chỉ trong 10 phút"),
        ("晨然 Ran ：02-20 | 怎样做出2500万曝光的 Seedance 2.0视频？怪奇物语结局重制复盘", "Thần Nhiên Ran: 02-20 | Làm thế nào tạo ra video Seedance 2.0 với 25 triệu lượt tiếp cận? Phân tích tái tạo kết thúc Stranger Things"),
        ("让 AI 像你一样思考：用 YouMind Skills 打造你的内容系统，实现稳定日更涨粉", "Để AI suy nghĩ như bạn: Dùng YouMind Skills xây dựng hệ thống nội dung của bạn, đạt tăng fan ổn định cập nhật hàng ngày"),
        ("用阿里百炼制作拜年视频、春节祝福语音多场景春节祝福文案模板，一次搞定一场直播结束，就能自己动手做春节祝福内容", "Dùng Alibaba Bailian làm video chúc Tết, giọng nói chúc Tết, mẫu lời chúc Tết đa cảnh, xong một buổi livestream là tự tay làm nội dung chúc Tết"),
        ("直播嘉宾：电波曲奇", "Khách mời livestream: Điện Ba Khúc Kỳ"),
        ("如何用 YouMind 拥有源源不断的选题+持续稳定输出爆款内容", "Cách dùng YouMind có nguồn đề tài không ngừng + liên tục ổn định sản xuất nội dung hot"),
        ("百度千帆发布的7款Skill ，手把手教你一键部署属于自己的 AI 助理", "7 Skill do Baidu Qianfan phát hành, cầm tay chỉ việc dạy bạn triển khai một cú nhấp trợ lý AI của riêng mình"),
        ("星企划总决赛", "Trận chung kết Kế hoạch Ngôi sao"),
        ("玩转新春 · 年味开始了", "Chơi đón Xuân - Hương vị Tết bắt đầu rồi"),
        ("百炼上手零门槛，轻松做新年内容", "Bắt đầu Bailian không rào cản, dễ dàng làm nội dung năm mới"),
        ("福字、年货清单、窗花剪纸一站式搞定", "Chữ Phúc, danh sách đồ Tết, cắt giấy hoa cửa sổ xử lý một cửa"),
        ("年夜饭 & 菜谱大全，解决"过年吃什么"", "Bữa cơm tất niên & tổng hợp công thức, giải quyết \"Tết ăn gì\""),
        ("不讲复杂概念，直接把 AI 变成年味工具箱", "Không nói khái niệm phức tạp, trực tiếp biến AI thành hộp công cụ hương vị Tết"),
        ("直播嘉宾｜电波曲奇老师", "Khách mời livestream | Thầy Điện Ba Khúc Kỳ"),
        ("大厂 AI 产品专家｜独立开发者｜小红书 AI 博主", "Chuyên gia sản phẩm AI công ty lớn | Nhà phát triển độc lập | Blogger AI Xiaohongshu"),
        ("今晚20:00直播｜带你深度解析AI硬件 x AI应用开发", "Tối nay 20:00 livestream | Dẫn bạn phân tích sâu phần cứng AI x phát triển ứng dụng AI"),
        ("银海（AI产品经理）", "Ngân Hải (Quản lý sản phẩm AI)"),
        ("拆解AI眼镜核心能力与落地场景", "Phân tích năng lực cốt lõi kính AI và kịch bản ứng dụng"),
        ("手把手带你搭建智能体工作流", "Cầm tay dẫn bạn xây dựng workflow agent thông minh"),
        ("`智能纪要：02-07 | 今天不卷了，让TRAE Skill干活！", "`Biên bản thông minh: 02-07 | Hôm nay không cạnh tranh nữa, để TRAE Skill làm việc!"),
        ("正式发布 让每一个人都能成为内容创作者", "Chính thức phát hành, để mỗi người đều có thể trở thành nhà sáng tạo nội dung"),
        ("鹿演Vol.009：QVeris：让你的AI Agent用一个接口调用上万种数据和工具", "Lộc Diễn Vol.009: QVeris: Để AI Agent của bạn dùng một giao diện gọi hàng vạn loại dữ liệu và công cụ"),
        ("特邀嘉宾：", "Khách mời đặc biệt:"),
        ("曲东奇｜QVeris合伙人、产品运营", "Khúc Đông Kỳ | Đối tác QVeris, vận hành sản phẩm"),
        ("主持人：张蔚", "Người chủ trì: Trương Úy"),
        ("孵化负责人｜心流资本合伙人", "Trưởng bộ phận ươm tạo | Đối tác Tâm Lưu Capital"),
        ("技术大V都在用秒哒整什么活", "Các KOL công nghệ đang dùng MiaoDa làm gì"),
        ("办公高效收尾：百炼模板一键搞定节前工作", "Kết thúc công việc văn phòng hiệu quả: Template Bailian một cú nhấp xong việc trước nghỉ"),
        ("上百度智能云部署", "Triển khai trên Baidu Intelligent Cloud"),
        ("用这个Agent Skills Builder批量复刻Clawdbot", "Dùng Agent Skills Builder này nhân bản hàng loạt Clawdbot"),
        ("语音AI输入法开发实战攻略与避坑指南", "Chiến lược thực chiến phát triển bộ gõ AI giọng nói và hướng dẫn tránh bẫy"),
        ("未来硅世界第11期：AI 审美浪潮下的哲学追问与反思", "Thế giới Silicon Tương lai kỳ 11: Câu hỏi triết học và suy ngẫm trong làn sóng thẩm mỹ AI"),
        ("普通小白也能使用的云端clawdbot/moltbot/openclaw", "Đám mây mà người mới cũng có thể sử dụng clawdbot/moltbot/openclaw"),
        ("上新：手把手教你一站式AI创作", "Ra mắt: Cầm tay chỉ việc dạy bạn sáng tạo AI một cửa"),
        ("文心5.0 +千帆：零门槛玩转Agent开发", "Wenxin 5.0 + Qianfan: Phát triển Agent không rào cản"),
        ("手把手部署指南——打造一个真正的AI助理", "Hướng dẫn triển khai cầm tay — Tạo một trợ lý AI thật sự"),
        ("时代下，如何快速开发 3D 游戏？48 小时极限开发实战复盘", "Trong thời đại AI, làm thế nào phát triển nhanh game 3D? Phân tích thực chiến phát triển giới hạn 48 giờ"),
        ("特邀嘉宾00后全流程游戏制作人：宣酱 &周杰zdj", "Khách mời đặc biệt nhà sản xuất game toàn quy trình thế hệ 00: Tuyên Tương & Chu Kiệt zdj"),
        ("手把手带你玩转开源版Claude Code——Kode Agent", "Cầm tay dẫn bạn sử dụng phiên bản mã nguồn mở Claude Code — Kode Agent"),
        ("来新璐：ShareAI Lab 创始人、Kode Agent（开源版Claude Code Agent）开发者", "Lai Xinlu: Nhà sáng lập ShareAI Lab, nhà phát triển Kode Agent (phiên bản mã nguồn mở Claude Code Agent)"),
        ("深度解析 Claude Code 原理&机制设计，以及教你从 0 到 1 手搓一个迷你 Claude Code 分享人：ShareAI 来新璐", "Phân tích chuyên sâu nguyên lý & thiết kế cơ chế Claude Code, và dạy bạn tự tay làm một mini Claude Code. Người chia sẻ: ShareAI Lai Xinlu"),
        ("深度实测！AI原生工作台如何解放双手？", "Thử nghiệm chuyên sâu! Bàn làm việc AI gốc giải phóng đôi tay như thế nào?"),
        ("寻鹭 ：MiniMax Agent 产品负责人", "Tìm Lộ: Người phụ trách sản phẩm MiniMax Agent"),
        ("爆改训练营（两日连播）", "Khóa đào tạo cải tạo bùng nổ (phát sóng liên tục hai ngày)"),
        ("到底更新了什么 嘉宾：罗文+二师兄", "Rốt cuộc đã cập nhật gì. Khách mời: La Văn + Nhị Sư Huynh"),
        ("职场AI，就用扣子——新功能Coze Skill上线", "AI nơi làm việc, dùng Coze — Tính năng mới Coze Skill ra mắt"),
        ("未来硅世界第10期：对话「闪电说」创始人：AI 产品出海的实战指南", "Thế giới Silicon Tương lai kỳ 10: Đối thoại với nhà sáng lập \"FlashSay\": Hướng dẫn thực chiến sản phẩm AI ra quốc tế"),
        ("特邀嘉宾", "Khách mời đặc biệt"),
        ("龚震：闪电说联合创始人，增长&商业化负责人", "Cung Chấn: Đồng sáng lập FlashSay, người phụ trách tăng trưởng & thương mại hóa"),
        ("余猛：闪电说产品经理 & CEO", "Dư Mãnh: Quản lý sản phẩm FlashSay & CEO"),
        ("主持团：向阳乔木、姚全刚、尼克西、元子", "Ban chủ trì: Hướng Dương Kiều Mộc, Diêu Toàn Cương, Nick Xi, Nguyên Tử"),
        ("全球首个实时生成世界模型正式上线", "Mô hình thế giới tạo thời gian thực đầu tiên toàn cầu chính thức ra mắt"),
        ("鹿演Vol.008：AOE：不只是Claude Cowork，而是Vibe Working", "Lộc Diễn Vol.008: AOE: Không chỉ là Claude Cowork, mà là Vibe Working"),
        ("谭少卿：AOE CEO & Co-Founder", "Đàm Thiếu Khanh: AOE CEO & Co-Founder"),
        ("李俊：AOE 增长负责人 & Co-Founder", "Lý Tuấn: Người phụ trách tăng trưởng AOE & Co-Founder"),
        ("开年重磅！海辛&阿文AI工作流分享", "Bom tấn đầu năm! Hải Tân & A Văn chia sẻ workflow AI"),
        ("下午15:00直播｜2026CES热乎情报速递，深度解读具身智能与无人驾驶两大赛道", "Chiều 15:00 livestream | Tin tức nóng hổi CES 2026, giải mã sâu hai đường đua trí tuệ hiện thân và lái xe tự động"),
        ("📌特邀嘉宾：", "Khách mời đặc biệt:"),
        ("📌特邀嘉宾", "Khách mời đặc biệt"),
        ("王玮滢：哈佛大学计算机博士、具身智能研究科学家、连续创业者", "Vương Vĩ Doanh: Tiến sĩ Khoa học Máy tính Đại học Harvard, nhà khoa học nghiên cứu trí tuệ hiện thân, doanh nhân khởi nghiệp liên tiếp"),
        (""秒哒-让创意变生意"应用变现第五期·开放麦圆桌会！", "\"MiaoDa - Biến sáng tạo thành kinh doanh\" kiếm tiền ứng dụng kỳ 5 - Hội bàn tròn mic mở!"),
        ("未来硅世界 🔍 揭秘X平台流量密码，3周如何快速涨粉1万+？", "Thế giới Silicon Tương lai - Khám phá mật mã lưu lượng nền tảng X, 3 tuần tăng nhanh hơn 10.000 follower?"),
        ("分享爆款提示词技巧，带你避开AI同质化", "Chia sẻ kỹ thuật prompt hot, dẫn bạn tránh đồng nhất hóa AI"),
        ("今晚20:00直播｜「AI短剧训练营」加餐课：AI视频工具实操技巧速学", "Tối nay 20:00 livestream | \"Khóa đào tạo phim ngắn AI\" bài học bổ sung: Học nhanh kỹ thuật thực hành công cụ video AI"),
        ("大鹏：AIGC数字艺术设计高级工程师｜AI动画师｜腾讯SSV数字守艺人", "Đại Bằng: Kỹ sư cao cấp thiết kế nghệ thuật số AIGC | Họa sĩ hoạt hình AI | Người giữ nghệ thuật số Tencent SSV"),
        ("实操课：批量出片 + 动态分层全拿捏", "Khóa thực hành: Xuất phim hàng loạt + Nắm vững phân lớp động"),
        ("周鹏：AIGC广告/ 短剧/动画导演、小红书万粉博主", "Chu Bằng: Đạo diễn quảng cáo/phim ngắn/hoạt hình AIGC, blogger 10 nghìn fan Xiaohongshu"),
        ("解锁AI影视广告创作新玩法", "Mở khóa cách chơi mới sáng tạo quảng cáo phim ảnh AI"),
        ("丁一：广告片/ 纪录片导演 / AIGC艺术家", "Đinh Nhất: Đạo diễn phim quảng cáo/phim tài liệu / Nghệ sĩ AIGC"),
        (""秒哒-让创意变生意"之应用变现第四期超重磅登场！", "\"MiaoDa - Biến sáng tạo thành kinh doanh\" kiếm tiền ứng dụng kỳ 4 siêu trọng thể!"),
        ("专为视频创作设计的 AI 智能助手，Medeo-今晚教你如何聊出一个好视频！ 分享嘉宾：晨然/歸藏/Mona", "Trợ lý thông minh AI được thiết kế chuyên cho sáng tạo video, Medeo - Tối nay dạy bạn cách trò chuyện ra một video hay! Khách mời chia sẻ: Thần Nhiên/Quy Tàng/Mona"),
        ("未来硅世界第八期：深挖近两年AI进化真相，解锁常用AI工具清单", "Thế giới Silicon Tương lai kỳ 8: Đào sâu sự thật tiến hóa AI hai năm gần đây, mở khóa danh sách công cụ AI thường dùng"),
        ("🔥千问APP上线全新「AI小剧场」功能！体验Sora2同款玩法！", "Ứng dụng Qwen ra mắt tính năng \"Sân khấu nhỏ AI\" hoàn toàn mới! Trải nghiệm cách chơi giống Sora2!"),
        (""秒哒-让创意变生意"之应用变现教学系列第三期来咯！", "\"MiaoDa - Biến sáng tạo thành kinh doanh\" loạt dạy kiếm tiền ứng dụng kỳ 3 đã đến!"),
        ("进阶教程：手把手玩转 MCP、Skills x等工具！", "Hướng dẫn nâng cao: Cầm tay sử dụng thành thạo MCP, Skills x và các công cụ khác!"),
        ("安装配置全攻略", "Toàn bộ chiến lược cài đặt cấu hình"),
        ("调香和背后的故事，在社区里成长起来的OPC项目", "Pha chế hương thơm và câu chuyện đằng sau, dự án OPC phát triển trong cộng đồng"),
        ("鹿演 Vol.007：Mulan.pro：从家庭主妇到 AI 公司创始人 普通人真的可以逆袭吗", "Lộc Diễn Vol.007: Mulan.pro: Từ bà nội trợ đến nhà sáng lập công ty AI, người bình thường thực sự có thể đảo ngược không"),
        (""秒哒-让创意变生意"之应用变现教学系列第二期火爆来袭！ 每周四秒哒时间", "\"MiaoDa - Biến sáng tạo thành kinh doanh\" loạt dạy kiếm tiền ứng dụng kỳ 2 bùng nổ! Mỗi thứ Năm giờ MiaoDa"),
        ("鹿演 Vol.006：Refly.AI 正式开启公测！限量邀请码发放", "Lộc Diễn Vol.006: Refly.AI chính thức mở thử nghiệm công khai! Phát mã mời giới hạn"),
        ("功能亮点：小白版扣子 /n8nAI自动化工作流，多场景方案直接复刻", "Điểm nổi bật tính năng: Coze phiên bản người mới / workflow tự động hóa AI n8n, phương án đa cảnh nhân bản trực tiếp"),
        ("如何用AI做IP形象/", "Cách dùng AI làm hình tượng IP /"),
        ("短剧训练营:开营第1课", "Khóa đào tạo phim ngắn: Bài 1 khai giảng"),
        ("《短剧行业现状与爆款观片》主讲:夜游榊", "\"Hiện trạng ngành phim ngắn và xem phim hot\" Giảng viên chính: Dạ Du Thần"),
        ("先看清这个行业在"赚谁的钱"，再决定你要不要进来 /", "Trước tiên xem rõ ngành này \"kiếm tiền ai\", rồi quyết định bạn có muốn vào không /"),
        ("+教育", "+ Giáo dục"),
        ("少儿AI春晚-绘本共学屋，孩子们的创意海报", "Thiếu nhi AI Gala đêm giao thừa - Phòng học chung sách tranh, poster sáng tạo của trẻ em"),
        ("音乐零基础入门之Suno实操｜百度「AI星企划」数字角色选秀大赛创作指南", "Nhập môn âm nhạc từ zero thực hành Suno | Hướng dẫn sáng tạo cuộc thi tuyển chọn nhân vật số Baidu \"Kế hoạch Ngôi sao AI\""),
        ("【JKMiles】", "[JKMiles]"),
        ("-华腾杯全国AI作品创新大奖赛全国金奖", "- Giải vàng toàn quốc cuộc thi sáng tạo tác phẩm AI Cúp Hoa Đằng"),
        ("-WaytoAGI社区音乐板块共创者", "- Đồng sáng tạo mảng âm nhạc cộng đồng WaytoAGI"),
        (""秒哒-让创意变生意"之应用变现教学讲解系列第一期来啦！", "\"MiaoDa - Biến sáng tạo thành kinh doanh\" loạt giảng giải dạy kiếm tiền ứng dụng kỳ 1 đã đến!"),
        ("插件召集令插件开发大赛冲刺倒计时6天！百宝箱 |通义灵码|", "Lệnh triệu tập plugin cuộc thi phát triển plugin đếm ngược 6 ngày! Bách Bảo Hòm | Tongyi Lingma |"),
        ("【分享嘉宾】", "[Khách mời chia sẻ]"),
        ("吴昞：国际知名房地产咨询外企高级财务经理、WaytoAGI赛事先锋官", "Ngô Bính: Quản lý tài chính cao cấp công ty nước ngoài tư vấn bất động sản quốc tế, tiên phong cuộc thi WaytoAGI"),
        ("孔立刚：世界五百强售后运营经理、WaytoAGI训练营优秀结业学员&助教", "Khổng Lập Cương: Quản lý vận hành hậu mãi Fortune 500, học viên tốt nghiệp xuất sắc & trợ giảng khóa đào tạo WaytoAGI"),
        ("百度×乐华娱乐×WaytoAGI「AI星企划」数字角色选秀大赛正式启动！", "Baidu x Le Hua Entertainment x WaytoAGI \"Kế hoạch Ngôi sao AI\" Cuộc thi tuyển chọn nhân vật số chính thức khởi động!"),
        ("鹿演Vol.005：Creaibo——专为优质内容而生的AI🎙️", "Lộc Diễn Vol.005: Creaibo — AI được sinh ra chuyên cho nội dung chất lượng"),
        ("千问APP众测", "Thử nghiệm cộng đồng ứng dụng Qwen"),
        ("千问app众测", "Thử nghiệm cộng đồng ứng dụng Qwen"),
        ("插件召集令插件开发大赛攻略来袭 💰奖金池丰富：解锁16万巨额现金激励🔥保姆式教学：全流程系统讲解，直击痛点问题 📌不写一行代码：用lingma基于FastMCP开发demo一键部署到百宝箱", "Chiến lược cuộc thi phát triển plugin Lệnh triệu tập plugin 💰 Quỹ giải thưởng phong phú: Mở khóa thưởng tiền mặt khổng lồ 160.000 🔥 Dạy kiểu bảo mẫu: Giảng giải hệ thống toàn quy trình, đánh thẳng vào điểm đau 📌 Không viết một dòng code: Dùng Lingma dựa trên FastMCP phát triển demo triển khai một cú nhấp lên Bách Bảo Hòm"),
        ("💥今晚20:00 | 进阶冲刺！豆包应用创作零门槛创作赛进阶攻略来袭！", "Tối nay 20:00 | Nước rút nâng cao! Chiến lược nâng cao cuộc thi sáng tạo ứng dụng Doubao không rào cản!"),
        ("众测，重磅嘉宾：苍何+梦飞+小歪", "Thử nghiệm cộng đồng, khách mời nặng ký: Thương Hà + Mộng Phi + Tiểu Oai"),
        ("未来硅世界-第六期 ：AI和未来的生活", "Thế giới Silicon Tương lai - kỳ 6: AI và cuộc sống tương lai"),
        ("「AI智能体训练营」第二期，第八节：Demo Day:从0到1交付完整AI应用", "\"Khóa đào tạo AI Agent\" kỳ 2, buổi 8: Demo Day: Giao hàng ứng dụng AI hoàn chỉnh từ 0 đến 1"),
        ("企业场景MCP插件召集令插件开发大赛启动，百宝箱丨通义灵码丨", "Khởi động cuộc thi phát triển plugin Lệnh triệu tập plugin kịch bản doanh nghiệp, Bách Bảo Hòm | Tongyi Lingma |"),
        ("「AI智能体训练营」第二期，第七节：精雕细琢:性能提速&体验翻倍", "\"Khóa đào tạo AI Agent\" kỳ 2, buổi 7: Chế tác tinh xảo: Tăng tốc hiệu suất & Trải nghiệm gấp đôi"),
        ("「AI智能体训练营」第二期，第六课：多元交互：卡片、图片、语音全覆盖", "\"Khóa đào tạo AI Agent\" kỳ 2, buổi 6: Tương tác đa dạng: Thẻ, ảnh, giọng nói bao phủ toàn diện"),
        ("「AI智能体训练营」第二期，第五课：知识库x记忆:打造Bot专属\"最强大脑", "\"Khóa đào tạo AI Agent\" kỳ 2, buổi 5: Kho tri thức x Bộ nhớ: Tạo \"Bộ não mạnh nhất\" riêng cho Bot"),
        ("校园AI创投活动优秀项目全国展示，「大学生创意秀」围观同龄人如何玩转飞书！校园场景 + AI 工具的奇妙碰撞，每一个项目都藏着惊喜；", "Trình diễn toàn quốc dự án xuất sắc hoạt động đầu tư AI campus, \"Show sáng tạo sinh viên\" xem bạn đồng trang lứa sử dụng Feishu! Cảnh campus + công cụ AI va chạm kỳ diệu, mỗi dự án đều ẩn chứa bất ngờ;"),
        ("「AI智能体训练营」第二期，第四节：工作流进阶：分支、循环、意图识别、图像处理一把抓", "\"Khóa đào tạo AI Agent\" kỳ 2, buổi 4: Workflow nâng cao: Nhánh, vòng lặp, nhận diện ý định, xử lý ảnh tất cả trong tay"),
        ("带你冲20万大奖，豆包应用创作挑战赛来袭！不止冲奖，更能学硬核技巧，1小时搞定投稿！讲师：许键", "Dẫn bạn giành giải thưởng 200.000, Cuộc thi thách thức sáng tạo ứng dụng Doubao! Không chỉ giành giải, còn học kỹ thuật hardcore, 1 giờ xong nộp bài! Giảng viên: Xu Jian"),
        ("「AI智能体训练营」第二期，第三节：拖拉拽入门：零代码工作流拼出复杂逻辑", "\"Khóa đào tạo AI Agent\" kỳ 2, buổi 3: Nhập môn kéo thả: Workflow không code ghép logic phức tạp"),
        ("11-10|AI也过双十一|藏师傅版\"88VIP\"福利大放送", "11-10 | AI cũng mua sắm ngày Lễ Độc thân | Phiên bản Tạng Sư Phụ \"88VIP\" đại tiệc phúc lợi"),
        ("「AI智能体训练营」第二期，第二节：Prompt魔法:一句话让Bot听懂人话", "\"Khóa đào tạo AI Agent\" kỳ 2, buổi 2: Phép thuật Prompt: Một câu cho Bot hiểu tiếng người"),
        ("未来硅世界第五期：畅谈AI和未来生活", "Thế giới Silicon Tương lai kỳ 5: Trò chuyện về AI và cuộc sống tương lai"),
        ("第三届AIPO校园AI创投活动全国路演", "Lần thứ 3 AIPO hoạt động đầu tư sáng tạo AI campus roadshow toàn quốc"),
        ("「AI智能体训练营」第二期开营仪式，8节直播课带你从0到1打造可上线的AI应用！第一节", "\"Khóa đào tạo AI Agent\" kỳ 2 lễ khai giảng, 8 buổi livestream dẫn bạn từ 0 đến 1 tạo ứng dụng AI có thể ra mắt! Buổi 1"),
        ("11-06 | 秒哒又双叒叕上新啦！", "11-06 | MiaoDa lại ra mắt sản phẩm mới!"),
        ("校园AIPO猫叔讲提示词", "Campus AIPO Mèo Chú giảng về prompt"),
        ("剪映 AI 模板创想季 —20 万奖金 + 千万流量，手把手教你赢赛事！", "Mùa sáng tạo template AI CapCut — 200.000 giải thưởng + hàng chục triệu lưu lượng, cầm tay dạy bạn thắng cuộc thi!"),
        ("WaytoAGI校园AIPO训练营 讲师：AJ 学习AI的工作流", "Khóa đào tạo WaytoAGI Campus AIPO. Giảng viên: AJ Workflow học AI"),
        ("训练营第二期：Agent智能体实战训练营 ，嘉宾：罗文,weina,王磊,", "Khóa đào tạo kỳ 2: Khóa đào tạo thực chiến Agent thông minh, khách mời: La Văn, weina, Vương Lỗi,"),
        ("训练营Part2  - 从 0-1 聚焦校园场景搭建自己的 AI 搭子", "Khóa đào tạo Phần 2 - Từ 0-1 tập trung cảnh campus xây dựng đối tác AI của riêng bạn"),
        ("训练营第一期: n8n训练营结营", "Khóa đào tạo kỳ 1: Kết thúc khóa n8n"),
        ("训练营 - 从 0-1 聚焦校园场景搭建自己的 AI 搭子​", "Khóa đào tạo - Từ 0-1 tập trung cảnh campus xây dựng đối tác AI của riêng bạn"),
        ("【AI训练营】AI智能体项目实战分享", "[Khóa đào tạo AI] Chia sẻ thực chiến dự án Agent AI"),
        ("海外最大AI视频比赛Chroma Awards解读", "Giải mã cuộc thi video AI lớn nhất nước ngoài Chroma Awards"),
        ("第三届AIPO启动会", "Hội nghị khởi động AIPO lần thứ 3"),
        ("编程实战技巧分享，30分钟从入门到沉迷｜Vibe Coze！扣子 AI 挑战赛教程💻", "Chia sẻ kỹ thuật thực chiến lập trình, 30 phút từ nhập môn đến say mê | Vibe Coze! Hướng dẫn cuộc thi thách thức Coze AI"),
        ("🎙️IndexTTS：让声音更有温度👨\u200d🏫 讲师：思绎：bilibili IndexTTS 语音大模型首席算法专家/紫泽：bilibili 语音大模型产品运营专家", "IndexTTS: Cho âm thanh thêm ấm áp. Giảng viên: Tư Dịch: Chuyên gia thuật toán trưởng mô hình ngôn ngữ lớn giọng nói IndexTTS bilibili / Tử Trạch: Chuyên gia vận hành sản phẩm mô hình ngôn ngữ lớn giọng nói bilibili"),
        ("今晚 20:00 直播！拆解 100 万美金AI 工具权益 + 17.5 万奖金的 AI 创意竞赛", "Tối nay 20:00 livestream! Phân tích quyền lợi công cụ AI 1 triệu đô + cuộc thi sáng tạo AI giải thưởng 175.000"),
        ("特邀嘉宾：", "Khách mời đặc biệt:"),
        ("莫奈丽莎AI联合创始人，2025大阪世博会合作艺术家", "Đồng sáng lập AI Mona Lisa, nghệ sĩ hợp tác Triển lãm Osaka 2025"),
        ("编程 & AI 自媒体：避坑脱口秀🎯", "Lập trình & AI tự truyền thông: Talk show tránh bẫy"),
        ("特邀嘉宾：言大侠 14 年新媒体运营老兵、脱口秀吐槽小会：10天涨粉5.6w小红书粉丝，2周开发1个小程序卖10万，都踩了什么坑", "Khách mời đặc biệt: Ngôn Đại Hiệp, cựu binh vận hành truyền thông mới 14 năm, hội nhỏ talk show roast: 10 ngày tăng 56.000 fan Xiaohongshu, 2 tuần phát triển 1 mini app bán 100.000, đã giẫm phải những bẫy gì"),
        ("【提示未来】赛事解读", "[Gợi ý tương lai] Giải mã cuộc thi"),
        ("社区第一本书【AI绘画极简入门与应用】正式上线", "Cuốn sách đầu tiên của cộng đồng [Nhập môn tối giản và ứng dụng AI vẽ] chính thức ra mắt"),
        ("主题赛​", "Cuộc thi chủ đề"),
        ("训练营第一期 第三课n8n​商单case拆解，带你搭建复杂工作流系统​", "Khóa đào tạo kỳ 1 bài 3 n8n phân tích case đơn hàng thương mại, dẫn bạn xây dựng hệ thống workflow phức tạp"),
        ("「AI训练营」第二课主题：常见#n8n 自动化工作流案例", "\"Khóa đào tạo AI\" bài 2 chủ đề: Các trường hợp workflow tự động hóa #n8n phổ biến"),
        ("4天吃透n8n工作流！WaytoAGI「AI训练营」第一期开营！", "4 ngày thông thạo workflow n8n! WaytoAGI \"Khóa đào tạo AI\" kỳ 1 khai giảng!"),
        ("「未来硅世界」第四期：AI Agent时代，搜索不再为人而生🔍", "\"Thế giới Silicon Tương lai\" kỳ 4: Thời đại AI Agent, tìm kiếm không còn dành cho con người"),
        ("我的AI创业收入清单和AI创业故事💡", "Danh sách thu nhập khởi nghiệp AI và câu chuyện khởi nghiệp AI của tôi"),
        ("拆解AI时代的学习路径与信息差", "Phân tích lộ trình học tập và khoảng cách thông tin trong thời đại AI"),
        ("10-04 | 0-1极速入门 AI·绘画篇", "10-04 | Nhập môn siêu tốc 0-1 AI - Phần vẽ"),
        ("如何和大语言模型进行对话？（0基础小白极速入门版）", "Làm thế nào trò chuyện với mô hình ngôn ngữ lớn? (Phiên bản nhập môn siêu tốc cho người mới)"),
        ("短剧大赛：现场编写·现场投稿·现场展示", "Cuộc thi phim ngắn: Viết tại chỗ - Nộp tại chỗ - Trình bày tại chỗ"),
        ("10-01 | Sora2实测，邀请码接力，", "10-01 | Thử nghiệm thực tế Sora2, chuyền tiếp mã mời,"),
        ("切磋大会全国会议", "Hội nghị giao lưu toàn quốc"),
        ("导演大赛创作分享​🌟特邀嘉宾冰鱼仔、素语、言带你解锁 百度智能创作平台 AI 导演体验，干货满满！", "Chia sẻ sáng tạo cuộc thi đạo diễn. Khách mời đặc biệt Băng Ngư Tử, Tố Ngữ, Ngôn dẫn bạn mở khóa trải nghiệm đạo diễn AI nền tảng sáng tạo thông minh Baidu, đầy ắp kiến thức!"),
        ("​WaytoAGI晚8点共学", "WaytoAGI học chung lúc 8 giờ tối"),
        ("10万奖池比赛解说，百度AI追热季 AI・生存・宇宙故事创作视频挑战赛开启！", "Giải thuyết cuộc thi quỹ giải thưởng 100.000, Baidu AI mùa theo trend AI - Sinh tồn - Cuộc thi thách thức sáng tạo video câu chuyện vũ trụ khai mạc!"),
        ("#TrickleAI 编程赛火热开启！大奖是iPhone 17 Pro Max  歸藏 /向阳联合教学：Trickle 是一个无缝衔接多模态生成的 Vibe Coding 工具，好上手又强大", "#TrickleAI Cuộc thi lập trình nóng bỏng khai mạc! Giải lớn là iPhone 17 Pro Max. Quy Tàng / Hướng Dương giảng dạy liên hợp: Trickle là một công cụ Vibe Coding tạo đa phương thức liền mạch, dễ dùng lại mạnh mẽ"),
        ("导演大赛🌟工程师深度拆解「百度智能视频创作」玩法", "Cuộc thi đạo diễn. Kỹ sư phân tích sâu cách chơi \"Sáng tạo video thông minh Baidu\""),
        ("飞书多维表格接入即梦4.0，今晚王大仙教你玩出花", "Bảng đa chiều Feishu kết nối JiMeng 4.0, tối nay Vương Đại Tiên dạy bạn chơi sáng tạo"),
        ("百度世界 × 小红书科技联合呈现秒哒黑客松大赛权威解读", "Baidu World x Xiaohongshu Tech trình bày liên hợp giải mã cuộc thi hackathon MiaoDa"),
        ("从 0 到 1 部署正式网站！零基础也能玩转 AI 编程", "Triển khai website chính thức từ 0 đến 1! Không nền tảng cũng chơi được lập trình AI"),
        ("用Cursor+Zion搭建AI应用MVP 即刻变现!", "Dùng Cursor+Zion xây dựng MVP ứng dụng AI kiếm tiền ngay!"),
        ("智能体工作流设计模式教学，", "Giảng dạy mẫu thiết kế workflow Agent thông minh,"),
        ("拆解AI摆摊实验，提炼「商业落地金字塔」完整框架", "Phân tích thí nghiệm bán hàng AI, đúc kết framework hoàn chỉnh \"Kim tự tháp thương mại hóa\""),
        ("Qoder食用说明书：从入门到惊艳", "Hướng dẫn sử dụng Qoder: Từ nhập môn đến kinh ngạc"),
        ("阿里云百炼 AI Agent 创客开发实战课 讲师：许键", "Khóa thực chiến phát triển maker AI Agent Alibaba Cloud Bailian. Giảng viên: Xu Jian"),
        ("X百万流量，最全NanoBanana指南", "Triệu lưu lượng X, hướng dẫn NanoBanana toàn diện nhất"),
        ("全面盘点Vibe Coding工具，选对工具效率翻倍！主持人：Ben", "Tổng kết toàn diện công cụ Vibe Coding, chọn đúng công cụ hiệu quả gấp đôi! Người chủ trì: Ben"),
        ("解锁 Qwen-Image 技术秘籍与创作灵感！", "Mở khóa bí kíp kỹ thuật và cảm hứng sáng tạo Qwen-Image!"),
        ("最强生图模型？nano banana实测 ！", "Mô hình tạo ảnh mạnh nhất? Thử nghiệm thực tế nano banana!"),
        ("社区伦敦亮相+workshop直播-", "Cộng đồng xuất hiện tại London + livestream workshop -"),
        ("今晚8点！鹿演Vol.004：OpenCreator-内容创作者的一站式画布", "Tối nay 8 giờ! Lộc Diễn Vol.004: OpenCreator - Canvas một cửa cho nhà sáng tạo nội dung"),
        ("鹿演Vol.003：ListenHub：能帮创作者赚钱的AI嘴替", "Lộc Diễn Vol.003: ListenHub: AI thay lời giúp nhà sáng tạo kiếm tiền"),
        ("娜乌斯佳：AI视频最新教程，我AI北京大赛分享", "Nausica: Hướng dẫn mới nhất video AI, tôi chia sẻ cuộc thi AI Bắc Kinh"),
        ("视频教程08-13 | 一句话让创意到变现的超级工具箱，秒哒使用指南", "Video hướng dẫn 08-13 | Hộp công cụ siêu cấp biến sáng tạo thành kiếm tiền chỉ với một câu, hướng dẫn sử dụng MiaoDa"),
        ("共学", "Học chung"),
        ("一个人如何用AI完成一部动画 - 【瑞克和莫蒂勇闯刻板印象宇宙】", "Một người dùng AI hoàn thành một bộ hoạt hình như thế nào - [Rick và Morty dũng cảm xông vào vũ trụ khuôn mẫu]"),
        ("开源很可能带来\"第二波商业化红利\"，一起探讨，找到属于你的机遇！", "Mã nguồn mở rất có thể mang lại \"làn sóng thương mại hóa thứ hai\", cùng thảo luận, tìm cơ hội thuộc về bạn!"),
        ("08-02 | Vibe Coding 迷你黑客松_奇思妙想秀-", "08-02 | Vibe Coding Mini hackathon_Show ý tưởng sáng tạo -"),
        ("月入万刀的Agent开发者经验分享， Myshell手把手搭建，", "Chia sẻ kinh nghiệm nhà phát triển Agent thu nhập vạn đô/tháng, cầm tay xây dựng Myshell,"),
        ("+应用创作第一课：百度秒哒\"一句话建应用\"实战课", "+ Bài 1 sáng tạo ứng dụng: Khóa thực chiến \"Một câu tạo ứng dụng\" Baidu MiaoDa"),
        ("玩转扣子空间 网页设计新功能上线", "Sử dụng thành thạo Coze Space, tính năng thiết kế web mới ra mắt"),
        ("开源多模态Agent工具首发", "Ra mắt lần đầu công cụ Agent đa phương thức mã nguồn mở"),
        ("助手带你玩转数据分析！通义灵码保姆级教学 -", "Trợ lý dẫn bạn chơi phân tích dữ liệu! Giảng dạy kiểu bảo mẫu Tongyi Lingma -"),
        ("创始人", "Nhà sáng lập"),
    ]

    for cn, vi in phrases:
        t = t.replace(cn, vi)

    return t


# Apply translations
trans_data = copy.deepcopy(data)
total_text = 0
translated_count = 0
kept_count = 0

for block in trans_data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run':
            total_text += 1
            orig = el['content']
            if CN_PAT.search(orig):
                # First try exact match from FULL_MAP
                if orig in FULL_MAP:
                    el['content'] = FULL_MAP[orig]
                    translated_count += 1
                else:
                    # Try minutes translation
                    translated = translate_minutes_text(orig)
                    el['content'] = translated
                    if not CN_PAT.search(translated):
                        translated_count += 1
                    else:
                        kept_count += 1
                        remaining = ''.join(CN_PAT.findall(translated))
                        print(f"REMAIN [{block['block_id'][:12]}]: {remaining[:40]}...")
            else:
                kept_count += 1

print(f"\nStats: total={total_text}, translated={translated_count}, kept_unchanged={kept_count}")

with open('_art22_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans_data, f, ensure_ascii=False, indent=2)

print("Saved _art22_trans.json")
