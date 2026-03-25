import json
import re

with open('_art5_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation map: Chinese -> Vietnamese
translations = {}

def t(zh, vi):
    translations[zh] = vi

# Page title
t('3月21日杭州云谷龙虾街区盛大开业', 'Ngày 21/3 Khai trương hoành tráng Khu phố Tôm hùm Vân Cốc Hàng Châu')

# Heading2: 龙虾街区盛大开业！
t('龙虾街区盛大开业！', 'Khu phố Tôm hùm khai trương hoành tráng!')

# Heading3
t('你的虾从出生到上岗全包了', 'Tôm của bạn được lo trọn gói từ lúc ra đời đến khi đi làm')

# Text blocks
t('嘿！欢迎来到杭州阿里云谷中心的\u201c小龙虾街区\u201d！这里不是海鲜市场，而是一个神奇的地方——你将亲眼见证一只只 AI 小龙虾的诞生，从接生到护理，从上学到就业，我们为每一只小龙虾提供全生命周期服务。',
  'Xin chào! Chào mừng bạn đến với "Khu phố Tôm hùm" tại Trung tâm Alibaba Cloud Valley Hàng Châu! Đây không phải chợ hải sản, mà là một nơi kỳ diệu — bạn sẽ tận mắt chứng kiến sự ra đời của từng chú tôm hùm AI, từ đỡ đẻ đến chăm sóc, từ đi học đến đi làm, chúng tôi cung cấp dịch vụ trọn vòng đời cho mỗi chú tôm hùm.')

t('你只需要带上电脑，剩下的交给我们！', 'Bạn chỉ cần mang theo máy tính, phần còn lại để chúng tôi lo!')
t('报名链接', 'Link đăng ký')

# Section: 今天你能得到什么
t('🎁 今天你能得到什么？', '🎁 Hôm nay bạn nhận được gì?')
t('💰 重磅福利：0 元领养小龙虾！', '💰 Phúc lợi khủng: Nhận nuôi tôm hùm 0 đồng!')
t('到场的朋友都能获得 限量', 'Tất cả bạn bè có mặt đều nhận được phiên bản giới hạn')
t('200 元 Pro 版代金券（先到先得）', 'Voucher phiên bản Pro trị giá 200 tệ (ai đến trước được trước)')
t('致老朋友：已经购买阿里云百炼 Coding Plan Pro 用户现已开放 2 只百炼小龙虾的免费领取通道，Lite 版本用户也可获得 1 只 14 天体验权益。',
  'Gửi bạn cũ: Người dùng đã mua Alibaba Cloud Bách Luyện Coding Plan Pro hiện đã mở kênh nhận miễn phí 2 chú tôm hùm Bách Luyện, người dùng phiên bản Lite cũng nhận được quyền trải nghiệm 1 chú trong 14 ngày.')
t('致新朋友：我们要送出一波诚意大礼，百炼小龙虾 Pro 版本，面向云谷中心线下活动的新用户免费限量发放，手慢无，当天领完即止。',
  'Gửi bạn mới: Chúng tôi sẽ tặng một đợt quà tâm huyết, tôm hùm Bách Luyện phiên bản Pro, phát miễn phí giới hạn cho người dùng mới tại sự kiện offline Trung tâm Vân Cốc, chậm tay hết, phát xong trong ngày là dừng.')
t('仅限现场领取，绑定你的专属 UID，独一无二！', 'Chỉ nhận tại chỗ, liên kết UID chuyên dụng của bạn, độc nhất vô nhị!')

# 动手礼物
t('🎨 动手礼物：做就送！', '🎨 Quà tặng thực hành: Làm là có quà!')
t('完成一个 Skill 开发 → 龙虾玩偶/钥匙扣拿走', 'Hoàn thành phát triển một Skill → Mang về búp bê/móc khóa tôm hùm')
t('愿意上台分享 → 龙虾大礼包（T 恤、卫衣、日历、双肩包……）等你抱回家！', 'Sẵn sàng lên sân khấu chia sẻ → Gói quà tôm hùm (áo phông, áo hoodie, lịch, balo...) đang chờ bạn mang về nhà!')

# 龙虾街区地图
t('🗺️ 龙虾街区地图', '🗺️ Bản đồ Khu phố Tôm hùm')
t('整条街区为你的小龙虾提供一条龙服务！', 'Cả khu phố cung cấp dịch vụ trọn gói cho chú tôm hùm của bạn!')

# 接生站
t('🏥 接生站：小龙虾免费部署', '🏥 Trạm đỡ đẻ: Triển khai tôm hùm miễn phí')
t('营业时间', 'Giờ mở cửa')
t('：13:00 开始签到，14:30 正式接生', ': 13:00 bắt đầu check-in, 14:30 chính thức đỡ đẻ')
t('你要做什么？', 'Bạn cần làm gì?')
t('到场签到（别忘了带电脑和手机！）', 'Check-in tại chỗ (đừng quên mang máy tính và điện thoại!)')
t('开通百炼账号，获取你的专属 UID（就像给小龙虾上户口）', 'Mở tài khoản Bách Luyện, nhận UID chuyên dụng của bạn (giống như làm giấy khai sinh cho tôm hùm)')
t('领取\u201c龙虾档案\u201d地图（这是你的通关秘籍）', 'Nhận bản đồ "Hồ sơ Tôm hùm" (đây là bí kíp vượt ải của bạn)')
t('看看大屏幕倒计时，准备迎接激动人心的接生时刻！', 'Xem đồng hồ đếm ngược trên màn hình lớn, chuẩn bị đón khoảnh khắc đỡ đẻ đầy xúc động!')

# 14:30 接生仪式
t('14:30 准时接生仪式！', '14:30 Lễ đỡ đẻ đúng giờ!')
t('远长会亲自主持\u201c小龙虾出生仪式\u201d，宣布 300 张代金券正式发放。你需要用手机扫码，通过你的 UID 抢领属于你的那一张！',
  'Viễn Trường sẽ đích thân chủ trì "Lễ ra đời của tôm hùm", công bố phát hành chính thức 300 voucher. Bạn cần dùng điện thoại quét mã, thông qua UID của bạn để giành lấy tấm voucher thuộc về mình!')
t('温馨提示', 'Lưu ý')
t('：', ':')
t('提前 5 分钟到场，找个好位置', 'Đến sớm 5 phút, tìm chỗ ngồi tốt')
t('手机充好电，网络连接好', 'Sạc đầy điện thoại, kết nối mạng tốt')
t('代金券先到先得，手慢无！', 'Voucher ai đến trước được trước, chậm tay hết!')
t('小贴士', 'Mẹo nhỏ')
t('：新手建议先去龙虾学院听听产品介绍，老手可以直接冲向龙虾写字楼开始创作！',
  ': Người mới nên đến Học viện Tôm hùm nghe giới thiệu sản phẩm trước, người có kinh nghiệm có thể xông thẳng đến Tòa nhà Tôm hùm bắt đầu sáng tạo!')

# 产后护理
t('🛡️ 产后护理：灵魂设定，安全防护', '🛡️ Chăm sóc sau sinh: Thiết lập linh hồn, bảo vệ an toàn')
t('刚出生的小龙虾需要精心呵护！在这里你可以：', 'Tôm hùm mới sinh cần được chăm sóc tỉ mỉ! Tại đây bạn có thể:')
t('设定灵魂', 'Thiết lập linh hồn')
t('：给你的 Skill 起个响亮的名字，写上它的使命', ': Đặt cho Skill của bạn một cái tên ấn tượng, viết sứ mệnh của nó')
t('安全防护', 'Bảo vệ an toàn')
t('：配置权限、设置规则，让你的小龙虾安全成长', ': Cấu hình quyền hạn, thiết lập quy tắc, để tôm hùm của bạn phát triển an toàn')
t('健康检查', 'Kiểm tra sức khỏe')
t('：测试功能是否正常，确保它能顺利上岗', ': Kiểm tra chức năng có hoạt động bình thường không, đảm bảo nó có thể đi làm suôn sẻ')

# 龙虾学院
t('🎓 龙虾学院：技能学习', '🎓 Học viện Tôm hùm: Học kỹ năng')
t('这里是新手的天堂，老手的充电站！', 'Đây là thiên đường của người mới, trạm sạc của người có kinh nghiệm!')
t('课程内容', 'Nội dung khóa học')
t('百炼产品介绍与快速上手', 'Giới thiệu sản phẩm Bách Luyện và bắt đầu nhanh')
t('18 个内置 Skills 使用指南（搜索、文章生成、图像生成、语音识别……）', 'Hướng dẫn sử dụng 18 Skills tích hợp (tìm kiếm, tạo bài viết, tạo hình ảnh, nhận dạng giọng nói...)')
t('开发者实战案例分享（子木、斌子等大神）', 'Chia sẻ case study thực chiến từ nhà phát triển (Tử Mộc, Bân Tử và các cao thủ khác)')
t('远长亲自讲解最新玩法', 'Viễn Trường đích thân giảng giải cách chơi mới nhất')
t('学习方式', 'Hình thức học tập')
t('现场分享会（下午多场次）', 'Buổi chia sẻ tại chỗ (nhiều phiên buổi chiều)')
t('一对一技术咨询', 'Tư vấn kỹ thuật 1-1')
t('开发者交流互动', 'Giao lưu tương tác giữa các nhà phát triển')
t('毕业礼物', 'Quà tốt nghiệp')
t('：学会了就能去写字楼上班，完成作品就能领玩偶！', ': Học xong là có thể đến Tòa nhà đi làm, hoàn thành tác phẩm là nhận búp bê!')

# 龙虾写字楼
t('💼 龙虾写字楼：Skills 黑客松', '💼 Tòa nhà Tôm hùm: Hackathon Skills')
t('这里是创作者的主战场！', 'Đây là chiến trường chính của các nhà sáng tạo!')
t('你可以：', 'Bạn có thể:')
t('用百炼的 18 个内置 Skills 作为积木', 'Sử dụng 18 Skills tích hợp của Bách Luyện làm khối xây dựng')
t('组合出属于你自己的超能力', 'Kết hợp thành siêu năng lực riêng của bạn')
t('完成后提交上墙，立刻领取龙虾玩偶或钥匙扣！', 'Hoàn thành rồi nộp lên tường triển lãm, nhận ngay búp bê hoặc móc khóa tôm hùm!')
t('不会编程？没关系！', 'Không biết lập trình? Không sao!')
t('百炼就是为了让\u201c不会编程的人也能创造 AI 应用\u201d而生的！现场有技术支持，很多 Skill 就像搭积木一样简单。',
  'Bách Luyện được tạo ra chính là để "người không biết lập trình cũng có thể tạo ứng dụng AI"! Tại chỗ có hỗ trợ kỹ thuật, nhiều Skill đơn giản như xếp hình vậy.')
t('工作时长', 'Thời gian làm việc')
t('简单项目：10-30 分钟', 'Dự án đơn giản: 10-30 phút')
t('复杂项目：1-2 小时', 'Dự án phức tạp: 1-2 giờ')
t('不限难度，完成就有礼物！', 'Không giới hạn độ khó, hoàn thành là có quà!')

# 升职加薪
t('升职加薪', 'Thăng chức tăng lương')
t('：\n', ':\n')
t('如果你愿意上台分享你的创作（3-5 分钟就够），我们会送上超级豪华的\u201c龙虾大礼包\u201d——T 恤、卫衣、定制日历、双肩包……应有尽有！',
  'Nếu bạn sẵn sàng lên sân khấu chia sẻ sáng tạo của mình (chỉ cần 3-5 phút), chúng tôi sẽ tặng "Gói quà Tôm hùm" siêu sang — áo phông, áo hoodie, lịch tùy chỉnh, balo... đầy đủ hết!')
t('职业发展', 'Phát triển sự nghiệp')
t('表现优秀者将被邀请参加晚上 19:00 的线上直播，向全网展示你的作品！',
  'Người có thành tích xuất sắc sẽ được mời tham gia livestream online lúc 19:00 tối, trình diễn tác phẩm của bạn cho cả cộng đồng mạng!')
t('现场提供', 'Cung cấp tại chỗ')
t('空白海报模板（A4/A5 大小）', 'Mẫu poster trắng (kích thước A4/A5)')
t('马克笔、NFC 标签', 'Bút marker, thẻ NFC')
t('技术人员一对一指导', 'Nhân viên kỹ thuật hướng dẫn 1-1')
t('你需要做的', 'Những gì bạn cần làm')
t('在模板上手写你的 Skill 名称、主人名、简介', 'Viết tay tên Skill, tên chủ nhân, giới thiệu ngắn lên mẫu')
t('把你的 Skill 链接写入 NFC 标签', 'Ghi link Skill của bạn vào thẻ NFC')
t('贴到展示墙上，让全世界看到你的作品！', 'Dán lên tường triển lãm, để cả thế giới thấy tác phẩm của bạn!')

# 龙虾医院
t('🏥 龙虾医院：技术急诊', '🏥 Bệnh viện Tôm hùm: Cấp cứu kỹ thuật')
t('24 小时待命（活动期间），包治百病！', 'Túc trực 24 giờ (trong suốt sự kiện), chữa bách bệnh!')
t('急诊科室', 'Khoa cấp cứu')
t('Bug 科', 'Khoa Bug')
t('：小龙虾挂了？起死回生大法', ': Tôm hùm bị lỗi? Phép hồi sinh')
t('咨询科', 'Khoa tư vấn')
t('：不知道怎么用某个功能？来这里！', ': Không biết dùng chức năng nào đó? Đến đây!')
t('疑难杂症科', 'Khoa bệnh nan y')
t('：想要深度技术支持？还是来这里！', ': Muốn hỗ trợ kỹ thuật chuyên sâu? Cũng đến đây!')
t('医疗团队', 'Đội ngũ y tế')
t('：现场技术专家随时待命，药到病除！', ': Chuyên gia kỹ thuật tại chỗ luôn sẵn sàng, thuốc đến bệnh khỏi!')
t('就诊流程', 'Quy trình khám bệnh')
t('带上你的电脑', 'Mang theo máy tính của bạn')
t('描述你的问题', 'Mô tả vấn đề của bạn')
t('技术大夫现场诊断', 'Bác sĩ kỹ thuật chẩn đoán tại chỗ')
t('手把手教你解决', 'Cầm tay chỉ việc giúp bạn giải quyết')
t('医疗费用', 'Chi phí y tế')
t('：全免！', ': Miễn phí hoàn toàn!')

# 龙虾超市
t('🛒 龙虾超市：周边 Get', '🛒 Siêu thị Tôm hùm: Săn quà lưu niệm')
t('这里有你想要的一切龙虾周边！', 'Nơi đây có tất cả quà lưu niệm tôm hùm bạn muốn!')
t('货架清单', 'Danh sách hàng hóa')
t('🧸 毛绒玩偶（50-100 个，先到先得）', '🧸 Búp bê nhồi bông (50-100 cái, ai đến trước được trước)')
t('🔑 龙虾钥匙扣（200-300 个，管够）', '🔑 Móc khóa tôm hùm (200-300 cái, đủ dùng)')
t('🎨 贴纸、帆布袋（随便拿）', '🎨 Sticker, túi canvas (lấy thoải mái)')
t('👕 T 恤、卫衣（分享者专属）', '👕 Áo phông, áo hoodie (dành riêng cho người chia sẻ)')
t('📅 定制日历（高价值，限量）', '📅 Lịch tùy chỉnh (giá trị cao, số lượng giới hạn)')
t('🎒 双肩包（豪华礼包专属）', '🎒 Balo (dành riêng cho gói quà sang)')
t('☕ 杯子（惊喜款）', '☕ Cốc (phiên bản bất ngờ)')
t('购买方式', 'Cách nhận')
t('基础款', 'Gói cơ bản')
t('（玩偶/钥匙扣）：完成一个 Skill 开发即可兑换', ' (búp bê/móc khóa): Hoàn thành phát triển một Skill là đổi được')
t('豪华款', 'Gói sang')
t('（大礼包）：上台分享即可获得', ' (gói quà lớn): Lên sân khấu chia sẻ là nhận được')
t('隐藏款', 'Gói ẩn')
t('：看你的运气和表现！', ': Tùy vào vận may và biểu hiện của bạn!')
t('：每人限领一份基础礼物，但分享奖励不限次数哦！', ': Mỗi người chỉ nhận một phần quà cơ bản, nhưng phần thưởng chia sẻ không giới hạn số lần nhé!')

# 一日游玩时间表
t('🕐 一日游玩时间表', '🕐 Lịch trình vui chơi trong ngày')

# 新手快速通关攻略
t('💡 新手快速通关攻略', '💡 Hướng dẫn vượt ải nhanh cho người mới')
t('第一次来？跟着这个路线走准没错：', 'Lần đầu đến? Đi theo lộ trình này chắc chắn không sai:')
t('13:00', '13:00')
t(' 到接生站签到 → 开通百炼 → 领地图', ' Check-in tại Trạm đỡ đẻ → Mở tài khoản Bách Luyện → Nhận bản đồ')
t('13:30', '13:30')
t(' 去龙虾学院听产品介绍（15 分钟快速上手）', ' Đến Học viện Tôm hùm nghe giới thiệu sản phẩm (15 phút bắt đầu nhanh)')
t('14:25', '14:25')
t(' 回到接生站，找个好位置准备接生', ' Quay lại Trạm đỡ đẻ, tìm chỗ tốt chuẩn bị đỡ đẻ')
t('14:30', '14:30')
t(' 抢代金券！', ' Giành voucher!')
t('14:45', '14:45')
t(' 去产后护理区，了解如何设定 Skill', ' Đến khu Chăm sóc sau sinh, tìm hiểu cách thiết lập Skill')
t('15:00', '15:00')
t(' 去龙虾写字楼，在技术支持下做一个简单的 Skill', ' Đến Tòa nhà Tôm hùm, tạo một Skill đơn giản với sự hỗ trợ kỹ thuật')
t('16:00', '16:00')
t(' 遇到问题？去龙虾医院找技术大夫', ' Gặp vấn đề? Đến Bệnh viện Tôm hùm tìm bác sĩ kỹ thuật')
t('16:30', '16:30')
t(' 听听其他开发者的分享，找找灵感', ' Nghe chia sẻ từ các nhà phát triển khác, tìm cảm hứng')
t('17:00', '17:00')
t(' 完成 Skill，去产后护理区上墙展示', ' Hoàn thành Skill, đến khu Chăm sóc sau sinh trưng bày lên tường')
t('17:30', '17:30')
t(' 去龙虾超市领玩偶，带着满满的收获回家！', ' Đến Siêu thị Tôm hùm nhận búp bê, mang đầy chiến lợi phẩm về nhà!')

# 老手进阶玩法
t('🦞 老手进阶玩法', '🦞 Cách chơi nâng cao cho người có kinh nghiệm')
t('已经是百炼老用户？试试这些挑战：', 'Đã là người dùng lâu năm của Bách Luyện? Thử các thử thách này:')
t('🏆 ', '🏆 ')
t('速度挑战', 'Thử thách tốc độ')
t('：30 分钟内完成一个实用 Skill', ': Hoàn thành một Skill thực dụng trong 30 phút')
t('🎨 ', '🎨 ')
t('创意挑战', 'Thử thách sáng tạo')
t('：做一个最有趣/最实用/最脑洞的 Skill', ': Tạo một Skill thú vị nhất/thực dụng nhất/sáng tạo nhất')
t('🎤 ', '🎤 ')
t('分享挑战', 'Thử thách chia sẻ')
t('：上台分享，拿下龙虾大礼包', ': Lên sân khấu chia sẻ, giành Gói quà Tôm hùm')
t('🤝 ', '🤝 ')
t('社交挑战', 'Thử thách giao lưu')
t('：帮助 3 个新手完成他们的第一个 Skill', ': Giúp 3 người mới hoàn thành Skill đầu tiên của họ')
t('🌟 ', '🌟 ')
t('终极挑战', 'Thử thách tối thượng')
t('：被选中参加晚间直播', ': Được chọn tham gia livestream buổi tối')
t('🏅 ', '🏅 ')
t('全能挑战', 'Thử thách toàn năng')
t('：一天内完成 3 个不同类型的 Skill', ': Hoàn thành 3 Skill khác loại trong một ngày')

# 你需要带什么
t('🎒 你需要带什么？', '🎒 Bạn cần mang theo gì?')
t('⚠️ 必备清单', '⚠️ Danh sách cần thiết')
t('✅ ', '✅ ')
t('笔记本电脑', 'Máy tính xách tay')
t('（重要！自带电脑！！！）', '(Quan trọng! Tự mang máy tính!!!)')
t('手机', 'Điện thoại')
t('（充满电！）', '(Sạc đầy pin!)')
t('充电器和充电宝', 'Sạc và pin dự phòng')
t('（活动时间长，记得带）', '(Sự kiện kéo dài, nhớ mang theo)')
t('好奇心和创造力', 'Sự tò mò và sáng tạo')

# 不需要带
t('❌ 不需要带', '❌ Không cần mang')
t('❌ 编程基础（真的不需要！）', '❌ Kiến thức lập trình (thật sự không cần!)')
t('❌ 钱包（代金券免费领，礼物做就送）', '❌ Ví tiền (voucher nhận miễn phí, quà làm xong là tặng)')
t('❌ 紧张感（这里没有考试，只有玩耍）', '❌ Sự lo lắng (ở đây không có thi cử, chỉ có vui chơi)')

# 活动信息
t('📍 活动信息', '📍 Thông tin sự kiện')
t('时间', 'Thời gian')
t('：2026 年 3 月 21 日（周', ': Ngày 21 tháng 3 năm 2026 (Thứ ')
t('六', 'Bảy')
t('）13:00开始\n', ') bắt đầu lúc 13:00\n')
t('地点', 'Địa điểm')
t('：杭州市阿里云谷中心\n', ': Trung tâm Alibaba Cloud Valley, thành phố Hàng Châu\n')
t('报名', 'Đăng ký')
t('：扫描下方二维码填写报名问卷', ': Quét mã QR bên dưới để điền phiếu đăng ký')
t('【扫码报名】 👇', '【Quét mã đăng ký】 👇')
t('（现场也可以直接签到）', '(Tại hiện trường cũng có thể check-in trực tiếp)')

# 常见问题
t('❓ 常见问题', '❓ Câu hỏi thường gặp')
t('Q：我完全不会编程，能参加吗？', 'H: Tôi hoàn toàn không biết lập trình, có thể tham gia không?')
t('A：当然！百炼就是为你设计的。现场有龙虾医院和龙虾学院，技术支持全覆盖。',
  'Đ: Tất nhiên! Bách Luyện được thiết kế chính là dành cho bạn. Tại chỗ có Bệnh viện Tôm hùm và Học viện Tôm hùm, hỗ trợ kỹ thuật toàn diện.')
t('Q：必须带电脑吗？', 'H: Bắt buộc phải mang máy tính không?')
t('A：是的！创作 Skill 需要用到电脑。如果只是来逛逛、听分享，手机也可以。',
  'Đ: Đúng vậy! Tạo Skill cần dùng máy tính. Nếu chỉ đến tham quan, nghe chia sẻ thì điện thoại cũng được.')
t('Q：代金券一定能抢到吗？', 'H: Có chắc chắn giành được voucher không?')
t('A：我们准备了 300 张，只要你到场并准时参加 14:30 的出生仪式，基本都能领到！',
  'Đ: Chúng tôi đã chuẩn bị 300 tấm, chỉ cần bạn có mặt và tham gia đúng giờ Lễ ra đời lúc 14:30, cơ bản đều nhận được!')
t('Q：我能带朋友来吗？', 'H: Tôi có thể dẫn bạn bè đến không?')
t('A：欢迎！但记得让朋友也报名，这样才能领代金券哦。',
  'Đ: Chào đón! Nhưng nhớ cho bạn bè cũng đăng ký, như vậy mới nhận được voucher nhé.')
t('Q：做 Skill 大概需要多久？', 'H: Làm Skill mất khoảng bao lâu?')
t('A：简单的 10-30 分钟，复杂的可能需要 1-2 小时。但完成就有礼物，不限难度！',
  'Đ: Đơn giản thì 10-30 phút, phức tạp có thể cần 1-2 giờ. Nhưng hoàn thành là có quà, không giới hạn độ khó!')
t('Q：我能做多个 Skill 吗？', 'H: Tôi có thể làm nhiều Skill không?')
t('A：当然可以！做得越多，成就感越强。基础礼物每人一份，但分享奖励不限次数！',
  'Đ: Tất nhiên được! Làm càng nhiều, cảm giác thành tựu càng mạnh. Quà cơ bản mỗi người một phần, nhưng phần thưởng chia sẻ không giới hạn số lần!')
t('Q：现场有 Wi-Fi 吗？', 'H: Tại chỗ có Wi-Fi không?')
t('A：有！现场提供网络，但建议自备流量以防万一。',
  'Đ: Có! Tại chỗ cung cấp mạng, nhưng khuyến nghị tự chuẩn bị data phòng khi cần.')
t('Q：可以带小孩来吗？', 'H: Có thể dẫn trẻ em đến không?')
t('A：可以！但活动偏技术向，建议带对编程或 AI 感兴趣的大孩子。',
  'Đ: Được! Nhưng sự kiện thiên về kỹ thuật, khuyến nghị dẫn trẻ lớn có hứng thú với lập trình hoặc AI.')

# 最后的彩蛋
t('🎉 最后的彩蛋', '🎉 Bất ngờ cuối cùng')
t('这次活动只是\u201c小龙虾街区\u201d的第一站，后续还会有 ',
  'Sự kiện lần này chỉ là trạm đầu tiên của "Khu phố Tôm hùm", sau này còn có ')
t('40 城巡游', 'tour 40 thành phố')
t('！', '!')
t('如果你今天玩得开心，别忘了：', 'Nếu hôm nay bạn vui, đừng quên:')
t('把你的 Skill 分享给朋友', 'Chia sẻ Skill của bạn cho bạn bè')
t('在社交媒体上 @ 我们 # 阿里云百炼龙虾服务 #WaytoAGI', 'Tag chúng tôi trên mạng xã hội #AlibabaCoudBachLuyenTomHum #WaytoAGI')
t('期待下一次在你的城市相遇', 'Mong chờ lần gặp tiếp theo tại thành phố của bạn')

# 龙虾街区营业时间
t('🦞 龙虾街区营业时间', '🦞 Giờ mở cửa Khu phố Tôm hùm')
t('开业时间', 'Thời gian khai trương')
t('：2026 年 3 月 21 日 13:00 \n', ': Ngày 21 tháng 3 năm 2026 lúc 13:00 \n')
t('营业地址', 'Địa chỉ')
t('服务承诺', 'Cam kết dịch vụ')
t('：你的虾从出生到上岗全包了！', ': Tôm của bạn được lo trọn gói từ lúc ra đời đến khi đi làm!')
t('准备好了吗？', 'Bạn đã sẵn sàng chưa?')
t('小龙虾们在等你！🦞✨', 'Các chú tôm hùm đang chờ bạn! 🦞✨')
t('记得：', 'Nhớ nhé:')
t('自带电脑！！！', 'Tự mang máy tính!!!')
t('我们 3 月 21 日见！', 'Hẹn gặp ngày 21 tháng 3!')
t('P.S. 龙虾街区六大站点：接生站 → 产后护理 → 龙虾学院 → 龙虾写字楼 → 龙虾医院 → 龙虾超市，一条龙服务，包你满意！',
  'P.S. Sáu trạm của Khu phố Tôm hùm: Trạm đỡ đẻ → Chăm sóc sau sinh → Học viện Tôm hùm → Tòa nhà Tôm hùm → Bệnh viện Tôm hùm → Siêu thị Tôm hùm, dịch vụ trọn gói, đảm bảo hài lòng!')

# URL - keep as is
t('https://waytoagi.feishu.cn/share/base/form/shrcnXWdfyVNiUImM1wLmeiGDUg', 'https://waytoagi.feishu.cn/share/base/form/shrcnXWdfyVNiUImM1wLmeiGDUg')

# newline
t('\n', '\n')

# Apply translations
for block in data['blocks']:
    if 'elements' in block:
        for elem in block['elements']:
            if 'content' in elem and elem['content'] in translations:
                elem['content'] = translations[elem['content']]

# Update title
data['title'] = 'Ngày 21/3 Khai trương hoành tráng Khu phố Tôm hùm Vân Cốc Hàng Châu'

with open('_art5_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Verify no Chinese remains
chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
remaining = []
for i, block in enumerate(data['blocks']):
    if 'elements' in block:
        for elem in block['elements']:
            if 'content' in elem and chinese_pattern.search(elem['content']):
                remaining.append(f'Block {i} ({block["block_id"]}): {repr(elem["content"][:80])}')

if remaining:
    print(f'WARNING: {len(remaining)} elements still have Chinese:')
    for r in remaining:
        print(f'  {r}')
else:
    print('All content translated successfully!')
print(f'Total blocks: {len(data["blocks"])}')
