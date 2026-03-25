# -*- coding: utf-8 -*-
"""Build a properly escaped JSON translation file from a Python dict."""
import json

T = {}

def t(k, v):
    T[k] = v

# Title
t('AI切磋大会22期 3月29日-龙虾街区', 'Đại hội giao lưu AI kỳ 22 ngày 29/3 - Khu phố Tôm hùm')
t('\U0001f99e 小龙虾街区-40个城市同时开展', '\U0001f99e Khu phố Tôm hùm - Diễn ra đồng thời tại 40 thành phố')
t('报名地址：', 'Địa chỉ đăng ký:')
t('参与城市及活动地址', 'Các thành phố tham gia và địa điểm hoạt động')
t('城市名单：国内40', 'Danh sách thành phố: Trong nước 40')
t('海外：马德里，东京，清迈，澳洲悉尼，伦敦', 'Nước ngoài: Madrid, Tokyo, Chiang Mai, Sydney (Úc), London')
t('AI切磋大会3月29日全国场地确认中', 'Đại hội giao lưu AI ngày 29/3 - Đang xác nhận địa điểm toàn quốc')
t('北京、上海、广州、深圳、苏州、杭州、成都、武汉、天津、珠海、中山、重庆、郑州、襄阳、乌鲁木齐、威海、合肥、宁波、常州、西安、南昌、南京、济南、太原、温州、东莞、福州、青岛、昆明、慈溪、汕头、徐州、贵阳、大理、大连、厦门、石家庄、海口、衡水、淮北、沈阳、长春、无锡、湛江、泰国清迈、伦敦、马德里、悉尼、东京',
  'Bắc Kinh, Thượng Hải, Quảng Châu, Thâm Quyến, Tô Châu, Hàng Châu, Thành Đô, Vũ Hán, Thiên Tân, Chu Hải, Trung Sơn, Trùng Khánh, Trịnh Châu, Tương Dương, Urumqi, Uy Hải, Hợp Phì, Ninh Ba, Thường Châu, Tây An, Nam Xương, Nam Kinh, Tế Nam, Thái Nguyên, Ôn Châu, Đông Hoản, Phúc Châu, Thanh Đảo, Côn Minh, Từ Khê, Sán Đầu, Từ Châu, Quý Dương, Đại Lý, Đại Liên, Hạ Môn, Thạch Gia Trang, Hải Khẩu, Hành Thủy, Hoài Bắc, Thẩm Dương, Trường Xuân, Vô Tích, Trạm Giang, Chiang Mai (Thái Lan), London, Madrid, Sydney, Tokyo')
t('每个城市会制作自己城市的对应海报', 'Mỗi thành phố sẽ thiết kế poster tương ứng của riêng mình')
t('例如：下面是悉尼的', 'Ví dụ: Dưới đây là của Sydney')

# Section headings
t('一、核心概念', 'I. Khái niệm cốt lõi')
t('二、街区功能分区', 'II. Phân khu chức năng khu phố')
t('三、线上联动：龙虾实时地图', 'III. Liên kết trực tuyến: Bản đồ tôm hùm thời gian thực')
t('四、落地形式', 'IV. Hình thức triển khai')
t('五、商业价值', 'V. Giá trị thương mại')
t('六、核心价值', 'VI. Giá trị cốt lõi')
t('七、参与城市及活动地址', 'VII. Các thành phố tham gia và địa điểm hoạt động')

# Core concept
t('以当前\u201c小龙虾\u201d（openclaw项目）的爆发式热度为契机，打',
  'Nhân cơ hội bùng nổ của \u201cTôm hùm\u201d (dự án openclaw), tạo')
t('造一个沉浸式的', ' ra một')
t('\u201c龙虾街区\u201d', '\u201cKhu phố Tôm hùm\u201d')
t('主题体验空间\u2014\u2014将 AI 开发者社区活动包装成一条充满烟火气与科技感的\u201c商业街\u201d，让高手与小白在同一个场景中自然交融，既贴合当下热点，让大家都有收获',
  ' không gian trải nghiệm chủ đề nhập vai \u2014 biến hoạt động cộng đồng nhà phát triển AI thành một \u201cphố thương mại\u201d đầy hơi thở cuộc sống và cảm giác công nghệ, để người giỏi và người mới cùng hòa nhập tự nhiên trong cùng một bối cảnh, vừa bắt kịp xu hướng nóng, vừa giúp mọi người đều có thu hoạch')
t('。', '.')
t('报名链接：', 'Link đăng ký:')
t('2026年03月29日（周日） 13:00  - 18:00', 'Ngày 29/03/2026 (Chủ nhật) 13:00 - 18:00')
t('距离AI切磋大会第2', 'Còn cách Đại hội giao lưu AI kỳ thứ 2')
t('期线下活动开启时间还有：', ' hoạt động offline bắt đầu:')
t('物料：地图指示牌（玩法说明书）', 'Vật liệu: Biển chỉ dẫn bản đồ (Sách hướng dẫn cách chơi)')

# Zone 1
t('\U0001f99e 1. 小龙虾出生地（入口·品牌装机区）', '\U0001f99e 1. Nơi sinh Tôm hùm (Lối vào - Khu cài đặt thương hiệu)')
t('定位：', 'Định vị:')
t(' 街区的第一站，用户进入后的首个体验环节。', ' Trạm đầu tiên của khu phố, trải nghiệm đầu tiên khi người dùng bước vào.')
t('一排\u201c铺子\u201d对应各家厂商品牌，用户在这里完成装机体验\u2014\u2014\u201c你想吃谁家的小龙虾，就去谁家的铺子\u201d。每个铺位由一家厂商/品牌入驻，提供产品安装、试用和互动演示，用户自主选择感兴趣的品牌进行体验。',
  'Một dãy \u201ccửa hàng\u201d tương ứng với các thương hiệu nhà sản xuất, người dùng hoàn thành trải nghiệm cài đặt tại đây \u2014 \u201cBạn muốn ăn tôm hùm nhà nào thì đến cửa hàng nhà đó\u201d. Mỗi gian hàng do một nhà sản xuất/thương hiệu đặt chỗ, cung cấp cài đặt sản phẩm, dùng thử và demo tương tác, người dùng tự chọn thương hiệu quan tâm để trải nghiệm.')
