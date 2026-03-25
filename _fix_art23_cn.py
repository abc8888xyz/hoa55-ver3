# -*- coding: utf-8 -*-
"""Fix remaining Chinese in meeting notes section of art23_trans.json"""
import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

# Additional Chinese -> Vietnamese translations for meeting note titles
extra = {
    # Common title phrases
    "AI搭子上班记：你思考，DuMate干活": "Nhật ký đi làm cùng AI: Bạn suy nghĩ, DuMate làm việc",
    "还在自己整理文件、查资料、做表格？": "Vẫn đang tự sắp xếp tệp, tra cứu tài liệu, làm bảng tính?",
    "首个国产企业级满血版小龙虾——百度": "Tôm Hùm cấp doanh nghiệp nội địa đầu tiên phiên bản đầy đủ — Baidu",
    "已全量上线！": "đã ra mắt toàn bộ!",
    "一个人": "Một người",
    "一个小团队": "một đội nhỏ",
    "从文件管理到信息汇总，全流程": "Từ quản lý tệp đến tổng hợp thông tin, toàn bộ quy trình",
    "代劳": "thay thế",
    "今晚": "Tối nay",
    "直播": "Livestream",
    "带你揭秘": "Giải mã",
    "创业者都在用": "Nhà khởi nghiệp đang dùng",
    "做什么": "làm gì",
    "系列第一期": "số đầu tiên",
    "可规模化": "Có thể mở rộng quy mô",
    "安全兼容性": "Tính an toàn tương thích",
    "养虾经验谈": "Kinh nghiệm nuôi tôm",
    "我睡觉": "Tôi ngủ",
    "虾剪片": "Tôm cắt phim",
    "虾赚钱": "Tôm kiếm tiền",
    "广告、产品、品牌片全搞定": "Quảng cáo, sản phẩm, video thương hiệu đều xong",
    "今天晚上百度千帆开发者带你解锁新姿势": "Tối nay nhà phát triển Baidu Qianfan dẫn bạn mở khóa tư thế mới",
    "用": "Dùng",
    "实现全自动": "thực hiện tự động hoàn toàn",
    "剪辑": "cắt ghép",
    "你只管放心睡觉，小虾帮你剪片": "Bạn cứ yên tâm ngủ, tôm nhỏ giúp bạn cắt phim",
    "解放双手，大幅提升内容产出效率": "Giải phóng đôi tay, nâng cao hiệu suất sản xuất nội dung",
    "从概念到实操，手把手教你玩转": "Từ khái niệm đến thực hành, hướng dẫn chi tiết chơi",
    "向阳乔木": "Hướng Dương Kiều Mộc",
    "前": "Cựu",
    "商业化": "thương mại hóa",
    "产品经理": "PM sản phẩm",
    "自媒体人": "nhà sáng tạo nội dung",
    "姚金刚": "Diêu Kim Cương",
    "好未来学而思网校营销负责人": "trưởng bộ phận marketing Học Nhi Tư Online",
    "猎河科技": "Liệt Hà Tech",
    "搜索正在偷走你的流量": "search đang đánh cắp lưu lượng của bạn",
    "来聊聊怎么让": "Hãy nói về cách khiến",
    "主动引用你": "chủ động trích dẫn bạn",
    "当用户不再点击链接，而是直接看": "Khi người dùng không còn nhấp vào liên kết mà trực tiếp xem",
    "给的答案，你的内容还能被看到吗": "đưa ra, nội dung của bạn còn được nhìn thấy không",
    "的工作空间": "Agent",
    "少卿": "Thiếu Khanh",
    "出国点餐一条龙": "Dịch vụ trọn gói đặt món nước ngoài",
    "社区共创者": "Đồng sáng tạo cộng đồng",
    "带你解锁首个为一人公司打造的": "Mở khóa đầu tiên dành cho công ty một người",
    "工作空间": "không gian làm việc",
    "一键连接": "Kết nối một nút",
    "工具，实现本地与云端文件一站式管理": "công cụ, quản lý tệp cục bộ và cloud một cửa",
    "参与直播即可领取社区专属积分兑换码": "Tham gia livestream nhận mã đổi điểm độc quyền cộng đồng",
    "秒哒全球首发应用生成": "Miaoda ra mắt toàn cầu ứng dụng tạo",
    "帮你做应用": "giúp bạn làm ứng dụng",
    "营销增长与": "Tăng trưởng marketing và",
    "优化全攻略": "tối ưu hóa toàn bộ chiến lược",
    "对准科技创始人": "Nhà sáng lập Đối Chuẩn Tech",
    "增长专家，三年实战经验，服务": "Chuyên gia tăng trưởng, ba năm kinh nghiệm thực chiến, phục vụ",
    "产品": "sản phẩm",
    "擅长": "Giỏi",
    "内容营销、外链建设和增长策略": "content marketing, xây dựng backlink và chiến lược tăng trưởng",
    "掌握": "Nắm vững",
    "项": "mục",
    "实现精准获客与稳定增长": "thực hiện thu hút khách chính xác và tăng trưởng ổn định",
    "实战案例复盘，解锁可复用的增长方法论": "Phân tích lại case study thực chiến, mở khóa phương pháp tăng trưởng có thể tái sử dụng",
    "高玩分享": "Chia sẻ của cao thủ",
    "从扣子养虾到": "Từ nuôi tôm trên Coze đến",
    "大趋势": "xu hướng lớn",
    "跨": "Xuyên",
    "城": "thành phố",
    "社区伙伴共创的": "đối tác cộng đồng đồng sáng tạo",
    "年度": "năm",
    "贺岁片": "phim Tết",
    "老马的": "Lão Mã",
    "囧途": "chuyến đi dở khóc dở cười",
    "幕后分享": "chia sẻ hậu trường",
    "该上班了": "đến lúc đi làm rồi",
    "千帆养虾进阶实战": "Thực chiến nâng cao nuôi tôm trên Qianfan",
    "花": "Dành",
    "分钟": "phút",
    "彻底重构你的": "tái cấu trúc hoàn toàn",
    "知识管理体系": "hệ thống quản lý tri thức",
    "卡尔的": "Carl's",
    "沃茨": "Watts",
    "公众号": "công chúng hào",
    "视频号": "video hào",
    "字节大模型算法工程师": "kỹ sư thuật toán mô hình lớn ByteDance",
    "全程实操": "Thực hành toàn trình",
    "带你": "Dẫn bạn",
    "构建高效": "xây dựng hiệu quả",
    "避坑指南": "Hướng dẫn tránh bẫy",
    "拆解各个工具使用痛点与技巧，助你少走弯路快速上手": "Phân tích điểm đau và mẹo sử dụng từng công cụ, giúp bạn ít đi đường vòng nhanh bắt đầu",
    "如何突破": "Làm sao để đột phá",
    "短番量多精品少困局": "khó khăn phim ngắn nhiều nhưng ít tinh phẩm",
    "南墙": "Nam Tường",
    "技术开发": "Phát triển kỹ thuật",
    "中国美院": "Học viện Mỹ thuật Trung Quốc",
    "特聘": "đặc biệt",
    "首批国家级数智设计创作先锋": "Tiên phong thiết kế số thông minh cấp quốc gia đợt đầu",
    "联合创始人": "Đồng sáng lập",
    "百万粉丝博主": "blogger triệu fan",
    "拥有超": "hơn",
    "年影视特效经验": "năm kinh nghiệm kỹ xảo điện ảnh",
    "拆解": "Phân tích",
    "短番从脚本到成片的高效创作流程": "phim ngắn AI từ kịch bản đến thành phẩm quy trình sáng tạo hiệu quả",
    "揭秘高质量短番创作的实战技巧与避坑指南": "Tiết lộ mẹo thực chiến và hướng dẫn tránh bẫy trong sáng tạo phim ngắn chất lượng cao",
    "未来硅世界第": "Thế giới Silicon tương lai số ",
    "期": "",
    "最佳搭档": "đối tác tốt nhất",
    "背后的故事": "Câu chuyện đằng sau",
    "从文档到生命体，开启文件即软件新纪元": "Từ tài liệu đến sinh thể, mở ra kỷ nguyên mới tệp chính là phần mềm",
    "今晚是自习室": "Tối nay là phòng tự học",
    "来新璐带大家把": "Tân Lộ dẫn mọi người",
    "技术架构拆解，还能手搓一个最小的龙虾": "phân tích kiến trúc kỹ thuật, còn có thể tự tay làm một Tôm Hùm nhỏ nhất",
    "系列课": "Khóa học loạt",
    "一天消耗": "Tiêu thụ",
    "亿": "tỷ",
    "的龙虾养成记": "nhật ký nuôi Tôm Hùm mỗi ngày",
    "对谈": "Đối thoại với",
    "创始人": "nhà sáng lập",
    "分钟登顶": "phút lên đỉnh bảng xếp hạng",
    "榜首的出圈密码": "bí mật viral",
    "晨然": "Thần Nhiên",
    "怎样做出": "Làm thế nào để tạo",
    "万曝光的": "triệu lượt xem",
    "视频": "video",
    "怪奇物语结局重制复盘": "Phân tích lại việc tái tạo kết thúc Stranger Things",
    "让": "Để",
    "像你一样思考": "suy nghĩ như bạn",
    "打造你的内容系统，实现稳定日更涨粉": "xây dựng hệ thống nội dung của bạn, thực hiện đăng bài hàng ngày ổn định tăng fan",
    "用阿里百炼制作拜年视频、春节祝福语音多场景春节祝福文案模板，一次搞定一场直播结束，就能自己动手做春节祝福内容": "Dùng Alibaba Bailian làm video chúc Tết, giọng nói chúc Tết Nguyên đán, mẫu văn bản chúc Tết đa kịch bản, xong hết trong một buổi livestream, tự tay làm nội dung chúc Tết Nguyên đán",
    "电波曲奇": "Điện Ba Khúc Kỳ",
    "如何用": "Cách dùng",
    "拥有源源不断的选题": "có nguồn đề tài liên tục",
    "持续稳定输出爆款内容": "sản xuất nội dung hot ổn định bền vững",
    "百度千帆发布的": "do Baidu Qianfan phát hành",
    "款": "",
    "手把手教你一键部署属于自己的": "hướng dẫn chi tiết triển khai chỉ với một nút",
    "助理": "trợ lý",
    "星企划总决赛": "Chung kết Star Project",
    "玩转新春": "Vui Tết",
    "年味开始了": "Hương vị Tết bắt đầu rồi",
    "百炼上手零门槛，轻松做新年内容": "Bailian dễ bắt đầu không rào cản, dễ dàng làm nội dung Tết",
    "福字、年货清单、窗花剪纸一站式搞定": "Chữ Phúc, danh sách đồ Tết, giấy cắt hoa cửa sổ một cửa xong hết",
    "年夜饭": "Tiệc tất niên",
    "菜谱大全，解决": "Tuyển tập công thức, giải quyết",
    "过年吃什么": "ăn gì ngày Tết",
    "不讲复杂概念，直接把": "Không giảng khái niệm phức tạp, trực tiếp biến",
    "变成年味工具箱": "thành hộp công cụ Tết",
    "大厂": "Công ty lớn",
    "产品专家": "Chuyên gia sản phẩm",
    "独立开发者": "Nhà phát triển độc lập",
    "小红书": "Xiaohongshu",
    "博主": "Blogger",
    "带你深度解析": "Phân tích chuyên sâu",
    "硬件": "Phần cứng",
    "应用开发": "Phát triển ứng dụng",
    "银海": "Ngân Hải",
    "眼镜核心能力与落地场景": "kính năng lực cốt lõi và kịch bản triển khai",
    "手把手带你搭建智能体工作流": "Hướng dẫn chi tiết xây dựng workflow agent",
    "今天不卷了，让": "Hôm nay không cạnh tranh nữa, để",
    "干活": "làm việc",
    "正式发布": "chính thức ra mắt",
    "让每一个人都能成为内容创作者": "Để mọi người đều có thể trở thành nhà sáng tạo nội dung",
    "鹿演": "Lộc Diễn",
    "让你的": "Để",
    "的": "của bạn",
    "用一个接口调用上万种数据和工具": "gọi hàng vạn loại dữ liệu và công cụ qua một giao diện",
    "曲东奇": "Khúc Đông Kỳ",
    "合伙人、产品运营": "Đối tác, vận hành sản phẩm",
    "张蔚": "Trương Úy",
    "孵化负责人": "Trưởng bộ phận ươm tạo",
    "心流资本合伙人": "Đối tác Tâm Lưu Capital",
    "技术大": "KOL công nghệ",
    "都在用秒哒整什么活": "đang dùng Miaoda làm gì",
    "办公高效收尾：百炼模板一键搞定节前工作": "Kết thúc hiệu quả công việc văn phòng: Mẫu Bailian xử lý công việc trước Tết chỉ với một nút",
    "上百度智能云部署": "Triển khai trên Baidu Smart Cloud",
    "用这个": "Dùng",
    "批量复刻": "nhân bản hàng loạt",
    "语音": "Giọng nói",
    "输入法开发实战攻略与避坑指南": "Chiến lược thực chiến phát triển bàn phím AI và hướng dẫn tránh bẫy",
    "审美浪潮下的哲学追问与反思": "Câu hỏi triết học và phản tư dưới làn sóng thẩm mỹ",
    "普通小白也能使用的云端": "Cloud mà người mới cũng có thể sử dụng",
    "上新：手把手教你一站式": "ra mắt: Hướng dẫn chi tiết một cửa",
    "创作": "sáng tạo",
}

with open('_art23_trans.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply replacements to all remaining Chinese text
cn_fixed = 0
for block in data['blocks']:
    for el in block['elements']:
        if el['type'] != 'text_run':
            continue
        if not re.search(r'[\u4e00-\u9fff]', el['content']):
            continue
        text = el['content']
        for cn, vi in sorted(extra.items(), key=lambda x: -len(x[0])):
            text = text.replace(cn, vi)
        if text != el['content']:
            el['content'] = text
            cn_fixed += 1

# Check remaining
remaining = 0
for block in data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run' and re.search(r'[\u4e00-\u9fff]', el['content']):
            remaining += 1
            # Only print first 20
            if remaining <= 20:
                cn_chars = re.findall(r'[\u4e00-\u9fff]+', el['content'])
                print(f"  Remaining CN: {cn_chars[:5]}")

print(f"\nFixed: {cn_fixed} text_runs")
print(f"Still remaining: {remaining}")

with open('_art23_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved.")
