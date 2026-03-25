# -*- coding: utf-8 -*-
"""Full translation for art19 - all blocks including 智能纪要 titles"""
import json, sys, re, copy

sys.stdout.reconfigure(encoding='utf-8')

with open('_art19_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

# Full translation map: key = (block_index, element_index), value = translated text
# We load the partial translation first, then add the rest
with open('_art19_trans.json', 'r', encoding='utf-8') as f:
    partial = json.load(f)

# Start fresh from original
result = copy.deepcopy(data)

# Copy translations from blocks 0-115 from partial (those were good)
for i in range(min(116, len(result['blocks']))):
    for j, el in enumerate(result['blocks'][i]['elements']):
        if el['type'] == 'text_run':
            result['blocks'][i]['elements'][j]['content'] = partial['blocks'][i]['elements'][j]['content']

# Now translate blocks 116+ with full sentence translations
FULL_MAP = {}

# Helper: translate date pattern
def translate_date(text):
    """Replace Chinese date patterns like 2026年3月23日 -> ngày 23 tháng 3 năm 2026"""
    def replace_date(m):
        y, mo, d = m.group(1), m.group(2), m.group(3)
        return f"ngày {d} tháng {mo} năm {y}"
    text = re.sub(r'(\d{4})年(\d{1,2})月(\d{1,2})日', replace_date, text)
    return text

def translate_smart_minutes(text):
    """Translate a 智能纪要 block text"""
    if not has_chinese(text):
        return text

    t = text

    # Common header
    t = t.replace('智能纪要：', 'Biên bản thông minh: ')
    t = t.replace('WaytoAGI晚8点共学', 'WaytoAGI Cùng học lúc 8 giờ tối')

    # Dates
    t = translate_date(t)

    # Common phrases - translate in order of length (longest first)
    replacements = [
        # Long compound phrases first
        ('从文件管理到信息汇总，全流程 AI 代劳', 'Từ quản lý file đến tổng hợp thông tin, AI đảm nhận toàn bộ quy trình'),
        ('还在自己整理文件、查资料、做表格？', 'Bạn vẫn đang tự sắp xếp file, tra cứu tài liệu, làm bảng tính?'),
        ('首个国产企业级满血版小龙虾——百度 DuMate 已全量上线！', 'Con tôm hùm doanh nghiệp đầy đủ tính năng nội địa đầu tiên — Baidu DuMate đã ra mắt toàn diện!'),
        ('一个人 + 一个 DuMate = 一个小团队。', 'Một người + một DuMate = một đội nhỏ.'),
        ('磁盘整理 + 资料搜集 + 学习助手，三大办公场景实测', 'Dọn dẹp ổ đĩa + Thu thập tài liệu + Trợ lý học tập, test thực tế ba kịch bản văn phòng lớn'),
        ('AI搭子上班记：你思考，DuMate干活', 'Nhật ký đi làm cùng AI: Bạn suy nghĩ, DuMate làm việc'),
        ('今晚21:00直播｜「Agent Talk系列第一期」：带你揭秘YC创业者都在用Agent做什么', 'Livestream tối nay 21:00 | "Agent Talk Series Kỳ 1": Dẫn bạn khám phá YC founders đang dùng Agent làm gì'),
        ('硅谷最火的 Agent 方向拆解', 'Phân tích hướng Agent nóng nhất Silicon Valley'),
        ('从 Demo 到赚钱的完整路径', 'Lộ trình hoàn chỉnh từ Demo đến kiếm tiền'),
        ('可规模化Agent的安全兼容性', 'Tương thích bảo mật của Agent có thể mở rộng quy mô'),
        ('养虾经验谈：我睡觉，虾剪片', 'Kinh nghiệm nuôi tôm: Tôi ngủ, tôm cắt phim'),
        ('养虾经验谈：我睡觉，虾赚钱', 'Kinh nghiệm nuôi tôm: Tôi ngủ, tôm kiếm tiền'),
        ('—— 广告、产品、品牌片全搞定', '— Quảng cáo, sản phẩm, phim thương hiệu xong hết'),
        ('今天晚上百度千帆开发者带你解锁新姿势：', 'Tối nay nhà phát triển Baidu Qianfan dẫn bạn mở khóa tư thế mới:'),
        ('用 OpenClaw 实现全自动 AI 剪辑', 'Dùng OpenClaw thực hiện biên tập AI hoàn toàn tự động'),
        ('你只管放心睡觉，小虾帮你剪片！', 'Bạn cứ yên tâm ngủ, tôm nhỏ giúp bạn cắt phim!'),
        ('AI 全自动剪片流程，从脚本→成片一步到位', 'Quy trình cắt phim AI hoàn toàn tự động, từ kịch bản→thành phẩm một bước xong'),
        ('爆款视频一键复刻，一只虾就是一个剪辑团队', 'Video hot nhân bản một nút, một con tôm chính là một đội biên tập'),
        ('解放双手，大幅提升内容产出效率', 'Giải phóng đôi tay, nâng cao đáng kể hiệu suất sản xuất nội dung'),
        ('从概念到实操，手把手教你玩转GEO！', 'Từ khái niệm đến thực hành, hướng dẫn từng bước chơi thành thạo GEO!'),
        ('前TikTok商业化AI产品经理、AI自媒体人', 'Cựu Quản lý sản phẩm AI thương mại hóa TikTok, KOL AI'),
        ('前好未来学而思网校营销负责人、猎河科技CEO', 'Cựu Phụ trách marketing Xueersi Online TAL Education, CEO Liehe Technology'),
        ('AI 搜索正在偷走你的流量？来聊聊怎么让 AI 主动引用你！', 'AI search đang đánh cắp lưu lượng của bạn? Hãy bàn cách để AI chủ động trích dẫn bạn!'),
        ('当用户不再点击链接，而是直接看 AI 给的答案，你的内容还能被看到吗？', 'Khi người dùng không còn nhấp vào liên kết, mà trực tiếp xem câu trả lời AI đưa ra, nội dung của bạn còn được nhìn thấy không?'),
        ('带你揭秘ALL-IN-ONE 的 Agent 工作空间', 'Dẫn bạn khám phá không gian làm việc Agent ALL-IN-ONE'),
        ('出国点餐一条龙 Builder', 'Builder gọi món nước ngoài trọn gói'),
        ('社区共创者', 'Đồng sáng tạo cộng đồng'),
        ('带你解锁首个为一人公司打造的 AI 工作空间', 'Dẫn bạn mở khóa không gian làm việc AI đầu tiên dành cho công ty một người'),
        ('一键连接3500+工具，实现本地与云端文件一站式管理', 'Một nút kết nối 3500+ công cụ, quản lý file cục bộ và đám mây tất cả trong một'),
        ('参与直播即可领取社区专属积分兑换码', 'Tham gia livestream nhận mã đổi điểm độc quyền cộng đồng'),
        ('秒哒全球首发应用生成Skill，🦞帮你做应用', 'Miaoda ra mắt toàn cầu Skill tạo ứng dụng, 🦞giúp bạn làm ứng dụng'),
        ('营销增长与SEO优化全攻略', 'Toàn bộ chiến lược tăng trưởng marketing và tối ưu SEO'),
        ('对准科技创始人', 'Nhà sáng lập Duizhun Technology'),
        ('增长专家，三年实战经验，服务 100+ 产品', 'Chuyên gia tăng trưởng, ba năm kinh nghiệm thực chiến, phục vụ 100+ sản phẩm'),
        ('擅长 SEO、内容营销、外链建设和增长策略', 'Giỏi về SEO, marketing nội dung, xây dựng liên kết ngoài và chiến lược tăng trưởng'),
        ('掌握144 项Skills，实现精准获客与稳定增长', 'Nắm vững 144 Skills, thực hiện thu hút khách chính xác và tăng trưởng ổn định'),
        ('实战案例复盘，解锁可复用的增长方法论', 'Tổng kết case study thực chiến, mở khóa phương pháp luận tăng trưởng có thể tái sử dụng'),
        ('OpenClaw高玩分享！从扣子养虾到 Vibe Coding大趋势', 'Cao thủ OpenClaw chia sẻ! Từ nuôi tôm trên Coze đến xu hướng lớn Vibe Coding'),
        ('跨5城、30+WaytoAGI社区伙伴共创的2026年度AI贺岁片《老马的AI囧途》幕后分享', 'Xuyên 5 thành phố, 30+ đối tác cộng đồng WaytoAGI đồng sáng tạo phim Tết AI 2026 "Hành trình AI oái oăm của Lão Mã" chia sẻ hậu trường'),
        ('OpenClaw 该上班了！千帆养虾进阶实战', 'OpenClaw đi làm thôi! Thực chiến nâng cao nuôi tôm Qianfan'),
        ('花10分钟用Obsidian+OpenClaw彻底重构你的AI知识管理体系', 'Dành 10 phút dùng Obsidian+OpenClaw hoàn toàn tái cấu trúc hệ thống quản lý kiến thức AI của bạn'),
        ('公众号AI自媒体Top10、视频号AI自媒体Top30、前字节大模型算法工程师', 'Top10 AI KOL tài khoản công khai, Top30 AI KOL kênh video, cựu kỹ sư thuật toán mô hình lớn ByteDance'),
        ('全程实操｜带你用「Obsidian+OpenClaw」构建高效知识管理体系', 'Thực hành toàn bộ | Dẫn bạn dùng "Obsidian+OpenClaw" xây dựng hệ thống quản lý kiến thức hiệu quả'),
        ('避坑指南｜拆解各个工具使用痛点与技巧，助你少走弯路快速上手', 'Hướng dẫn tránh bẫy | Phân tích điểm đau và kỹ thuật sử dụng từng công cụ, giúp bạn ít đi đường vòng nhanh chóng bắt đầu'),
        ('如何突破AI短番量多精品少困局？', 'Làm sao vượt qua tình trạng phim ngắn AI nhiều lượng ít chất?'),
        ('技术开发、中国美院 AIGC 特聘讲师，首批国家级数智设计创作先锋', 'Phát triển kỹ thuật, Giảng viên thỉnh giảng đặc biệt AIGC Học viện Mỹ thuật Trung Quốc, Tiên phong sáng tạo thiết kế số thông minh cấp quốc gia đợt đầu'),
        ('联合创始人，百万粉丝博主，拥有超 10 年影视特效经验', 'Đồng sáng lập, blogger triệu người theo dõi, sở hữu hơn 10 năm kinh nghiệm hiệu ứng phim ảnh'),
        ('拆解 AI 短番从脚本到成片的高效创作流程', 'Phân tích quy trình sáng tạo hiệu quả phim ngắn AI từ kịch bản đến thành phẩm'),
        ('揭秘高质量短番创作的实战技巧与避坑指南', 'Tiết lộ kỹ thuật thực chiến sáng tạo phim ngắn chất lượng cao và hướng dẫn tránh bẫy'),
        ('未来硅世界第12期：Claude Code最佳搭档CC Switch背后的故事', 'Thế giới Silicon tương lai Kỳ 12: Câu chuyện đằng sau CC Switch - đối tác tốt nhất của Claude Code'),
        ('海辛：我给小龙虾造了一个可视化工作间', 'Hải Tân: Tôi đã tạo một không gian làm việc trực quan cho tôm hùm nhỏ'),
        ('从文档到生命体，开启文件即软件新纪元', 'Từ tài liệu đến sinh thể, mở ra kỷ nguyên mới file chính là phần mềm'),
        ('拆解Self Instance：解锁"文件即软件"的终极形态', 'Phân tích Self Instance: Mở khóa hình thái cuối cùng "file chính là phần mềm"'),
        ('架构师面对面：从底层逻辑到实战搭建，全流程打通Selfware', 'Gặp mặt kiến trúc sư: Từ logic nền tảng đến xây dựng thực chiến, xuyên suốt toàn bộ quy trình Selfware'),
        ('今晚是自习室', 'Tối nay là phòng tự học'),
        ('OpenClaw系列课：一天消耗10亿token的龙虾养成记', 'Chuỗi bài OpenClaw: Nhật ký nuôi tôm hùm tiêu thụ 1 tỷ token mỗi ngày'),
        ('对谈 EvoMap创始人：10分钟登顶ClawHub榜首的出圈密码', 'Trò chuyện với nhà sáng lập EvoMap: Bí quyết viral lên đỉnh ClawHub trong 10 phút'),
        ('怎样做出2500万曝光的 Seedance 2.0视频？怪奇物语结局重制复盘', 'Làm thế nào tạo ra video Seedance 2.0 có 25 triệu lượt hiển thị? Tổng kết làm lại kết thúc Stranger Things'),
        ('让 AI 像你一样思考：用 YouMind Skills 打造你的内容系统，实现稳定日更涨粉', 'Để AI suy nghĩ giống bạn: Dùng YouMind Skills xây dựng hệ thống nội dung của bạn, thực hiện đăng bài hàng ngày ổn định tăng người theo dõi'),
        ('用阿里百炼制作拜年视频、春节祝福语音多场景春节祝福文案模板，一次搞定一场直播结束，就能自己动手做春节祝福内容', 'Dùng Alibaba Bách Luyện làm video chúc Tết, giọng nói chúc Tết đa kịch bản mẫu nội dung chúc Tết, một lần xong một buổi livestream kết thúc, là có thể tự tay làm nội dung chúc Tết'),
        ('直播嘉宾：电波曲奇', 'Khách mời livestream: Điện Ba Khúc Kỳ'),
        ('如何用 YouMind 拥有源源不断的选题+持续稳定输出爆款内容', 'Làm sao dùng YouMind có nguồn đề tài vô tận + sản xuất liên tục ổn định nội dung hot'),
        ('百度千帆发布的7款Skill ，手把手教你一键部署属于自己的 AI 助理', 'Baidu Qianfan ra mắt 7 Skill, hướng dẫn từng bước triển khai AI trợ lý của riêng bạn chỉ với một nút bấm'),
        ('AI星企划总决赛', 'Chung kết Kế hoạch Ngôi sao AI'),
        ('玩转新春 · 年味开始了', 'Chơi thành thạo Năm mới · Hương vị Tết bắt đầu rồi'),
        ('百炼上手零门槛，轻松做新年内容', 'Bách Luyện dễ sử dụng không rào cản, dễ dàng làm nội dung Năm mới'),
        ('AI 福字、年货清单、窗花剪纸一站式搞定', 'Chữ phúc AI, danh sách hàng Tết, cắt giấy trang trí cửa sổ tất cả trong một'),
        ('年夜饭 & 菜谱大全，解决"过年吃什么"', 'Bữa cơm tất niên & toàn tập công thức, giải quyết "ăn gì ngày Tết"'),
        ('不讲复杂概念，直接把 AI 变成年味工具箱', 'Không nói khái niệm phức tạp, trực tiếp biến AI thành hộp công cụ Tết'),
        ('大厂 AI 产品专家｜独立开发者｜小红书 AI 博主', 'Chuyên gia sản phẩm AI công ty lớn | Nhà phát triển độc lập | Blogger AI Xiaohongshu'),
        ('今晚20:00直播｜带你深度解析AI硬件 x AI应用开发', 'Livestream tối nay 20:00 | Dẫn bạn phân tích chuyên sâu phần cứng AI x phát triển ứng dụng AI'),
        ('银海（AI产品经理）', 'Ngân Hải (Quản lý sản phẩm AI)'),
        ('拆解AI眼镜核心能力与落地场景', 'Phân tích năng lực cốt lõi kính AI và kịch bản triển khai'),
        ('手把手带你搭建智能体工作流', 'Hướng dẫn từng bước xây dựng quy trình làm việc trí tuệ thể'),
        ('`智能纪要：02-07 | 今天不卷了，让TRAE Skill干活！', '`Biên bản thông minh: 02-07 | Hôm nay không cuộn nữa, để TRAE Skill làm việc!'),
        ('YouMind 0.8 正式发布 让每一个人都能成为内容创作者', 'YouMind 0.8 chính thức ra mắt Để mỗi người đều có thể trở thành nhà sáng tạo nội dung'),
        ('鹿演Vol.009：QVeris：让你的AI Agent用一个接口调用上万种数据和工具', 'Lộc Diễn Vol.009: QVeris: Để AI Agent của bạn dùng một API gọi hàng vạn loại dữ liệu và công cụ'),
        ('曲东奇｜QVeris合伙人、产品运营', 'Khúc Đông Kỳ | Đối tác QVeris, Vận hành sản phẩm'),
        ('主持人：张蔚', 'Người dẫn chương trình: Zhang Wei'),
        ('WaytoAGI孵化负责人｜心流资本合伙人', 'Phụ trách ươm tạo WaytoAGI | Đối tác Xinliu Capital'),
        ('技术大V都在用秒哒整什么活', 'KOL công nghệ đều đang dùng Miaoda làm trò gì'),
        ('AI办公高效收尾：百炼模板一键搞定节前工作', 'AI văn phòng hoàn thành hiệu quả: Mẫu Bách Luyện một nút xong công việc trước kỳ nghỉ'),
        ('上百度智能云部署OpenClaw/moltbot/clawdbot', 'Triển khai OpenClaw/moltbot/clawdbot trên Baidu Smart Cloud'),
        ('用这个Agent Skills Builder批量复刻Clawdbot', 'Dùng Agent Skills Builder này nhân bản hàng loạt Clawdbot'),
        ('语音AI输入法开发实战攻略与避坑指南', 'Chiến lược thực chiến phát triển bàn phím AI giọng nói và hướng dẫn tránh bẫy'),
        ('未来硅世界第11期：AI 审美浪潮下的哲学追问与反思', 'Thế giới Silicon tương lai Kỳ 11: Truy vấn triết học và phản tư trong làn sóng thẩm mỹ AI'),
        ('普通小白也能使用的云端clawdbot/moltbot/openclaw', 'clawdbot/moltbot/openclaw đám mây mà người mới bình thường cũng dùng được'),
        ('ListenHub 2.0上新：手把手教你一站式AI创作', 'ListenHub 2.0 ra mắt tính năng mới: Hướng dẫn từng bước sáng tạo AI tất cả trong một'),
        ('文心5.0 +千帆：零门槛玩转Agent开发', 'Wenxin 5.0 + Qianfan: Không rào cản chơi thành thạo phát triển Agent'),
        ('Clawdbot手把手部署指南——打造一个真正的AI助理', 'Hướng dẫn triển khai Clawdbot từng bước — xây dựng một AI trợ lý thực sự'),
        ('AI 时代下，如何快速开发 3D 游戏？48 小时极限开发实战复盘', 'Trong kỷ nguyên AI, làm sao phát triển nhanh game 3D? Tổng kết thực chiến phát triển cực hạn 48 giờ'),
        ('特邀嘉宾00后全流程游戏制作人：宣酱 &周杰zdj', 'Khách mời đặc biệt nhà sản xuất game toàn quy trình gen Z: Tuyên Tương & Chu Kiệt zdj'),
        ('手把手带你玩转开源版Claude Code——Kode Agent', 'Hướng dẫn từng bước chơi thành thạo phiên bản mã nguồn mở Claude Code — Kode Agent'),
        ('来新璐：ShareAI Lab 创始人、Kode Agent（开源版Claude Code Agent）开发者', 'Lai Xinlu: Nhà sáng lập ShareAI Lab, Nhà phát triển Kode Agent (Agent Claude Code mã nguồn mở)'),
        ('深度解析 Claude Code 原理&机制设计，以及教你从 0 到 1 手搓一个迷你 Claude Code 分享人：ShareAI 来新璐', 'Phân tích chuyên sâu nguyên lý & thiết kế cơ chế Claude Code, cùng dạy bạn từ 0 đến 1 tự tay làm Claude Code mini Người chia sẻ: ShareAI Lai Xinlu'),
        ('MiniMax Agent 2.0深度实测！AI原生工作台如何解放双手？', 'Test chuyên sâu MiniMax Agent 2.0! Bàn làm việc native AI giải phóng đôi tay như thế nào?'),
        ('寻鹭 ：MiniMax Agent 产品负责人', 'Tầm Lộ: Phụ trách sản phẩm MiniMax Agent'),
        ('Skills爆改训练营（两日连播）', 'Trại huấn luyện cải tạo Skills (hai ngày liên tiếp)'),
        ('Coze2.0 到底更新了什么 嘉宾：罗文+二师兄', 'Coze2.0 cuối cùng đã cập nhật gì Khách mời: La Văn + Nhị Sư Huynh'),
        ('职场AI，就用扣子——新功能Coze Skill上线', 'AI công sở, cứ dùng Coze — Tính năng mới Coze Skill lên sóng'),
        ('未来硅世界第10期：对话「闪电说」创始人：AI 产品出海的实战指南', 'Thế giới Silicon tương lai Kỳ 10: Đối thoại nhà sáng lập "Shandiansuo": Hướng dẫn thực chiến đưa sản phẩm AI ra nước ngoài'),
        ('龚震：闪电说联合创始人，增长&商业化负责人', 'Cung Chấn: Đồng sáng lập Shandiansuo, Phụ trách tăng trưởng & thương mại hóa'),
        ('余猛：闪电说产品经理 & CEO', 'Dư Mãnh: Quản lý sản phẩm & CEO Shandiansuo'),
        ('主持团：向阳乔木、姚全刚、尼克西、元子', 'Đội dẫn chương trình: Hướng Dương Kiều Mộc, Diêu Toàn Cương, Nick West, Yuan Zi'),
        ('PixVerse R1—全球首个实时生成世界模型正式上线', 'PixVerse R1 — Mô hình thế giới tạo thời gian thực đầu tiên toàn cầu chính thức lên sóng'),
        ('鹿演Vol.008：AOE：不只是Claude Cowork，而是Vibe Working', 'Lộc Diễn Vol.008: AOE: Không chỉ là Claude Cowork, mà là Vibe Working'),
        ('谭少卿：AOE CEO & Co-Founder', 'Đàm Thiếu Khanh: AOE CEO & Co-Founder'),
        ('李俊：AOE 增长负责人 & Co-Founder', 'Lý Tuấn: Phụ trách tăng trưởng AOE & Co-Founder'),
        ('开年重磅！海辛&阿文AI工作流分享', 'Trọng điểm đầu năm! Hải Tân & A Văn chia sẻ quy trình làm việc AI'),
        ('下午15:00直播｜2026CES热乎情报速递，深度解读具身智能与无人驾驶两大赛道', 'Livestream chiều 15:00 | Tin tức nóng hổi CES 2026, giải mã chuyên sâu hai đường đua lớn trí tuệ hiện thân và lái xe tự động'),
        ('王玮滢：哈佛大学计算机博士、具身智能研究科学家、连续创业者', 'Vương Vĩ Dĩnh: Tiến sĩ Khoa học Máy tính Đại học Harvard, Nhà khoa học nghiên cứu trí tuệ hiện thân, Doanh nhân liên tục'),
        ('"秒哒-让创意变生意"应用变现第五期·开放麦圆桌会！', '"Miaoda - Biến sáng tạo thành kinh doanh" Biến ứng dụng thành tiền Kỳ 5 · Hội thảo bàn tròn Open mic!'),
        ('未来硅世界 🔍 揭秘X平台流量密码，3周如何快速涨粉1万+？', 'Thế giới Silicon tương lai 🔍 Tiết lộ bí mật lưu lượng nền tảng X, 3 tuần làm sao tăng nhanh 10k+ người theo dõi?'),
        ('分享爆款提示词技巧，带你避开AI同质化', 'Chia sẻ kỹ thuật prompt hot, dẫn bạn tránh đồng nhất AI'),
        ('今晚20:00直播｜「AI短剧训练营」加餐课：AI视频工具实操技巧速学', 'Livestream tối nay 20:00 | "Trại huấn luyện phim ngắn AI" Bài bổ sung: Học nhanh kỹ thuật thực hành công cụ video AI'),
        ('大鹏：AIGC数字艺术设计高级工程师｜AI动画师｜腾讯SSV数字守艺人', 'Đại Bàng: Kỹ sư cao cấp thiết kế nghệ thuật số AIGC | Họa sĩ hoạt hình AI | Người gìn giữ nghệ thuật số Tencent SSV'),
        ('Lovart/Tapnow 实操课：批量出片 + 动态分层全拿捏', 'Lovart/Tapnow Bài thực hành: Xuất phim hàng loạt + Hoàn toàn nắm bắt phân lớp động'),
        ('周鹏：AIGC广告/ 短剧/动画导演、小红书万粉博主', 'Chu Bằng: Đạo diễn quảng cáo/phim ngắn/hoạt hình AIGC, Blogger vạn người theo dõi Xiaohongshu'),
        ('解锁AI影视广告创作新玩法', 'Mở khóa cách chơi mới sáng tạo quảng cáo phim AI'),
        ('丁一：广告片/ 纪录片导演 / AIGC艺术家', 'Đinh Nhất: Đạo diễn phim quảng cáo/phim tài liệu / Nghệ sĩ AIGC'),
        ('"秒哒-让创意变生意"的应用变现第四期超重磅登场！', '"Miaoda - Biến sáng tạo thành kinh doanh" Biến ứng dụng thành tiền Kỳ 4 xuất hiện hoành tráng!'),
        ('专为视频创作设计的 AI 智能助手，Medeo-今晚教你如何聊出一个好视频！', 'Trợ lý AI thông minh thiết kế chuyên cho sáng tạo video, Medeo - Tối nay dạy bạn cách nói chuyện để tạo video hay!'),
        ('分享嘉宾：晨然/', 'Diễn giả chia sẻ: Thần Nhiên/'),
        ('未来硅世界第八期：深挖近两年AI进化真相，解锁常用AI工具清单', 'Thế giới Silicon tương lai Kỳ 8: Đào sâu sự thật tiến hóa AI hai năm gần đây, mở khóa danh sách công cụ AI thường dùng'),
        ('🔥千问APP上线全新「AI小剧场」功能！体验Sora2同款玩法！', '🔥Qwen APP ra mắt chức năng "Rạp chiếu nhỏ AI" hoàn toàn mới! Trải nghiệm cách chơi cùng kiểu Sora2!'),
        ('"秒哒-让创意变生意"的应用变现教学系列第三期来咯！', '"Miaoda - Biến sáng tạo thành kinh doanh" Chuỗi giảng dạy biến ứng dụng thành tiền Kỳ 3 đến rồi!'),
        ('Claude Code 进阶教程：手把手玩转 MCP、Skills 等工具！', 'Claude Code hướng dẫn nâng cao: Hướng dẫn từng bước chơi thành thạo MCP, Skills và các công cụ khác!'),
        ('Claude Code/CodeX+Skills安装配置全攻略', 'Toàn bộ chiến lược cài đặt cấu hình Claude Code/CodeX+Skills'),
        ('如何用AI做IP形象/', 'Làm sao dùng AI tạo hình ảnh IP/'),
        ('AI短剧训练营:开营第1课', 'Trại huấn luyện phim ngắn AI: Khai mạc Bài 1'),
        ('《短剧行业现状与爆款观片》主讲:夜游榊', '"Hiện trạng ngành phim ngắn và xem phim hot" Giảng viên: Dạ Du Thần'),
        ('先看清这个行业在"赚谁的钱"，再决定你要不要进来', 'Trước hết nhìn rõ ngành này đang "kiếm tiền của ai", rồi quyết định bạn có muốn vào không'),
        ('AI+教育', 'AI + Giáo dục'),
        ('少儿AI春晚-绘本共学屋，孩子的创意海报', 'Gala AI thiếu nhi - Phòng đọc truyện tranh cùng học, poster sáng tạo của trẻ'),
        ('AI音乐零基础入门之Suno实操｜百度「AI星企划」数字角色选秀大赛创作指南', 'Nhập môn Âm nhạc AI không cần nền tảng - Thực hành Suno | Hướng dẫn sáng tạo Cuộc thi tuyển chọn nhân vật số Baidu "Kế hoạch Ngôi sao AI"'),
        ('【JKMiles】', '【JKMiles】'),
        ('华腾杯全国AI作品创新大奖赛全国金奖', 'Giải vàng toàn quốc Cuộc thi sáng tạo tác phẩm AI Cúp Hoa Đằng'),
        ('WaytoAGI社区共创者', 'Đồng sáng tạo cộng đồng WaytoAGI'),
        ('"秒哒-让创意变生意"的应用变现教学讲解系列第一期来啦！', '"Miaoda - Biến sáng tạo thành kinh doanh" Chuỗi giảng dạy biến ứng dụng thành tiền Kỳ 1 đến rồi!'),
        ('MCP插件召集令插件开发大赛冲刺倒计时6天！百宝箱 |通义灵码|', 'Lệnh triệu tập plugin MCP Cuộc thi phát triển plugin đếm ngược nước rút 6 ngày! Hộp bảo bối | Tongyi Lingma |'),
        ('吴昞：国际知名房地产咨询外企高级财务经理、WaytoAGI赛事先锋官', 'Ngô Bỉnh: Quản lý tài chính cao cấp công ty nước ngoài tư vấn bất động sản quốc tế nổi tiếng, Tiên phong sự kiện thi đấu WaytoAGI'),
        ('孔立刚：世界五百强企业供应链管理专家、WaytoAGI赛事先锋官', 'Khổng Lập Cương: Chuyên gia quản lý chuỗi cung ứng doanh nghiệp Fortune 500, Tiên phong sự kiện thi đấu WaytoAGI'),
        ('百度×乐华娱乐×WaytoAGI「AI星企划」数字角色选秀大赛正式启动！', 'Baidu × Yuehua Entertainment × WaytoAGI "Kế hoạch Ngôi sao AI" Cuộc thi tuyển chọn nhân vật số chính thức khởi động!'),
        ('鹿演Vol.005：Creaibo——专为优质内容而生的AI🎙️', 'Lộc Diễn Vol.005: Creaibo — AI chuyên dành cho nội dung chất lượng 🎙️'),
        ('千问APP众测', 'Test cộng đồng Qwen APP'),
        ('MCP插件召集令插件开发大赛攻略来袭 💰奖金池丰富：解锁16万巨额现金激励🔥保姆式教程带你轻松上手', 'Lệnh triệu tập plugin MCP Cuộc thi phát triển plugin chiến lược đến rồi 💰Quỹ tiền thưởng phong phú: Mở khóa 160k tiền mặt khuyến khích khổng lồ 🔥Hướng dẫn chi tiết giúp bạn dễ dàng bắt đầu'),
        ('进阶冲刺！豆包应用创作零门槛创作赛进阶攻略来袭', 'Nước rút nâng cao! Chiến lược nâng cao cuộc thi sáng tạo không rào cản ứng dụng Doubao đến rồi'),
        ('Nano Banana Pro众测，重磅嘉宾：苍何+梦飞+小歪', 'Test cộng đồng Nano Banana Pro, Khách mời trọng điểm: Thương Hà + Mộng Phi + Tiểu Oai'),
        ('未来硅世界-第六期 ：AI与未来的生活', 'Thế giới Silicon tương lai Kỳ 6: AI và cuộc sống tương lai'),
        ('「AI智能体训练营」第二期，第八节：Demo Day:从0到1交付完整AI应用', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2, Buổi 8: Demo Day: Giao từ 0 đến 1 ứng dụng AI hoàn chỉnh'),
        ('企业场景MCP插件召集令插件开发大赛启动，百宝箱丨通义灵码丨', 'Cuộc thi phát triển plugin MCP kịch bản doanh nghiệp khởi động, Hộp bảo bối | Tongyi Lingma |'),
        ('「AI智能体训练营」第二期，第七节：精雕细琢:性能提速&体验翻倍', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2, Buổi 7: Chạm khắc tinh xảo: Tăng tốc hiệu năng & Nhân đôi trải nghiệm'),
        ('千问app众测', 'Test cộng đồng Qwen app'),
        ('「AI智能体训练营」第二期，第六课：多元交互：卡片、图片、语音全覆盖', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2, Bài 6: Tương tác đa dạng: Thẻ, hình ảnh, giọng nói bao phủ toàn diện'),
        ('「AI智能体训练营」第二期，第五课：知识库x记忆:打造Bot专属"最强大脑', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2, Bài 5: Kho kiến thức x bộ nhớ: Xây dựng "bộ não siêu cường" chuyên dành cho Bot'),
        ('AIPO校园AI创投活动优秀项目全国展示，「大学生创意秀」围观同龄人如何玩转飞书！校园场景 + AI 工具的奇妙碰撞，每一个项目都藏着惊喜；', 'Trưng bày dự án xuất sắc toàn quốc hoạt động đầu tư AI campus AIPO, "Show sáng tạo sinh viên" xem bạn bè đồng trang lứa chơi thành thạo Lark! Kịch bản campus + công cụ AI va chạm kỳ diệu, mỗi dự án đều ẩn chứa bất ngờ;'),
        ('「AI智能体训练营」第二期，第四节：工作流进阶：分支、循环、意图识别、图像处理一把掌握', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2, Buổi 4: Quy trình làm việc nâng cao: Nhánh, vòng lặp, nhận dạng ý định, xử lý hình ảnh nắm chắc tất cả'),
        ('带你冲20万大奖，豆包应用创作挑战赛来袭！不止冲奖，更能学硬核技巧，1小时搞定投稿！讲师：许键', 'Dẫn bạn xông tới giải 200k, Cuộc thi thử thách sáng tạo ứng dụng Doubao đến rồi! Không chỉ thi giải, còn học được kỹ thuật chuyên sâu, 1 giờ xong bài nộp! Giảng viên: Hứa Kiện'),
        ('「AI智能体训练营」第二期，第三节：拖拉拽入门：零代码工作流拼出复杂逻辑', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2, Buổi 3: Nhập môn kéo thả: Quy trình làm việc zero-code ghép logic phức tạp'),
        ('11-10|AI也过双十一|藏师傅版"88VIP"福利大放送', '11-10 | AI cũng mua sắm Double 11 | Phúc lợi phiên bản "88VIP" Tạng Sư Phụ đại phóng tặng'),
        ('「AI智能体训练营」第二期，第二节：Prompt魔法:一句话让Bot听懂人话', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2, Buổi 2: Prompt ma thuật: Một câu để Bot hiểu ngôn ngữ con người'),
        ('未来硅世界第五期：畅谈AI与未来生活', 'Thế giới Silicon tương lai Kỳ 5: Bàn về AI và cuộc sống tương lai'),
        ('第三届AIPO校园AI创投活动全国路演', 'Roadshow toàn quốc hoạt động đầu tư AI campus AIPO lần thứ 3'),
        ('「AI智能体训练营」第二期开营仪式，8节直播课带你从0到1打造可上架的AI应用', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2 Lễ khai mạc, 8 buổi livestream dẫn bạn từ 0 đến 1 xây dựng ứng dụng AI có thể lên sàn'),
        ('11-06 | 秒哒又双叒叕上新功能啦！', '11-06 | Miaoda lại ra mắt tính năng mới nữa rồi!'),
        ('校园AIPO猫叔讲提示词', 'Campus AIPO Mèo Thúc giảng về prompt'),
        ('剪映 AI 模板创想季 —20 万奖金 + 千万流量，手把手教你赢赛事！', 'Mùa sáng tạo mẫu AI CapCut — 200k tiền thưởng + hàng chục triệu lưu lượng, hướng dẫn từng bước giúp bạn thắng cuộc thi!'),
        ('WaytoAGI校园AIPO训练营 讲师：AJ 学习AI的工作流', 'Trại huấn luyện campus AIPO WaytoAGI Giảng viên: AJ Quy trình làm việc học AI'),
        ('AI训练营第二期：Agent智能体实战训练营 ，嘉宾：罗文,weina,王立', 'Trại huấn luyện AI Kỳ 2: Trại huấn luyện thực chiến Agent trí tuệ thể, Khách mời: La Văn, Weina, Vương Lập'),
        ('AIPO训练营Part2  - 从 0-1 聚焦校园场景搭建自己的 AI 搭子', 'Trại huấn luyện AIPO Part2 - Từ 0-1 tập trung kịch bản campus xây dựng AI đồng hành của riêng mình'),
        ('AI训练营第一期: n8n训练营结营', 'Trại huấn luyện AI Kỳ 1: Kết thúc trại huấn luyện n8n'),
        ('AIPO 训练营 - 从 0-1 聚焦校园场景搭建自己的 AI 搭子​', 'Trại huấn luyện AIPO - Từ 0-1 tập trung kịch bản campus xây dựng AI đồng hành của riêng mình'),
        ('海外最大AI视频比赛Chroma Awards解读', 'Giải mã Chroma Awards cuộc thi video AI lớn nhất nước ngoài'),
        ('第三届AIPO启动会', 'Hội khởi động AIPO lần thứ 3'),
        ('AI 编程实战技巧分享，30分钟从入门到沉迷｜Vibe Coze！扣子 AI 挑战赛教程💻', 'Chia sẻ kỹ thuật thực chiến lập trình AI, 30 phút từ nhập môn đến say mê | Vibe Coze! Hướng dẫn cuộc thi thử thách AI Coze 💻'),
        ('🎙️IndexTTS：让声音更有温度👨‍🏫 讲师：思绎：bilibili IndexTTS 语音大模型首席算法专家/紫泽：bilibili IndexTTS 算法工程师', '🎙️IndexTTS: Để giọng nói ấm áp hơn 👨‍🏫 Giảng viên: Tư Dịch: Chuyên gia thuật toán trưởng Mô hình lớn giọng nói IndexTTS bilibili / Tử Trạch: Kỹ sư thuật toán IndexTTS bilibili'),
        ('今晚 20:00 直播！拆解 100 万美金AI 工具权益 + 17.5 万奖金的 AI 创意竞赛', 'Livestream tối nay 20:00! Phân tích quyền lợi công cụ AI 1 triệu đô + Cuộc thi sáng tạo AI 175k tiền thưởng'),
        ('AI 编程 & AI 自媒体：避坑脱口秀🎯 🌟特邀嘉宾:言大侠 14 年新媒体运营老兵、AI 独立开发者、AI 自媒体博主、新媒体高级项目负责人。', 'Lập trình AI & KOL AI: Talkshow tránh bẫy 🎯 🌟Khách mời đặc biệt: Ngôn Đại Hiệp 14 năm kinh nghiệm vận hành truyền thông mới, Nhà phát triển độc lập AI, Blogger KOL AI, Phụ trách dự án cao cấp truyền thông mới.'),
        ('【提示未来】赛事解读', 'Giải mã sự kiện thi đấu [Gợi ý Tương lai]'),
        ('WaytoAGI社区第一本书【AI绘画极简入门与应用】正式上线', 'Cuốn sách đầu tiên của cộng đồng WaytoAGI [Nhập môn tối giản và ứng dụng vẽ AI] chính thức lên sóng'),
        ('n8n主题赛​', 'Cuộc thi chủ đề n8n'),
        ('AI训练营第一期 第三课n8n​商单case拆解，带你搭建复杂工作流系统​', 'Trại huấn luyện AI Kỳ 1 Bài 3: Phân tích case đơn hàng thương mại n8n, dẫn bạn xây dựng hệ thống quy trình làm việc phức tạp'),
        ('WaytoAGI「AI训练营」第二课主题：常见#n8n 自动化工作流案例', 'WaytoAGI "Trại huấn luyện AI" Bài 2 Chủ đề: Case quy trình làm việc tự động #n8n thường gặp'),
        ('4天吃透n8n工作流！WaytoAGI「AI训练营」第一期开营！', '4 ngày nắm chắc quy trình làm việc n8n! WaytoAGI "Trại huấn luyện AI" Kỳ 1 khai mạc!'),
        ('「未来硅世界」第四期：AI Agent时代，搜索不再为人而生🔍', '"Thế giới Silicon tương lai" Kỳ 4: Thời đại AI Agent, tìm kiếm không còn sinh ra vì con người 🔍'),
        ('我的AI创业收入清单和AI创业故事💡', 'Danh sách thu nhập khởi nghiệp AI và câu chuyện khởi nghiệp AI của tôi 💡'),
        ('拆解AI时代的学习路径与信息差', 'Phân tích lộ trình học tập và khoảng cách thông tin trong kỷ nguyên AI'),
        ('0-1极速入门 AI·绘画篇', '0-1 nhập môn cực tốc AI · Phần vẽ'),
        ('如何与大语言模型进行对话？（0基础小白极速入门版）', 'Làm sao đối thoại với mô hình ngôn ngữ lớn? (Phiên bản nhập môn cực tốc cho người mới 0 nền tảng)'),
        ('Sora2短剧大赛：现场编写·现场投稿·现场展示', 'Cuộc thi phim ngắn Sora2: Viết tại chỗ · Nộp tại chỗ · Trình diễn tại chỗ'),
        ('Sora2实测，邀请码接力，', 'Test thực tế Sora2, tiếp sức mã mời,'),
        ('切磋大会全国会议', 'Hội nghị giao lưu toàn quốc'),
        ('AI 导演大赛创作分享​🌟特邀嘉宾冰鱼仔、素语、言带你解锁 百度智能创作平台 AI 导演体验，干货满满！', 'Chia sẻ sáng tạo cuộc thi đạo diễn AI 🌟Khách mời đặc biệt Băng Ngư Tử, Tố Ngữ, Ngôn dẫn bạn mở khóa trải nghiệm đạo diễn AI nền tảng sáng tạo thông minh Baidu, đầy đủ kiến thức thực tiễn!'),
        ('10万奖池比赛解说，百度AI追热季 AI・生存・宇宙故事创作视频挑战赛开启！', 'Giải thuyết cuộc thi 100k quỹ giải thưởng, Baidu AI mùa săn hot AI · Sinh tồn · Cuộc thi thử thách sáng tạo video câu chuyện vũ trụ khai mở!'),
        ('#TrickleAI 编程赛火热开启！大奖是iPhone 17 Pro Max  歸藏 /向阳联合教学：Trickle 是一个无缝衔接多模态生成的 Vibe Coding 工具，好上手又强大', '#TrickleAI Cuộc thi lập trình khởi động nóng bỏng! Giải lớn là iPhone 17 Pro Max  Quy Tàng / Hướng Dương giảng dạy phối hợp: Trickle là công cụ Vibe Coding kết nối liền mạch tạo đa phương thức, dễ sử dụng lại mạnh mẽ'),
        ('AI 导演大赛🌟工程师深度拆解「百度智能视频创作」玩法', 'Cuộc thi đạo diễn AI 🌟Kỹ sư phân tích chuyên sâu cách chơi "Sáng tạo video thông minh Baidu"'),
        ('飞书多维表格接入即梦4.0，今晚王大仙教你玩出花', 'Bảng đa chiều Lark kết nối Jimeng 4.0, tối nay Vương Đại Tiên dạy bạn chơi sáng tạo'),
        ('百度世界 × 小红书科技联合呈现秒哒黑客松大赛权威解读', 'Baidu World × Xiaohongshu Tech đồng trình bày giải mã chính thức cuộc thi hackathon Miaoda'),
        ('从 0 到 1 部署正式网站！零基础也可以玩转 AI 编程', 'Từ 0 đến 1 triển khai website chính thức! Không cần nền tảng cũng có thể chơi thành thạo lập trình AI'),
        ('用Cursor+Zion搭建AI应用MVP 即刻变现!', 'Dùng Cursor+Zion xây dựng MVP ứng dụng AI biến thành tiền ngay!'),
        ('智能体工作流设计模式教学，', 'Giảng dạy mẫu thiết kế quy trình làm việc trí tuệ thể,'),
        ('拆解AI摆摊实验，提炼「商业落地金字塔」完整框架', 'Phân tích thí nghiệm bán hàng rong AI, tinh lọc framework hoàn chỉnh "Kim tự tháp thương mại hóa"'),
        ('Qoder食用说明书：从入门到惊艳', 'Hướng dẫn sử dụng Qoder: Từ nhập môn đến kinh ngạc'),
        ('阿里云百炼 AI Agent 创客开发实战课 讲师：许键', 'Bài thực chiến phát triển AI Agent sáng tạo Alibaba Cloud Bách Luyện Giảng viên: Hứa Kiện'),
        ('Zho：X百万流量，最全NanoBanana指南', 'Zho: X triệu lưu lượng, Hướng dẫn NanoBanana đầy đủ nhất'),
        ('全面盘点Vibe Coding工具，选对工具效率翻倍！主持人：Ben', 'Tổng kiểm kê toàn diện công cụ Vibe Coding, chọn đúng công cụ hiệu suất gấp đôi! Người dẫn: Ben'),
        ('解锁 Qwen-Image 技术秘籍与创作灵感！', 'Mở khóa bí kíp kỹ thuật và cảm hứng sáng tạo Qwen-Image!'),
        ('最强生图模型？nano banana实测 ！', 'Mô hình tạo ảnh mạnh nhất? Test thực tế nano banana!'),
        ('社区伦敦亮相+workshop直播-', 'Cộng đồng xuất hiện tại London + Livestream workshop -'),
        ('🔥 今晚8点！鹿演Vol.004：OpenCreator-内容创作者的一站式画布', '🔥 Tối nay 8 giờ! Lộc Diễn Vol.004: OpenCreator - Canvas tất cả trong một cho nhà sáng tạo nội dung'),
        ('鹿演Vol.003：ListenHub：能帮创作者赚钱的AI嘴替', 'Lộc Diễn Vol.003: ListenHub: AI thay miệng giúp nhà sáng tạo kiếm tiền'),
        ('娜乌斯佳：AI视频最新教程，我AI北京大赛分享', 'Nausatia: Hướng dẫn mới nhất video AI, Chia sẻ cuộc thi AI Bắc Kinh của tôi'),
        ('视频教程08-13 | 一句话让创意到变现的超级工具箱，秒哒使用指南', 'Video hướng dẫn 08-13 | Hộp công cụ siêu cấp biến sáng tạo thành tiền chỉ với một câu, Hướng dẫn sử dụng Miaoda'),
        ('一人如何用AI完成一部动画 - 【瑞克与莫蒂勇闯刻板印象宇宙】', 'Một người làm sao dùng AI hoàn thành một bộ hoạt hình - [Rick và Morty dũng cảm vào vũ trụ định kiến]'),
        ('Coze开源很可能带来"第二波商业化红利"，一起探讨，找到属于你的机遇！', 'Coze mã nguồn mở rất có thể mang lại "đợt chia lợi thương mại hóa thứ hai", cùng thảo luận, tìm cơ hội thuộc về bạn!'),
        ('玩转扣子空间 网页设计新功能上线', 'Chơi thành thạo không gian Coze Tính năng mới thiết kế web lên sóng'),
        ('08-02 | Vibe Coding 迷你黑客松_奇思妙想秀-', '08-02 | Vibe Coding Mini Hackathon_Show ý tưởng sáng tạo -'),
        ('Jaaz - 开源多模态Agent工具首发', 'Jaaz - Ra mắt đầu tiên công cụ Agent đa phương thức mã nguồn mở'),
        ('AI 助手带你玩转数据分析！通义灵码保姆级教学 -', 'AI trợ lý dẫn bạn chơi thành thạo phân tích dữ liệu! Hướng dẫn chi tiết Tongyi Lingma -'),
        ('月入万刀的Agent开发者经验分享， Myshell手把手搭建，', 'Chia sẻ kinh nghiệm nhà phát triển Agent thu nhập vạn đô/tháng, Hướng dẫn xây dựng Myshell từng bước,'),
        ('AI+应用创作第一课：百度秒哒"一句话建应用"实战课', 'Bài 1 sáng tạo AI + ứng dụng: Bài thực chiến "Một câu tạo ứng dụng" Baidu Miaoda'),
        # Common patterns
        # Additional missing translations
        ('今天不卷了，让TRAE Skill干活！', 'Hôm nay không cuộn nữa, để TRAE Skill làm việc!'),
        ('向阳乔木', 'Hướng Dương Kiều Mộc'),
        ('姚金刚', 'Diêu Kim Cương'),
        ('少卿', 'Thiếu Khanh'),
        ('卡尔的AI沃茨', 'Karl AI Watts'),
        ('南墙', 'Nam Tường'),
        ('晨然 Ran', 'Thần Nhiên Ran'),
        ('晨然/', 'Thần Nhiên/'),
        ('🎙️特邀嘉宾', '🎙️Khách mời đặc biệt'),
        ('特邀嘉宾', 'Khách mời đặc biệt'),
        ('"秒哒-让创意变生意"之', '"Miaoda - Biến sáng tạo thành kinh doanh"'),
        ('"秒哒-让创意变生意"的', '"Miaoda - Biến sáng tạo thành kinh doanh"'),
        ('应用变现第四期超重磅登场！', 'Biến ứng dụng thành tiền Kỳ 4 xuất hiện hoành tráng!'),
        ('应用变现教学系列第三期来咯！', 'Chuỗi giảng dạy biến ứng dụng thành tiền Kỳ 3 đến rồi!'),
        ('应用变现教学系列第二期火爆来袭！ 每周四秒哒时间', 'Chuỗi giảng dạy biến ứng dụng thành tiền Kỳ 2 đến cực hot! Mỗi thứ Năm giờ Miaoda'),
        ('应用变现教学讲解系列第一期来啦！', 'Chuỗi giảng dạy biến ứng dụng thành tiền Kỳ 1 đến rồi!'),
        ('专为视频创作设计的 AI 智能助手，Medeo-今晚教你如何聊出一个好视频！ 分享嘉宾：晨然/', 'Trợ lý AI thông minh chuyên cho sáng tạo video, Medeo - Tối nay dạy bạn cách tạo video hay! Diễn giả: Thần Nhiên/'),
        ('进阶教程：手把手玩转 MCP、Skills x等工具！', 'Hướng dẫn nâng cao: Hướng dẫn từng bước chơi thành thạo MCP, Skills và các công cụ khác!'),
        ('Yee\'s AI调香和背后的故事，在社区里成长起来的OPC项目', 'AI pha chế nước hoa của Yee và câu chuyện đằng sau, dự án OPC phát triển trong cộng đồng'),
        ('鹿演 Vol.007：Mulan.pro：从家庭主妇到 AI 公司创始人 普通人真的可以逆袭吗', 'Lộc Diễn Vol.007: Mulan.pro: Từ bà nội trợ đến nhà sáng lập công ty AI - Người thường thực sự có thể lật ngược tình thế?'),
        ('鹿演 Vol.006：Refly.AI 正式开启公测！限量邀请码发放', 'Lộc Diễn Vol.006: Refly.AI chính thức mở beta công khai! Phát hành mã mời giới hạn'),
        ('小白版扣子 /n8nAI自动化工作流，多场景方案直接复刻', 'Coze phiên bản người mới / Quy trình tự động n8n AI, nhân bản trực tiếp giải pháp đa kịch bản'),
        ('先看清这个行业在', 'Trước hết nhìn rõ ngành này đang'),
        ('"赚谁的钱"，再决定你要不要进来', '"kiếm tiền của ai", rồi quyết định bạn có muốn vào không'),
        ('少儿AI春晚-绘本共学屋，孩子们的创意海报', 'Gala AI thiếu nhi - Phòng đọc truyện tranh cùng học, poster sáng tạo của trẻ em'),
        ('少儿AI春晚-绘本共学屋，孩子的创意海报', 'Gala AI thiếu nhi - Phòng đọc truyện tranh cùng học, poster sáng tạo của trẻ'),
        ('MCP插件召集令插件开发大赛攻略来袭', 'Lệnh triệu tập plugin MCP chiến lược cuộc thi phát triển plugin đến rồi'),
        ('奖金池丰富：解锁16万巨额现金激励🔥保姆式教学：全流程系统讲解，直击痛点问题', 'Quỹ giải thưởng phong phú: Mở khóa 160k tiền mặt khuyến khích khổng lồ 🔥Giảng dạy chi tiết: Giảng giải hệ thống toàn quy trình, đánh thẳng vào vấn đề đau'),
        ('📌不写一行代码：用lingma基于FastMCP开发demo一键部署到百宝箱', '📌Không viết một dòng code: Dùng Lingma phát triển demo dựa trên FastMCP triển khai một nút đến Hộp bảo bối'),
        ('今晚20:00 |', 'Tối nay 20:00 |'),
        ('「AI智能体训练营」第二期，第五课：知识库x记忆:打造Bot专属"最强大脑', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2, Bài 5: Kho kiến thức x bộ nhớ: Xây dựng "bộ não siêu cường" chuyên dành cho Bot'),
        ('「AI智能体训练营」第二期，第四节：工作流进阶：分支、循环、意图识别、图像处理一把抓', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2, Buổi 4: Quy trình nâng cao: Nhánh, vòng lặp, nhận dạng ý định, xử lý hình ảnh nắm chắc tất cả'),
        ('未来硅世界第五期：畅谈AI和未来生活', 'Thế giới Silicon tương lai Kỳ 5: Bàn về AI và cuộc sống tương lai'),
        ('未来硅世界-第六期 ：AI和未来的生活', 'Thế giới Silicon tương lai Kỳ 6: AI và cuộc sống tương lai'),
        ('「AI智能体训练营」第二期开营仪式，8节直播课带你从0到1打造可上线的AI应用！第一节', '"Trại huấn luyện trí tuệ thể AI" Kỳ 2 Lễ khai mạc, 8 buổi livestream dẫn bạn từ 0 đến 1 xây dựng ứng dụng AI có thể ra mắt! Buổi 1'),
        ('秒哒又双叒叕上新啦！', 'Miaoda lại ra mắt tính năng mới nữa rồi!'),
        ('AI训练营第二期：Agent智能体实战训练营 ，嘉宾：罗文,weina,王磊,', 'Trại huấn luyện AI Kỳ 2: Trại huấn luyện thực chiến Agent trí tuệ thể, Khách mời: La Văn, Weina, Vương Lỗi,'),
        ('【AI训练营】AI智能体项目实战分享', '"Trại huấn luyện AI" Chia sẻ thực chiến dự án trí tuệ thể AI'),
        ('🎙️IndexTTS：让声音更有温度👨‍🏫 讲师：思绎：bilibili IndexTTS 语音大模型首席算法专家/紫泽：bilibili 语音大模型产品运营专家', '🎙️IndexTTS: Để giọng nói ấm áp hơn 👨‍🏫 Giảng viên: Tư Dịch: Chuyên gia thuật toán trưởng mô hình lớn giọng nói IndexTTS bilibili / Tử Trạch: Chuyên gia vận hành sản phẩm mô hình lớn giọng nói bilibili'),
        ('特邀嘉宾：\n- Davis：Director/ Producer\n-', 'Khách mời đặc biệt:\n- Davis: Director/ Producer\n-'),
        ('AI 编程 & AI 自媒体：避坑脱口秀🎯 🌟特邀嘉宾:言大侠 14 年新媒体运营老兵、', 'Lập trình AI & KOL AI: Talkshow tránh bẫy 🎯 🌟Khách mời đặc biệt: Ngôn Đại Hiệp 14 năm kinh nghiệm vận hành truyền thông mới,'),
        ('脱口秀吐槽小会：10天涨粉5.6w小红书粉丝，2周开发1个小程序卖10万，都踩了什么坑', 'Hội talkshow phàn nàn: 10 ngày tăng 56k người theo dõi Xiaohongshu, 2 tuần phát triển 1 mini app bán 100k, đã dẫm phải bẫy gì'),
        ('如何和大语言模型进行对话？（0基础小白极速入门版）', 'Làm sao đối thoại với mô hình ngôn ngữ lớn? (Phiên bản nhập môn cực tốc cho người mới)'),
        ('从 0 到 1 部署正式网站！零基础也能玩转 AI 编程', 'Từ 0 đến 1 triển khai website chính thức! Không cần nền tảng cũng chơi thành thạo lập trình AI'),
        ('一个人如何用AI完成一部动画 - 【瑞克和莫蒂勇闯刻板印象宇宙】', 'Một người làm sao dùng AI hoàn thành một bộ hoạt hình - [Rick và Morty dũng cảm vào vũ trụ định kiến]'),
        ('Coze开源很可能带来"第二波商业化红利"，一起探讨，找到属于你的机遇！', 'Coze mã nguồn mở rất có thể mang lại "đợt chia lợi thương mại hóa thứ hai", cùng thảo luận, tìm cơ hội thuộc về bạn!'),
        ('分享嘉宾', 'Diễn giả chia sẻ'),
        ('嘉宾：', 'Khách mời: '),
        # More specific fixes
        ('\u201c秒哒-让创意变生意\u201d', '"Miaoda - Biến sáng tạo thành kinh doanh"'),
        ('应用变现第五期\u00b7开放麦圆桌会！', 'Biến ứng dụng thành tiền Kỳ 5 · Hội thảo bàn tròn Open mic!'),
        ('AI调香和背后的故事，在社区里成长起来的OPC项目', 'AI pha chế nước hoa và câu chuyện đằng sau, dự án OPC phát triển trong cộng đồng'),
        ('\u201c赚谁的钱\u201d，再决定你要不要进来', '"kiếm tiền của ai", rồi quyết định bạn có muốn vào không'),
        ('歸藏', 'Quy Tàng'),
        ('莫奈丽莎AI', 'Mona Lisa AI'),
        ('「AI智能体训练营」', '"Trại huấn luyện trí tuệ thể AI"'),
        ('第二期，第五课：知识库x记忆:打造Bot专属\u201c最强大脑', 'Kỳ 2, Bài 5: Kho kiến thức x bộ nhớ: Xây dựng "bộ não siêu cường" chuyên cho Bot'),
        ('Coze开源很可能带来\u201c第二波商业化红利\u201d，一起探讨，找到属于你的机遇！', 'Coze mã nguồn mở rất có thể mang lại "đợt chia lợi thương mại hóa thứ hai", cùng thảo luận, tìm cơ hội thuộc về bạn!'),
        ('AI 编程 & AI 自媒体：避坑脱口秀', 'Lập trình AI & KOL AI: Talkshow tránh bẫy'),
        ('言大侠 14 年新媒体运营老兵、', 'Ngôn Đại Hiệp 14 năm vận hành truyền thông mới,'),
        ('直播核心亮点', 'Điểm nổi bật cốt lõi livestream'),
        ('直播亮点', 'Điểm nổi bật livestream'),
        ('功能亮点', 'Điểm nổi bật chức năng'),
        ('架构师', 'Kiến trúc sư'),
        ('拆解', 'Phân tích'),
        ('解锁', 'Mở khóa'),
        ('文件即软件', 'File chính là phần mềm'),
        ('的终极形态', ' hình thái cuối cùng'),
        ('年夜饭', 'Bữa cơm tất niên'),
        ('菜谱大全', 'Toàn tập công thức'),
        ('解决', 'Giải quyết'),
        ('过年吃什么', 'Ăn gì ngày Tết'),
        ('电波曲奇', 'Điện Ba Khúc Kỳ'),
        ('社区音乐板块共创者', 'Đồng sáng tạo mảng âm nhạc cộng đồng'),
        ('孔立刚', 'Khổng Lập Cương'),
        ('世界五百强售后运营经理', 'Quản lý vận hành hậu mãi Fortune 500'),
        ('训练营优秀结业学员', 'Học viên tốt nghiệp xuất sắc trại huấn luyện'),
        ('助教', 'Trợ giảng'),
        ('联合', 'Liên hiệp'),
        ('大阪世博会合作艺术家', 'Nghệ sĩ hợp tác World Expo Osaka'),
        ('之', ''),
        ('：', ': '),
        ('，', ', '),
        ('、', ', '),
        ('WaytoAGI共学', 'WaytoAGI Cùng học'),
        ('📌特邀嘉宾', '📌Khách mời đặc biệt'),
        ('📌特邀嘉宾：', '📌Khách mời đặc biệt:'),
        ('🎤 特邀嘉宾', '🎤 Khách mời đặc biệt'),
        ('🎤 特邀嘉宾：', '🎤 Khách mời đặc biệt:'),
        ('👨‍💻特邀嘉宾：', '👨‍💻Khách mời đặc biệt:'),
        ('🌟特邀嘉宾：', '🌟Khách mời đặc biệt:'),
        ('🌟特邀嘉宾', '🌟Khách mời đặc biệt'),
        ('💡 直播核心亮点：', '💡 Điểm nổi bật cốt lõi livestream:'),
        ('💡直播核心亮点：', '💡Điểm nổi bật cốt lõi livestream:'),
        ('💡直播亮点：', '💡Điểm nổi bật livestream:'),
        ('🎬 直播亮点：', '🎬 Điểm nổi bật livestream:'),
        ('🎯 直播亮点：', '🎯 Điểm nổi bật livestream:'),
        ('💡功能亮点：', '💡Điểm nổi bật chức năng:'),
        ('分享嘉宾：', 'Diễn giả chia sẻ: '),
        ('直播嘉宾｜', 'Khách mời livestream | '),
        ('发起人', 'Người khởi xướng'),
        ('创始人', 'Nhà sáng lập'),
        ('联合创始人', 'Đồng sáng lập'),
        ('老师', 'Giáo viên'),
        ('​', ''),
        ('晚8点', 'lúc 8 giờ tối'),
    ]

    for cn, vi in replacements:
        if cn in t:
            t = t.replace(cn, vi)

    # Translate dates last
    t = translate_date(t)

    return t

# Apply translations to blocks 116+
for i in range(116, len(result['blocks'])):
    for j, el in enumerate(result['blocks'][i]['elements']):
        if el['type'] == 'text_run':
            orig = data['blocks'][i]['elements'][j]['content']
            result['blocks'][i]['elements'][j]['content'] = translate_smart_minutes(orig)

# Update title
result['title'] = partial['title']

# Count stats
total_text_runs = 0
translated_count = 0
kept_count = 0
cn_remaining = 0

for i, (ob, tb) in enumerate(zip(data['blocks'], result['blocks'])):
    for j, (oe, te) in enumerate(zip(ob['elements'], tb['elements'])):
        if oe['type'] == 'text_run':
            total_text_runs += 1
            if oe['content'] != te['content']:
                translated_count += 1
            else:
                kept_count += 1
            if has_chinese(te['content']):
                cn_remaining += 1

print(f"Total text_runs: {total_text_runs}")
print(f"Translated: {translated_count}")
print(f"Kept as-is: {kept_count}")
print(f"Chinese remaining: {cn_remaining}")

with open('_art19_trans.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("Saved to _art19_trans.json")