t('物料：出生证明（包含编号，小龙虾名字，性别，时间，地址，接生医生姓名）电子版出生证明（3:4比例发小红书）',
  'Vật liệu: Giấy khai sinh (bao gồm số hiệu, tên tôm hùm, giới tính, thời gian, địa chỉ, tên bác sĩ đỡ đẻ) Giấy khai sinh điện tử (tỷ lệ 3:4 đăng Xiaohongshu)')
t('准备： 每个城市一只接生虾，做虾的档案登记（日后可以虾和虾联络）',
  'Chuẩn bị: Mỗi thành phố một con tôm đỡ đẻ, làm hồ sơ đăng ký tôm (sau này tôm có thể liên lạc với nhau)')
t('设计：虾宝宝，包单布。KT手举牌形式。（如果有物料虾宝宝的玩偶更好）',
  'Thiết kế: Tôm bé, khăn quấn. Dạng bảng KT cầm tay. (Nếu có vật liệu búp bê tôm bé càng tốt)')
t('拍照环节：喜当爹', 'Phần chụp ảnh: Lên chức bố')

# Zone 2
t('\U0001f3e0 2. 小龙虾产后护理（个性化配置·初始化区）', '\U0001f3e0 2. Chăm sóc hậu sản Tôm hùm (Cấu hình cá nhân hóa - Khu khởi tạo)')
t(' 装机后的\u201c月子中心\u201d，让你的小龙虾拥有灵魂。', ' \u201cTrung tâm chăm sóc sau sinh\u201d sau khi cài đặt, giúp tôm hùm của bạn có linh hồn.')
t('用户完成装机后，来这里为自己的 AI 助手进行个性化设置，让它真正成为\u201c你的\u201d小龙虾：',
  'Sau khi người dùng hoàn thành cài đặt, đến đây để thiết lập cá nhân hóa trợ lý AI của mình, biến nó thực sự thành tôm hùm \u201ccủa bạn\u201d:')
t('工具集成', 'Tích hợp công cụ')
t('：配置飞书、QQ、企业微信等 IM 工具，打通工作流', ': Cấu hình Feishu, QQ, WeChat doanh nghiệp và các công cụ IM khác, kết nối quy trình làm việc')
t('人设定制（', 'Tùy chỉnh nhân vật (')
t('）', ')')
t('：设定 AI 助手的性格、说话风格、专业领域等个性化特征', ': Thiết lập tính cách, phong cách nói chuyện, lĩnh vực chuyên môn và các đặc điểm cá nhân hóa của trợ lý AI')
t('安全配置', 'Cấu hình bảo mật')
t('：设置安全问题、隐私保护、访问权限等安全选项', ': Thiết lập câu hỏi bảo mật, bảo vệ quyền riêng tư, quyền truy cập và các tùy chọn bảo mật khác')
t('使用场景预设', 'Cài đặt sẵn kịch bản sử dụng')
t('：根据用户职业（开发者/产品经理/创作者等）推荐最佳配置方案', ': Đề xuất phương án cấu hình tối ưu dựa trên nghề nghiệp người dùng (nhà phát triển/quản lý sản phẩm/nhà sáng tạo...)')
t('由社区志愿者和产品专家提供指导，确保每个用户都能把小龙虾\u201c养\u201d得得心应手。',
  'Được hướng dẫn bởi tình nguyện viên cộng đồng và chuyên gia sản phẩm, đảm bảo mỗi người dùng đều có thể \u201cnuôi\u201d tôm hùm một cách thuần thục.')
t('物料：虾儿童，护理打油诗，', 'Vật liệu: Tôm trẻ em, thơ vui chăm sóc,')
t('真人装扮：金牌月嫂（购买月嫂服，金牌月嫂的铭牌）', 'Hóa trang thật: Bảo mẫu vàng (mua đồ bảo mẫu, biển hiệu bảo mẫu vàng)')
t('拍照选介：满月照', 'Giới thiệu chụp ảnh: Ảnh đầy tháng')

# Zone 3
t('\U0001f3e5 3. 龙虾医院-虾疗（技术支持·Bug 修复区）', '\U0001f3e5 3. Bệnh viện Tôm hùm - Tôm liệu pháp (Hỗ trợ kỹ thuật - Khu sửa Bug)')
t(' 装机后的\u201c急救站\u201d。', ' \u201cTrạm cấp cứu\u201d sau khi cài đặt.')
t('用户在装机过程中遇到的任何 Bug、兼容性问题、配置疑难，都可以来这里\u201c抢救你的小龙虾\u201d。由技术志愿者和社区高手坐诊，提供一对一的问题排查与解决方案，既实用又有趣。',
  'Mọi Bug, vấn đề tương thích, khó khăn cấu hình mà người dùng gặp trong quá trình cài đặt đều có thể đến đây để \u201ccấp cứu tôm hùm của bạn\u201d. Các tình nguyện viên kỹ thuật và cao thủ cộng đồng trực khám, cung cấp giải pháp xử lý sự cố 1-1, vừa thiết thực vừa thú vị.')
t('物料：残废虾，', 'Vật liệu: Tôm tàn phế,')

# Zone 4
t('\U0001f4da 4. 龙虾学院 （技能学习中心，Skills 培训区）', '\U0001f4da 4. Học viện Tôm hùm (Trung tâm học kỹ năng, Khu đào tạo Skills)')
t(' 从装机到上手的能力跃迁空间。', ' Không gian nâng cấp năng lực từ cài đặt đến thành thạo.')
t('设定一个定时任务', 'Thiết lập một tác vụ hẹn giờ')
t('安装n个skills', 'Cài đặt n skills')
t('面向小白用户，提供龙虾相关 Skills 的教学与实操。课程内容来源于黑客松的优秀成果\u2014\u2014高手们在隔壁做出来的 Skills，小白们在这里直接学习和安装使用，形成\u201c创造\u2192传播\u2192学习\u201d的闭环。',
  'Hướng đến người dùng mới, cung cấp giảng dạy và thực hành Skills liên quan đến tôm hùm. Nội dung khóa học đến từ thành quả xuất sắc của hackathon \u2014 Skills mà các cao thủ tạo ra ở bên cạnh, người mới ở đây trực tiếp học và cài đặt sử dụng, hình thành vòng khép kín \u201cSáng tạo \u2192 Lan tỏa \u2192 Học hỏi\u201d.')
