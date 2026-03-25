#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Translate _art4_orig.json Chinese -> Vietnamese, output _art4_trans.json"""

import json
import re
import copy

# Load original
with open('_art4_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Chinese -> Vietnamese translation dictionary for this document
# We'll translate each content string

def has_chinese(text):
    """Check if text contains Chinese characters"""
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def translate(text):
    """Translate Chinese text to Vietnamese"""
    if not text or not text.strip():
        return text

    # Keep URLs, emails, @mentions, English-only text unchanged
    if re.match(r'^https?://', text.strip()):
        return text
    if re.match(r'^@[A-Za-z]', text.strip()):
        return text
    if not has_chinese(text):
        return text

    # Full mapping of all Chinese content found in the document
    translations = {
        # Title
        "AI切磋大会22期 3月29日-龙虾街区": "Đại hội giao lưu AI kỳ 22 ngày 29/3 - Khu phố Tôm hùm",

        # Heading 1
        "🦞 小龙虾街区-40个城市同时开展": "🦞 Khu phố Tôm hùm - Diễn ra đồng thời tại 40 thành phố",

        # Registration
        "报名地址：": "Địa chỉ đăng ký:",

        # Section headings
        "参与城市及活动地址": "Các thành phố tham gia và địa điểm hoạt động",
        "一、核心概念": "I. Khái niệm cốt lõi",
        "二、街区功能分区": "II. Phân khu chức năng khu phố",
        "三、线上联动：龙虾实时地图": "III. Liên kết trực tuyến: Bản đồ tôm hùm thời gian thực",
        "四、落地形式": "IV. Hình thức triển khai",
        "五、商业价值": "V. Giá trị thương mại",
        "六、核心价值": "VI. Giá trị cốt lõi",
        "七、参与城市及活动地址": "VII. Các thành phố tham gia và địa điểm hoạt động",

        # City lists
        "城市名单：国内40": "Danh sách thành phố: Trong nước 40",
        "海外：马德里，东京，清迈，澳洲悉尼，伦敦": "Nước ngoài: Madrid, Tokyo, Chiang Mai, Sydney (Úc), London",

        # Confirmation heading
        "AI切磋大会3月29日全国场地确认中": "Đại hội giao lưu AI ngày 29/3 - Đang xác nhận địa điểm toàn quốc",

        # Long city list
        "北京、上海、广州、深圳、苏州、杭州、成都、武汉、天津、珠海、中山、重庆、郑州、襄阳、乌鲁木齐、威海、合肥、宁波、常州、西安、南昌、南京、济南、太原、温州、东莞、福州、青岛、昆明、慈溪、汕头、徐州、贵阳、大理、大连、厦门、石家庄、海口、衡水、淮北、沈阳、长春、无锡、湛江、泰国清迈、伦敦、马德里、悉尼、东京":
            "Bắc Kinh, Thượng Hải, Quảng Châu, Thâm Quyến, Tô Châu, Hàng Châu, Thành Đô, Vũ Hán, Thiên Tân, Chu Hải, Trung Sơn, Trùng Khánh, Trịnh Châu, Tương Dương, Urumqi, Uy Hải, Hợp Phì, Ninh Ba, Thường Châu, Tây An, Nam Xương, Nam Kinh, Tế Nam, Thái Nguyên, Ôn Châu, Đông Hoản, Phúc Châu, Thanh Đảo, Côn Minh, Từ Khê, Sán Đầu, Từ Châu, Quý Dương, Đại Lý, Đại Liên, Hạ Môn, Thạch Gia Trang, Hải Khẩu, Hành Thủy, Hoài Bắc, Thẩm Dương, Trường Xuân, Vô Tích, Trạm Giang, Chiang Mai (Thái Lan), London, Madrid, Sydney, Tokyo",

        # Second long city list
        "北京、上海、广州、深圳、苏州、杭州、成都、武汉、天津、珠海、中山、重庆、郑州、襄阳、乌鲁木齐、库尔勒、威海、合肥、宁波、常州、西安、南昌、南京、济南、太原、温州、东莞、福州、呼和浩特、青岛、昆明、慈溪、汕头、徐州、":
            "Bắc Kinh, Thượng Hải, Quảng Châu, Thâm Quyến, Tô Châu, Hàng Châu, Thành Đô, Vũ Hán, Thiên Tân, Chu Hải, Trung Sơn, Trùng Khánh, Trịnh Châu, Tương Dương, Urumqi, Korla, Uy Hải, Hợp Phì, Ninh Ba, Thường Châu, Tây An, Nam Xương, Nam Kinh, Tế Nam, Thái Nguyên, Ôn Châu, Đông Hoản, Phúc Châu, Hohhot, Thanh Đảo, Côn Minh, Từ Khê, Sán Đầu, Từ Châu,",

        "贵阳、邯郸、泰国清迈、大理、大连、厦门、石家庄、海口、衡水、淮北、宜春奉新":
            "Quý Dương, Hàm Đan, Chiang Mai (Thái Lan), Đại Lý, Đại Liên, Hạ Môn, Thạch Gia Trang, Hải Khẩu, Hành Thủy, Hoài Bắc, Nghi Xuân Phụng Tân",
        "、无锡": ", Vô Tích",
        "、沈阳、长春": ", Thẩm Dương, Trường Xuân",
        "、湛江": ", Trạm Giang",

        # Text blocks
        "每个城市会制作自己城市的对应海报": "Mỗi thành phố sẽ thiết kế poster tương ứng của riêng mình",
        "例如：下面是悉尼的": "Ví dụ: Dưới đây là của Sydney",

        # Core concept section
        "以当前"小龙虾"（openclaw项目）的爆发式热度为契机，打": "Nhân cơ hội bùng nổ của \"Tôm hùm\" (dự án openclaw), tạo",
        "造一个沉浸式的": " ra một",
        ""龙虾街区"": "\"Khu phố Tôm hùm\"",
        "主题体验空间——将 AI 开发者社区活动包装成一条充满烟火气与科技感的"商业街"，让高手与小白在同一个场景中自然交融，既贴合当下热点，让大家都有收获":
            " không gian trải nghiệm chủ đề nhập vai — biến hoạt động cộng đồng nhà phát triển AI thành một \"phố thương mại\" đầy hơi thở cuộc sống và cảm giác công nghệ, để người giỏi và người mới cùng hòa nhập tự nhiên trong cùng một bối cảnh, vừa bắt kịp xu hướng nóng, vừa giúp mọi người đều có thu hoạch",
        "。": ".",

        "报名链接：": "Link đăng ký:",
        "2026年03月29日（周日） 13:00  - 18:00": "Ngày 29/03/2026 (Chủ nhật) 13:00 - 18:00",
        "距离AI切磋大会第2": "Còn cách Đại hội giao lưu AI kỳ thứ 2",
        "期线下活动开启时间还有：": " hoạt động offline bắt đầu:",

        "物料：地图指示牌（玩法说明书）": "Vật liệu: Biển chỉ dẫn bản đồ (Sách hướng dẫn cách chơi)",

        # Zone 1
        "🦞 1. 小龙虾出生地（入口·品牌装机区）": "🦞 1. Nơi sinh Tôm hùm (Lối vào - Khu cài đặt thương hiệu)",
        "定位：": "Định vị:",
        " 街区的第一站，用户进入后的首个体验环节。": " Trạm đầu tiên của khu phố, trải nghiệm đầu tiên khi người dùng bước vào.",
        "一排"铺子"对应各家厂商品牌，用户在这里完成装机体验——"你想吃谁家的小龙虾，就去谁家的铺子"。每个铺位由一家厂商/品牌入驻，提供产品安装、试用和互动演示，用户自主选择感兴趣的品牌进行体验。":
            "Một dãy \"cửa hàng\" tương ứng với các thương hiệu nhà sản xuất, người dùng hoàn thành trải nghiệm cài đặt tại đây — \"Bạn muốn ăn tôm hùm nhà nào thì đến cửa hàng nhà đó\". Mỗi gian hàng do một nhà sản xuất/thương hiệu đặt chỗ, cung cấp cài đặt sản phẩm, dùng thử và demo tương tác, người dùng tự chọn thương hiệu quan tâm để trải nghiệm.",
        "物料：出生证明（包含编号，小龙虾名字，性别，时间，地址，接生医生姓名）电子版出生证明（3:4比例发小红书）":
            "Vật liệu: Giấy khai sinh (bao gồm số hiệu, tên tôm hùm, giới tính, thời gian, địa chỉ, tên bác sĩ đỡ đẻ) Giấy khai sinh điện tử (tỷ lệ 3:4 đăng Xiaohongshu)",
        "准备： 每个城市一只接生虾，做虾的档案登记（日后可以虾和虾联络）":
            "Chuẩn bị: Mỗi thành phố một con tôm đỡ đẻ, làm hồ sơ đăng ký tôm (sau này tôm có thể liên lạc với nhau)",
        "设计：虾宝宝，包单布。KT手举牌形式。（如果有物料虾宝宝的玩偶更好）":
            "Thiết kế: Tôm bé, khăn quấn. Dạng bảng KT cầm tay. (Nếu có vật liệu búp bê tôm bé càng tốt)",
        "拍照环节：喜当爹": "Phần chụp ảnh: Lên chức bố",

        # Zone 2
        "🏠 2. 小龙虾产后护理（个性化配置·初始化区）": "🏠 2. Chăm sóc hậu sản Tôm hùm (Cấu hình cá nhân hóa - Khu khởi tạo)",
        " 装机后的"月子中心"，让你的小龙虾拥有灵魂。": " \"Trung tâm chăm sóc sau sinh\" sau khi cài đặt, giúp tôm hùm của bạn có linh hồn.",
        "用户完成装机后，来这里为自己的 AI 助手进行个性化设置，让它真正成为"你的"小龙虾：":
            "Sau khi người dùng hoàn thành cài đặt, đến đây để thiết lập cá nhân hóa trợ lý AI của mình, biến nó thực sự thành tôm hùm \"của bạn\":",
        "工具集成": "Tích hợp công cụ",
        "：配置飞书、QQ、企业微信等 IM 工具，打通工作流": ": Cấu hình Feishu, QQ, WeChat doanh nghiệp và các công cụ IM khác, kết nối quy trình làm việc",
        "人设定制（": "Tùy chỉnh nhân vật (",
        "）": ")",
        "：设定 AI 助手的性格、说话风格、专业领域等个性化特征": ": Thiết lập tính cách, phong cách nói chuyện, lĩnh vực chuyên môn và các đặc điểm cá nhân hóa của trợ lý AI",
        "安全配置": "Cấu hình bảo mật",
        "：设置安全问题、隐私保护、访问权限等安全选项": ": Thiết lập câu hỏi bảo mật, bảo vệ quyền riêng tư, quyền truy cập và các tùy chọn bảo mật khác",
        "使用场景预设": "Cài đặt sẵn kịch bản sử dụng",
        "：根据用户职业（开发者/产品经理/创作者等）推荐最佳配置方案": ": Đề xuất phương án cấu hình tối ưu dựa trên nghề nghiệp người dùng (nhà phát triển/quản lý sản phẩm/nhà sáng tạo...)",
        "由社区志愿者和产品专家提供指导，确保每个用户都能把小龙虾"养"得得心应手。":
            "Được hướng dẫn bởi tình nguyện viên cộng đồng và chuyên gia sản phẩm, đảm bảo mỗi người dùng đều có thể \"nuôi\" tôm hùm một cách thuần thục.",
        "物料：虾儿童，护理打油诗，": "Vật liệu: Tôm trẻ em, thơ vui chăm sóc,",
        "真人装扮：金牌月嫂（购买月嫂服，金牌月嫂的铭牌）": "Hóa trang thật: Bảo mẫu vàng (mua đồ bảo mẫu, biển hiệu bảo mẫu vàng)",
        "拍照选介：满月照": "Giới thiệu chụp ảnh: Ảnh đầy tháng",

        # Zone 3
        "🏥 3. 龙虾医院-虾疗（技术支持·Bug 修复区）": "🏥 3. Bệnh viện Tôm hùm - Tôm liệu pháp (Hỗ trợ kỹ thuật - Khu sửa Bug)",
        " 装机后的"急救站"。": " \"Trạm cấp cứu\" sau khi cài đặt.",
        "用户在装机过程中遇到的任何 Bug、兼容性问题、配置疑难，都可以来这里"抢救你的小龙虾"。由技术志愿者和社区高手坐诊，提供一对一的问题排查与解决方案，既实用又有趣。":
            "Mọi Bug, vấn đề tương thích, khó khăn cấu hình mà người dùng gặp trong quá trình cài đặt đều có thể đến đây để \"cấp cứu tôm hùm của bạn\". Các tình nguyện viên kỹ thuật và cao thủ cộng đồng trực khám, cung cấp giải pháp xử lý sự cố 1-1, vừa thiết thực vừa thú vị.",
        "物料：残废虾，": "Vật liệu: Tôm tàn phế,",

        # Zone 4
        "📚 4. 龙虾学院 （技能学习中心，Skills 培训区）": "📚 4. Học viện Tôm hùm (Trung tâm học kỹ năng, Khu đào tạo Skills)",
        " 从装机到上手的能力跃迁空间。": " Không gian nâng cấp năng lực từ cài đặt đến thành thạo.",
        "设定一个定时任务": "Thiết lập một tác vụ hẹn giờ",
        "安装n个skills": "Cài đặt n skills",
        "面向小白用户，提供龙虾相关 Skills 的教学与实操。课程内容来源于黑客松的优秀成果——高手们在隔壁做出来的 Skills，小白们在这里直接学习和安装使用，形成"创造→传播→学习"的闭环。":
            "Hướng đến người dùng mới, cung cấp giảng dạy và thực hành Skills liên quan đến tôm hùm. Nội dung khóa học đến từ thành quả xuất sắc của hackathon — Skills mà các cao thủ tạo ra ở bên cạnh, người mới ở đây trực tiếp học và cài đặt sử dụng, hình thành vòng khép kín \"Sáng tạo → Lan tỏa → Học hỏi\".",
        "技能可以是卡片（nfc）形式，直接复制命令就可以安装，仅需手机即可":
            "Kỹ năng có thể ở dạng thẻ (NFC), chỉ cần sao chép lệnh là có thể cài đặt, chỉ cần điện thoại là đủ",
        "物料：抓周，抓技能（套圈）。培训班/鸡娃，转盘，摇签，解签":
            "Vật liệu: Bốc thăm tuổi, bắt kỹ năng (ném vòng). Lớp đào tạo/ép con học, vòng quay, rút thẻ, giải thẻ",
        "拍照：抓周过程，和你的技能合影": "Chụp ảnh: Quá trình bốc thăm, chụp ảnh cùng kỹ năng của bạn",
        "安装好skills之后完成一个skills应用后可以毕业": "Sau khi cài đặt xong skills và hoàn thành một ứng dụng skills thì có thể tốt nghiệp",
        "形象：教练/ 手举口号"鸡娃"": "Hình tượng: Huấn luyện viên/ Cầm khẩu hiệu \"Ép con học\"",
        "物料：学生卡+博士帽+"毕业了"": "Vật liệu: Thẻ sinh viên + Mũ tiến sĩ + \"Tốt nghiệp rồi\"",

        # Zone 5
        "🏆 5. 龙虾写字楼考核中心（ Skills 黑客松 创造·竞技区）": "🏆 5. Tòa nhà văn phòng Tôm hùm - Trung tâm đánh giá (Skills Hackathon - Khu sáng tạo & thi đấu)",
        " 街区的核心引擎，高手的主战场。": " Động cơ cốt lõi của khu phố, chiến trường chính của cao thủ.",
        "以龙虾 Skills 开发为主题的轻量级黑客松，门槛相对较低，参与感强。开发者现场组队、限时开发，产出的优秀 Skills 直接输送到技能学习中心供小白体验，实现高手与小白的价值连接。":
            "Hackathon nhẹ với chủ đề phát triển Skills Tôm hùm, ngưỡng tham gia tương đối thấp, cảm giác tham gia mạnh. Nhà phát triển tổ đội tại chỗ, phát triển giới hạn thời gian, Skills xuất sắc được chuyển thẳng đến trung tâm học kỹ năng cho người mới trải nghiệm, thực hiện kết nối giá trị giữa cao thủ và người mới.",
        "映射到进入职场": "Ánh xạ đến việc bước vào thị trường lao động",
        "黑客松志愿者：我是老板": "Tình nguyện viên hackathon: Tôi là sếp",
        "黑客松选手的背后/胸前贴贴纸： 上班虾 牛马虾": "Dán sticker phía sau/trước ngực thí sinh hackathon: Tôm đi làm, Tôm cày cuốc",
        "拍照：KT板手举牌"卷起来" ": "Chụp ảnh: Bảng KT cầm tay \"Cày lên nào\" ",

        # Zone 6
        "🎁 6. 龙虾超市（文化·周边集市社交区） 技能包实体化": "🎁 6. Siêu thị Tôm hùm (Khu văn hóa - Chợ phụ kiện & giao lưu xã hội) Gói kỹ năng thực thể hóa",
        " 街区的休闲与社交空间。": " Không gian giải trí và giao lưu xã hội của khu phố.",
        "售卖/展示龙虾主题周边产品，营造社区文化氛围。这里是拍照打卡、社交破冰的自然场所，让整个街区不只是技术活动，更是一次有温度的社区聚会。":
            "Bán/trưng bày sản phẩm phụ kiện chủ đề tôm hùm, tạo bầu không khí văn hóa cộng đồng. Đây là nơi check-in chụp ảnh, phá băng giao tiếp xã hội một cách tự nhiên, khiến cả khu phố không chỉ là hoạt động công nghệ mà còn là buổi họp mặt cộng đồng đầy ấm áp.",
        "物料：小票": "Vật liệu: Hóa đơn nhỏ",

        # Online section
        ""海辛阿文"式的互动地图，搭建一个": "Bản đồ tương tác kiểu \"Hashing Awen\", xây dựng một",
        "线上实时可视化平台": "nền tảng trực quan hóa thời gian thực trực tuyến",
        "，让所有人都能看到：": ", cho phép tất cả mọi người đều thấy:",
        "🔴 谁正在"龙虾医院"抢救 Bug": "🔴 Ai đang \"cấp cứu\" Bug tại \"Bệnh viện Tôm hùm\"",
        "📖 谁正在技能学习中心学习 Skills": "📖 Ai đang học Skills tại trung tâm học kỹ năng",
        "⚡ 谁正在黑客松现场开发": "⚡ Ai đang phát triển tại hiện trường hackathon",
        "🗺️ 各城市街区的实时活跃状态": "🗺️ Trạng thái hoạt động thời gian thực của khu phố các thành phố",
        "这不仅增强了参与感和趣味性，也为无法到场的线上用户提供了一种"云逛街"的体验，形成社交传播素材。":
            "Điều này không chỉ tăng cường cảm giác tham gia và tính thú vị, mà còn cung cấp trải nghiệm \"dạo phố trên mây\" cho người dùng trực tuyến không thể đến hiện trường, tạo thành tài liệu truyền thông xã hội.",

        # Commercial value
        "可以融入各个AI公司产品及促进更好使用，希望可以提供经济实惠的价格和套餐给到社区成员，希望有赞助可以覆盖社区的人力成本物料成本":
            "Có thể tích hợp sản phẩm của các công ty AI và thúc đẩy sử dụng tốt hơn, hy vọng có thể cung cấp giá cả và gói ưu đãi hợp lý cho thành viên cộng đồng, hy vọng có tài trợ để trang trải chi phí nhân lực và vật liệu của cộng đồng",
        "另外AI训练营正在进行中，可以联动": "Ngoài ra trại huấn luyện AI đang diễn ra, có thể liên kết",
        "第五期：小龙虾OpenClaw训练营": "Kỳ 5: Trại huấn luyện Tôm hùm OpenClaw",
        "欢迎AI公司和社区媒体一起参与": "Hoan nghênh các công ty AI và truyền thông cộng đồng cùng tham gia",
        "合作请联系： AJWaytoAGI": "Liên hệ hợp tác: AJWaytoAGI",

        # Core value
        "希望用一个生动的"街区"隐喻，把技术社区活动变成了一件所有人都能理解、都想参与的事。":
            "Hy vọng dùng một ẩn dụ sinh động về \"khu phố\", biến hoạt động cộng đồng công nghệ thành điều mà tất cả mọi người đều có thể hiểu và muốn tham gia.",
        " 小白不会被"黑客松"吓退，因为他们是来"逛街"的；高手不会觉得无聊，因为他们是街区的"主厨"。":
            " Người mới sẽ không bị \"hackathon\" làm e ngại, vì họ đến để \"dạo phố\"; cao thủ sẽ không thấy nhàm chán, vì họ là \"đầu bếp chính\" của khu phố.",
        "招募本次活动策划组织落地的社区伙伴": "Tuyển dụng đối tác cộng đồng lên kế hoạch tổ chức và triển khai hoạt động này",

        # Table headers and city entries
        "城市": "Thành phố",
        "地址": "Địa chỉ",
        "组织者": "Người tổ chức",

        # City + status entries
        "北京": "Bắc Kinh",
        "场地": "Địa điểm",
        "【地址已确认】": "【Đã xác nhận địa chỉ】",
        "上海【地址已确认】": "Thượng Hải 【Đã xác nhận địa chỉ】",
        "成都【": "Thành Đô 【",
        "地址已确认": "Đã xác nhận địa chỉ",
        "】": "】",
        "深圳【地址确认】": "Thâm Quyến 【Đã xác nhận địa chỉ】",
        "杭州【地址未确认】": "Hàng Châu 【Chưa xác nhận địa chỉ】",
        "广州【地址未确认】": "Quảng Châu 【Chưa xác nhận địa chỉ】",
        "武汉【地址未确认】": "Vũ Hán 【Chưa xác nhận địa chỉ】",
        "呼和浩特【地址未确认】": "Hohhot 【Chưa xác nhận địa chỉ】",
        "苏州【地址已确认】": "Tô Châu 【Đã xác nhận địa chỉ】",
        "天津【地址未确认】": "Thiên Tân 【Chưa xác nhận địa chỉ】",
        "福州【地址未确认】": "Phúc Châu 【Chưa xác nhận địa chỉ】",
        "珠海【地址未确认】": "Chu Hải 【Chưa xác nhận địa chỉ】",
        "南京【地址": "Nam Kinh 【Địa chỉ",
        "已": "đã",
        "确认】": "xác nhận】",
        "中山【地址未确认】": "Trung Sơn 【Chưa xác nhận địa chỉ】",
        "济南【地址": "Tế Nam 【Địa chỉ",
        "东莞【地址未确认】": "Đông Hoản 【Chưa xác nhận địa chỉ】",
        "常州【地址待确认】": "Thường Châu 【Chờ xác nhận địa chỉ】",
        "青岛【地址未确认】": "Thanh Đảo 【Chưa xác nhận địa chỉ】",
        "太原【地址": "Thái Nguyên 【Địa chỉ",
        "温州【地址": "Ôn Châu 【Địa chỉ",
        "重庆": "Trùng Khánh",
        "合肥【地址未确认】": "Hợp Phì 【Chưa xác nhận địa chỉ】",
        "襄阳【地址确认】": "Tương Dương 【Đã xác nhận địa chỉ】",

        # Addresses (keep Chinese location names but translate structure words)
        "北京亦庄分会场：": "Phân hội trường Bắc Kinh Diệc Trang:",
        "北京亦庄信创园会议中心": "Trung tâm hội nghị Tín Sáng Viên Bắc Kinh Diệc Trang",
        "北京朝阳分会场：北京市朝阳区酒仙桥北路乙十号院星地中心C座10层路演厅":
            "Phân hội trường Bắc Kinh Triều Dương: Phòng roadshow tầng 10 tòa C, Trung tâm Tinh Địa, viện số 10B đường Bắc Tửu Tiên Kiều, quận Triều Dương, Bắc Kinh",
        "张江科学之门": "Cổng Khoa học Trương Giang",
        "成都·": "Thành Đô·",
        "天府长岛数字文创园路演厅": "Phòng roadshow Khu sáng tạo số Thiên Phủ Trường Đảo",
        "（高新区盛通街88号2栋1层）": "(Tầng 1 tòa 2, số 88 đường Thịnh Thông, khu Cao Tân)",
        "深圳南山区前海深国际前海颐都大厦5F（国家对外文化贸易基地（深圳）出海中心）":
            "Tầng 5F tòa nhà Thâm Quốc Tế Tiền Hải Di Đô, quận Nam Sơn, Thâm Quyến (Trung tâm ra nước ngoài Cơ sở Thương mại Văn hóa Đối ngoại Quốc gia (Thâm Quyến))",
        "杭州东站未来数智港一楼": "Tầng 1 Cảng Số Trí Tương Lai, Ga Đông Hàng Châu",
        "或云谷中心": "Hoặc Trung tâm Vân Cốc",

        "广州市海珠区华新中心18楼": "Tầng 18 Trung tâm Hoa Tân, quận Hải Châu, thành phố Quảng Châu",
        "鄂港澳青创园5楼报告厅": "Phòng báo cáo tầng 5 Khu Thanh niên Sáng tạo Ngạc Cảng Áo",
        "呼和浩特水岸小镇D区7号楼模创空间": "Không gian Mô Sáng, tòa 7 khu D, Thị trấn Thủy Ngạn, Hohhot",
        "苏州工业园区南岸新地6号楼三楼 光合厅 ": "Tầng 3 tòa 6, Nam Ngạn Tân Địa, Khu Công nghiệp Tô Châu - Hội trường Quang Hợp ",
        "天津市西青区智慧山南塔405": "Phòng 405 Tháp Nam Trí Tuệ Sơn, quận Tây Thanh, thành phố Thiên Tân",

        "福州市晋安区前歧路27号 洋下党群服务中心 4楼": "Tầng 4 Trung tâm Phục vụ Đảng Quần Dương Hạ, số 27 đường Tiền Kỳ, quận Tấn An, thành phố Phúc Châu",
        "珠海市中电南方软件园A2二层202会议室": "Phòng họp 202 tầng 2 A2, Vườn Phần mềm Trung Điện Nam Phương, thành phố Chu Hải",
        "南京市玄武大道699号徐庄高新区行政大楼A座1楼": "Tầng 1 tòa A, Tòa nhà Hành chính Khu Cao Tân Từ Trang, số 699 đại lộ Huyền Vũ, thành phố Nam Kinh",
        "中山东区街道中山四路88号盛景尚峰1座2楼中山青年创业梦工场":
            "Công xưởng Mơ ước Thanh niên Khởi nghiệp Trung Sơn, tầng 2 tòa 1 Thịnh Cảnh Thượng Phong, số 88 đường Trung Sơn Tứ, phường Đông Khu, Trung Sơn",
        "山东省济南市历下区新泺大街1766号齐鲁软件园大厦A座12F":
            "Tầng 12F tòa A, Tòa nhà Vườn Phần mềm Tề Lỗ, số 1766 đường Tân Lạc, quận Lịch Hạ, thành phố Tế Nam, tỉnh Sơn Đông",

        "松山湖国际创新创业社区": "Cộng đồng Đổi mới Sáng tạo Quốc tế Tùng Sơn Hồ",
        "G4栋21楼": "Tầng 21 tòa G4",
        "金坛清风路 2 号 金坛区图书馆": "Thư viện quận Kim Đàn, số 2 đường Thanh Phong, Kim Đàn",
        "青岛市李沧区青山路700号金海牛能源环境产业园A座521会议室":
            "Phòng họp 521 tòa A, Khu Công nghiệp Năng lượng Môi trường Kim Hải Ngưu, số 700 đường Thanh Sơn, quận Lý Thương, thành phố Thanh Đảo",
        "好": "Tốt",
        "太原市": "Thành phố Thái Nguyên",
        "府西街28号（邮政储蓄银行，右侧3层）": "Số 28 đường Phủ Tây (Ngân hàng Tiết kiệm Bưu chính, tầng 3 bên phải)",
        "温州市瓯海区（温州）数安港A2栋三楼温州数据研究院":
            "Viện Nghiên cứu Dữ liệu Ôn Châu, tầng 3 tòa A2 Cảng Số An (Ôn Châu), quận Âu Hải, thành phố Ôn Châu",

        # More city entries
        "郑州【地址未确认】": "Trịnh Châu 【Chưa xác nhận địa chỉ】",
        "乌鲁木齐【地址已确认】": "Urumqi 【Đã xác nhận địa chỉ】",
        "西安【地址未确认】": "Tây An 【Chưa xác nhận địa chỉ】",
        "南昌【地址未确认】": "Nam Xương 【Chưa xác nhận địa chỉ】",
        "宁波【地址未确认】": "Ninh Ba 【Chưa xác nhận địa chỉ】",
        "威海【地址未确认】": "Uy Hải 【Chưa xác nhận địa chỉ】",
        "昆明【地址已确认】": "Côn Minh 【Đã xác nhận địa chỉ】",
        "慈溪【地址未确认】": "Từ Khê 【Chưa xác nhận địa chỉ】",
        "汕头【地址未确认】": "Sán Đầu 【Chưa xác nhận địa chỉ】",
        "徐州【地址未确认】": "Từ Châu 【Chưa xác nhận địa chỉ】",
        "贵阳【地址未确认】": "Quý Dương 【Chưa xác nhận địa chỉ】",
        "大理【地址": "Đại Lý 【Địa chỉ",
        "大连【地址未确认】": "Đại Liên 【Chưa xác nhận địa chỉ】",
        "厦门【地址未确认】": "Hạ Môn 【Chưa xác nhận địa chỉ】",
        "石家庄【地址未确认】": "Thạch Gia Trang 【Chưa xác nhận địa chỉ】",
        "海口【地址已确认】": "Hải Khẩu 【Đã xác nhận địa chỉ】",
        "淮北【地址已确认】": "Hoài Bắc 【Đã xác nhận địa chỉ】",
        "衡水【地址已确认】": "Hành Thủy 【Đã xác nhận địa chỉ】",
        "沈阳【地址未确认】": "Thẩm Dương 【Chưa xác nhận địa chỉ】",
        "长春": "Trường Xuân",
        "无锡【地址已确认】": "Vô Tích 【Đã xác nhận địa chỉ】",
        "湛江【地址已确认】": "Trạm Giang 【Đã xác nhận địa chỉ】",
        "库尔勒【地址已确认】": "Korla 【Đã xác nhận địa chỉ】",
        "邯郸【地址确认】": "Hàm Đan 【Đã xác nhận địa chỉ】",
        "宜春奉新【地址已确认】": "Nghi Xuân Phụng Tân 【Đã xác nhận địa chỉ】",

        # More addresses
        "郑州市高新区大学科技园东区16号楼C座2楼":
            "Tầng 2 tòa C, tòa 16 khu Đông Công viên Khoa học Đại học, khu Cao Tân, thành phố Trịnh Châu",
        "乌鲁木齐市高新区（新市区）北京南路358号大成国际大厦20层2006":
            "Phòng 2006 tầng 20, Tòa nhà Quốc tế Đại Thành, số 358 đường Nam Bắc Kinh, khu Cao Tân (quận Tân Thị), thành phố Urumqi",
        "西安市·高新区高新二路": "Đường Cao Tân Nhị, khu Cao Tân, thành phố Tây An",
        "南昌市高新区·艾溪湖北路77号北航科技园B1栋903":
            "Phòng 903 tòa B1, Khu Công nghệ Bắc Hàng, số 77 đường Bắc Hồ Ngải Khê, khu Cao Tân, thành phố Nam Xương",
        "宁波市人才之家4楼": "Tầng 4 Nhà Nhân tài, thành phố Ninh Ba",
        "威海市环翠区青岛北路2号中国·威海人力资源服务产业园二楼":
            "Tầng 2 Khu Công nghiệp Dịch vụ Nhân lực Trung Quốc·Uy Hải, số 2 đường Bắc Thanh Đảo, quận Hoàn Thúy, thành phố Uy Hải",
        "昆明市盘龙区联盟街道金瓦路69号云南能投大厦": "Tòa nhà Vân Nam Năng Đầu, số 69 đường Kim Ngõa, phường Liên Minh, quận Bàn Long, thành phố Côn Minh",
        "慈溪市周巷镇联胜路56号三楼杭州湾畔岸": "Tầng 3 số 56 đường Liên Thắng, trấn Chu Hạng, thành phố Từ Khê - Bờ Vịnh Hàng Châu",
        "汕头市大学路叠金工业区榕江创客空间": "Không gian Sáng tạo Dung Giang, Khu Công nghiệp Điệp Kim, đường Đại Học, thành phố Sán Đầu",
        "徐州市泉山区翡翠花园翡翠时光街12号（翡翠时光咖啡）":
            "Số 12 phố Thời Quang Phỉ Thúy, Khu vườn Phỉ Thúy, quận Tuyền Sơn, thành phố Từ Châu (Cà phê Thời Quang Phỉ Thúy)",

        "重庆市九龙坡区渝州路27号重庆赛博AI社区·二厂（重庆市科协大楼A栋附4号）":
            "Cộng đồng AI Trùng Khánh Cyborg·Nhà máy số 2, số 27 đường Du Châu, quận Cửu Long Pha, thành phố Trùng Khánh (Phụ số 4 tòa A, Tòa nhà Hiệp hội Khoa học Kỹ thuật Trùng Khánh)",
        "合肥市蜀山区黄山路与石台路交口安徽国际商务中心A座":
            "Tòa A Trung tâm Thương mại Quốc tế An Huy, ngã tư đường Hoàng Sơn và đường Thạch Đài, quận Thục Sơn, thành phố Hợp Phì",
        "襄阳市高新区追日路2号襄阳科技馆四楼学术报告厅":
            "Phòng Báo cáo Học thuật tầng 4, Bảo tàng Khoa học Kỹ thuật Tương Dương, số 2 đường Truy Nhật, khu Cao Tân, thành phố Tương Dương",

        "贵阳市花溪区溪北路贵州大学数智学部": "Khoa Số Trí, Đại học Quý Châu, đường Khê Bắc, quận Hoa Khê, thành phố Quý Dương",
        "大理市下关嘉士柏小镇创翼楼四楼白鹤堂": "Phòng Bạch Hạc, tầng 4 tòa Sáng Dực, Thị trấn Carlsberg, Hạ Quan, thành phố Đại Lý",
        "大连市中山区友好路101号曼哈顿大厦2905":
            "Phòng 2905 Tòa nhà Manhattan, số 101 đường Hữu Hảo, quận Trung Sơn, thành phố Đại Liên",
        "厦门集美区（待定）": "Quận Tập Mỹ, Hạ Môn (chờ xác định)",
        "石家庄裕华区裕华万达1404": "Phòng 1404 Vạn Đạt Dụ Hoa, quận Dụ Hoa, Thạch Gia Trang",
        "海口市美兰区海甸二西路16号海南省创业就业协会3楼":
            "Tầng 3 Hiệp hội Khởi nghiệp Việc làm tỉnh Hải Nam, số 16 đường Tây 2 Hải Điện, quận Mỹ Lan, thành phố Hải Khẩu",
        "淮北市相山区淮海西路与长山路交口东北侧、杭淮科学大厦7楼704":
            "Phòng 704 tầng 7, Tòa nhà Khoa học Hàng Hoài, phía Đông Bắc ngã tư đường Tây Hoài Hải và đường Trường Sơn, quận Tương Sơn, thành phố Hoài Bắc",
        "滨湖区金城西路500-1号图书馆负一楼指挥大厅（无锡市滨湖区城市运行管理中心）":
            "Đại sảnh Chỉ huy tầng hầm 1, Thư viện số 500-1 đường Tây Kim Thành, quận Tân Hồ (Trung tâm Quản lý Vận hành Đô thị quận Tân Hồ, thành phố Vô Tích)",
        "衡水市桃城区衡水市图书馆": "Thư viện thành phố Hành Thủy, quận Đào Thành, thành phố Hành Thủy",
        "融创空间（原思维盒子众创空间(华盛新城店)），赤坎区海田路5号华盛新城商住小区Q-1栋Q-2栋一层10号商铺":
            "Không gian Dung Sáng (nguyên Không gian sáng tạo Hộp Tư duy (chi nhánh Hoa Thịnh Tân Thành)), cửa hàng số 10 tầng 1 tòa Q-1 Q-2, khu thương mại Hoa Thịnh Tân Thành, số 5 đường Hải Điền, quận Xích Khảm",

        "库尔勒经济技术开发区新疆库尔勒高新数字产业园12号楼":
            "Tòa 12, Khu Công nghiệp Số Cao Tân Tân Cương Korla, Khu Phát triển Kinh tế Kỹ thuật Korla",
        "邯郸市丛台区联通北路和联防路交叉口东南角众创大厦801":
            "Phòng 801 Tòa nhà Chúng Sáng, góc Đông Nam ngã tư đường Bắc Liên Thông và đường Liên Phòng, quận Tùng Đài, thành phố Hàm Đan",
        "宜春市奉新县凤凰山路新时代文明实践中心":
            "Trung tâm Thực hành Văn minh Thời đại Mới, đường Phượng Hoàng Sơn, huyện Phụng Tân, thành phố Nghi Xuân",

        # People names - keep as-is or transliterate
        "茹九儿": "Như Cửu Nhi",
        "嘉琛": "Gia Thâm",
        "、无锡一棵树": ", Nhất Khỏa Thụ (Vô Tích)",
        "田颖芊": "Điền Dĩnh Thiên",
        "、罗东": ", La Đông",

        # Year planning section
        "✅2026全年活动规划": "✅ Kế hoạch hoạt động cả năm 2026",
        "每月最后一个周日": "Chủ nhật cuối cùng mỗi tháng",
        "1月25日（": "25/1 (",
        "【已结束】AI切磋大会🌟第21期1月25日 - AI年货节": "【Đã kết thúc】Đại hội giao lưu AI 🌟 Kỳ 21 ngày 25/1 - Hội chợ năm mới AI",
        "3月29日（": "29/3 (",
        "4月26日（）": "26/4 ()",
        "5月31日（）": "31/5 ()",
        "6月28日（）": "28/6 ()",
        "7月26日（）": "26/7 ()",
        "8月30日（）": "30/8 ()",
        "9月27日（）": "27/9 ()",
        "10月25日（）": "25/10 ()",
        "11月29日（）": "29/11 ()",
        "12月27日（AI年度总结）": "27/12 (Tổng kết năm AI)",

        # Additional entries that might appear
        "     组织者": "     Người tổ chức",
        "@\n": "@\n",
        "   ": "   ",
        " ": " ",

        # More city status variants
        "地址未确认": "Chưa xác nhận địa chỉ",
        "地址待确认": "Chờ xác nhận địa chỉ",
        "地址确认": "Đã xác nhận địa chỉ",

        # Additional misc
        "马德里【地址未确认】": "Madrid 【Chưa xác nhận địa chỉ】",
        "东京": "Tokyo",
        "清迈【地址未确认】": "Chiang Mai 【Chưa xác nhận địa chỉ】",
        "悉尼【地址未确认】": "Sydney 【Chưa xác nhận địa chỉ】",
        "伦敦【地址未确认】": "London 【Chưa xác nhận địa chỉ】",
        "泰国清迈": "Chiang Mai, Thái Lan",
        "海外【地址未确认】": "Nước ngoài 【Chưa xác nhận địa chỉ】",
    }

    # Exact match first
    if text in translations:
        return translations[text]

    # Try stripping whitespace for match
    stripped = text.strip()
    if stripped in translations:
        # Preserve original whitespace
        prefix = text[:len(text) - len(text.lstrip())]
        suffix = text[len(text.rstrip()):]
        return prefix + translations[stripped] + suffix

    # For texts not in the dictionary, do character-level translation for common patterns
    # This handles any remaining Chinese text
    result = text

    # Common word replacements for any remaining Chinese
    remaining_translations = {
        "城市": "Thành phố",
        "地址": "Địa chỉ",
        "组织者": "Người tổ chức",
        "场地": "Địa điểm",
        "地址已确认": "Đã xác nhận địa chỉ",
        "地址未确认": "Chưa xác nhận địa chỉ",
        "地址待确认": "Chờ xác nhận địa chỉ",
        "地址确认": "Đã xác nhận địa chỉ",
        "已确认": "Đã xác nhận",
        "未确认": "Chưa xác nhận",
        "待确认": "Chờ xác nhận",
        "确认": "xác nhận",
        "已": "đã",
        "北京": "Bắc Kinh",
        "上海": "Thượng Hải",
        "广州": "Quảng Châu",
        "深圳": "Thâm Quyến",
        "成都": "Thành Đô",
        "杭州": "Hàng Châu",
        "武汉": "Vũ Hán",
        "天津": "Thiên Tân",
        "苏州": "Tô Châu",
        "南京": "Nam Kinh",
        "重庆": "Trùng Khánh",
        "西安": "Tây An",
        "郑州": "Trịnh Châu",
        "济南": "Tế Nam",
        "太原": "Thái Nguyên",
        "南昌": "Nam Xương",
        "福州": "Phúc Châu",
        "珠海": "Chu Hải",
        "中山": "Trung Sơn",
        "东莞": "Đông Hoản",
        "合肥": "Hợp Phì",
        "昆明": "Côn Minh",
        "青岛": "Thanh Đảo",
        "温州": "Ôn Châu",
        "宁波": "Ninh Ba",
        "常州": "Thường Châu",
        "大连": "Đại Liên",
        "厦门": "Hạ Môn",
        "贵阳": "Quý Dương",
        "襄阳": "Tương Dương",
        "威海": "Uy Hải",
        "汕头": "Sán Đầu",
        "徐州": "Từ Châu",
        "海口": "Hải Khẩu",
        "衡水": "Hành Thủy",
        "淮北": "Hoài Bắc",
        "大理": "Đại Lý",
        "石家庄": "Thạch Gia Trang",
        "乌鲁木齐": "Urumqi",
        "呼和浩特": "Hohhot",
        "慈溪": "Từ Khê",
        "沈阳": "Thẩm Dương",
        "长春": "Trường Xuân",
        "无锡": "Vô Tích",
        "湛江": "Trạm Giang",
        "库尔勒": "Korla",
        "邯郸": "Hàm Đan",
        "清迈": "Chiang Mai",
        "悉尼": "Sydney",
        "马德里": "Madrid",
        "伦敦": "London",
        "东京": "Tokyo",
        "宜春奉新": "Nghi Xuân Phụng Tân",
        "分会场": "Phân hội trường",
        "会议室": "Phòng họp",
        "报告厅": "Phòng báo cáo",
        "路演厅": "Phòng roadshow",
        "图书馆": "Thư viện",
        "省": "tỉnh",
        "市": "thành phố ",
        "区": "quận ",
        "街道": "phường ",
        "路": " đường ",
        "号": " số ",
        "楼": " tầng ",
        "栋": " tòa ",
        "层": " tầng ",
        "座": " tòa ",
    }

    # Try replacing known substrings in order from longest to shortest
    sorted_keys = sorted(remaining_translations.keys(), key=len, reverse=True)
    for cn, vi in [(k, remaining_translations[k]) for k in sorted_keys]:
        result = result.replace(cn, vi)

    return result


# Now process all blocks
translated = copy.deepcopy(data)
total_text_segments = 0
translated_segments = 0
kept_segments = 0

for block in translated['blocks']:
    for el in block.get('elements', []):
        if 'content' in el:
            original = el['content']
            total_text_segments += 1

            # Check if it has a link - keep URLs unchanged
            if el.get('style', {}).get('link'):
                # Only translate if it has Chinese, keep link URL
                if has_chinese(original):
                    el['content'] = translate(original)
                    translated_segments += 1
                else:
                    kept_segments += 1
            elif has_chinese(original):
                el['content'] = translate(original)
                translated_segments += 1
            else:
                kept_segments += 1

# Save translated file
with open('_art4_trans.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f"Total blocks: {len(translated['blocks'])}")
print(f"Total text segments: {total_text_segments}")
print(f"Translated segments: {translated_segments}")
print(f"Kept unchanged: {kept_segments}")
print("Saved to _art4_trans.json")
