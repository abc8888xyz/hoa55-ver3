# -*- coding: utf-8 -*-
"""Translate art19 - OpenClaw technical architecture livestream"""
import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('_art19_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

# Translation map for this article
T = {
    # Page title
    "02-24直播回放 | 🦞来新璐带大家把OpenClaw技术架构拆解，还能手搓一个最小的龙虾 WaytoAGI晚8点共学 2026年2月24日":
        "02-24 Phát lại livestream | 🦞Lai Xinlu dẫn mọi người phân tích kiến trúc kỹ thuật OpenClaw, còn có thể tự tay làm một con tôm hùm tối giản WaytoAGI Cùng học lúc 8 giờ tối ngày 24 tháng 2 năm 2026",

    "会议主题：02-24 | 🦞来新璐带大家把OpenClaw技术架构拆解，还能手搓一个最小的龙虾 WaytoAGI晚8点共学":
        "Chủ đề cuộc họp: 02-24 | 🦞Lai Xinlu dẫn mọi người phân tích kiến trúc kỹ thuật OpenClaw, còn có thể tự tay làm một con tôm hùm tối giản WaytoAGI Cùng học lúc 8 giờ tối",

    "会议时间：2026年2月24日（周二） 19:55 - 22:29 （GMT+08）":
        "Thời gian cuộc họp: Ngày 24 tháng 2 năm 2026 (Thứ Ba) 19:55 - 22:29 (GMT+08)",

    "视频回放：": "Video phát lại:",
    "上两期直播回放：": "Phát lại hai kỳ livestream trước:",

    "01-25 | 🧑‍💻手把手带你玩转开源版Claude Code——Kode Agent":
        "01-25 | 🧑‍💻Hướng dẫn từng bước chơi phiên bản mã nguồn mở Claude Code — Kode Agent",

    "01-24 | 深度解析 Claude Code 原理&机制设计，以及教你从 0 到 1 手搓一个迷你 Claude Code":
        "01-24 | Phân tích chuyên sâu nguyên lý & thiết kế cơ chế Claude Code, cùng hướng dẫn bạn tự tay làm một Claude Code mini từ 0 đến 1",

    "总结": "Tổng kết",

    "本次会议由来新璐分享 Openclaw 相关知识，包括其发展历程、技术架构、核心机制、部署方法等内容，还探讨了记忆系统、应用场景及存在的问题，为参会者深入了解和使用 Openclaw 提供了指导，内容如下：":
        "Cuộc họp lần này do Lai Xinlu chia sẻ kiến thức liên quan đến Openclaw, bao gồm lịch sử phát triển, kiến trúc kỹ thuật, cơ chế cốt lõi, phương pháp triển khai, đồng thời thảo luận về hệ thống bộ nhớ, kịch bản ứng dụng và các vấn đề tồn tại, cung cấp hướng dẫn cho người tham gia hiểu sâu và sử dụng Openclaw, nội dung như sau:",

    "Openclaw 概述": "Tổng quan Openclaw",
    "发展背景与优势": "Bối cảnh phát triển và ưu thế",

    "发展历程：Openclaw 从最初到现在历经三次改名，创始人最终确定了现用名。此前其创始人还通过播客分享了心路历程和自身背景。":
        "Lịch sử phát triển: Openclaw từ ban đầu đến nay đã trải qua ba lần đổi tên, nhà sáng lập cuối cùng đã xác định tên hiện tại. Trước đó, nhà sáng lập cũng đã chia sẻ hành trình tâm lý và nền tảng cá nhân qua podcast.",

    "使用优势：AJ 表示，Openclaw 的优势在于其方式方法能让 AI agent 更贴近用户，可安装在手机端。他以自身经历举例，过去出门需携带沉重电脑处理任务，如今可在手机上遥控 AI 操控虚拟机，使用起来更加方便。":
        "Ưu thế sử dụng: AJ cho biết, ưu thế của Openclaw nằm ở phương pháp giúp AI agent gần gũi hơn với người dùng, có thể cài đặt trên điện thoại. Anh ấy lấy ví dụ từ kinh nghiệm bản thân, trước đây ra ngoài phải mang theo máy tính nặng để xử lý công việc, giờ đây có thể điều khiển AI từ xa trên điện thoại để vận hành máy ảo, sử dụng thuận tiện hơn nhiều.",

    "行业影响：AJ 认为，今年会出现范式的改变和转移，各行业的 AI 渗透率可能由普通从业者推动，而非开发工程师。例如，Claude code 一周年线下活动的黑客松比赛中，第一名和第三名是医生和律师等非代码经验从业者，他们凭借行业技能和经验，结合低门槛的 AI 技术完成任务。":
        "Tác động ngành: AJ cho rằng, năm nay sẽ xuất hiện sự thay đổi và chuyển dịch mô hình, tỷ lệ thâm nhập AI trong các ngành có thể được thúc đẩy bởi người hành nghề phổ thông, chứ không phải kỹ sư phát triển. Ví dụ, trong cuộc thi hackathon kỷ niệm một năm Claude Code, giải nhất và giải ba là bác sĩ và luật sư - những người không có kinh nghiệm lập trình, họ dựa vào kỹ năng và kinh nghiệm ngành kết hợp với công nghệ AI dễ tiếp cận để hoàn thành nhiệm vụ.",

    "微图一摘的目标": "Mục tiêu của WaytoAGI",
    "：微图一摘希望更多人学习 Openclaw 技术，该技术并非难以掌握。如与一个搞 AI 视频的小伙伴交流，他原本未想过用命令行配置 Claude out code 和 Openclaw，但在 AJ 的指导下，通过向 AI 豆包、Gemini 等工具咨询，最终成功完成配置。":
        ": WaytoAGI hy vọng nhiều người hơn học công nghệ Openclaw, công nghệ này không khó nắm bắt. Ví dụ khi trao đổi với một bạn làm video AI, ban đầu bạn ấy chưa từng nghĩ đến việc dùng dòng lệnh để cấu hình Claude Code và Openclaw, nhưng dưới sự hướng dẫn của AJ, thông qua tham vấn các công cụ AI như Doubao, Gemini, cuối cùng đã hoàn thành cấu hình thành công.",

    "Openclaw 技术架构拆解": "Phân tích kiến trúc kỹ thuật Openclaw",
    "发展脉络梳理": "Sắp xếp mạch phát triển",

    "产品演变：来新璐回顾了相关产品的发展历程，去年先是 CC（Claude code）火爆，之后出现面向普通人的 coworker，接着涌现出大量 Openwork 项目，如 Opencode。小龙虾（Openclaw）最初叫 crowbot，后改名 opencrow，其心智主要集中在 BOT 场景。":
        "Tiến hóa sản phẩm: Lai Xinlu nhìn lại lịch sử phát triển sản phẩm liên quan, năm ngoái đầu tiên CC (Claude Code) bùng nổ, sau đó xuất hiện coworker hướng đến người thường, tiếp theo xuất hiện hàng loạt dự án Openwork như Opencode. Tôm hùm nhỏ (Openclaw) ban đầu tên là crowbot, sau đổi tên thành opencrow, tư duy chính tập trung vào kịch bản BOT.",

    "早期用户情况：去年 2 - 3 月，Claude code 和 Manus 发布，5 月中国出现一批早期用户，11 月大量非程序编码行业的普通用户开始使用 CC。在此过程中，社区出现了许多开源类的 agent 项目，如 cursor 曾被广泛使用，但因功能局限逐渐被 CC 淘汰。":
        "Tình hình người dùng sớm: Tháng 2-3 năm ngoái, Claude Code và Manus ra mắt, tháng 5 Trung Quốc xuất hiện một lượng người dùng sớm, tháng 11 nhiều người dùng phổ thông không thuộc ngành lập trình bắt đầu sử dụng CC. Trong quá trình này, cộng đồng xuất hiện nhiều dự án agent mã nguồn mở, như Cursor từng được sử dụng rộng rãi, nhưng do hạn chế chức năng dần bị CC thay thế.",

    "Openclaw 与其他产品关系：Openclaw 基于派 agent 框架，该框架是对 Opencode 或 CC 的最小化实现。来新璐所在团队去年 10 - 11 月编写的 learn cloud code 仓库，对如何手写一个简单版本的 CC 进行了心智拆解，派 agent 的实现与该仓库有一定关联。":
        "Mối quan hệ giữa Openclaw và các sản phẩm khác: Openclaw dựa trên framework Pydantic Agent, framework này là triển khai tối giản hóa của Opencode hoặc CC. Nhóm của Lai Xinlu viết kho learn cloud code vào tháng 10-11 năm ngoái, phân tích tư duy về cách viết tay một phiên bản đơn giản của CC, việc triển khai Pydantic Agent có liên quan nhất định với kho này.",

    "核心机制分析": "Phân tích cơ chế cốt lõi",
    "周期性任务机制（Cron）": "Cơ chế tác vụ định kỳ (Cron)",

    "主动性体现：Claude code 等是被动式 agent，而 Openclaw 是主动式 agent。Cron 机制是其主动性的重要体现，它支持模型通过工具调用操作系统，设置任务调度。":
        "Thể hiện tính chủ động: Claude Code và các agent khác là agent bị động, trong khi Openclaw là agent chủ động. Cơ chế Cron là thể hiện quan trọng của tính chủ động, nó hỗ trợ mô hình gọi hệ điều hành thông qua công cụ, thiết lập lịch trình tác vụ.",

    "任务类型：包括一次性任务（如设置特定时间的提醒）、周期性任务（如每天早上 10 点给用户惊喜）和特定时间触发任务。这些任务可由用户或 agent 主动设置，通过 crontab 机制触发 agent 执行。":
        "Loại tác vụ: Bao gồm tác vụ một lần (như đặt nhắc nhở vào thời gian cụ thể), tác vụ định kỳ (như mỗi sáng 10 giờ tạo bất ngờ cho người dùng) và tác vụ kích hoạt theo thời gian cụ thể. Các tác vụ này có thể được người dùng hoặc agent chủ động thiết lập, thông qua cơ chế crontab kích hoạt agent thực thi.",

    "内部设计实现：Cron 机制有三层任务抽象设计，分别是指定时间点运行一次的任务、周期性执行的任务和纯表达式任务。通过这些机制，agent 可自动执行后台任务，如总结推特内容、读取开源代码仓库的 issues 等。":
        "Triển khai thiết kế nội bộ: Cơ chế Cron có thiết kế trừu tượng tác vụ ba lớp, lần lượt là tác vụ chạy một lần tại thời điểm chỉ định, tác vụ thực thi định kỳ và tác vụ biểu thức thuần túy. Thông qua các cơ chế này, agent có thể tự động thực thi tác vụ nền, như tóm tắt nội dung Twitter, đọc issues của kho mã nguồn mở, v.v.",

    "心跳机制（Heartbeat）": "Cơ chế nhịp tim (Heartbeat)",

    "机制含义：来新璐认为，心跳机制是 agent 在用户未主动发起任务时，能自己产生想法并给自己发送消息，主动处理一些认为有必要的工作。它依赖定时器，默认每 30 秒执行一次。":
        "Ý nghĩa cơ chế: Lai Xinlu cho rằng, cơ chế nhịp tim là khi người dùng không chủ động khởi tạo tác vụ, agent có thể tự tạo ý tưởng và gửi tin nhắn cho chính mình, chủ động xử lý một số công việc cần thiết. Nó dựa vào bộ đếm thời gian, mặc định thực thi mỗi 30 giây.",

    "实现方式：心跳机制通过向 agent 发送包含心跳点 MD 文档内容的消息来实现。该文档记录了周期性任务和提醒信息，agent 根据返回结果决定是否在相应渠道给用户发送消息。":
        "Phương thức triển khai: Cơ chế nhịp tim thực hiện bằng cách gửi tin nhắn chứa nội dung tài liệu MD heartbeat đến agent. Tài liệu này ghi lại tác vụ định kỳ và thông tin nhắc nhở, agent dựa vào kết quả trả về quyết định có gửi tin nhắn cho người dùng trên kênh tương ứng hay không.",

    "相关注意事项：心跳机制涉及一些特定的 meta 信息，如激活时间段等。Openclaw 项目更新频繁，但主要机制变化不大，不过在使用国产模型时可能会出现幻觉问题，建议优先使用 Claude 模型。":
        "Lưu ý liên quan: Cơ chế nhịp tim liên quan đến một số thông tin meta cụ thể, như khoảng thời gian kích hoạt, v.v. Dự án Openclaw cập nhật thường xuyên, nhưng cơ chế chính thay đổi không nhiều, tuy nhiên khi sử dụng mô hình nội địa có thể xuất hiện vấn đề ảo giác, khuyến nghị ưu tiên sử dụng mô hình Claude.",

    "人格系统（": "Hệ thống nhân cách (",
    "）": ")",

    "解耦原理：来新璐指出，在传统的 cloud code 中，系统提示词包含大量信息。而 Openclaw 将系统提示词中的一部分，如 agent 的人格设定、信息设定和做事风格等，解耦出来形成 seal.md 文件。":
        "Nguyên lý tách rời: Lai Xinlu chỉ ra rằng, trong cloud code truyền thống, system prompt chứa lượng lớn thông tin. Openclaw tách một phần system prompt, như thiết lập nhân cách agent, thiết lập thông tin và phong cách làm việc, tách rời thành file seal.md.",

    '作用与意义：seal.md 文件类似于 agent 的\u201c灵魂\u201d，可在社区传播，用户可上传和下载。在启动 agent 时，会将其作为上下文的一部分加载到系统提示词中。不同的 agent 可对应不同的 seal，实现个性化配置。':
        'Vai trò và ý nghĩa: File seal.md tương tự "linh hồn" của agent, có thể lan truyền trong cộng đồng, người dùng có thể tải lên và tải xuống. Khi khởi động agent, nó sẽ được tải vào system prompt như một phần của ngữ cảnh. Các agent khác nhau có thể tương ứng với seal khác nhau, thực hiện cấu hình cá nhân hóa.',

    "记忆系统（memory）": "Hệ thống bộ nhớ (memory)",

    "现状分析：当前 Openclaw 的记忆系统设计较为薄弱，Claude code 等 agent 的记忆机制也较浅，主要服务于临时任务。来新璐认为，Openclaw 的记忆系统越设计越复杂，不太喜欢当前的设计，更倾向于回归最初的纯 Markdown 文件系统。":
        "Phân tích hiện trạng: Hiện tại thiết kế hệ thống bộ nhớ của Openclaw khá yếu, cơ chế bộ nhớ của các agent như Claude Code cũng nông, chủ yếu phục vụ tác vụ tạm thời. Lai Xinlu cho rằng, hệ thống bộ nhớ của Openclaw càng thiết kế càng phức tạp, không thích thiết kế hiện tại, thiên về quay lại hệ thống file Markdown thuần túy ban đầu.",

    "推荐项目：推荐参考 memoryu 和 Openviking 项目的设计理念。memoryu 采用 Unix style 的文件哲学维护记忆系统，设计优雅；Openviking 是字节开源的项目，适合生产级，设计大而全。":
        "Dự án khuyến nghị: Khuyến nghị tham khảo lý niệm thiết kế của dự án memoryu và Openviking. memoryu áp dụng triết lý file kiểu Unix để duy trì hệ thống bộ nhớ, thiết kế thanh lịch; Openviking là dự án mã nguồn mở của ByteDance, phù hợp cấp sản xuất, thiết kế toàn diện.",

    "系统提示词构建：系统提示词由人格（seal.md）、硬编码信息和最近的记忆拼接而成，将人格信息放在前面可利用模型训练时对初始 TOKEN 注意力分数高的特点。":
        "Xây dựng system prompt: System prompt được ghép từ nhân cách (seal.md), thông tin hard-code và bộ nhớ gần đây, đặt thông tin nhân cách lên trước để tận dụng đặc điểm điểm attention cao của TOKEN đầu tiên khi huấn luyện mô hình.",

    "Openclaw 部署与应用": "Triển khai và ứng dụng Openclaw",
    "部署方法": "Phương pháp triển khai",

    "借助已有 agent 安装：来新璐分享了部署 Openclaw 的经验，可先在电脑上安装 Claude code 或其他国产版 Claude code 等 agent，然后通过 NPM 安装 Openclaw 包。也可让已有 agent 帮助安装，告知其 API key 等信息，让其自动完成部署。":
        "Cài đặt nhờ agent có sẵn: Lai Xinlu chia sẻ kinh nghiệm triển khai Openclaw, có thể cài đặt trước Claude Code hoặc các agent phiên bản nội địa khác trên máy tính, sau đó cài đặt gói Openclaw qua NPM. Cũng có thể để agent có sẵn hỗ trợ cài đặt, cung cấp thông tin API key, v.v., để nó tự động hoàn thành triển khai.",

    "飞书部署问题：在飞书部署 Openclaw 较为复杂，需要创建企业自建应用，复制 API ID 和 API key，开通权限，设置事件订阅等。来新璐在部署过程中遇到了添加事件订阅时加号无法点击的问题，最终通过先发布应用，再发送事件建立连接后才解决。":
        "Vấn đề triển khai Lark: Triển khai Openclaw trên Lark khá phức tạp, cần tạo ứng dụng tự xây dựng doanh nghiệp, sao chép API ID và API key, kích hoạt quyền, thiết lập đăng ký sự kiện, v.v. Lai Xinlu gặp vấn đề nút cộng không thể nhấn khi thêm đăng ký sự kiện trong quá trình triển khai, cuối cùng giải quyết bằng cách phát hành ứng dụng trước, sau đó gửi sự kiện thiết lập kết nối.",

    "不同平台比较：Telegram 部署 Openclaw 最简单，只需一个 TOKEN 即可关联 BOT；Discord 部署也较麻烦，来新璐尝试一半后放弃。":
        "So sánh các nền tảng khác nhau: Triển khai Openclaw trên Telegram đơn giản nhất, chỉ cần một TOKEN là có thể liên kết BOT; triển khai Discord cũng khá phiền phức, Lai Xinlu thử được nửa chừng rồi bỏ cuộc.",

    "应用场景与体验": "Kịch bản ứng dụng và trải nghiệm",

    "本地部署优势：来新璐认为，将 Openclaw 部署在本地电脑上，能访问本地数据，可完成清理文件、优化电池策略、查询黄金价格并绘制图表等任务，而部署在云端则与 Manus 等产品功能类似，缺乏本地数据访问能力。":
        "Ưu thế triển khai cục bộ: Lai Xinlu cho rằng, triển khai Openclaw trên máy tính cục bộ có thể truy cập dữ liệu cục bộ, hoàn thành các tác vụ như dọn dẹp file, tối ưu chiến lược pin, tra cứu giá vàng và vẽ biểu đồ, trong khi triển khai trên đám mây thì tương tự các sản phẩm như Manus, thiếu khả năng truy cập dữ liệu cục bộ.",

    "功能局限性：当前 Openclaw 的交互性存在一定局限，如使用纯文本模态模型时，无法进行截图和全局应用操作，需要配置扩展的截图方案和浏览器自动化方案才能增强其功能。":
        "Hạn chế chức năng: Hiện tại tính tương tác của Openclaw có một số hạn chế, như khi sử dụng mô hình thuần văn bản, không thể chụp ảnh màn hình và thao tác ứng dụng toàn cục, cần cấu hình giải pháp chụp ảnh mở rộng và giải pháp tự động hóa trình duyệt để nâng cao chức năng.",

    "Openclaw 项目现状与未来展望": "Hiện trạng và triển vọng tương lai dự án Openclaw",

    "项目更新情况": "Tình hình cập nhật dự án",
    "：来新璐提到，Openclaw 项目更新非常迅速，一周内可能有近 5000 个 commit。但由于更新速度过快，可能导致一些问题，如出现莫名其妙的 bug，作者可能无法及时 review 代码，部分代码可能由 agent 编写并直接合并。":
        ": Lai Xinlu đề cập, dự án Openclaw cập nhật rất nhanh, trong một tuần có thể có gần 5000 commit. Nhưng do tốc độ cập nhật quá nhanh, có thể dẫn đến một số vấn đề, như xuất hiện bug khó hiểu, tác giả có thể không kịp review code, một phần code có thể do agent viết và merge trực tiếp.",

    "未来发展方向": "Hướng phát triển tương lai",
    "：虽然当前 Openclaw 存在一些问题，但如果未来更新更多更好的特性，值得保持关注。后续还将举办 Openclaw 训练营，邀请崟海和 CY 参加，CY 会携带硬件，让参与者进行组装，探索更多应用场景。":
        ": Mặc dù hiện tại Openclaw còn một số vấn đề, nhưng nếu tương lai cập nhật thêm nhiều tính năng tốt hơn, đáng để tiếp tục theo dõi. Sau đó còn sẽ tổ chức trại huấn luyện Openclaw, mời Yinhai và CY tham gia, CY sẽ mang theo phần cứng, để người tham gia lắp ráp, khám phá thêm nhiều kịch bản ứng dụng.",

    "问答与互动环节": "Phần hỏi đáp và tương tác",

    "Facetime 通话测试": "Kiểm tra cuộc gọi Facetime",
    "：来新璐在直播中进行了 Facetime 通话测试，尝试让 Openclaw 调用 Facetime 拨打电话。在测试过程中遇到了一些问题，如自己给自己打电话可能无法接通，需要拨打他人号码。最终成功拨通网友电话，实现了互动连线。":
        ": Lai Xinlu đã thực hiện kiểm tra cuộc gọi Facetime trong livestream, thử để Openclaw gọi Facetime. Trong quá trình kiểm tra gặp một số vấn đề, như tự gọi cho mình có thể không kết nối được, cần gọi số người khác. Cuối cùng đã gọi thành công cho một khán giả, thực hiện kết nối tương tác.",

    "输入法与模型使用": "Bàn phím gõ và sử dụng mô hình",
    "：来新璐使用智谱的 GLM - M5 模型，搭配政府的 coding plan，认为该模型够用但不如 cloud 模型。同时提到使用的语音输入法准确率一般，存在错别字问题。":
        ": Lai Xinlu sử dụng mô hình GLM-M5 của Zhipu, kết hợp với coding plan, cho rằng mô hình này đủ dùng nhưng không bằng mô hình Cloud. Đồng thời đề cập bàn phím giọng nói đang sử dụng có độ chính xác trung bình, tồn tại vấn đề lỗi chính tả.",

    "安全性问题": "Vấn đề bảo mật",
    "：来新璐强调，部署 Openclaw 在本地电脑上虽然能获得更多权限，但也存在安全风险，如差点误删甲方的数据集文件。因此，在使用时需要谨慎，做好安全隔离和资源隔离。":
        ": Lai Xinlu nhấn mạnh, triển khai Openclaw trên máy tính cục bộ tuy có thể được nhiều quyền hơn, nhưng cũng tồn tại rủi ro bảo mật, như suýt xóa nhầm file dataset của khách hàng. Do đó, khi sử dụng cần cẩn thận, làm tốt cách ly bảo mật và cách ly tài nguyên.",

    "后续工作计划": "Kế hoạch công việc tiếp theo",

    "仓库代码优化": "Tối ưu mã nguồn kho",
    "：来新璐表示，直播结束后会对克劳 0 仓库的代码进行优化，使其更加简洁清晰。":
        ": Lai Xinlu cho biết, sau khi livestream kết thúc sẽ tối ưu code của kho Claw 0, làm cho nó gọn gàng và rõ ràng hơn.",

    "飞书实现扩展": "Mở rộng triển khai Lark",
    "：计划在克劳 0 仓库中添加飞书的实现，方便用户在飞书机器人上直接使用。":
        ": Kế hoạch thêm triển khai Lark vào kho Claw 0, thuận tiện cho người dùng sử dụng trực tiếp trên bot Lark.",

    "Openclaw 训练营": "Trại huấn luyện Openclaw",
    "：后续将举办 Openclaw 训练营，邀请崟海和 CY 参与，CY 会携带硬件，让参与者进行组装，探索更多 Openclaw 的应用场景。":
        ": Sau đó sẽ tổ chức trại huấn luyện Openclaw, mời Yinhai và CY tham gia, CY sẽ mang theo phần cứng, để người tham gia lắp ráp, khám phá thêm nhiều kịch bản ứng dụng của Openclaw.",

    "待办": "Việc cần làm",

    "直播稿分享：发送火山引擎 Open Viking 项目的直播稿，分享项目设计理念和哲学":
        "Chia sẻ bản thảo livestream: Gửi bản thảo livestream dự án Open Viking của Volcano Engine, chia sẻ lý niệm thiết kế và triết lý dự án",

    "知识库发送：将微推荐的大知识库发送给大家，知识库中有两期内容，重点参考第一期的讲解内容（来自来新璐） ":
        "Gửi kho kiến thức: Gửi kho kiến thức lớn được WaytoAGI khuyến nghị cho mọi người, kho kiến thức có hai kỳ nội dung, trọng tâm tham khảo nội dung giảng giải kỳ đầu tiên (từ Lai Xinlu) ",

    "飞书功能扩展：在 Monica 代码中扩展飞书的实现，以便将仓库代码直接运行在飞书机器人上进行演示，避免重新配置权限":
        "Mở rộng chức năng Lark: Mở rộng triển khai Lark trong code Monica, để có thể chạy trực tiếp code kho trên bot Lark để demo, tránh phải cấu hình lại quyền",

    "飞书部署建议：向飞书团队提出建议，能否像 TG 一样，使用一个 TOKEN 即可部署一个 BOT，以简化部署流程（来自来新璐） ":
        "Đề xuất triển khai Lark: Đề xuất với đội ngũ Lark, liệu có thể giống TG, sử dụng một TOKEN là có thể triển khai một BOT, để đơn giản hóa quy trình triển khai (từ Lai Xinlu) ",

    "直播回放发送：将本次直播回放发给所有参会人员，其中包含所有文字内容，供大家参考学习 Openclaw 原理及 setup 方法 ":
        "Gửi phát lại livestream: Gửi phát lại livestream lần này cho tất cả người tham gia, trong đó chứa toàn bộ nội dung văn bản, để mọi người tham khảo học tập nguyên lý Openclaw và phương pháp setup ",

    "智能章节": "Chương thông minh",

    # Timestamp sections
    "02:05": "02:05",
    "  开场": "  Khai mạc",
    "开场": "Khai mạc",

    "10:00": "10:00",
    "  技术工具热度转换及开源项目介绍": "  Chuyển đổi độ phổ biến công cụ kỹ thuật và giới thiệu dự án mã nguồn mở",

    "本章节由来新璐发言，她表示要带大家了解相关内容，很多同学没部署过也不知其用途。她自己并非早期用户，起初觉得龙虾能力类似Claude code等，后来深入使用才意识到不同。还复盘了近三个月热度转换，去年CC火后推出coworker，之后出现Openwork项目，coworker前后有开源项目Opencode，还曾讲过写其开源版的方法。":
        "Chương này do Lai Xinlu phát biểu, cô ấy cho biết sẽ dẫn mọi người tìm hiểu nội dung liên quan, nhiều bạn chưa từng triển khai và không biết công dụng. Bản thân cô ấy không phải người dùng sớm, ban đầu nghĩ năng lực tôm hùm tương tự Claude Code, sau khi sử dụng sâu mới nhận ra sự khác biệt. Còn phân tích lại sự chuyển đổi độ phổ biến ba tháng gần đây, năm ngoái CC nổi rồi ra mắt coworker, sau đó xuất hiện dự án Openwork, trước sau coworker có dự án mã nguồn mở Opencode, còn từng giảng về cách viết phiên bản mã nguồn mở.",

    "12:11": "12:11",
    "  小龙虾等项目发展历程及相关仓库情况": "  Lịch sử phát triển dự án tôm hùm nhỏ và tình hình kho liên quan",

    "本章节主要围绕小龙虾项目及相关产品展开。小龙虾历经改名，心智集中在 BOT 场景。回顾去年，Claude code、Manus 发布，5月起程序员使用，11月普通用户也开始用。CURSOR 因功能局限被 CC 淘汰，open crawl 基于派 agent 框架，该框架或受 learn cloud code 仓库影响，约等于 CC 的最小化实现。":
        "Chương này chủ yếu xoay quanh dự án tôm hùm nhỏ và các sản phẩm liên quan. Tôm hùm nhỏ trải qua nhiều lần đổi tên, tư duy tập trung vào kịch bản BOT. Nhìn lại năm ngoái, Claude Code, Manus ra mắt, từ tháng 5 lập trình viên sử dụng, tháng 11 người dùng phổ thông cũng bắt đầu dùng. CURSOR do hạn chế chức năng bị CC thay thế, open crawl dựa trên framework Pydantic Agent, framework này có thể chịu ảnh hưởng từ kho learn cloud code, xấp xỉ triển khai tối giản hóa CC.",

    "16:40": "16:40",
    "  OpenCrowd项目中Agent主动机制及任务调度解析": "  Phân tích cơ chế chủ động Agent và lịch trình tác vụ trong dự án OpenCrowd",

    "本章节围绕open cloud agent展开，指出其火热源于agent以外的机制。重点介绍了Cron机制，它是主动式agent，与以往被动、临时的agent不同。Cron有一次性、周期性等任务类型，支持模型工具调用设置任务。还提及Opencrow项目中任务的三层抽象设计，可实现agent主动设置任务及后台学习等功能。":
        "Chương này xoay quanh open cloud agent, chỉ ra sự phổ biến của nó bắt nguồn từ cơ chế ngoài agent. Trọng tâm giới thiệu cơ chế Cron, đây là agent chủ động, khác với agent bị động, tạm thời trước đây. Cron có các loại tác vụ một lần, định kỳ, v.v., hỗ trợ gọi công cụ mô hình thiết lập tác vụ. Còn đề cập thiết kế trừu tượng ba lớp tác vụ trong dự án Opencrow, có thể thực hiện agent chủ động thiết lập tác vụ và học tập nền, v.v.",

    "28:00": "28:00",
    "  OpenCrowd心跳机制及模型使用与成本探讨": "  Cơ chế nhịp tim OpenCrowd và thảo luận sử dụng mô hình và chi phí",

    "本章节主要介绍 Heartbeat 机制。可在 GitHub 搜 crowd 0 查看相关仓库，其文档后续会扩充语言、简化内容。Heartbeat 即心跳，是周期性机制，每 30 秒让 agent 自我检查、主动工作。还提到部署建议、模型选择，指出可复用订阅降低成本，小龙虾项目因历史原因未替换 agent car。":
        "Chương này chủ yếu giới thiệu cơ chế Heartbeat. Có thể tìm trên GitHub crowd 0 để xem kho liên quan, tài liệu sau này sẽ mở rộng ngôn ngữ, đơn giản hóa nội dung. Heartbeat tức nhịp tim, là cơ chế định kỳ, mỗi 30 giây để agent tự kiểm tra, chủ động làm việc. Còn đề cập đề xuất triển khai, lựa chọn mô hình, chỉ ra có thể tái sử dụng đăng ký để giảm chi phí, dự án tôm hùm nhỏ vì lý do lịch sử chưa thay thế agent car.",

    "54:43": "54:43",
    "  小虾项目人格系统及技能文档解耦解析": "  Phân tích hệ thống nhân cách và tách rời tài liệu kỹ năng dự án tôm nhỏ",

    "本章节主要介绍了Pro的两个主要机制之一，即人格系统。它是将系统提示词中的一部分，如agent的人格、价值观等信息拆出成seal点MD文档。这与之前流行的agent skill类似，都是上下文的固定或标准化策略。还提及不同工具修改system prompt的方式不同，最后谈到本地小模型的弊端及TOKEN用量增加等情况。":
        "Chương này chủ yếu giới thiệu một trong hai cơ chế chính của Pro, tức hệ thống nhân cách. Nó tách một phần system prompt, như nhân cách, giá trị quan của agent thành tài liệu seal.md. Điều này tương tự agent skill phổ biến trước đây, đều là chiến lược cố định hoặc chuẩn hóa ngữ cảnh. Còn đề cập các công cụ khác nhau sửa system prompt theo cách khác nhau, cuối cùng nói về hạn chế của mô hình nhỏ cục bộ và tình trạng tăng lượng sử dụng TOKEN.",

    "01:05:49": "01:05:49",
    "  Agent记忆系统设计及开源项目情况探讨": "  Thảo luận thiết kế hệ thống bộ nhớ Agent và tình hình dự án mã nguồn mở",

    "本章节主要围绕记忆部分展开，指出cloud code等的agent记忆设计薄弱，多服务临时任务。介绍了学习cloud code仓库新增章节，包括agent团队、任务系统等高级特性，还提到OpenCrow等项目局限。推荐了火山引擎的OpenViking和memoryu开源项目，认为记忆设计应大道至简，还阐述了系统提示词构建及心跳机制。":
        "Chương này chủ yếu xoay quanh phần bộ nhớ, chỉ ra thiết kế bộ nhớ agent của cloud code yếu, chủ yếu phục vụ tác vụ tạm thời. Giới thiệu chương mới của kho learn cloud code, bao gồm đội agent, hệ thống tác vụ và các tính năng nâng cao khác, còn đề cập hạn chế của dự án OpenCrow. Khuyến nghị dự án mã nguồn mở OpenViking của Volcano Engine và memoryu, cho rằng thiết kế bộ nhớ nên đại đạo chí giản, còn trình bày xây dựng system prompt và cơ chế nhịp tim.",

    "01:20:59": "01:20:59",
    "  小龙虾项目机制、通信适配及安全问题解析": "  Phân tích cơ chế dự án tôm hùm nhỏ, tương thích giao tiếp và vấn đề bảo mật",

    "本章节主要介绍小龙虾技术，包括与IM通信，如连接飞书、Telegram等，其中Telegram配agent最简单。还提到消息收发、渠道标记、多agent区分及上下文管理。指出小龙虾等于CC加周期性任务机制和心跳，同时强调使用时要平衡安全与功能，最后推荐memory u和Openviking用于改善记忆模块。":
        "Chương này chủ yếu giới thiệu công nghệ tôm hùm nhỏ, bao gồm giao tiếp với IM, như kết nối Lark, Telegram, v.v., trong đó Telegram cấu hình agent đơn giản nhất. Còn đề cập thu phát tin nhắn, đánh dấu kênh, phân biệt đa agent và quản lý ngữ cảnh. Chỉ ra tôm hùm nhỏ bằng CC cộng cơ chế tác vụ định kỳ và nhịp tim, đồng thời nhấn mạnh khi sử dụng cần cân bằng bảo mật và chức năng, cuối cùng khuyến nghị memory u và Openviking để cải thiện module bộ nhớ.",

    "01:38:29": "01:38:29",
    "  教学文档章节安排及仓库代码实现与应用介绍": "  Sắp xếp chương tài liệu giảng dạy và giới thiệu triển khai code kho và ứng dụng",

    "本章节由来新璐介绍教学文档相关内容，前三个section因与之前直播内容雷同性高不再讲解，主要涉及开发agent的基本知识概念。后续章节有对应代码实现，如简单agent loop、核心agent等，还提及消息机制处理、平台协议对接。之后表示会添加飞书实现，还谈到网关和解耦，以及如何区分不同用户使用不同agent。":
        "Chương này do Lai Xinlu giới thiệu nội dung liên quan đến tài liệu giảng dạy, ba section đầu do trùng lặp cao với nội dung livestream trước nên không giảng nữa, chủ yếu liên quan đến khái niệm kiến thức cơ bản phát triển agent. Các chương tiếp theo có triển khai code tương ứng, như agent loop đơn giản, agent cốt lõi, v.v., còn đề cập xử lý cơ chế tin nhắn, đối tiếp giao thức nền tảng. Sau đó cho biết sẽ thêm triển khai Lark, còn nói về gateway và tách rời, cũng như cách phân biệt người dùng khác nhau sử dụng agent khác nhau.",

    "01:41:01": "01:41:01",
    "  memory记忆拼接及人格文档前置设计原因": "  Ghép nối bộ nhớ memory và lý do thiết kế đặt tài liệu nhân cách lên trước",

    "本章节中，来新璐主要介绍了在memory中实现记忆偏好的记忆及定义人格文档的相关内容。启动时进行搜索并拼接，将soul点MD放最前，再拼硬编码信息、最近及常驻记忆，确保人格在前。虽前后放置对现有模型影响不大，但将其放前面有设计道理，因传统模型首个TOKEN注意力分数高。":
        "Trong chương này, Lai Xinlu chủ yếu giới thiệu nội dung liên quan đến triển khai bộ nhớ ưu tiên và định nghĩa tài liệu nhân cách trong memory. Khi khởi động thực hiện tìm kiếm và ghép nối, đặt soul.md lên đầu, tiếp theo ghép thông tin hard-code, bộ nhớ gần đây và bộ nhớ thường trú, đảm bảo nhân cách ở trước. Tuy việc đặt trước hay sau ảnh hưởng không lớn đến mô hình hiện tại, nhưng đặt lên trước có lý do thiết kế, vì mô hình truyền thống có điểm attention cao cho TOKEN đầu tiên.",

    "01:42:08": "01:42:08",
    "  飞书心跳机制、agent 隔离及任务层级介绍": "  Giới thiệu cơ chế nhịp tim Lark, cách ly agent và cấp bậc tác vụ",

    "本章节主要讨论了飞书与小龙虾通信的心跳问题，指出飞书心跳用于维护网络通信，小龙虾项目演化快会反复出现并修复小bug。还介绍了基于周期性任务每隔30秒的心跳机制，该机制与gateway绑定，不同agent相互隔离，有独立memory资源，最后提及可用正则表达式实现筛选机制及几种层级机制。":
        "Chương này chủ yếu thảo luận vấn đề nhịp tim giao tiếp giữa Lark và tôm hùm nhỏ, chỉ ra nhịp tim Lark dùng để duy trì giao tiếp mạng, dự án tôm hùm nhỏ phát triển nhanh sẽ liên tục xuất hiện và sửa bug nhỏ. Còn giới thiệu cơ chế nhịp tim mỗi 30 giây dựa trên tác vụ định kỳ, cơ chế này liên kết với gateway, các agent khác nhau cách ly lẫn nhau, có tài nguyên memory độc lập, cuối cùng đề cập có thể dùng biểu thức chính quy triển khai cơ chế lọc và một số cơ chế cấp bậc.",

    "01:44:11": "01:44:11",
    "  小龙虾消息通信的兜底机制及多实例特性": "  Cơ chế dự phòng giao tiếp tin nhắn tôm hùm nhỏ và đặc tính đa instance",

    "本章节主要围绕热更新及兜底机制展开。因网络抖动等情况，如坐高铁切换网络、过隧道等，可能导致消息中断、任务停止，需做兜底机制确保任务持续运转。该机制实现复杂度不高，且可在不同平台完成创建。目前发言者仅养了一只小龙虾，多个小龙虾的记忆、心跳和周期性任务执行相互隔离。":
        "Chương này chủ yếu xoay quanh cập nhật nóng và cơ chế dự phòng. Do tình trạng mạng không ổn định, như ngồi tàu cao tốc chuyển mạng, đi qua đường hầm, v.v., có thể dẫn đến gián đoạn tin nhắn, tác vụ dừng lại, cần làm cơ chế dự phòng đảm bảo tác vụ tiếp tục vận hành. Cơ chế này độ phức tạp triển khai không cao, và có thể tạo trên các nền tảng khác nhau. Hiện tại người phát biểu chỉ nuôi một con tôm hùm nhỏ, bộ nhớ, nhịp tim và thực thi tác vụ định kỳ của nhiều con tôm hùm nhỏ cách ly lẫn nhau.",

    "01:45:59": "01:45:59",
    "  直播仓库结构参考及项目问题解决建议": "  Tham khảo cấu trúc kho livestream và đề xuất giải quyết vấn đề dự án",

    "本章节中，来新璐提到网友可查看上一次直播回放和 learning cloud 仓库。本次直播教学仓库参考 17.6k star 仓库搭建。介绍了可参考 CLAW0 或 learn to code 创建开源项目，还提及教学顺序、agent 相关机制、skill 概念等，也指出小龙虾项目更新快维护混乱问题及上下文压缩策略需依模型调整。":
        "Trong chương này, Lai Xinlu đề cập khán giả có thể xem phát lại livestream lần trước và kho learning cloud. Kho giảng dạy livestream lần này tham khảo kho 17.6k star để xây dựng. Giới thiệu có thể tham khảo CLAW0 hoặc learn to code để tạo dự án mã nguồn mở, còn đề cập thứ tự giảng dạy, cơ chế liên quan agent, khái niệm skill, v.v., cũng chỉ ra vấn đề dự án tôm hùm nhỏ cập nhật nhanh bảo trì lộn xộn và chiến lược nén ngữ cảnh cần điều chỉnh theo mô hình.",

    "01:50:06": "01:50:06",
    "  任务系统设计、云文档权限及Agent机制探讨": "  Thảo luận thiết kế hệ thống tác vụ, quyền tài liệu đám mây và cơ chế Agent",

    "本章节主要围绕任务系统、云文档和 agent 相关内容展开。任务系统设计涉及任务间的并行与串行关系；对于网友提出的飞书云文档权限问题，发言人表示无相关需求无法作答。还提到将任务委托到后台可提高效率，介绍了小龙虾（CC）、open Crawl 等概念，指出虾是 CC 类 agent 加上定时、主动找事及记忆机制，不过记忆机制目前做得欠佳。":
        "Chương này chủ yếu xoay quanh hệ thống tác vụ, tài liệu đám mây và nội dung liên quan agent. Thiết kế hệ thống tác vụ liên quan đến quan hệ song song và tuần tự giữa các tác vụ; đối với vấn đề quyền tài liệu đám mây Lark mà khán giả nêu ra, người phát biểu cho biết không có nhu cầu liên quan nên không thể trả lời. Còn đề cập việc ủy thác tác vụ ra nền có thể nâng cao hiệu suất, giới thiệu các khái niệm tôm hùm nhỏ (CC), open Crawl, v.v., chỉ ra tôm là agent loại CC cộng thêm cơ chế định thời, chủ động tìm việc và bộ nhớ, tuy nhiên cơ chế bộ nhớ hiện tại làm chưa tốt.",

    "01:53:23": "01:53:23",
    "  Cloud Code中Agent Team与Worktree功能介绍": "  Giới thiệu chức năng Agent Team và Worktree trong Cloud Code",

    "本章节主要讨论了agent team机制，目前core中未引入team组局用法，仍为单一agent工作。agent team可让不同agent协作完成看板任务，节省时间，其成员是平等协作关系，通过最小化邮箱通信。还提到worktree是CC的更新，当前需手动开启，未来有望由agent按需开启，与任务系统联动较深。":
        "Chương này chủ yếu thảo luận cơ chế agent team, hiện tại trong core chưa đưa vào cách dùng team tổ đội, vẫn là agent đơn lẻ làm việc. Agent team có thể để các agent khác nhau hợp tác hoàn thành tác vụ kanban, tiết kiệm thời gian, các thành viên có quan hệ hợp tác bình đẳng, thông qua giao tiếp email tối giản hóa. Còn đề cập worktree là bản cập nhật của CC, hiện tại cần bật thủ công, tương lai hy vọng agent sẽ bật theo nhu cầu, liên kết sâu với hệ thống tác vụ.",

    "01:56:30": "01:56:30",
    "  Cloudcode版本更新情况及内容分享": "  Tình hình cập nhật phiên bản Cloudcode và chia sẻ nội dung",

    "本章节中，来新璐介绍一款 code，称其每周下载量几百到几千不等，上周为100。重点提及 cloudcode 已更新到52版本，查看其更新日志，指出51版本更新小问题，未涉及 agent 设计模式更新，52版本更新了 Web hook 小问题，还提到在相关内容里讲解了 agent 团队、任务看板等多方面内容。":
        "Trong chương này, Lai Xinlu giới thiệu một code, cho biết lượng tải xuống mỗi tuần dao động từ vài trăm đến vài nghìn, tuần trước là 100. Trọng tâm đề cập cloudcode đã cập nhật lên phiên bản 52, xem nhật ký cập nhật, chỉ ra phiên bản 51 cập nhật vấn đề nhỏ, không liên quan đến cập nhật mẫu thiết kế agent, phiên bản 52 cập nhật vấn đề nhỏ Web hook, còn đề cập trong nội dung liên quan đã giảng giải đội agent, kanban tác vụ và nhiều nội dung khác.",

    "01:57:59": "01:57:59",
    "  小龙虾项目部署过程、难点与换模型方法": "  Quá trình triển khai, khó khăn và phương pháp đổi mô hình dự án tôm hùm nhỏ",

    "本章节主要讲述小龙虾项目的部署过程。来新璐介绍可借助Claude code等工具，通过NPM安装Open Crawl。部署时飞书环节较复杂，需按指引操作，设置长连接易遇卡点，可先本地启动程序。还提及TT部署最简单，换模型也方便，可让工具根据API key完成操作，无需自行研究攻略。":
        "Chương này chủ yếu mô tả quá trình triển khai dự án tôm hùm nhỏ. Lai Xinlu giới thiệu có thể nhờ các công cụ như Claude Code, cài đặt Open Crawl qua NPM. Khi triển khai phần Lark khá phức tạp, cần thao tác theo hướng dẫn, thiết lập kết nối dài dễ gặp điểm nghẽn, có thể khởi động chương trình cục bộ trước. Còn đề cập triển khai TT đơn giản nhất, đổi mô hình cũng thuận tiện, có thể để công cụ hoàn thành thao tác dựa trên API key, không cần tự nghiên cứu hướng dẫn.",

    "02:07:37": "02:07:37",
    "  小龙虾本地与云端部署体验及代码仓库分享": "  Chia sẻ trải nghiệm triển khai cục bộ và đám mây tôm hùm nhỏ và kho code",

    "本章节中，来新璐分享了选择将小龙虾部署在本地电脑而非云端的原因。她对比了云端部署与本地部署的差异，指出本地部署能操作本地资料等。但小龙虾交互性较局限，默认能力与CC相近。还提到今晚部署agent的问题、本地与云端部署体验不同，代码在克劳0仓库，后续会优化代码使其更简洁。":
        "Trong chương này, Lai Xinlu chia sẻ lý do chọn triển khai tôm hùm nhỏ trên máy tính cục bộ thay vì đám mây. Cô ấy so sánh sự khác biệt giữa triển khai đám mây và cục bộ, chỉ ra triển khai cục bộ có thể thao tác dữ liệu cục bộ. Nhưng tính tương tác của tôm hùm nhỏ khá hạn chế, năng lực mặc định tương tự CC. Còn đề cập vấn đề triển khai agent tối nay, trải nghiệm triển khai cục bộ và đám mây khác nhau, code ở kho Claw 0, sau này sẽ tối ưu code cho gọn gàng hơn.",

    "02:13:04": "02:13:04",
    "  Facetime通话测试及AI任务执行情况探讨": "  Kiểm tra cuộc gọi Facetime và thảo luận tình hình thực thi tác vụ AI",

    "本章节围绕Claw、Facetime通话展开讨论。来新璐尝试用Claw和Facetime打电话，询问其调用权限、能否完成任务等。测试中发现给自己打邮箱能通，但不确定是否真打通，还提及智谱模型的多模态情况。此外，还提到任务执行易混乱、输入法准确率低以及AI响应问题，不清楚其内部运转情况。":
        "Chương này xoay quanh thảo luận về cuộc gọi Claw, Facetime. Lai Xinlu thử dùng Claw và Facetime gọi điện thoại, hỏi về quyền gọi, liệu có thể hoàn thành tác vụ hay không. Trong kiểm tra phát hiện gọi email cho mình có thể kết nối, nhưng không chắc có thực sự kết nối, còn đề cập tình hình đa phương thức của mô hình Zhipu. Ngoài ra, còn đề cập thực thi tác vụ dễ lộn xộn, độ chính xác bàn phím thấp và vấn đề phản hồi AI, không rõ tình hình vận hành nội bộ.",

    "02:18:31": "02:18:31",
    "  语音输入法及小龙虾模型使用体验与探讨": "  Trải nghiệm và thảo luận bàn phím giọng nói và sử dụng mô hình tôm hùm nhỏ",

    "本章节主要围绕语音输入法和模型使用展开交流。AJ询问来新璐所用语音输入法，得知是智谱的。来新璐认为其准确率一般，本地部署慢且消息易串。之后连线网友陆萌，陆萌介绍自己是车企程序员。还谈及龙虾模型，称部署本地有危险，小龙虾功能有局限，但能进行face time操作，回顾上次直播设想。":
        "Chương này chủ yếu xoay quanh trao đổi về bàn phím giọng nói và sử dụng mô hình. AJ hỏi Lai Xinlu về bàn phím giọng nói đang dùng, biết được là của Zhipu. Lai Xinlu cho rằng độ chính xác trung bình, triển khai cục bộ chậm và tin nhắn dễ lẫn lộn. Sau đó kết nối với khán giả Lục Manh, Lục Manh giới thiệu bản thân là lập trình viên công ty ô tô. Còn nói về mô hình tôm hùm, cho biết triển khai cục bộ có nguy hiểm, chức năng tôm hùm nhỏ có hạn chế, nhưng có thể thực hiện thao tác Facetime, nhìn lại ý tưởng livestream lần trước.",

    "02:24:26": "02:24:26",
    "  Open Cloud开源进展迅猛但更新质量存忧": "  Tiến triển mã nguồn mở Open Cloud nhanh chóng nhưng chất lượng cập nhật đáng lo",

    "本章节中，来新璐和🌈AJ讨论了开源生态进展。自上次直播约三周后，开源生态发展迅猛，如open cloud代码一周就有近5000个commit。不过这也带来问题，很多代码由网友用agent所写直接合入，Kidd作者可能来不及审核，导致出现莫名其妙的bug。未来若OpenCrow更新更好特性值得关注，来新璐还提及跑过翻译项目。":
        "Trong chương này, Lai Xinlu và 🌈AJ thảo luận tiến triển hệ sinh thái mã nguồn mở. Khoảng ba tuần sau livestream lần trước, hệ sinh thái mã nguồn mở phát triển nhanh chóng, như code open cloud một tuần có gần 5000 commit. Tuy nhiên điều này cũng mang đến vấn đề, nhiều code do khán giả dùng agent viết và merge trực tiếp, tác giả Kidd có thể không kịp review, dẫn đến xuất hiện bug khó hiểu. Tương lai nếu OpenCrow cập nhật tính năng tốt hơn đáng theo dõi, Lai Xinlu còn đề cập đã chạy dự án dịch thuật.",

    "02:27:16": "02:27:16",
    "  安卓与苹果使用体验对比及bytepro项目分享": "  So sánh trải nghiệm sử dụng Android và Apple và chia sẻ dự án bytepro",

    "本章节中，来新璐分享了使用手机的体验，过去一年苹果手机使用率低，尝试将习惯迁移到苹果后又迁回安卓，认为安卓装谷歌商店后软件生态超苹果。他介绍了在安卓手机通过 Termux 获得 Linux 系统包。还提到做了 bytepro 项目，从 Openpro 翻译而来，分享编码工具使用经验，认为 Web 编码严谨项目上 Codex 实现度更高。":
        "Trong chương này, Lai Xinlu chia sẻ trải nghiệm sử dụng điện thoại, một năm qua tỷ lệ sử dụng iPhone thấp, thử chuyển thói quen sang Apple rồi chuyển lại Android, cho rằng Android sau khi cài Google Store hệ sinh thái phần mềm vượt Apple. Anh ấy giới thiệu việc nhận gói hệ thống Linux qua Termux trên điện thoại Android. Còn đề cập đã làm dự án bytepro, dịch từ Openpro, chia sẻ kinh nghiệm sử dụng công cụ code, cho rằng trên dự án code web nghiêm túc Codex có mức độ triển khai cao hơn.",

    "02:30:10": "02:30:10",
    "  飞书机器人使用分享及Openclaw活动预告": "  Chia sẻ sử dụng bot Lark và thông báo sự kiện Openclaw",

    '本章节主要围绕来新璐的飞书机器人展开讨论。来新璐设置飞书机器人仅自己可用，尝试用\u201c退出飞书\u201d指令实现下播，还探讨了会话消息在同一 agent 中运行的情况。最后 AJ 表示会发回放，提及此次直播讲了 Openclaw 原理及搭建方法，后续还有训练营，可拿硬件回家组装探索新玩法。':
        'Chương này chủ yếu xoay quanh thảo luận về bot Lark của Lai Xinlu. Lai Xinlu thiết lập bot Lark chỉ mình dùng, thử dùng lệnh "thoát Lark" để kết thúc livestream, còn thảo luận tình huống tin nhắn hội thoại chạy trong cùng một agent. Cuối cùng AJ cho biết sẽ gửi phát lại, đề cập livestream lần này đã giảng nguyên lý Openclaw và phương pháp xây dựng, sau đó còn có trại huấn luyện, có thể mang phần cứng về nhà lắp ráp khám phá cách chơi mới.',

    "会议中的金句时刻": "Khoảnh khắc câu nói hay trong cuộc họp",
    "相关链接": "Liên kết liên quan",

    "妙记：": "Biên bản thông minh: ",
    "02-24 | 🦞来新璐带大家把OpenClaw技术架构拆解，还能手搓一个最小的龙虾 WaytoAGI晚8点共学":
        "02-24 | 🦞Lai Xinlu dẫn mọi người phân tích kiến trúc kỹ thuật OpenClaw, còn có thể tự tay làm một con tôm hùm tối giản WaytoAGI Cùng học lúc 8 giờ tối",

    "文字记录": "Bản ghi văn bản",

    "02-24 | 🦞来新璐带大家把OpenClaw技术架构拆解，还能手搓一个最小的龙虾 WaytoAGI晚8点共学 2026年2月24日":
        "02-24 | 🦞Lai Xinlu dẫn mọi người phân tích kiến trúc kỹ thuật OpenClaw, còn có thể tự tay làm một con tôm hùm tối giản WaytoAGI Cùng học lúc 8 giờ tối ngày 24 tháng 2 năm 2026",

    "相关会议纪要": "Biên bản cuộc họp liên quan",
}

# Common recurring patterns for the 智能纪要 blocks
# These are partial translations for commonly repeated phrases
COMMON = {
    "智能纪要：": "Biên bản thông minh: ",
    "WaytoAGI晚8点共学": "WaytoAGI Cùng học lúc 8 giờ tối",
    "特邀嘉宾": "Khách mời đặc biệt",
    "直播亮点": "Điểm nổi bật livestream",
    "直播核心亮点": "Điểm nổi bật cốt lõi livestream",
    "分享嘉宾": "Diễn giả chia sẻ",
    "主持人": "Người dẫn chương trình",
    "主持团": "Đội dẫn chương trình",
    "直播嘉宾": "Khách mời livestream",
    "特邀嘉宾：": "Khách mời đặc biệt:",
    "创始人": "Nhà sáng lập",
    "联合创始人": "Đồng sáng lập",
    "产品经理": "Quản lý sản phẩm",
    "产品负责人": "Phụ trách sản phẩm",
    "增长负责人": "Phụ trách tăng trưởng",
    "技术开发": "Phát triển kỹ thuật",
    "合伙人": "Đối tác",
    "产品运营": "Vận hành sản phẩm",
    "社区共创者": "Đồng sáng tạo cộng đồng",
    "独立开发者": "Nhà phát triển độc lập",
    "连续创业者": "Doanh nhân liên tục",
    "年": "năm",
    "月": "tháng",
    "日": "ngày",
    # Content phrases
    "手把手带你": "Hướng dẫn từng bước",
    "手把手教你": "Hướng dẫn từng bước",
    "深度解析": "Phân tích chuyên sâu",
    "正式发布": "Chính thức ra mắt",
    "正式上线": "Chính thức lên sóng",
    "实战": "Thực chiến",
    "实操": "Thực hành",
    "零门槛": "Không rào cản",
    "从入门到": "Từ nhập môn đến",
    "训练营": "Trại huấn luyện",
    "开营": "Khai mạc",
    "应用变现": "Biến ứng dụng thành tiền",
    "避坑指南": "Hướng dẫn tránh bẫy",
    "开放麦": "Open mic",
    "圆桌会": "Hội thảo bàn tròn",
    "大赛": "Cuộc thi lớn",
    "挑战赛": "Cuộc thi thử thách",
    "先锋官": "Tiên phong",
    "选秀大赛": "Cuộc thi tuyển chọn",
    "今晚": "Tối nay",
    "直播": "Livestream",
    "解锁": "Mở khóa",
    "全自动": "Hoàn toàn tự động",
    "一键": "Một nút bấm",
    "搭建": "Xây dựng",
    "拆解": "Phân tích",
    "揭秘": "Tiết lộ bí mật",
    "玩转": "Chơi thành thạo",
    "全攻略": "Toàn bộ chiến lược",
    "工作流": "Quy trình làm việc",
    "短剧": "Phim ngắn",
    "工作空间": "Không gian làm việc",
    "知识管理": "Quản lý kiến thức",
    "内容创作": "Sáng tạo nội dung",
    "创作者": "Nhà sáng tạo",
    "涨粉": "Tăng người theo dõi",
    "爆款": "Hot trend",
    "流量": "Lưu lượng",
    "赚钱": "Kiếm tiền",
    "获客": "Thu hút khách hàng",
    "增长": "Tăng trưởng",
    "前": "Cựu",
    "养虾经验谈": "Kinh nghiệm nuôi tôm",
    "养虾": "Nuôi tôm",
    "部署": "Triển khai",
    "部署指南": "Hướng dẫn triển khai",
    "进阶": "Nâng cao",
    "技巧": "Kỹ thuật",
    "场景": "Kịch bản",
    "校园": "Khuôn viên trường",
    "办公": "Văn phòng",
    "编程": "Lập trình",
    "游戏": "Trò chơi",
    "音乐": "Âm nhạc",
    "视频": "Video",
    "图片": "Hình ảnh",
    "设计": "Thiết kế",
    "营销": "Marketing",
    "数据": "Dữ liệu",
    "工具": "Công cụ",
    "平台": "Nền tảng",
    "项目": "Dự án",
    "功能": "Chức năng",
    "用户": "Người dùng",
    "开发": "Phát triển",
    "系统": "Hệ thống",
    "开源": "Mã nguồn mở",
    "模型": "Mô hình",
    "技术": "Kỹ thuật",
    "百度": "Baidu",
    "字节": "ByteDance",
    "阿里": "Alibaba",
    "腾讯": "Tencent",
    "文心": "Wenxin",
    "千帆": "Qianfan",
    "百炼": "Bách Luyện",
    "豆包": "Doubao",
    "通义灵码": "Tongyi Lingma",
    "扣子": "Coze",
    "飞书": "Lark",
    "小红书": "Xiaohongshu",
    "好未来": "TAL Education",
    "学而思": "Xueersi",
    "中国美院": "Học viện Mỹ thuật Trung Quốc",
    "哈佛大学": "Đại học Harvard",
    "计算机博士": "Tiến sĩ Khoa học Máy tính",
    "具身智能": "Trí tuệ hiện thân",
    "无人驾驶": "Lái xe tự động",
    "大模型": "Mô hình lớn",
    "算法工程师": "Kỹ sư thuật toán",
    "高级工程师": "Kỹ sư cao cấp",
    "产品专家": "Chuyên gia sản phẩm",
    "博主": "Blogger",
    "万粉": "vạn người theo dõi",
    "数字角色": "Nhân vật số",
    "公众号": "Tài khoản công khai",
    "视频号": "Kênh video",
    "自媒体": "Truyền thông tự thân",
    "孵化负责人": "Phụ trách ươm tạo",
    "AI搭子": "AI đồng hành",
    "上班记": "Nhật ký đi làm",
    "思考": "Suy nghĩ",
    "干活": "Làm việc",
    "秒哒": "Miaoda",
    "让创意变生意": "Biến sáng tạo thành kinh doanh",
    "今天不卷了": "Hôm nay không cuộn nữa",
    "鹿演": "Lộc Diễn",
    "未来硅世界": "Thế giới Silicon tương lai",
    "广告片": "Phim quảng cáo",
    "纪录片": "Phim tài liệu",
    "导演": "Đạo diễn",
    "艺术家": "Nghệ sĩ",
    "讲师": "Giảng viên",
    "特聘讲师": "Giảng viên thỉnh giảng đặc biệt",
    "国家级": "Cấp quốc gia",
    "全国金奖": "Giải vàng toàn quốc",
    "影视特效": "Hiệu ứng phim ảnh",
    "经验": "Kinh nghiệm",
    "负责人": "Phụ trách",
    "架构师": "Kiến trúc sư",
    "研究科学家": "Nhà khoa học nghiên cứu",
    "财务经理": "Quản lý tài chính",
    "高级财务经理": "Quản lý tài chính cao cấp",
    "赛事": "Sự kiện thi đấu",
    "情报速递": "Tin tức nhanh",
    "重磅": "Trọng điểm",
    "嘉宾": "Khách mời",
    "分享": "Chia sẻ",
    "对话": "Đối thoại",
    "对谈": "Trò chuyện",
    "从概念到实操": "Từ khái niệm đến thực hành",
    "批量": "Hàng loạt",
    "复刻": "Nhân bản",
    "全流程": "Toàn bộ quy trình",
    "一站式": "Tất cả trong một",
    "从脚本到成片": "Từ kịch bản đến thành phẩm",
    "剪辑": "Biên tập video",
    "剪片": "Cắt phim",
    "解放双手": "Giải phóng đôi tay",
    "大幅提升": "Nâng cao đáng kể",
    "内容产出效率": "Hiệu suất sản xuất nội dung",
    "规模化": "Quy mô hóa",
    "安全兼容性": "Tương thích bảo mật",
    "我睡觉": "Tôi ngủ",
    "虾赚钱": "tôm kiếm tiền",
    "虾剪片": "tôm cắt phim",
    "让每一个人都能成为": "Để mỗi người đều có thể trở thành",
    "AI时代下": "Trong kỷ nguyên AI",
    "快速开发": "Phát triển nhanh",
    "极限开发实战复盘": "Tổng kết thực chiến phát triển cực hạn",
    "正式开启公测": "Chính thức mở beta công khai",
    "限量邀请码发放": "Phát hành mã mời giới hạn",
    "行业现状": "Hiện trạng ngành",
    "开营第": "Khai mạc buổi",
    "课": "bài",
    "创作指南": "Hướng dẫn sáng tạo",
    "入门": "Nhập môn",
    "加餐课": "Bài bổ sung",
    "普通小白": "Người mới bình thường",
    "也能使用的": "cũng có thể sử dụng",
    "云端": "Đám mây",
    "上新": "Ra mắt tính năng mới",
    "新功能": "Tính năng mới",
    "上线": "Lên sóng",
    "职场AI": "AI công sở",
    "就用": "cứ dùng",
    "深度实测": "Test chuyên sâu",
    "如何解放双手": "Làm sao giải phóng đôi tay",
    "原生工作台": "Bàn làm việc native",
    "两日连播": "Hai ngày liên tiếp",
    "爆改": "Cải tạo mạnh mẽ",
    "到底更新了什么": "Cuối cùng đã cập nhật gì",
    "版本": "Phiên bản",
    "更新": "Cập nhật",
    "全球首个": "Đầu tiên trên toàn cầu",
    "全球首发": "Ra mắt toàn cầu đầu tiên",
    "实时生成": "Tạo thời gian thực",
    "世界模型": "Mô hình thế giới",
    "登顶": "Lên đỉnh",
    "出圈密码": "Bí quyết viral",
    "怎样做出": "Làm thế nào tạo ra",
    "曝光": "Lượt hiển thị",
    "复盘": "Tổng kết",
    "结局重制": "Làm lại phần kết",
    "稳定日更": "Đăng bài hàng ngày ổn định",
    "拜年视频": "Video chúc Tết",
    "春节祝福": "Lời chúc Tết",
    "语音": "Giọng nói",
    "文案": "Nội dung quảng cáo",
    "模板": "Mẫu",
    "一次搞定": "Một lần xong",
    "一场直播结束": "Một buổi livestream kết thúc",
    "就能自己动手做": "là có thể tự tay làm",
    "选题": "Chọn đề tài",
    "持续稳定输出": "Sản xuất ổn định liên tục",
    "总决赛": "Chung kết",
    "新春": "Năm mới",
    "年味": "Hương vị Tết",
    "开始了": "Bắt đầu rồi",
    "年夜饭": "Bữa cơm tất niên",
    "菜谱": "Công thức nấu ăn",
    "大全": "Toàn tập",
    "解决": "Giải quyết",
    "过年吃什么": "Ăn gì ngày Tết",
    "不讲复杂概念": "Không nói khái niệm phức tạp",
    "直接把": "Trực tiếp biến",
    "变成": "thành",
    "年味工具箱": "Hộp công cụ Tết",
    "大厂": "Công ty lớn",
    "硬件": "Phần cứng",
    "眼镜": "Kính",
    "核心能力": "Năng lực cốt lõi",
    "落地场景": "Kịch bản triển khai",
    "智能体": "Trí tuệ thể",
    "搭建智能体工作流": "Xây dựng quy trình làm việc trí tuệ thể",
    "让你的": "Để",
    "用一个接口调用": "Dùng một API gọi",
    "上万种": "hàng vạn loại",
    "数据和工具": "dữ liệu và công cụ",
    "技术大V": "KOL công nghệ",
    "都在用": "đều đang dùng",
    "整什么活": "làm trò gì",
    "高效收尾": "Hoàn thành hiệu quả",
    "节前工作": "Công việc trước kỳ nghỉ",
    "一键搞定": "Một nút bấm xong",
    "批量复刻": "Nhân bản hàng loạt",
    "开发实战攻略": "Chiến lược thực chiến phát triển",
    "避坑": "Tránh bẫy",
    "语音AI输入法": "Bàn phím AI giọng nói",
    "AI审美浪潮下的哲学追问与反思": "Truy vấn triết học và phản tư trong làn sóng thẩm mỹ AI",
    "对准科技": "Duizhun Technology",
    "增长专家": "Chuyên gia tăng trưởng",
    "服务": "phục vụ",
    "擅长": "Giỏi về",
    "内容营销": "Marketing nội dung",
    "外链建设": "Xây dựng liên kết ngoài",
    "增长策略": "Chiến lược tăng trưởng",
    "掌握": "Nắm vững",
    "实现精准获客与稳定增长": "Thực hiện thu hút khách chính xác và tăng trưởng ổn định",
    "可复用的增长方法论": "Phương pháp luận tăng trưởng có thể tái sử dụng",
    "实战案例复盘": "Tổng kết case study thực chiến",
    "从扣子养虾到": "Từ nuôi tôm trên Coze đến",
    "大趋势": "Xu hướng lớn",
    "高玩": "Cao thủ",
    "跨": "Xuyên",
    "城": "thành phố",
    "伙伴共创的": "đối tác đồng sáng tạo",
    "年度AI贺岁片": "Phim Tết AI hàng năm",
    "幕后分享": "Chia sẻ hậu trường",
    "该上班了": "Đi làm thôi",
    "进阶实战": "Thực chiến nâng cao",
    "花": "Dành",
    "分钟用": "phút dùng",
    "彻底重构你的": "Hoàn toàn tái cấu trúc",
    "体系": "Hệ thống",
    "全程实操": "Thực hành toàn bộ",
    "带你用": "Dẫn bạn dùng",
    "构建高效": "Xây dựng hiệu quả",
    "拆解各个工具使用痛点与技巧": "Phân tích điểm đau và kỹ thuật sử dụng từng công cụ",
    "助你少走弯路快速上手": "Giúp bạn ít đi đường vòng nhanh chóng bắt đầu",
    "如何突破": "Làm sao vượt qua",
    "量多精品少困局": "Tình trạng nhiều lượng ít chất",
    "揭秘高质量": "Tiết lộ bí quyết chất lượng cao",
    "创作的实战技巧": "Kỹ thuật thực chiến sáng tạo",
    "最佳搭档": "Đối tác tốt nhất",
    "背后的故事": "Câu chuyện đằng sau",
    "从文档到生命体": "Từ tài liệu đến sinh thể",
    "开启文件即软件新纪元": "Mở ra kỷ nguyên mới file chính là phần mềm",
    "底层逻辑": "Logic nền tảng",
    "全流程打通": "Xuyên suốt toàn bộ quy trình",
    "今晚是自习室": "Tối nay là phòng tự học",
    "一天消耗": "Một ngày tiêu thụ",
    "亿": "trăm triệu",
    "龙虾养成记": "Nhật ký nuôi tôm hùm",
    "全球首个实时生成世界模型正式上线": "Mô hình thế giới tạo thời gian thực đầu tiên toàn cầu chính thức lên sóng",
    "不只是": "Không chỉ là",
    "而是": "mà là",
    "开年重磅": "Trọng điểm đầu năm",
    "工作流分享": "Chia sẻ quy trình làm việc",
    "下午": "Buổi chiều",
    "热乎情报速递": "Tin tức nóng hổi",
    "深度解读": "Giải mã chuyên sâu",
    "两大赛道": "Hai đường đua lớn",
    "每周四": "Mỗi thứ Năm",
    "时间": "Thời gian",
    "火爆来袭": "Đến rồi cực hot",
    "教学系列": "Chuỗi giảng dạy",
    "第二期": "Kỳ thứ hai",
    "第三期": "Kỳ thứ ba",
    "第五期": "Kỳ thứ năm",
    "功能亮点": "Điểm nổi bật chức năng",
    "小白版": "Phiên bản người mới",
    "自动化工作流": "Quy trình làm việc tự động",
    "多场景方案直接复刻": "Nhân bản trực tiếp giải pháp đa kịch bản",
    "开源很可能带来": "Mã nguồn mở rất có thể mang lại",
    "第二波商业化红利": "Đợt chia lợi thương mại hóa thứ hai",
    "一起探讨": "Cùng thảo luận",
    "找到属于你的机遇": "Tìm cơ hội thuộc về bạn",
    "网页设计新功能上线": "Tính năng mới thiết kế web lên sóng",
    "普通人真的可以逆袭吗": "Người thường thực sự có thể lật ngược tình thế không",
    "从家庭主妇到": "Từ bà nội trợ đến",
    "公司": "Công ty",
    "在社区里成长起来的": "Phát triển lên trong cộng đồng",
    "AI调香和背后的故事": "Pha chế nước hoa AI và câu chuyện đằng sau",
    "冲刺倒计时": "Đếm ngược nước rút",
    "天": "ngày",
    "百宝箱": "Hộp bảo bối",
    "插件开发大赛": "Cuộc thi phát triển plugin",
    "插件召集令": "Lệnh triệu tập plugin",
    "正式启动": "Chính thức khởi động",
    "众测": "Test cộng đồng",
    "重磅嘉宾": "Khách mời trọng điểm",
    "进阶冲刺": "Nước rút nâng cao",
    "进阶攻略来袭": "Chiến lược nâng cao đã đến",
    "创作零门槛创作赛": "Cuộc thi sáng tạo không rào cản",
    "企业场景": "Kịch bản doanh nghiệp",
    "优秀项目全国展示": "Trưng bày dự án xuất sắc toàn quốc",
    "大学生创意秀": "Show sáng tạo sinh viên",
    "围观同龄人如何玩转": "Xem bạn bè đồng trang lứa chơi thành thạo như thế nào",
    "每一个项目都藏着惊喜": "Mỗi dự án đều ẩn chứa bất ngờ",
    "奇妙碰撞": "Va chạm kỳ diệu",
    "带你冲": "Dẫn bạn xông tới",
    "万大奖": "vạn giải thưởng",
    "不止冲奖": "Không chỉ thi giải",
    "更能学硬核技巧": "Còn học được kỹ thuật chuyên sâu",
    "小时搞定投稿": "giờ xong bài nộp",
    "奖金": "Tiền thưởng",
    "千万流量": "Hàng chục triệu lưu lượng",
    "教你赢赛事": "Dạy bạn thắng cuộc thi",
    "从 0-1 聚焦校园场景搭建自己的": "Từ 0-1 tập trung kịch bản trường học xây dựng",
    "AI编程实战技巧分享": "Chia sẻ kỹ thuật thực chiến lập trình AI",
    "从入门到沉迷": "Từ nhập môn đến say mê",
    "百万美金": "Triệu đô",
    "工具权益": "Quyền lợi công cụ",
    "AI创意竞赛": "Cuộc thi sáng tạo AI",
    "我的AI创业收入清单和AI创业故事": "Danh sách thu nhập khởi nghiệp AI và câu chuyện khởi nghiệp AI của tôi",
    "4天吃透": "4 ngày nắm chắc",
    "第一期开营": "Kỳ đầu tiên khai mạc",
    "火热开启": "Khởi động nóng bỏng",
    "大奖是": "Giải lớn là",
    "联合教学": "Giảng dạy phối hợp",
    "是一个无缝衔接多模态生成的": "là một công cụ",
    "好上手又强大": "dễ sử dụng lại mạnh mẽ",
    "AI导演大赛创作分享": "Chia sẻ sáng tạo cuộc thi đạo diễn AI",
    "带你解锁": "Dẫn bạn mở khóa",
    "体验": "Trải nghiệm",
    "干货满满": "Đầy đủ kiến thức thực tiễn",
    "即刻变现": "Biến thành tiền ngay lập tức",
    "食用说明书": "Hướng dẫn sử dụng",
    "从入门到惊艳": "Từ nhập môn đến kinh ngạc",
    "揭秘X平台流量密码": "Tiết lộ bí mật lưu lượng nền tảng X",
    "周如何快速涨粉": "tuần cách tăng nhanh người theo dõi",
    "分享爆款提示词技巧": "Chia sẻ kỹ thuật prompt hot",
    "带你避开AI同质化": "Dẫn bạn tránh đồng nhất AI",
    "今晚20:00直播": "Livestream tối nay 20:00",
    "今晚21:00直播": "Livestream tối nay 21:00",
    "速学": "Học nhanh",
    "实操技巧": "Kỹ thuật thực hành",
    "先看清这个行业在": "Trước hết nhìn rõ ngành này đang",
    "赚谁的钱": "kiếm tiền của ai",
    "再决定你要不要进来": "rồi quyết định bạn có muốn vào không",
    "动态分层全拿捏": "Hoàn toàn nắm bắt phân lớp động",
    "出片": "Xuất phim",
    "解锁AI影视广告创作新玩法": "Mở khóa cách chơi mới sáng tạo quảng cáo phim AI",
    "能帮创作者赚钱的AI嘴替": "AI thay miệng giúp nhà sáng tạo kiếm tiền",
    "内容创作者的一站式画布": "Canvas tất cả trong một cho nhà sáng tạo nội dung",
    "AI 产品出海的实战指南": "Hướng dẫn thực chiến đưa sản phẩm AI ra nước ngoài",
    "如何": "Làm sao",
    "及": "và",
    "的": "của",
    "与": "và",
    "是": "là",
    "在": "tại",
    "和": "và",
    "等": "v.v.",
    "中": "trong",
    "也": "cũng",
    "都": "đều",
    "了": "rồi",
    "可": "có thể",
    "将": "sẽ",
    "为": "cho",
    "让": "để",
    "把": "đem",
    "从": "từ",
    "到": "đến",
    "以": "để",
    "之": "của",
    "或": "hoặc",
    "但": "nhưng",
    "更": "hơn",
    "再": "lại",
    "就": "thì",
    "还": "còn",
    "上": "trên",
    "下": "dưới",
    "不": "không",
    "能": "có thể",
    "会": "sẽ",
    "被": "bị",
    "给": "cho",
    "要": "cần",
    "带": "mang",
    "做": "làm",
    "看": "xem",
    "用": "dùng",
    "有": "có",
    "这": "này",
    "那": "kia",
    "你": "bạn",
    "我": "tôi",
    "他": "anh ấy",
    "她": "cô ấy",
    "们": "",
    "个": "",
    "位": "vị",
}

def translate_text(text):
    """Translate a Chinese text to Vietnamese"""
    # First check if we have an exact match
    if text in T:
        return T[text]

    # If no Chinese, return as-is
    if not has_chinese(text):
        return text

    # For longer texts not in the map, do word-level replacement
    result = text
    # Sort by length descending to match longest patterns first
    sorted_common = sorted(COMMON.items(), key=lambda x: len(x[0]), reverse=True)
    for cn, vi in sorted_common:
        if cn in result:
            result = result.replace(cn, vi)

    return result

# Process all blocks
translated_count = 0
kept_count = 0
total_text_runs = 0

for block in data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run' and el.get('content'):
            total_text_runs += 1
            orig = el['content']
            translated = translate_text(orig)
            if translated != orig:
                el['content'] = translated
                translated_count += 1
            else:
                kept_count += 1

# Update title
data['title'] = translate_text(data['title'])

print(f"Total text_runs: {total_text_runs}")
print(f"Translated: {translated_count}")
print(f"Kept as-is: {kept_count}")

with open('_art19_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved to _art19_trans.json")