t('技能可以是卡片（nfc）形式，直接复制命令就可以安装，仅需手机即可',
  'Kỹ năng có thể ở dạng thẻ (NFC), chỉ cần sao chép lệnh là có thể cài đặt, chỉ cần điện thoại là đủ')
t('物料：抓周，抓技能（套圈）。培训班/鸡娃，转盘，摇签，解签',
  'Vật liệu: Bốc thăm tuổi, bắt kỹ năng (ném vòng). Lớp đào tạo/ép con học, vòng quay, rút thẻ, giải thẻ')
t('拍照：抓周过程，和你的技能合影', 'Chụp ảnh: Quá trình bốc thăm, chụp ảnh cùng kỹ năng của bạn')
t('安装好skills之后完成一个skills应用后可以毕业', 'Sau khi cài đặt xong skills và hoàn thành một ứng dụng skills thì có thể tốt nghiệp')
t('形象：教练/ 手举口号\u201c鸡娃\u201d', 'Hình tượng: Huấn luyện viên/ Cầm khẩu hiệu \u201cÉp con học\u201d')
t('物料：学生卡+博士帽+\u201c毕业了\u201d', 'Vật liệu: Thẻ sinh viên + Mũ tiến sĩ + \u201cTốt nghiệp rồi\u201d')

# Zone 5
t('\U0001f3c6 5. 龙虾写字楼考核中心（ Skills 黑客松 创造·竞技区）', '\U0001f3c6 5. Tòa nhà văn phòng Tôm hùm - Trung tâm đánh giá (Skills Hackathon - Khu sáng tạo & thi đấu)')
t(' 街区的核心引擎，高手的主战场。', ' Động cơ cốt lõi của khu phố, chiến trường chính của cao thủ.')
t('以龙虾 Skills 开发为主题的轻量级黑客松，门槛相对较低，参与感强。开发者现场组队、限时开发，产出的优秀 Skills 直接输送到技能学习中心供小白体验，实现高手与小白的价值连接。',
  'Hackathon nhẹ với chủ đề phát triển Skills Tôm hùm, ngưỡng tham gia tương đối thấp, cảm giác tham gia mạnh. Nhà phát triển tổ đội tại chỗ, phát triển giới hạn thời gian, Skills xuất sắc được chuyển thẳng đến trung tâm học kỹ năng cho người mới trải nghiệm, thực hiện kết nối giá trị giữa cao thủ và người mới.')
t('映射到进入职场', 'Ánh xạ đến việc bước vào thị trường lao động')
t('黑客松志愿者：我是老板', 'Tình nguyện viên hackathon: Tôi là sếp')
t('黑客松选手的背后/胸前贴贴纸： 上班虾 牛马虾', 'Dán sticker phía sau/trước ngực thí sinh hackathon: Tôm đi làm, Tôm cày cuốc')
t('拍照：KT板手举牌\u201c卷起来\u201d ', 'Chụp ảnh: Bảng KT cầm tay \u201cCày lên nào\u201d ')

# Zone 6
t('\U0001f381 6. 龙虾超市（文化·周边集市社交区） 技能包实体化', '\U0001f381 6. Siêu thị Tôm hùm (Khu văn hóa - Chợ phụ kiện & giao lưu xã hội) Gói kỹ năng thực thể hóa')
t(' 街区的休闲与社交空间。', ' Không gian giải trí và giao lưu xã hội của khu phố.')
t('售卖/展示龙虾主题周边产品，营造社区文化氛围。这里是拍照打卡、社交破冰的自然场所，让整个街区不只是技术活动，更是一次有温度的社区聚会。',
  'Bán/trưng bày sản phẩm phụ kiện chủ đề tôm hùm, tạo bầu không khí văn hóa cộng đồng. Đây là nơi check-in chụp ảnh, phá băng giao tiếp xã hội một cách tự nhiên, khiến cả khu phố không chỉ là hoạt động công nghệ mà còn là buổi họp mặt cộng đồng đầy ấm áp.')
t('物料：小票', 'Vật liệu: Hóa đơn nhỏ')

# Online map section
t('\u201c海辛阿文\u201d式的互动地图，搭建一个', 'Bản đồ tương tác kiểu \u201cHashing Awen\u201d, xây dựng một')
t('线上实时可视化平台', 'nền tảng trực quan hóa thời gian thực trực tuyến')
t('，让所有人都能看到：', ', cho phép tất cả mọi người đều thấy:')
t('\U0001f534 谁正在\u201c龙虾医院\u201d抢救 Bug', '\U0001f534 Ai đang \u201ccấp cứu\u201d Bug tại \u201cBệnh viện Tôm hùm\u201d')
t('\U0001f4d6 谁正在技能学习中心学习 Skills', '\U0001f4d6 Ai đang học Skills tại trung tâm học kỹ năng')
t('\u26a1 谁正在黑客松现场开发', '\u26a1 Ai đang phát triển tại hiện trường hackathon')
t('\U0001f5fa\ufe0f 各城市街区的实时活跃状态', '\U0001f5fa\ufe0f Trạng thái hoạt động thời gian thực của khu phố các thành phố')
t('这不仅增强了参与感和趣味性，也为无法到场的线上用户提供了一种\u201c云逛街\u201d的体验，形成社交传播素材。',
  'Điều này không chỉ tăng cường cảm giác tham gia và tính thú vị, mà còn cung cấp trải nghiệm \u201cdạo phố trên mây\u201d cho người dùng trực tuyến không thể đến hiện trường, tạo thành tài liệu truyền thông xã hội.')

# Commercial value
t('可以融入各个AI公司产品及促进更好使用，希望可以提供经济实惠的价格和套餐给到社区成员，希望有赞助可以覆盖社区的人力成本物料成本',
  'Có thể tích hợp sản phẩm của các công ty AI và thúc đẩy sử dụng tốt hơn, hy vọng có thể cung cấp giá cả và gói ưu đãi hợp lý cho thành viên cộng đồng, hy vọng có tài trợ để trang trải chi phí nhân lực và vật liệu của cộng đồng')
t('另外AI训练营正在进行中，可以联动', 'Ngoài ra trại huấn luyện AI đang diễn ra, có thể liên kết')
t('第五期：小龙虾OpenClaw训练营', 'Kỳ 5: Trại huấn luyện Tôm hùm OpenClaw')
t('欢迎AI公司和社区媒体一起参与', 'Hoan nghênh các công ty AI và truyền thông cộng đồng cùng tham gia')
t('合作请联系： AJWaytoAGI', 'Liên hệ hợp tác: AJWaytoAGI')

# Core value
t('希望用一个生动的\u201c街区\u201d隐喻，把技术社区活动变成了一件所有人都能理解、都想参与的事。',
  'Hy vọng dùng một ẩn dụ sinh động về \u201ckhu phố\u201d, biến hoạt động cộng đồng công nghệ thành điều mà tất cả mọi người đều có thể hiểu và muốn tham gia.')
t(' 小白不会被\u201c黑客松\u201d吓退，因为他们是来\u201c逛街\u201d的；高手不会觉得无聊，因为他们是街区的\u201c主厨\u201d。',
  ' Người mới sẽ không bị \u201chackathon\u201d làm e ngại, vì họ đến để \u201cdạo phố\u201d; cao thủ sẽ không thấy nhàm chán, vì họ là \u201cđầu bếp chính\u201d của khu phố.')
t('招募本次活动策划组织落地的社区伙伴', 'Tuyển dụng đối tác cộng đồng lên kế hoạch tổ chức và triển khai hoạt động này')

# Table headers
t('城市', 'Thành phố')
t('地址', 'Địa chỉ')
t('组织者', 'Người tổ chức')
t('场地', 'Địa điểm')
t('     组织者', '     Người tổ chức')

# City status entries
t('北京', 'Bắc Kinh')
t('【地址已确认】', '【Đã xác nhận địa chỉ】')
t('【地址未确认】', '【Chưa xác nhận địa chỉ】')
t('上海【地址已确认】', 'Thượng Hải 【Đã xác nhận địa chỉ】')
t('成都【', 'Thành Đô 【')
t('地址已确认', 'Đã xác nhận địa chỉ')
t('】', '】')
t('深圳【地址确认】', 'Thâm Quyến 【Đã xác nhận địa chỉ】')
t('杭州【地址未确认】', 'Hàng Châu 【Chưa xác nhận địa chỉ】')
t('广州【地址未确认】', 'Quảng Châu 【Chưa xác nhận địa chỉ】')
t('武汉【地址未确认】', 'Vũ Hán 【Chưa xác nhận địa chỉ】')
t('呼和浩特【地址未确认】', 'Hohhot 【Chưa xác nhận địa chỉ】')
t('苏州【地址已确认】', 'Tô Châu 【Đã xác nhận địa chỉ】')
t('天津【地址未确认】', 'Thiên Tân 【Chưa xác nhận địa chỉ】')
t('福州【地址未确认】', 'Phúc Châu 【Chưa xác nhận địa chỉ】')
t('珠海【地址未确认】', 'Chu Hải 【Chưa xác nhận địa chỉ】')
t('南京【地址', 'Nam Kinh 【Địa chỉ')
t('已', 'đã')
t('确认】', 'xác nhận】')
t('中山【地址未确认】', 'Trung Sơn 【Chưa xác nhận địa chỉ】')
t('济南【地址', 'Tế Nam 【Địa chỉ')
t('东莞【地址未确认】', 'Đông Hoản 【Chưa xác nhận địa chỉ】')
t('常州【地址待确认】', 'Thường Châu 【Chờ xác nhận địa chỉ】')
t('青岛【地址未确认】', 'Thanh Đảo 【Chưa xác nhận địa chỉ】')
t('太原【地址', 'Thái Nguyên 【Địa chỉ')
t('温州【地址', 'Ôn Châu 【Địa chỉ')
t('重庆', 'Trùng Khánh')
t('合肥【地址未确认】', 'Hợp Phì 【Chưa xác nhận địa chỉ】')
t('襄阳【地址确认】', 'Tương Dương 【Đã xác nhận địa chỉ】')
t('郑州【地址未确认】', 'Trịnh Châu 【Chưa xác nhận địa chỉ】')
t('乌鲁木齐【地址', 'Urumqi 【Địa chỉ')
t('西安1【地址未确认】', 'Tây An 1 【Chưa xác nhận địa chỉ】')
t('西安2【', 'Tây An 2 【')
t('南昌【地址未确认】', 'Nam Xương 【Chưa xác nhận địa chỉ】')
t('宁波【地址未确认】', 'Ninh Ba 【Chưa xác nhận địa chỉ】')
t('威海【地址确认】', 'Uy Hải 【Đã xác nhận địa chỉ】')
t('昆明【地址未确认】', 'Côn Minh 【Chưa xác nhận địa chỉ】')
t('慈溪【地址未确认】', 'Từ Khê 【Chưa xác nhận địa chỉ】')
t('汕头【地址未确认】', 'Sán Đầu 【Chưa xác nhận địa chỉ】')
t('徐州【地址未确认】', 'Từ Châu 【Chưa xác nhận địa chỉ】')
t('大理【地址未确认】', 'Đại Lý 【Chưa xác nhận địa chỉ】')
t('大连【地址', 'Đại Liên 【Địa chỉ')
t('厦门【地址未确认】', 'Hạ Môn 【Chưa xác nhận địa chỉ】')
t('石家庄【地址', 'Thạch Gia Trang 【Địa chỉ')
t('海口【地址未确认】', 'Hải Khẩu 【Chưa xác nhận địa chỉ】')
t('淮北【地址未确认】', 'Hoài Bắc 【Chưa xác nhận địa chỉ】')
t('沈阳【地址', 'Thẩm Dương 【Địa chỉ')
t('贵阳【地址', 'Quý Dương 【Địa chỉ')
t('衡水【地址', 'Hành Thủy 【Địa chỉ')
t('泰国清迈【地址', 'Chiang Mai, Thái Lan 【Địa chỉ')
t('天津', 'Thiên Tân')
t('贵阳', 'Quý Dương')
t('无锡【地址已确认】', 'Vô Tích 【Đã xác nhận địa chỉ】')
t('衡水【地址已确认】', 'Hành Thủy 【Đã xác nhận địa chỉ】')
t('湛江【地址已确认】', 'Trạm Giang 【Đã xác nhận địa chỉ】')
t('长春【地址已确认】', 'Trường Xuân 【Đã xác nhận địa chỉ】')
t('长沙【地址未确认】', 'Trường Sa 【Chưa xác nhận địa chỉ】')
t('邯郸【地址未确认】', 'Hàm Đan 【Chưa xác nhận địa chỉ】')
t('宜春【地址未确认】', 'Nghi Xuân 【Chưa xác nhận địa chỉ】')
t('库尔勒', 'Korla')
t('已确认]', 'đã xác nhận]')
t('淮', 'Hoài')
t('江苏', 'Giang Tô')

# Second city list
t('北京、上海、广州、深圳、苏州、杭州、成都、武汉、天津、珠海、中山、重庆、郑州、襄阳、乌鲁木齐、库尔勒、威海、合肥、宁波、常州、西安、南昌、南京、济南、太原、温州、东莞、福州、呼和浩特、青岛、昆明、慈溪、汕头、徐州、',
  'Bắc Kinh, Thượng Hải, Quảng Châu, Thâm Quyến, Tô Châu, Hàng Châu, Thành Đô, Vũ Hán, Thiên Tân, Chu Hải, Trung Sơn, Trùng Khánh, Trịnh Châu, Tương Dương, Urumqi, Korla, Uy Hải, Hợp Phì, Ninh Ba, Thường Châu, Tây An, Nam Xương, Nam Kinh, Tế Nam, Thái Nguyên, Ôn Châu, Đông Hoản, Phúc Châu, Hohhot, Thanh Đảo, Côn Minh, Từ Khê, Sán Đầu, Từ Châu,')
t('贵阳、邯郸、泰国清迈、大理、大连、厦门、石家庄、海口、衡水、淮北、宜春奉新',
  'Quý Dương, Hàm Đan, Chiang Mai (Thái Lan), Đại Lý, Đại Liên, Hạ Môn, Thạch Gia Trang, Hải Khẩu, Hành Thủy, Hoài Bắc, Nghi Xuân Phụng Tân')
t('、无锡', ', Vô Tích')
t('、沈阳、长春', ', Thẩm Dương, Trường Xuân')
t('、湛江', ', Trạm Giang')

# Addresses
t('北京亦庄分会场：', 'Phân hội trường Bắc Kinh Diệc Trang:')
t('北京亦庄信创园会议中心', 'Trung tâm Hội nghị Tín Sáng Viên Bắc Kinh Diệc Trang')
t('北京朝阳分会场：北京市朝阳区酒仙桥北路乙十号院星地中心C座10层路演厅',
  'Phân hội trường Bắc Kinh Triều Dương: Phòng roadshow tầng 10 tòa C, Trung tâm Tinh Địa, viện số 10B đường Bắc Tửu Tiên Kiều, quận Triều Dương, Bắc Kinh')
t('张江科学之门', 'Cổng Khoa học Trương Giang')
t('成都·', 'Thành Đô·')
t('天府长岛数字文创园路演厅', 'Phòng roadshow Khu Sáng tạo Số Thiên Phủ Trường Đảo')
t('（高新区盛通街88号2栋1层）', '(Tầng 1 tòa 2, số 88 đường Thịnh Thông, khu Cao Tân)')
t('深圳南山区前海深国际前海颐都大厦5F（国家对外文化贸易基地（深圳）出海中心）',
  'Tầng 5F Tòa nhà Thâm Quốc Tế Tiền Hải Di Đô, quận Nam Sơn, Thâm Quyến (Trung tâm Ra nước ngoài Cơ sở Thương mại Văn hóa Đối ngoại Quốc gia (Thâm Quyến))')
t('杭州东站未来数智港一楼', 'Tầng 1 Cảng Số Trí Tương Lai, Ga Đông Hàng Châu')
t('或云谷中心', 'Hoặc Trung tâm Vân Cốc')
t('广州市海珠区华新中心18楼', 'Tầng 18 Trung tâm Hoa Tân, quận Hải Châu, thành phố Quảng Châu')
t('鄂港澳青创园5楼报告厅', 'Phòng báo cáo tầng 5 Khu Thanh niên Sáng tạo Ngạc Cảng Áo')
t('呼和浩特水岸小镇D区7号楼模创空间', 'Không gian Mô Sáng, tòa 7 khu D, Thị trấn Thủy Ngạn, Hohhot')
t('苏州工业园区南岸新地6号楼三楼 光合厅 ', 'Tầng 3 tòa 6, Nam Ngạn Tân Địa, Khu Công nghiệp Tô Châu - Hội trường Quang Hợp ')
t('天津市西青区智慧山南塔405', 'Phòng 405 Tháp Nam Trí Tuệ Sơn, quận Tây Thanh, thành phố Thiên Tân')
t('福州市晋安区前歧路27号 洋下党群服务中心 4楼', 'Tầng 4 Trung tâm Phục vụ Đảng Quần Dương Hạ, số 27 đường Tiền Kỳ, quận Tấn An, thành phố Phúc Châu')
t('珠海市中电南方软件园A2二层202会议室', 'Phòng họp 202 tầng 2 A2, Vườn Phần mềm Trung Điện Nam Phương, thành phố Chu Hải')
t('南京市玄武大道699号徐庄高新区行政大楼A座1楼', 'Tầng 1 tòa A, Tòa nhà Hành chính Khu Cao Tân Từ Trang, số 699 đại lộ Huyền Vũ, thành phố Nam Kinh')
t('中山东区街道中山四路88号盛景尚峰1座2楼中山青年创业梦工场', 'Công xưởng Mơ ước Thanh niên Khởi nghiệp Trung Sơn, tầng 2 tòa 1 Thịnh Cảnh Thượng Phong, số 88 đường Trung Sơn Tứ, phường Đông Khu, Trung Sơn')
t('山东省济南市历下区新泺大街1766号齐鲁软件园大厦A座12F', 'Tầng 12F tòa A, Tòa nhà Vườn Phần mềm Tề Lỗ, số 1766 đường Tân Lạc, quận Lịch Hạ, thành phố Tế Nam, tỉnh Sơn Đông')
t('松山湖国际创新创业社区', 'Cộng đồng Đổi mới Sáng tạo Quốc tế Tùng Sơn Hồ')
t('G4栋21楼', 'Tầng 21 tòa G4')
t('金坛清风路 2 号 金坛区图书馆', 'Thư viện quận Kim Đàn, số 2 đường Thanh Phong, Kim Đàn')
t('青岛市李沧区青山路700号金海牛能源环境产业园A座521会议室', 'Phòng họp 521 tòa A, Khu Công nghiệp Năng lượng Môi trường Kim Hải Ngưu, số 700 đường Thanh Sơn, quận Lý Thương, thành phố Thanh Đảo')
t('好', 'Tốt')
t('太原市', 'Thành phố Thái Nguyên')
t('府西街28号（邮政储蓄银行，右侧3层）', 'Số 28 đường Phủ Tây (Ngân hàng Tiết kiệm Bưu chính, tầng 3 bên phải)')
t('温州市瓯海区（温州）数安港A2栋三楼温州数据研究院', 'Viện Nghiên cứu Dữ liệu Ôn Châu, tầng 3 tòa A2 Cảng Số An (Ôn Châu), quận Âu Hải, thành phố Ôn Châu')
t('郑州市高新区大学科技园东区16号楼C座2楼', 'Tầng 2 tòa C, tòa 16 khu Đông Công viên Khoa học Đại học, khu Cao Tân, thành phố Trịnh Châu')
t('商都路华丰灯饰界设计师大厦11楼 （注：来旺达商旅酒店11楼）', 'Tầng 11 Tòa nhà Nhà thiết kế Giới Đèn trang trí Hoa Phong, đường Thương Đô (Chú: Tầng 11 Khách sạn Thương mại Lai Vượng Đạt)')
t('乌鲁木齐市高新区（新市区）北京南路358号大成国际大厦20层2006', 'Phòng 2006 tầng 20, Tòa nhà Quốc tế Đại Thành, số 358 đường Nam Bắc Kinh, khu Cao Tân (quận Tân Thị), thành phố Urumqi')
t('乌鲁木齐市图书馆三楼研学空间（六馆一心）   ', 'Không gian Nghiên học tầng 3 Thư viện thành phố Urumqi (Lục Quán Nhất Tâm)   ')
t('新汇嘉5楼翰林书店小圆厅 ', 'Phòng tròn nhỏ Nhà sách Hàn Lâm tầng 5 Tân Hối Gia ')
t('西安市·高新区高新二路', 'Đường Cao Tân Nhị, khu Cao Tân, thành phố Tây An')
t('南昌市高新区·艾溪湖北路77号北航科技园B1栋903', 'Phòng 903 tòa B1, Khu Công nghệ Bắc Hàng, số 77 đường Bắc Hồ Ngải Khê, khu Cao Tân, thành phố Nam Xương')
t('宁波市人才之家4楼', 'Tầng 4 Nhà Nhân tài, thành phố Ninh Ba')
t('宁波市江北区老外滩党群服务中心3楼', 'Tầng 3 Trung tâm Phục vụ Đảng Quần Lão Ngoại Than, quận Giang Bắc, thành phố Ninh Ba')
t('文蔚路与学林路交叉口200米(宁大科院北校区)', '200m từ ngã tư đường Văn Úy và đường Học Lâm (Khu Bắc Học viện Khoa học Đại học Ninh Ba)')
t('威海市环翠区青岛北路2号中国·威海人力资源服务产业园二楼', 'Tầng 2 Khu Công nghiệp Dịch vụ Nhân lực Trung Quốc·Uy Hải, số 2 đường Bắc Thanh Đảo, quận Hoàn Thúy, thành phố Uy Hải')
t('威海智慧谷', 'Trí Tuệ Cốc Uy Hải')
t('昆明市盘龙区联盟街道金瓦路69号云南能投大厦', 'Tòa nhà Vân Nam Năng Đầu, số 69 đường Kim Ngõa, phường Liên Minh, quận Bàn Long, thành phố Côn Minh')
t('云南省昆明市西山区西园南路36号融城优郡A座写字楼8楼 ', 'Tầng 8 tòa văn phòng A, Dung Thành Ưu Quận, số 36 đường Nam Tây Viên, quận Tây Sơn, thành phố Côn Minh, tỉnh Vân Nam ')
t('慈溪市周巷镇联胜路56号三楼杭州湾畔岸', 'Tầng 3 số 56 đường Liên Thắng, trấn Chu Hạng, thành phố Từ Khê - Bờ Vịnh Hàng Châu')
t('慈溪市', 'Thành phố Từ Khê')
t('汕头市龙湖区侨韵路22号深汕数字科创产业园12号楼会议中心', 'Trung tâm Hội nghị tòa 12, Khu Công nghiệp Khoa Sáng Số Thâm Sán, số 22 đường Kiều Vận, quận Long Hồ, thành phố Sán Đầu')
t('汕头市大学路叠金工业区榕江创客空间', 'Không gian Sáng tạo Dung Giang, Khu Công nghiệp Điệp Kim, đường Đại Học, thành phố Sán Đầu')
t('徐州市泉山区翡翠花园翡翠时光街12号（翡翠时光咖啡）', 'Số 12 phố Thời Quang Phỉ Thúy, Khu vườn Phỉ Thúy, quận Tuyền Sơn, thành phố Từ Châu (Cà phê Thời Quang Phỉ Thúy)')
t('重庆市九龙坡区渝州路27号重庆赛博AI社区·二厂（重庆市科协大楼A栋附4号）', 'Cộng đồng AI Trùng Khánh Cyborg·Nhà máy số 2, số 27 đường Du Châu, quận Cửu Long Pha, thành phố Trùng Khánh (Phụ số 4 tòa A, Tòa nhà Hiệp hội Khoa học Kỹ thuật Trùng Khánh)')
t('重庆市两江新区星光大道62号海王星科技大厦C区1号门4层博拉AI模创空间', 'Không gian Mô sáng AI Bác Lạp, tầng 4 cửa số 1 khu C Tòa nhà Khoa học Hải Vương Tinh, số 62 đại lộ Tinh Quang, Khu Mới Lưỡng Giang, thành phố Trùng Khánh')
t('合肥市蜀山区黄山路与石台路交口安徽国际商务中心A座', 'Tòa A Trung tâm Thương mại Quốc tế An Huy, ngã tư đường Hoàng Sơn và đường Thạch Đài, quận Thục Sơn, thành phố Hợp Phì')
t('安徽省合肥市', 'Thành phố Hợp Phì, tỉnh An Huy')
t('高新区安徽省人工智能先导区（模立方OPC社区）', 'Khu Tiên đạo Trí tuệ Nhân tạo tỉnh An Huy, khu Cao Tân (Cộng đồng OPC Mô Lập Phương)')
t('襄阳市高新区追日路2号襄阳科技馆四楼学术报告厅', 'Phòng Báo cáo Học thuật tầng 4, Bảo tàng Khoa học Kỹ thuật Tương Dương, số 2 đường Truy Nhật, khu Cao Tân, thành phố Tương Dương')
t('所在地区: 湖北省襄阳市樊城区团山镇', 'Khu vực: Trấn Đoàn Sơn, quận Phàn Thành, thành phố Tương Dương, tỉnh Hồ Bắc')
t('手机号码: 15271026633', 'Số điện thoại: 15271026633')
t('收件人: 蔡乐', 'Người nhận: Thái Lạc')
t('详细地址: 襄阳人才大厦', 'Địa chỉ chi tiết: Tòa nhà Nhân tài Tương Dương')
t('贵阳市花溪区溪北路贵州大学数智学部', 'Khoa Số Trí, Đại học Quý Châu, đường Khê Bắc, quận Hoa Khê, thành phố Quý Dương')
t('市观山湖区茅台商务中心C座45楼1号会议厅', 'Phòng họp số 1 tầng 45 tòa C, Trung tâm Thương mại Mao Đài, quận Quan Sơn Hồ')
t('大理家海房子\n', 'Nhà Gia Hải Đại Lý\n')
t('大理市下关嘉士柏小镇创翼楼四楼白鹤堂', 'Phòng Bạch Hạc, tầng 4 tòa Sáng Dực, Thị trấn Carlsberg, Hạ Quan, thành phố Đại Lý')
t('大连市中山区友好路101号曼哈顿大厦2905', 'Phòng 2905 Tòa nhà Manhattan, số 101 đường Hữu Hảo, quận Trung Sơn, thành phố Đại Liên')
t('中山区青泥洼佳兆业三楼且漾书店', 'Nhà sách Thả Dương tầng 3, Giai Triệu Nghiệp Thanh Nê Oa, quận Trung Sơn')
t('厦门市集美区软件园三期', 'Giai đoạn 3 Vườn Phần mềm, quận Tập Mỹ, thành phố Hạ Môn')
t('石家庄裕华区裕华万达1404', 'Phòng 1404 Vạn Đạt Dụ Hoa, quận Dụ Hoa, Thạch Gia Trang')
t('石家庄市师范街与自强路交汇处西行五十米路南，安吉书院', 'Học viện An Cát, 50m về phía Tây phía Nam đường tại ngã tư đường Sư Phạm và đường Tự Cường, thành phố Thạch Gia Trang')
t('海口市美兰区海甸二西路16号海南省创业就业协会3楼', 'Tầng 3 Hiệp hội Khởi nghiệp Việc làm tỉnh Hải Nam, số 16 đường Tây 2 Hải Điện, quận Mỹ Lan, thành phố Hải Khẩu')
t('海口市美兰区和风家园蓝天居1栋1单元26楼', 'Tầng 26 đơn nguyên 1 tòa 1, Lam Thiên Cư Hòa Phong Gia Viên, quận Mỹ Lan, thành phố Hải Khẩu')
t('安徽省淮北市相山区人民中路282号副楼3楼第3会议室', 'Phòng họp số 3 tầng 3 tòa phụ, số 282 đường Trung Nhân Dân, quận Tương Sơn, thành phố Hoài Bắc, tỉnh An Huy')
t('淮北市相山区淮海西路与长山路交口东北侧、杭淮科学大厦7楼704', 'Phòng 704 tầng 7, Tòa nhà Khoa học Hàng Hoài, phía Đông Bắc ngã tư đường Tây Hoài Hải và đường Trường Sơn, quận Tương Sơn, thành phố Hoài Bắc')
t('浑南区金科街7-3号 数字人才基地2楼205报告厅', 'Phòng báo cáo 205 tầng 2 Cơ sở Nhân tài Số, số 7-3 đường Kim Khoa, quận Hồn Nam')
t('吉林省长春市高新区国家广告产业园区GIGO吉广AI创意产业学院4楼漫剧训练营（吉林省长春市高新技术产业开发区生态东街3330号）',
  'Trại huấn luyện Mạn kịch tầng 4 Học viện Công nghiệp Sáng tạo AI GIGO Cát Quảng, Khu Công nghiệp Quảng cáo Quốc gia, khu Cao Tân, thành phố Trường Xuân, tỉnh Cát Lâm (Số 3330 đường Đông Sinh Thái, Khu Phát triển Công nghiệp Công nghệ Cao, thành phố Trường Xuân, tỉnh Cát Lâm)')
t('滨湖区金城西路500-1号图书馆负一楼指挥大厅（无锡市滨湖区城市运行管理中心）',
  'Đại sảnh Chỉ huy tầng hầm 1 Thư viện, số 500-1 đường Tây Kim Thành, quận Tân Hồ (Trung tâm Quản lý Vận hành Đô thị quận Tân Hồ, thành phố Vô Tích)')
t('衡水市桃城区衡水市图书馆', 'Thư viện thành phố Hành Thủy, quận Đào Thành, thành phố Hành Thủy')
t('河北省衡水市图书馆', 'Thư viện thành phố Hành Thủy, tỉnh Hà Bắc')
t('融创空间（原思维盒子众创空间(华盛新城店)），赤坎区海田路5号华盛新城商住小区Q-1栋Q-2栋一层10号商铺',
  'Không gian Dung Sáng (nguyên Không gian sáng tạo Hộp Tư duy (chi nhánh Hoa Thịnh Tân Thành)), cửa hàng số 10 tầng 1 tòa Q-1 Q-2, khu thương mại Hoa Thịnh Tân Thành, số 5 đường Hải Điền, quận Xích Khảm')
t('库尔勒经济技术开发区新疆库尔勒高新数字产业园12号楼', 'Tòa 12, Khu Công nghiệp Số Cao Tân Tân Cương Korla, Khu Phát triển Kinh tế Kỹ thuật Korla')
t('邯郸市丛台区联通北路和联防路交叉口东南角众创大厦801', 'Phòng 801 Tòa nhà Chúng Sáng, góc Đông Nam ngã tư đường Bắc Liên Thông và đường Liên Phòng, quận Tùng Đài, thành phố Hàm Đan')
t('邯郸市丛台区光明北大街三龙商贸B座15层', 'Tầng 15 tòa B Tam Long Thương Mại, đường Bắc Quang Minh, quận Tùng Đài, thành phố Hàm Đan')
t('宜春市奉新县凤凰山路新时代文明实践中心', 'Trung tâm Thực hành Văn minh Thời đại Mới, đường Phượng Hoàng Sơn, huyện Phụng Tân, thành phố Nghi Xuân')
t('江西省宜春市奉新县文体中心', 'Trung tâm Văn Thể, huyện Phụng Tân, thành phố Nghi Xuân, tỉnh Giang Tây')
t('江西省南昌市红谷滩区莱蒙都会5期熙梦城2-2单元3楼', 'Tầng 3 đơn nguyên 2-2, Hy Mộng Thành giai đoạn 5 Lai Mông Đô Hội, quận Hồng Cốc Than, thành phố Nam Xương, tỉnh Giang Tây')
t('湖南省长沙市开福区望麓园街道民主东街2号四号栋一层低空啡行', 'Quán cà phê Đê Không Phi Hành tầng 1 tòa 4, số 2 đường Đông Dân Chủ, phường Vọng Lộc Viên, quận Khai Phúc, thành phố Trường Sa, tỉnh Hồ Nam')
t('陕西省西咸新区沣西新城沣柳路与英秀二路十字文创小镇6号楼8层', 'Tầng 8 tòa 6, Thị trấn Văn sáng Thập tự, đường Phong Liễu và đường Anh Tú Nhị, Phong Tây Tân Thành, Khu Mới Tây Hàm, tỉnh Thiểm Tây')
t('陕西省西安市雁塔区博文路欣景苑西南门(科技二路那个口) ', 'Cổng Tây Nam Hân Cảnh Uyển, đường Bác Văn, quận Nhạn Tháp, thành phố Tây An, tỉnh Thiểm Tây (cửa đường Khoa Kỹ Nhị) ')
t('距离甘家寨地铁口D口 步行150米左右', 'Cách cửa D ga tàu điện Cam Gia Trại khoảng 150m đi bộ')
t('宁神司茶事（欣景苑店）', 'Trà quán Ninh Thần Tư (chi nhánh Hân Cảnh Uyển)')
t('海科技城·数字经济产业园Ｅ5-8层', 'Khu Công nghiệp Kinh tế Số · Thành Khoa học Biển E tầng 5-8')
t('西青区智慧山南塔405', 'Phòng 405 Tháp Nam Trí Tuệ Sơn, quận Tây Thanh')
t('（可以早点去，早上有出海主题', '(Có thể đến sớm, buổi sáng có chủ đề ra nước ngoài')
t('15, อําเภ, 1 Chaiyapoom Soi 2, Chang Moi Sub-district, เมือง, Chiang Mai 50300 清迈客栈',
  '15, อําเภ, 1 Chaiyapoom Soi 2, Chang Moi Sub-district, เมือง, Chiang Mai 50300 Nhà trọ Chiang Mai')
t(' 这期暂停办', ' Kỳ này tạm dừng tổ chức')

# Person names
t('茹九儿', 'Như Cửu Nhi')
t('嘉琛', 'Gia Thâm')
t('、无锡一棵树', ', Nhất Khỏa Thụ (Vô Tích)')
t('田颖芊', 'Điền Dĩnh Thiên')
t('、罗东', ', La Đông')
t('@Eason秦', '@Eason Tần')
t('@乐源', '@Lạc Nguyên')
t('@蜜薯翠翠', '@Mật Thử Thúy Thúy')
t('@邦主', '@Bang Chủ')
t('刘洋', 'Lưu Dương')
t('张少斌', 'Trương Thiếu Bân')
t('张羽昊', 'Trương Vũ Hạo')
t('徐琴Jossolo', 'Từ Cầm Jossolo')
t('枫子', 'Phong Tử')
t('宫莉', 'Cung Lị')
t('小孙同学', 'Bạn Tiểu Tôn')
t('颦儿', 'Tần Nhi')
t('高丹丹', 'Cao Đan Đan')
t('甲九', 'Giáp Cửu')
t('赵军、云旗', 'Triệu Quân, Vân Kỳ')

# Year planning
t('\u2705 2026全年活动规划', '\u2705 Kế hoạch hoạt động cả năm 2026')
t('每月最后一个周日', 'Chủ nhật cuối cùng mỗi tháng')
t('1月25日（', '25/1 (')
t('【已结束】AI切磋大会\U0001f31f第21期1月25日 - AI年货节', '【Đã kết thúc】Đại hội giao lưu AI \U0001f31f Kỳ 21 ngày 25/1 - Hội chợ năm mới AI')
t('3月29日（', '29/3 (')
t('4月26日（）', '26/4 ()')
t('5月31日（）', '31/5 ()')
t('6月28日（）', '28/6 ()')
t('7月26日（）', '26/7 ()')
t('8月30日（）', '30/8 ()')
t('9月27日（）', '27/9 ()')
t('10月25日（）', '25/10 ()')
t('11月29日（）', '29/11 ()')
t('12月27日（AI年度总结）', '27/12 (Tổng kết năm AI)')

# Save as JSON with ensure_ascii
with open('_art4_trans_map.json', 'w', encoding='utf-8') as f:
    json.dump(T, f, ensure_ascii=True, indent=2)

print(f"Built {len(T)} translation entries")
print("Saved to _art4_trans_map.json")
