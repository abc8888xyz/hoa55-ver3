# -*- coding: utf-8 -*-
"""
Translate Lark document blocks from Chinese to Vietnamese.
Processes every block from top to bottom.
Writes translated_blocks.json then updates Lark.
"""
import json
import copy
import re
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))

def translate_text(text):
    """Translate Chinese text to Vietnamese. Only translates Chinese characters."""
    # Dictionary of all translations
    T = {}

    # Title
    T["🎬 Seedance 2.0 使用手册（全新多模态创作体验）"] = "🎬 Seedance 2.0 Hướng dẫn sử dụng (Trải nghiệm sáng tạo đa phương thức hoàn toàn mới)"
    T["视频 Seedance 2.0 正式上线！"] = "Video Seedance 2.0 chính thức ra mắt!"
    T["还记得从只能用文字和首/尾帧「讲故事」的那天起，我们就想做出一个真正听得懂你表达的视频模型。今天，它真的来了！"] = 'Còn nhớ từ ngày chỉ có thể dùng văn bản và khung hình đầu/cuối để "kể chuyện", chúng tôi đã muốn tạo ra một mô hình video thực sự hiểu được cách bạn diễn đạt. Hôm nay, nó thực sự đã đến!'
    T["Seedance 2.0 现在支持图像、视频、音频、文本四种模态输入，表达方式更丰富，生成也更可控"] = "Seedance 2.0 hiện hỗ trợ bốn loại đầu vào đa phương thức: hình ảnh, video, âm thanh, văn bản — cách diễn đạt phong phú hơn, việc tạo nội dung cũng dễ kiểm soát hơn"
    T["你可以用一张图定下画面风格，用一个视频指定角色的动作和镜头的变化，再用几秒音频带起节奏氛围……搭配提示词，让创作过程变得更自然、更高效，也更像真正的\u201c导演\u201d。"] = 'Bạn có thể dùng một bức ảnh để định phong cách hình ảnh, dùng một video để chỉ định động tác nhân vật và chuyển động ống kính, rồi dùng vài giây âm thanh để tạo nhịp điệu và bầu không khí... kết hợp với prompt, quá trình sáng tạo trở nên tự nhiên hơn, hiệu quả hơn, và giống một "đạo diễn" thực sự hơn.'
    T["这次升级中，"] = "Trong lần nâng cấp này,"
    T["\u201c参考能力\u201d是最大亮点"] = '"Khả năng tham chiếu" là điểm nổi bật lớn nhất'
    T["："] = ":"
    T["📷 参考图像可精准还原画面构图、角色细节"] = "📷 Hình ảnh tham chiếu có thể tái tạo chính xác bố cục hình ảnh, chi tiết nhân vật"
    T["🎥 参考视频支持镜头语言、复杂的动作节奏、创意特效的复刻"] = "🎥 Video tham chiếu hỗ trợ ngôn ngữ ống kính, nhịp độ động tác phức tạp, tái tạo hiệu ứng sáng tạo"
    T["⏱ 视频支持平滑延长与衔接，可按用户提示生成连续镜头，不止生成，还能\u201c接着拍\u201d"] = '⏱ Video hỗ trợ kéo dài mượt mà và nối tiếp, có thể tạo cảnh quay liên tục theo gợi ý người dùng, không chỉ tạo mới mà còn "quay tiếp"'
    T["✂️ 编辑能力同步增强，支持对已有视频进行角色更替、删减、增加"] = "✂️ Khả năng chỉnh sửa được tăng cường đồng bộ, hỗ trợ thay thế, cắt giảm, thêm nhân vật trong video có sẵn"
    T["我们知道，视频创作从来不仅是\u201c生成\u201d，更是对表达的控制。2.0 不只是多模态，更是一种真正可控的创作方式"] = 'Chúng tôi biết rằng sáng tạo video không chỉ là "tạo ra", mà còn là kiểm soát cách diễn đạt. 2.0 không chỉ là đa phương thức, mà còn là một phương thức sáng tạo thực sự có thể kiểm soát'
    T["Seedance 2.0，多模态创作，从这里启程。请你们大胆想象，其余的交给它"] = "Seedance 2.0, sáng tạo đa phương thức, khởi hành từ đây. Hãy mạnh dạn tưởng tượng, phần còn lại để nó lo"
    T["参数预览"] = "Xem trước thông số"
    T["核心维度"] = "Thông số cốt lõi"
    T["图片输入"] = "Đầu vào hình ảnh"
    T["≤ 9 张"] = "≤ 9 tấm"
    T["视频输入"] = "Đầu vào video"
    T["≤ 3 个，总时长不超过15s"] = "≤ 3 file, tổng thời lượng không quá 15s"
    T["（有参考视频会贵一点哦）"] = "(Có video tham chiếu sẽ tốn hơn một chút nhé)"
    T["音频输入"] = "Đầu vào âm thanh"
    T["支持 MP3 上传，数量≤ 3 个，总时长不超过15s"] = "Hỗ trợ tải lên MP3, số lượng ≤ 3 file, tổng thời lượng không quá 15s"
    T["文本输入"] = "Đầu vào văn bản"
    T["自然语言"] = "Ngôn ngữ tự nhiên"
    T["生成时长"] = "Thời lượng tạo"
    T["≤ 15s，可自由选择4-15s"] = "≤ 15s, có thể tự do chọn 4-15s"
    T["声音输出"] = "Đầu ra âm thanh"
    T["自带音效/配乐"] = "Tích hợp sẵn hiệu ứng âm thanh/nhạc nền"
    T["交互限制："] = "Giới hạn tương tác:"
    T["目前支持的混合输入总上限是 12 个文件"] = "Hiện tại tổng giới hạn đầu vào hỗn hợp là 12 file"
    T["。建议优先上传对画面或节奏影响最大的素材，合理分配不同模态的文件数量"] = ". Khuyến nghị ưu tiên tải lên tài liệu có ảnh hưởng lớn nhất đến hình ảnh hoặc nhịp điệu, phân bổ hợp lý số lượng file của các phương thức khác nhau"
    T["交互形式"] = "Hình thức tương tác"
    T["⚠️注意："] = "⚠️Lưu ý:"
    T["Seedance 2.0 支持"] = "Seedance 2.0 hỗ trợ"
    T["「首尾帧」"] = "「Khung hình đầu cuối」"
    T["和"] = "và"
    T["「全能参考」"] = "「Tham chiếu toàn năng」"
    T["入口，"] = "đầu vào,"
    T["智能多帧和主体参考无法选中"] = "Đa khung hình thông minh và tham chiếu chủ thể không thể chọn"
    T["。若你只上传首帧图 + prompt，可走首尾帧入口；如需多模态（图、视频、音频、文本）组合输入，则需进入全能参考入口"] = ". Nếu bạn chỉ tải lên ảnh khung hình đầu + prompt, có thể dùng đầu vào khung hình đầu cuối; nếu cần kết hợp đa phương thức (ảnh, video, âm thanh, văn bản), thì cần vào đầu vào tham chiếu toàn năng"
    T["当前支持的交互方式是通过\u201c@素材名\u201d来指定每个图片、视频、音频的用途，例如：@图片1 作为首帧，@视频1 参考镜头语言，@音频1 用于配乐"] = 'Cách tương tác hiện tại là thông qua "@tên tài liệu" để chỉ định mục đích của mỗi hình ảnh, video, âm thanh, ví dụ: @Ảnh1 làm khung hình đầu, @Video1 tham chiếu ngôn ngữ ống kính, @Âm thanh1 dùng làm nhạc nền'
    T["主界面："] = "Giao diện chính:"
    T["入口：Seedance 2.0 - 全能参考/首尾帧"] = "Đầu vào: Seedance 2.0 - Tham chiếu toàn năng/Khung hình đầu cuối"
    T["唤起本地文件弹窗"] = "Mở cửa sổ chọn file nội bộ"
    T["选定文件，添加至输入框"] = "Chọn file, thêm vào ô nhập liệu"
    T["全能参考模式下如何@："] = "Cách dùng @ trong chế độ tham chiếu toàn năng:"
    T["方法1：输入\u201c@\u201d唤起参考调用"] = 'Cách 1: Nhập "@" để gọi tham chiếu'
    T["输入\u201c@\u201d"] = 'Nhập "@"'
    T["选择参考，落入输入框"] = "Chọn tham chiếu, đưa vào ô nhập liệu"
    T["输入prompt"] = "Nhập prompt"
    T["方法2：点击参数工具\u201c@\u201d唤起参考调用"] = 'Cách 2: Nhấp vào công cụ "@" để gọi tham chiếu'
    T["点击\u201c@\u201d"] = 'Nhấp "@"'
    T["上传素材后，"] = "Sau khi tải lên tài liệu,"
    T["图片、视频、音频"] = "hình ảnh, video, âm thanh"
    T["都支持"] = "đều hỗ trợ"
    T["悬停预览"] = "xem trước khi di chuột"
    T["下面是一些不同场景下的用法和玩法，帮助你更好地理解 Seedance 2.0 在生成质量上、控制能力和创意表现上的升级。如果你还不知道从哪开始，不如先看看这些例子，激发灵感～"] = "Dưới đây là một số cách sử dụng và chơi trong các tình huống khác nhau, giúp bạn hiểu rõ hơn về sự nâng cấp của Seedance 2.0 trong chất lượng tạo nội dung, khả năng kiểm soát và biểu hiện sáng tạo. Nếu bạn chưa biết bắt đầu từ đâu, hãy xem qua các ví dụ này để lấy cảm hứng~"
    T["Seedance 2.0 能力 / 提升预览"] = "Seedance 2.0 Năng lực / Xem trước nâng cấp"
    T["基础能力显著增强：更稳、更顺、更像真的！ "] = "Năng lực cơ bản tăng cường đáng kể: Ổn định hơn, mượt hơn, giống thật hơn! "
    T["不只是多模态，Seedance 2.0 在基础层面显著增强，"] = "Không chỉ là đa phương thức, Seedance 2.0 được tăng cường đáng kể ở tầng cơ bản,"
    T["物理规律更合理"] = "Quy luật vật lý hợp lý hơn"
    T["、"] = ","
    T["动作表现更自然流畅"] = "Biểu hiện động tác tự nhiên mượt mà hơn"
    T["指令理解更精准"] = "Hiểu lệnh chính xác hơn"
    T["风格保持更稳定"] = "Giữ phong cách ổn định hơn"
    T["，不仅能稳定完成复杂动作、连续运动等高难度生成任务，也让整体视频效果更真实、更顺滑，是一次底层能力的全面进化！"] = ", không chỉ hoàn thành ổn định các nhiệm vụ tạo nội dung khó như động tác phức tạp, chuyển động liên tục, mà còn làm hiệu ứng video tổng thể chân thực hơn, mượt mà hơn — đây là một cuộc tiến hóa toàn diện ở tầng nền tảng!"
    T["Case："] = "Ví dụ:"
    T["女孩在优雅的晒衣服，晒完接着在桶里拿出另一件，用力抖一抖衣服。"] = "Cô gái đang phơi quần áo một cách duyên dáng, phơi xong lại lấy ra một chiếc khác từ thùng, rũ mạnh chiếc áo."
    T["超强真实感"] = "Cảm giác chân thực siêu mạnh"
    T["画里面的人物心虚的表情，眼睛左右看了看探出画框，快速的将手伸出画框拿起可乐喝了一口，然后露出一脸满足的表情，这时传来脚步声，画中的人物赶紧将可乐放回原位，此时一位西部牛仔拿起杯子里的可乐走了，最后镜头前推画面慢慢变得纯黑背景只有顶光照耀的罐装可乐，画面最下方出现艺术感字幕和旁白：\u201c宜口可乐，不可不尝！\u201d"] = 'Nhân vật trong tranh với vẻ mặt ngại ngùng, mắt nhìn trái phải rồi thò ra khỏi khung tranh, nhanh chóng đưa tay ra ngoài khung lấy lon coca uống một ngụm, rồi lộ vẻ mặt mãn nguyện. Lúc này vang lên tiếng bước chân, nhân vật trong tranh vội vàng đặt coca về chỗ cũ. Một cao bồi miền Tây cầm lon coca trong cốc bước đi. Cuối cùng ống kính đẩy tới, màn hình dần chuyển sang nền đen thuần chỉ có ánh đèn trên chiếu xuống lon coca, phía dưới màn hình xuất hiện phụ đề nghệ thuật và lời bình: "Coca ngon, không thể không thử!"'
    T["镜头小幅度拉远（露出街头全景）并跟随女主移动，风吹拂着女主的裙摆，女主走在19世纪的伦敦大街上；女主走着走着右边街道驶来一辆蒸汽机车，快速驶过女主身旁，风将女主的裙摆吹起，女主一脸震惊的赶忙用双手向下捂住裙摆；背景音效为走路声，人群声，汽车声等等"] = "Ống kính kéo ra nhẹ (lộ toàn cảnh đường phố) và theo dõi nữ chính di chuyển, gió thổi tà váy nữ chính bay, nữ chính đi trên con phố London thế kỷ 19; nữ chính đang đi thì từ bên phải đường một chiếc xe hơi chạy bằng hơi nước lao tới, nhanh chóng vượt qua bên cạnh nữ chính, gió thổi tung tà váy, nữ chính mặt đầy kinh ngạc vội dùng hai tay giữ chặt váy; âm thanh nền là tiếng bước chân, tiếng đám đông, tiếng xe cộ v.v."
    T["镜头跟随黑衣男子快速逃亡，后面一群人在追，镜头转为侧面跟拍，人物惊慌撞倒路边的水果摊爬起来继续逃，人群慌乱的声音。"] = "Ống kính theo dõi người đàn ông áo đen chạy trốn nhanh chóng, phía sau một đám người đuổi theo, ống kính chuyển sang quay bám từ bên cạnh, nhân vật hoảng loạn đâm đổ quầy trái cây bên đường rồi đứng dậy tiếp tục chạy, tiếng đám đông hỗn loạn."
    T["多模态全面升级：视频创作进入\u201c自由组合\u201d时代！"] = 'Đa phương thức nâng cấp toàn diện: Sáng tạo video bước vào thời đại "tự do kết hợp"!'
    T["Seedance 2.0 多模态介绍"] = "Giới thiệu đa phương thức Seedance 2.0"
    T["支持上传文本、图片、视频、音频，这些素材都可以被用作使用对象或参考对象。你可以参考任何内容的动作、特效、形式、运镜、人物、场景、声音，"] = "Hỗ trợ tải lên văn bản, hình ảnh, video, âm thanh — tất cả tài liệu này đều có thể dùng làm đối tượng sử dụng hoặc đối tượng tham chiếu. Bạn có thể tham chiếu động tác, hiệu ứng, hình thức, chuyển động ống kính, nhân vật, bối cảnh, âm thanh của bất kỳ nội dung nào,"
    T["只要提示词写得清楚"] = "chỉ cần prompt viết rõ ràng"
    T["，模型都能理解。"] = ", mô hình đều có thể hiểu."
    T["Seedance 2.0 = 多模态参考能力（可参考万物） + 强创意生成 + 指令响应精准（理解力很棒）"] = "Seedance 2.0 = Khả năng tham chiếu đa phương thức (có thể tham chiếu mọi thứ) + Tạo nội dung sáng tạo mạnh mẽ + Phản hồi lệnh chính xác (khả năng hiểu tuyệt vời)"
    T["用自然语言描述你想要的画面和动作就可以啦，明确是参考，还是编辑～素材多的时候，建议你多检查一下各个 @对象有没有标清楚，别把图、视频、角色搞混了哦"] = "Chỉ cần dùng ngôn ngữ tự nhiên mô tả hình ảnh và động tác bạn muốn là được, nói rõ là tham chiếu hay chỉnh sửa~ Khi có nhiều tài liệu, khuyến nghị kiểm tra lại xem các @đối tượng đã ghi rõ chưa, đừng nhầm lẫn giữa ảnh, video và nhân vật nhé"
    T["特殊使用方式（不设限，仅供参考）："] = "Cách sử dụng đặc biệt (không giới hạn, chỉ mang tính tham khảo):"
    T["有首帧/尾帧图？还想参考视频动作？"] = "Có ảnh khung hình đầu/cuối? Còn muốn tham chiếu động tác video?"
    T[" → 提示词中写清楚，如：\u201c@图1为首帧，参考@视频1的打斗动作\u201d"] = ' → Viết rõ trong prompt, ví dụ: "@Ảnh1 làm khung hình đầu, tham chiếu động tác đánh nhau của @Video1"'
    T["想延长一个已有的视频？"] = "Muốn kéo dài một video có sẵn?"
    T[" → 说明延长时间，如\u201c将@视频1延长 5s\u201d，"] = ' → Nêu rõ thời gian kéo dài, ví dụ "Kéo dài @Video1 thêm 5s",'
    T["注意：此时选择的生成时长应为\u201c新增部分\u201d的时长"] = 'Lưu ý: Lúc này thời lượng tạo được chọn phải là thời lượng của "phần mới thêm"'
    T["（例如延长 5s，生成长度也选 5s"] = "(Ví dụ kéo dài 5s, thời lượng tạo cũng chọn 5s"
    T["想融合多个视频？"] = "Muốn kết hợp nhiều video?"
    T[" → 提示词中说明合成逻辑，如：\u201c我要在@视频1和@视频2之间加一个场景，内容为xxx\u201d"] = ' → Nêu rõ logic ghép nối trong prompt, ví dụ: "Tôi muốn thêm một cảnh giữa @Video1 và @Video2, nội dung là xxx"'
    T["没音频素材？可以直接参考视频里的声音"] = "Không có tài liệu âm thanh? Có thể trực tiếp tham chiếu âm thanh trong video"
    T["想生成连续动作？"] = "Muốn tạo động tác liên tục?"
    T[" → 可以在提示词中加入连续性描述，如：\u201c角色从跳跃直接过渡到翻滚，保持动作连贯流畅\u201d@图1@图2@图3..."] = ' → Có thể thêm mô tả liên tục trong prompt, ví dụ: "Nhân vật từ nhảy chuyển thẳng sang lăn, giữ động tác liền mạch mượt mà" @Ảnh1@Ảnh2@Ảnh3...'
    T["那些一直很难做的视频问题，现在真的能搞定了！"] = "Những vấn đề video khó giải quyết bấy lâu, giờ thực sự đã xử lý được!"
    T["做视频总会碰到一些让人头疼的地方：比如人脸换了、动作不像、视频延长不自然、改着改着整个节奏都变了……这次多模态能把这些\u201c老大难\u201d问题一口气解决了，下面就是具体的使用案例👇"] = 'Làm video luôn gặp phải những điểm đau đầu: ví dụ khuôn mặt bị đổi, động tác không giống, kéo dài video không tự nhiên, sửa mãi cả nhịp điệu đều thay đổi... Lần này đa phương thức có thể giải quyết hết những vấn đề "nan giải" này trong một lần, dưới đây là các ví dụ sử dụng cụ thể👇'
    T["一致性全面提升"] = "Tính nhất quán nâng cấp toàn diện"
    T[" "] = " "
    T["你可能遇到过这些烦恼：画面里人物前后长得不一样、商品细节丢了、小字模糊、场景跳变、镜头风格无法统一……这些在创作中常见的一致性问题，现在在 2.0 中都能被解决。从人脸到服装，再到字体细节，整体一致性更稳、更准"] = "Bạn có thể đã gặp những phiền toái này: nhân vật trong hình trước sau trông khác nhau, chi tiết sản phẩm bị mất, chữ nhỏ mờ, cảnh nhảy đột ngột, phong cách ống kính không thể thống nhất... Những vấn đề nhất quán thường gặp trong sáng tạo, giờ đều có thể giải quyết trong 2.0. Từ khuôn mặt đến trang phục, cho đến chi tiết phông chữ, tính nhất quán tổng thể ổn định hơn, chính xác hơn"
    T["生成结果"] = "Kết quả tạo"
    T["男人@图片1下班后疲惫的走在走廊，脚步变缓，最后停在家门口，脸部特写镜头，男人深呼吸，调整情绪，收起了负面情绪，变得轻松，然后特写翻找出钥匙，插入门锁，进入家里后，他的小女儿和一只宠物狗，欢快的跑过来迎接拥抱，室内非常的温馨，全程自然对话"] = "Người đàn ông @Ảnh1 sau giờ làm mệt mỏi đi trong hành lang, bước chân chậm lại, cuối cùng dừng trước cửa nhà, cận cảnh khuôn mặt, người đàn ông hít thở sâu, điều chỉnh cảm xúc, gạt bỏ cảm xúc tiêu cực, trở nên thoải mái, rồi cận cảnh tìm chìa khóa, cắm vào ổ khóa, sau khi vào nhà, cô con gái nhỏ và một chú chó cưng vui vẻ chạy tới đón ôm, trong nhà rất ấm áp, toàn bộ hội thoại tự nhiên"
    T["将@视频1中的女生换成戏曲花旦，场景在一个精美的舞台上，参考@视频1的运镜和转场效果，利用镜头匹配人物的动作，极致的舞台美感，增强视觉冲击力"] = "Thay cô gái trong @Video1 thành đào nương hý kịch, bối cảnh trên một sân khấu tinh xảo, tham chiếu chuyển động ống kính và hiệu ứng chuyển cảnh của @Video1, dùng ống kính phối hợp với động tác nhân vật, vẻ đẹp sân khấu tuyệt đỉnh, tăng cường tác động thị giác"
    T["使用参考图片人物的形象生成一段古装穿越剧的预告短片。\n 0-3秒画面：参考图片1人物形象的男主手里举起一个篮球，抬头望向镜头。说话\u201c我只是想喝杯酒，该不会要穿越了吧……\u201d \n"] = 'Sử dụng hình tượng nhân vật trong ảnh tham chiếu để tạo trailer phim cổ trang xuyên không.\n 0-3 giây: Nam chính theo hình tượng nhân vật Ảnh1 giơ một quả bóng rổ, ngước nhìn ống kính. Nói "Tôi chỉ muốn uống ly rượu, không lẽ sắp xuyên không..." \n'
    T["4-8秒画面：镜头突然剧烈晃动，操场的场景开始剧烈震动，瞬间切换成古宅的雨夜。一个穿着古装，长相清秀的女主，冷冽的目光穿透雨幕，望向镜头方向。雷鸣声，衣袂猎猎声。女主说话\u201c何人擅闯我永宁侯府？\u201d 9-13秒画面：镜头切到一个穿着明官服的男子坐在衙门里，眼神锐利如刀，愤怒说话\u201c来人！即刻拿下此\u2018妖人\u2019！\u201d 画面闪回：男主穿着不合身的粗布麻衣；在官差的围堵下慌不择路；与女主的身影在雨巷里交错；男主穿着官服走在皇宫里。 14-15秒画面：黑屏，打出片名《醉梦惊华》，伴随着沉重的鼓点。"] = '4-8 giây: Ống kính đột ngột rung lắc dữ dội, cảnh sân vận động bắt đầu rung chuyển mạnh, tức thì chuyển sang đêm mưa cổ trạch. Một nữ chính mặc cổ trang, gương mặt thanh tú, ánh mắt lạnh lẽo xuyên qua màn mưa, nhìn về phía ống kính. Tiếng sấm vang, tiếng vạt áo bay phần phật. Nữ chính nói "Ai dám tự tiện xông vào Vĩnh Ninh Hầu phủ ta?" 9-13 giây: Ống kính chuyển sang một nam nhân mặc quan phục triều Minh ngồi trong nha môn, ánh mắt sắc bén như dao, tức giận nói "Người đâu! Lập tức bắt lấy \'yêu nhân\' này!" Cảnh hồi tưởng: Nam chính mặc áo vải thô không vừa; hoảng loạn chạy trốn dưới sự vây bắt của quan sai; bóng dáng giao nhau với nữ chính trong ngõ mưa; nam chính mặc quan phục đi trong hoàng cung. 14-15 giây: Màn hình đen, hiện tên phim《Túy Mộng Kinh Hoa》, kèm theo tiếng trống trầm.'
    T["参考 @视频1的所有转场和运镜，一镜到底，画面以棋局为起始，镜头左移，展示地板的黄色沙砾，镜头上移来到一个沙滩，沙滩上有足印，一个穿着白色素衣的女生在沙滩上渐行渐远，镜头切到空中的俯拍视角，海水在冲刷（不要出现人物），无缝渐变转场，冲刷的海浪变成飘动的窗帘，镜头拉远，展示女孩的面部特写，一镜到底"] = "Tham chiếu tất cả chuyển cảnh và chuyển động ống kính của @Video1, quay liền một mạch, hình ảnh bắt đầu từ bàn cờ, ống kính dịch trái, hiển thị cát vàng trên sàn, ống kính di chuyển lên đến một bãi biển, trên bãi biển có dấu chân, một cô gái mặc váy trắng trên bãi biển dần xa dần, ống kính chuyển sang góc quay từ trên cao, nước biển đang xô bờ (không có nhân vật), chuyển cảnh hòa tan liền mạch, sóng biển xô bờ biến thành rèm cửa bay phất phơ, ống kính kéo xa, hiển thị cận cảnh khuôn mặt cô gái, quay liền một mạch"
    T["0-2秒画面：快速四格闪切，红、粉、紫、豹纹四款蝴蝶结依次定格，特写缎面光泽与 \u201cch\u00e9ri\u201d 品牌字样。画外音\u201cCh\u00e9ri \uc790\uc11d \ub9ac\ubd04\uc73c\ub85c \ubb34\uad81\ubb34\uc9c4\ud55c \uc544\ub984\ub2e4\uc6c0\uc744 \uc5f0\ucd9c\ud574 \ubcf4\uc138\uc694!\u201d"] = '0-2 giây: Bốn khung hình cắt nhanh, bốn kiểu nơ đỏ, hồng, tím, da báo lần lượt đóng khung, cận cảnh độ bóng lụa sa-tanh và chữ thương hiệu "chéri". Giọng ngoài hình "Chéri \uc790\uc11d \ub9ac\ubd04\uc73c\ub85c \ubb34\uad81\ubb34\uc9c4\ud55c \uc544\ub984\ub2e4\uc6c0\uc744 \uc5f0\ucd9c\ud574 \ubcf4\uc138\uc694!"'
    T["3-6秒画面：特写银色磁吸扣 \u201c咔嗒\u201d 吸合，再轻轻一拉分开，展示丝滑质感与便捷性。画外音\u201c\ub2e8 1\ucd08 \ub9cc\uc5d0 \uc7a0\uadf8\uace0, \ucd5c\uace0\uc758 \uc2a4\ud0c0\uc77c\uc744 \uc644\uc131\ud558\uc138\uc694!\u201d"] = '3-6 giây: Cận cảnh khóa từ tính bạc "tách" hít vào nhau, rồi nhẹ nhàng kéo ra, thể hiện chất cảm mượt mà và tính tiện lợi. Giọng ngoài hình "\ub2e8 1\ucd08 \ub9cc\uc5d0 \uc7a0\uadf8\uace0, \ucd5c\uace0\uc758 \uc2a4\ud0c0\uc77c\uc744 \uc644\uc131\ud558\uc138\uc694!"'
    T["7-12 秒画面：快速切换佩戴场景：酒红款别在大衣领口，通勤氛围感拉满；粉色款绑在马尾，甜妹出街；紫色款系在包带，小众高级；豹纹款挂在西装领，辣妹气场全开。画外音\u201c\ucf54\ud2b8, \uac00\ubc29, \ud5e4\uc5b4 \uc561\uc138\uc11c\ub9ac\uae4c\uc9c0, \ub2e4\uc7ac\ub2e4\ub2a5\ud558\uace0 \uac1c\uc131 \ub118\uce58\ub294 \uc2a4\ud0c0\uc77c\uc744 \uc644\uc131\ud558\uc138\uc694!\u201d"] = '7-12 giây: Cắt nhanh các cảnh đeo: Kiểu đỏ rượu cài ở cổ áo khoác, cảm giác đi làm đầy đủ; kiểu hồng buộc trên đuôi ngựa, gái ngọt ra phố; kiểu tím buộc trên dây đeo túi, độc đáo cao cấp; kiểu da báo treo trên cổ vest, phong thái gái cá tính toàn khai. Giọng ngoài hình "\ucf54\ud2b8, \uac00\ubc29, \ud5e4\uc5b4 \uc561\uc138\uc11c\ub9ac\uae4c\uc9c0, \ub2e4\uc7ac\ub2e4\ub2a5\ud558\uace0 \uac1c\uc131 \ub118\uce58\ub294 \uc2a4\ud0c0\uc77c\uc744 \uc644\uc131\ud558\uc138\uc694!"'
    T["13-15秒画面：四款蝴蝶结并排陈列，品牌名 \u201cch\u00e9ri, \ub2f9\uc2e0\uc5d0\uac8c \uc989\uac01\uc801\uc778 \uc544\ub984\ub2e4\uc6c0\uc744 \uc120\uc0ac\ud569\ub2c8\ub2e4!\u201d"] = '13-15 giây: Bốn kiểu nơ bày cạnh nhau, tên thương hiệu "chéri, \ub2f9\uc2e0\uc5d0\uac8c \uc989\uac01\uc801\uc778 \uc544\ub984\ub2e4\uc6c0\uc744 \uc120\uc0ac\ud569\ub2c8\ub2e4!"'
    T["对@图片2的包包进行商业化的摄像展示，包包的侧面参考@图片1，包包的表面材质参考@图片3，要求将包包的细节均有所展示，背景音恢宏大气，"] = "Quay trình diễn thương mại cho túi xách @Ảnh2, mặt bên của túi tham chiếu @Ảnh1, chất liệu bề mặt túi tham chiếu @Ảnh3, yêu cầu hiển thị tất cả chi tiết của túi, nhạc nền hoành tráng,"
    T["把@图片1作为画面的首帧图，第一人称视角，参考@视频1的运镜效果，上方场景参考@图片2，左边场景参考@图片3，右边场景参考@图片4。"] = "Lấy @Ảnh1 làm khung hình đầu, góc nhìn thứ nhất, tham chiếu hiệu ứng chuyển động ống kính @Video1, cảnh phía trên tham chiếu @Ảnh2, cảnh bên trái tham chiếu @Ảnh3, cảnh bên phải tham chiếu @Ảnh4."
    T["高难度/可控的运镜和动作精准复刻"] = "Chuyển động ống kính và động tác có độ khó cao/có thể kiểm soát, tái tạo chính xác"
    T["以前想让模型模仿电影里的走位、运镜或者复杂动作，要么写一堆细节提示词，要么干脆做不到。而现在，只需要上传一段参考视频，就可以了"] = "Trước đây muốn mô hình bắt chước di chuyển, chuyển động ống kính hoặc động tác phức tạp trong phim, hoặc phải viết hàng loạt prompt chi tiết, hoặc đơn giản là không làm được. Nhưng bây giờ, chỉ cần tải lên một đoạn video tham chiếu là được"
    T["创意模版 / 复杂特效精准复刻"] = "Mẫu sáng tạo / Hiệu ứng phức tạp tái tạo chính xác"
    T["不止能生图写故事，Seedance 2.0 还支持\u201c照着模仿\u201d——创意转场、广告成片、电影片段、复杂剪辑，只要你有参考图或视频，模型就能识别动作节奏、镜头语言、视觉结构，并精准复刻出来。不懂专业术语也没关系，写清楚你想参考的部分，比如\u201c参考 @视频1 的节奏和运镜，@图1 的角色造型\u201d，模型就能高质量生成属于你的版本。大胆试！它真的能做到"] = 'Không chỉ tạo ảnh viết chuyện, Seedance 2.0 còn hỗ trợ "bắt chước theo" — chuyển cảnh sáng tạo, phim quảng cáo hoàn chỉnh, đoạn phim điện ảnh, biên tập phức tạp. Chỉ cần bạn có ảnh hoặc video tham chiếu, mô hình có thể nhận diện nhịp độ động tác, ngôn ngữ ống kính, cấu trúc thị giác và tái tạo chính xác. Không hiểu thuật ngữ chuyên ngành cũng không sao, viết rõ phần bạn muốn tham chiếu, ví dụ "Tham chiếu nhịp điệu và chuyển động ống kính @Video1, tạo hình nhân vật @Ảnh1", mô hình có thể tạo ra phiên bản chất lượng cao của riêng bạn. Cứ thử đi! Nó thực sự làm được'
    T["模型的创意性、剧情补全能力"] = "Tính sáng tạo của mô hình, khả năng bổ sung cốt truyện"
    T["视频延长"] = "Kéo dài video"
    T["音色更准，声音更真"] = "Âm sắc chính xác hơn, giọng nói chân thực hơn"
    T["固定镜头，中央鱼眼镜头透过圆形孔洞向下窥视，参考视频1的鱼眼镜头，让@视频2中的马看向鱼眼镜头，参考@视频1中的说话动作，背景BGM参考@视频3中的音效。"] = "Ống kính cố định, ống kính mắt cá ở giữa nhìn xuống qua lỗ tròn, tham chiếu ống kính mắt cá của Video1, để con ngựa trong @Video2 nhìn về phía ống kính mắt cá, tham chiếu động tác nói chuyện trong @Video1, nhạc nền BGM tham chiếu hiệu ứng âm thanh trong @Video3."
    T["根据提供的写字楼宣传照，生成一段15秒电影级写实风格的地产纪录片，采用2.35:1宽银幕，24fps，细腻的画面风格，其中旁白的音色参考@视频1，拍摄 \u201c写字楼的生态\u201d，呈现楼内不同企业的运作，结合旁白阐述写字楼如何成为一个充满活力的商业生态系统."] = 'Dựa trên ảnh quảng cáo tòa nhà văn phòng được cung cấp, tạo một đoạn phim tài liệu bất động sản phong cách điện ảnh siêu thực 15 giây, sử dụng màn hình rộng 2.35:1, 24fps, phong cách hình ảnh tinh tế, trong đó âm sắc lời bình tham chiếu @Video1, quay "hệ sinh thái tòa nhà văn phòng", thể hiện hoạt động của các doanh nghiệp khác nhau trong tòa nhà, kết hợp lời bình giải thích tòa nhà văn phòng trở thành hệ sinh thái thương mại đầy sức sống như thế nào.'
    T["在\u201c猫狗吐槽间\u201d里的一段吐槽对话，要求情感丰沛，符合脱口秀表演：\n喵酱（猫主持，舔毛翻眼）：\"家人们谁懂啊，我身边这位，每天除了摇尾巴、拆沙发，就只会用那种\u201c我超乖求摸摸\u201d的眼神骗人类零食，明明拆家的时候比谁都凶，还好意思叫旺仔，我看叫\u201c旺拆\u201d还差不多哈哈哈\"\n"] = 'Một đoạn hội thoại "phàn nàn" trong "Phòng chó mèo chém gió", yêu cầu cảm xúc dồi dào, phù hợp biểu diễn talkshow:\nMiao-chan (mèo MC, liếm lông lật mắt): "Mọi người ai hiểu không, vị bên cạnh tôi đây, mỗi ngày ngoài vẫy đuôi, phá ghế sofa ra, chỉ biết dùng ánh mắt kiểu \'em ngoan lắm xin vuốt đầu\' lừa đồ ăn vặt của con người, rõ ràng lúc phá nhà còn hung hơn ai hết, còn mặt mũi nào gọi là Vượng Tử, tôi thấy gọi \'Vượng Phá\' còn đúng hơn hahaha"\n'
    T["旺仔（狗主持，歪头晃尾巴）：\"你还好意思说我？你每天睡18个小时，醒了就蹭人类腿要罐头，掉毛掉得人类黑衣服上全是你的毛，人家扫完地，你转身又在沙发上滚一圈，还好意思装高冷贵族？\""] = 'Vượng Tử (chó MC, nghiêng đầu vẫy đuôi): "Mày còn mặt mũi nào nói tao? Mày mỗi ngày ngủ 18 tiếng, thức dậy là cọ chân người đòi đồ hộp, rụng lông rụng đến mức quần áo đen của người ta đầy lông mày, người ta quét nhà xong, mày quay lưng lại lăn một vòng trên sofa, còn mặt mũi nào giả vờ quý tộc cao lạnh?"'
    T["豫剧经前桥段《铡美案》的伴奏响起，左侧的黑衣包拯指着右侧的红衣陈世美，咬牙切齿地唱着豫剧：\u201c刀对鞘，真凭实据你敢不招？\u201d 陈世美的眼珠左右滴溜溜乱转，寻找着权宜之策，面色窘迫至极。此时，画面外传来一声豫剧旦角的念白：\u201c且慢！\u201d包拯和陈世美一齐向画面右侧看去。"] = 'Phần nhạc đệm kinh kịch Dự kịch đoạn mở đầu《Trảm Mỹ Án》vang lên, Bao Chửng áo đen bên trái chỉ tay vào Trần Thế Mỹ áo đỏ bên phải, nghiến răng hát Dự kịch: "Dao đối vỏ, bằng chứng rõ ràng ngươi dám không khai?" Mắt Trần Thế Mỹ đảo qua đảo lại, tìm cách đối phó, sắc mặt vô cùng lúng túng. Lúc này, từ ngoài hình truyền đến tiếng niệm bạch của đào nương Dự kịch: "Khoan đã!" Bao Chửng và Trần Thế Mỹ cùng nhìn về phía phải màn hình.'
    T["生成一个15秒的MV视频。关键词：稳重构图 / 轻推拉 / 低角度英雄感 / 纪实但高级A超广角建立镜头，低机位轻微仰拍，悬崖土路与复古旅行车占画面下三分之一，远处海面与地平线拉开空间，夕阳侧逆光体积光穿过尘粒，电影级构图，真实胶片颗粒，微风吹动衣角。"] = "Tạo một video MV 15 giây. Từ khóa: bố cục ổn định / đẩy kéo nhẹ / góc thấp cảm giác anh hùng / phong cách tài liệu nhưng cao cấp. Ống kính siêu rộng thiết lập cảnh, máy quay thấp hơi ngước lên, đường đất vách đá và xe du lịch cổ điển chiếm 1/3 dưới khung hình, mặt biển xa và đường chân trời mở rộng không gian, ánh hoàng hôn ngược bên sườn với tia sáng thể tích xuyên qua bụi, bố cục cấp điện ảnh, hạt phim thực, gió nhẹ thổi vạt áo."
    T["画面中间戴帽子的女孩温柔地唱着说\"I'm so proud of my family!\"，之后转身拥抱中间的黑人女孩。黑人女孩感动地回应\"My sweetie, you're the heart of our family\"，回抱她。左侧的黄衣服男孩开心地说\"Folks, let's dance together to celebrate!\u201d 最右侧的女孩紧接着回复： \u201cI'll bring the music!\"，背景拉美音乐响起，左侧穿橙色裙的女性（朱丽叶塔）笑着点头，右侧扎辫女性（路易莎）握紧拳头挥动手臂。人群中有人开始踏起步子，孩子们跟着节奏拍手，整个家族即将围成圈，伴着欢快的音乐，裙摆飞扬，在五彩的街道上尽情舞动，传递着喜悦与温暖。"] = 'Cô gái đội mũ ở giữa màn hình dịu dàng hát "I\'m so proud of my family!", sau đó quay lại ôm cô gái da đen ở giữa. Cô gái da đen xúc động đáp lại "My sweetie, you\'re the heart of our family", ôm lại. Cậu bé áo vàng bên trái vui vẻ nói "Folks, let\'s dance together to celebrate!" Cô gái ngoài cùng bên phải tiếp lời: "I\'ll bring the music!", nhạc Mỹ Latinh vang lên, phụ nữ mặc váy cam bên trái (Julieta) cười gật đầu, phụ nữ tết tóc bên phải (Luisa) nắm chặt tay vung cánh tay. Có người trong đám đông bắt đầu bước nhịp, trẻ em theo nhịp vỗ tay, cả gia tộc sắp quây thành vòng tròn, theo nhạc vui nhộn, tà váy bay phất phơ, nhảy múa hết mình trên con phố đầy màu sắc, truyền tải niềm vui và hơi ấm.'
    T["固定镜头。站着的壮汉（队长）握拳挥臂用西班牙语说着：\u201c三分钟后突袭！\u201d持刀者收刀入鞘，金发队员站在检查枪械，绿发队员握紧战术手电。黑人队员搭肩问同伴用西班牙语说：\u201c侧翼包抄？\u201d队长点头用西班牙语说：\u201c老规矩，活口留审讯。\u201d全员肃然，装备碰撞声中完成战术手势，默契起身，大家都严阵以待，左侧两个男生也争先站起来准备战斗。"] = 'Ống kính cố định. Người đàn ông vạm vỡ đứng (đội trưởng) nắm đấm vung tay nói bằng tiếng Tây Ban Nha: "Ba phút nữa tấn công!" Người cầm dao thu đao vào bao, đội viên tóc vàng đứng kiểm tra súng, đội viên tóc xanh nắm chặt đèn pin chiến thuật. Đội viên da đen vỗ vai đồng đội hỏi bằng tiếng Tây Ban Nha: "Bao vây sườn?" Đội trưởng gật đầu nói bằng tiếng Tây Ban Nha: "Quy tắc cũ, bắt sống để thẩm vấn." Toàn đội nghiêm trang, trong tiếng va chạm trang bị hoàn thành ký hiệu chiến thuật, đồng loạt đứng dậy ăn ý, tất cả sẵn sàng chiến đấu, hai nam sinh bên trái cũng tranh nhau đứng dậy chuẩn bị chiến đấu.'
    T["0-3秒：开头闹钟响起来，画面朦胧中出现画面1； "] = "0-3 giây: Mở đầu đồng hồ báo thức kêu, trong hình ảnh mờ ảo xuất hiện Hình 1; "
    T["3-10秒：快速摇镜头，转向对面特写男人面部，男人无奈的叫女生起床，语气和音色参考@视频1； "] = "3-10 giây: Ống kính quay nhanh, chuyển sang cận cảnh khuôn mặt người đàn ông đối diện, người đàn ông bất lực gọi cô gái dậy, giọng điệu và âm sắc tham chiếu @Video1; "
    T["10-12秒：女生撅着嘴躲进被子里面； "] = "10-12 giây: Cô gái chu môi trốn vào chăn; "
    T["12-15秒：切换到男主全身，他叹着气说：\u201c真拿你没办法！\u201d"] = '12-15 giây: Chuyển sang toàn thân nam chính, anh thở dài nói: "Thật chẳng biết làm sao với em!"'
    T["@图片1的猴子走向奶茶店柜台，镜头跟随在他身后，一位@图片2的比熊服务员正在吧台处擦拭制作工具，猴子向服务员用四川口音点单：\u201c幺妹儿，霸王别姬有得没得？\u201d\n切镜，特写。\n服务员放下手里的活，怪异地看了老头一眼后回答：\u201c没得，美式要不要得嘛\u201d\n"] = 'Con khỉ @Ảnh1 đi về phía quầy tiệm trà sữa, ống kính theo sau, một nhân viên chó Bichon @Ảnh2 đang lau dụng cụ pha chế tại quầy bar, con khỉ dùng giọng Tứ Xuyên gọi món: "Em ơi, Bá Vương Biệt Cơ có không vậy?"\nCắt cảnh, cận cảnh.\nNhân viên đặt công việc xuống, nhìn ông già một cái kỳ lạ rồi trả lời: "Không có, Americano muốn không?"\n'
    T["切镜，镜头给到猴子。"] = "Cắt cảnh, ống kính chuyển sang con khỉ."
    T["他挠了挠头念念有词：\u201c没事……？我有事！孙儿叫我来买个奶茶，就叫个撒子霸王别姬嘛\u201d"] = 'Nó gãi đầu lẩm bẩm: "Không sao...? Tôi có việc! Cháu tôi bảo tôi ra mua trà sữa, gọi cái gì Bá Vương Biệt Cơ đó"'
    T["用科普风格和音色，将"] = "Dùng phong cách và giọng khoa học phổ thông, diễn giải"
    T["图片1"] = "Ảnh1"
    T["中的内容演绎出来，内容包括悟空为过火焰山，到翠云山向铁扇公主借芭蕉扇。铁扇公主因红孩儿被悟空降伏拜观音为童子，母子分离，不肯借扇还欲报仇。悟空好言相劝无果，二人随即起了争执的小故事进行讲解。"] = "nội dung trong đó, bao gồm câu chuyện Ngộ Không muốn vượt Hỏa Diệm Sơn, đến Thúy Vân Sơn mượn quạt Ba Tiêu của Thiết Phiến Công Chúa. Thiết Phiến Công Chúa vì Hồng Hài Nhi bị Ngộ Không thu phục và bái Quan Âm làm đồng tử, mẹ con ly tán, không chịu cho mượn quạt còn muốn trả thù. Ngộ Không nói tốt thuyết phục không được, hai bên liền xảy ra tranh cãi."
    T["镜头连贯性（一镜到底）更强"] = "Tính liền mạch ống kính (quay một mạch) mạnh hơn"
    T["@图片1@图片2@图片3@图片4@图片5，一镜到底的追踪镜头，从街头跟随跑步者上楼梯、穿过走廊、进入屋顶，最终俯瞰城市。"] = "@Ảnh1@Ảnh2@Ảnh3@Ảnh4@Ảnh5, ống kính theo dõi quay một mạch, từ đường phố theo người chạy lên cầu thang, xuyên qua hành lang, vào mái nhà, cuối cùng nhìn xuống thành phố."
    T["以@图片1为首帧，画面放大至飞机舷窗外，一团团云朵缓缓飘至画面中，其中一朵为彩色糖豆点缀的云朵，始终在画面中居中，然后缓缓变形为@图片2的冰淇淋，镜头推远回到机舱内，坐在窗边的@图片3伸手从窗外拿进冰淇淋，吃了一口，嘴巴上沾满奶油，脸上洋溢出甜蜜的笑容，此时视频配音为@视频1."] = "Lấy @Ảnh1 làm khung hình đầu, hình ảnh phóng to ra ngoài cửa sổ máy bay, từng đám mây từ từ trôi vào hình, trong đó có một đám mây điểm xuyết kẹo màu, luôn ở giữa hình, rồi từ từ biến hình thành kem @Ảnh2, ống kính kéo xa trở lại khoang máy bay, @Ảnh3 ngồi bên cửa sổ đưa tay lấy kem từ ngoài cửa sổ vào, cắn một miếng, miệng dính đầy kem, mặt rạng rỡ nụ cười ngọt ngào, lúc này lồng tiếng video là @Video1."
    T["谍战片风格，@图片1作为首帧画面，镜头正面跟拍穿着红风衣的女特工向前走，镜头全景跟随，不断有路人遮挡红衣女子，走到一个拐角处，参考@图片2的拐角建筑，固定镜头红衣女子离开画面，走在拐角处消失，一个戴面具的女孩在拐角处躲着恶狠狠的盯着她，面具女孩形象参考@图片3，只参考形象，女孩站在拐角处。镜头往前摇向红衣女特工，她走进一座豪宅消失不见了，豪宅参考@图片4。全程不要切镜头，一镜到底。"] = "Phong cách phim gián điệp, @Ảnh1 làm khung hình đầu, ống kính chính diện bám theo nữ đặc vụ mặc áo gió đỏ đi về phía trước, ống kính toàn cảnh theo dõi, liên tục có người qua đường che khuất nữ áo đỏ, đi đến một góc rẽ, tham chiếu kiến trúc góc rẽ @Ảnh2, ống kính cố định nữ áo đỏ rời khỏi hình, đi ở góc rẽ biến mất, một cô gái đeo mặt nạ ở góc rẽ nấp và nhìn cô ấy một cách hung dữ, hình tượng cô gái mặt nạ tham chiếu @Ảnh3, chỉ tham chiếu hình tượng, cô gái đứng ở góc rẽ. Ống kính quay về phía trước hướng về nữ đặc vụ áo đỏ, cô ấy bước vào một biệt thự và biến mất, biệt thự tham chiếu @Ảnh4. Toàn bộ không cắt cảnh, quay một mạch."
    T["根据@图片1外景的镜头，第一人称主观视角快推镜头到木屋内的环境场景近景，一只小鹿@图片2和一只羊@图片3在围炉旁喝茶聊天，镜头推进特写茶杯的样式参考@图片4."] = "Dựa trên ống kính ngoại cảnh @Ảnh1, góc nhìn chủ quan thứ nhất đẩy nhanh ống kính đến cận cảnh bối cảnh bên trong nhà gỗ, một con nai nhỏ @Ảnh2 và một con cừu @Ảnh3 đang uống trà trò chuyện bên lò sưởi, ống kính đẩy vào cận cảnh kiểu dáng tách trà tham chiếu @Ảnh4."
    T["@图片1@图片2@图片3@图片4@图片5，主观视角一镜到底的惊险过山车的镜头，过山车的速度越来越快。"] = "@Ảnh1@Ảnh2@Ảnh3@Ảnh4@Ảnh5, ống kính tàu lượn siêu tốc thót tim quay một mạch từ góc nhìn chủ quan, tốc độ tàu lượn ngày càng nhanh."
    T["视频编辑可用度高"] = "Tính khả dụng chỉnh sửa video cao"
    T["有时候你已经有了一段视频，不想从头再找图或重做一遍，只是希望调整其中一小段动作、延长几秒钟，或让角色表现更贴近你的想法。现在你可以直接用已有视频作为输入，在不改变其它内容的前提下，指定片段、动作或节奏进行定向修改。无需重头生成，也能快速完成调整"] = "Đôi khi bạn đã có một đoạn video, không muốn tìm ảnh lại từ đầu hay làm lại, chỉ muốn điều chỉnh một đoạn động tác nhỏ, kéo dài vài giây, hoặc để nhân vật biểu hiện gần hơn với ý tưởng của bạn. Bây giờ bạn có thể trực tiếp dùng video có sẵn làm đầu vào, không thay đổi nội dung khác, chỉ định đoạn cụ thể, động tác hoặc nhịp điệu để sửa đổi có mục tiêu. Không cần tạo lại từ đầu, cũng có thể nhanh chóng hoàn thành điều chỉnh"
    T["颠覆@视频1的整个剧情"] = "Đảo ngược toàn bộ cốt truyện @Video1"
    T["0\u20133秒画面：西装男坐在酒吧，神情冷静，手里轻晃酒杯。 镜头缓慢推进，光影高级、氛围严肃。 环境音低沉，西装男小声说\u201c这单生意，很大。\u201d"] = '0-3 giây: Người đàn ông vest ngồi trong quán bar, vẻ mặt bình tĩnh, tay nhẹ nhàng lắc ly rượu. Ống kính từ từ đẩy tới, ánh sáng cao cấp, bầu không khí nghiêm túc. Âm thanh môi trường trầm, người đàn ông vest nói nhỏ "Thương vụ này, rất lớn."'
    T["3\u20136秒画面：身后的女人表情紧张问\u201c有多大？\u201d西装男抬眼，压低声音：\u201c非常大。\u201d镜头切手部特写——他把酒杯放下，气场拉满。"] = '3-6 giây: Người phụ nữ phía sau mặt căng thẳng hỏi "Lớn đến mức nào?" Người đàn ông vest ngước mắt, hạ giọng: "Rất lớn." Ống kính cắt sang cận cảnh bàn tay — anh ta đặt ly rượu xuống, khí chất đầy ắp.'
    T["6\u20139秒画面：突然西装男从桌下掏出—— 一大包体积夸张的零食礼包，\u201c咚\u201d的一声重重放在桌上。"] = '6-9 giây: Đột nhiên người đàn ông vest lấy ra từ dưới bàn — một gói quà đồ ăn vặt cỡ khổng lồ, "bịch" một tiếng đặt mạnh lên bàn.'
    T["9\u201312秒画面：身后的女人原本放在腰间的手，肌肉从僵硬到松弛，整个人表情放松。画面氛围轻松起来。"] = "9-12 giây: Tay người phụ nữ phía sau vốn đặt ở eo, cơ bắp từ cứng nhắc dần thả lỏng, toàn bộ biểu cảm trở nên thoải mái. Bầu không khí hình ảnh nhẹ nhàng lên."
    T["13\u201315秒画面：西装男拿出一包零食给女人，镜头拉远展示酒馆全景，画面变得透明模糊—— 字幕弹出\u201c再忙，也要记得吃点零食~\u201d"] = '13-15 giây: Người đàn ông vest lấy ra một gói đồ ăn vặt đưa cho người phụ nữ, ống kính kéo xa hiển thị toàn cảnh quán bar, hình ảnh trở nên trong suốt mờ — phụ đề hiện lên "Dù bận đến mấy, cũng nhớ ăn chút đồ ăn vặt nhé~"'
    T["视频1中的女主唱换成图片1的男主唱，动作完全模仿原视频，不要出现切镜，乐队演唱音乐。"] = "Thay nữ ca sĩ chính trong Video1 thành nam ca sĩ chính của Ảnh1, động tác hoàn toàn bắt chước video gốc, không cắt cảnh, ban nhạc biểu diễn."
    T["将视频1女人发型变成红色长发，图片1中的大白鲨缓缓浮出半个脑袋，在她身后。"] = "Đổi kiểu tóc người phụ nữ trong Video1 thành tóc dài đỏ, con cá mập trắng trong Ảnh1 từ từ nổi lên nửa đầu, ở phía sau cô ấy."
    T["视频1镜头右摇，炸鸡老板忙碌地将炸鸡递给排队的客户，用普通话说\u201c做完他的，做你的，大家文明排队。\u201d一说完，就去拿纸袋子去装炸鸡。特写展示老板拿印有图1的纸袋子，特写展示递给客户的手部特写。"] = 'Video1 ống kính quay phải, ông chủ gà rán bận rộn đưa gà rán cho khách xếp hàng, nói bằng tiếng phổ thông "Làm xong của anh ấy, rồi đến anh, mọi người xếp hàng văn minh." Nói xong liền đi lấy túi giấy đựng gà rán. Cận cảnh ông chủ cầm túi giấy in Ảnh1, cận cảnh đưa cho khách.'
    T["可进行音乐卡点"] = "Có thể canh nhịp nhạc"
    T["情绪演绎更好"] = "Diễn giải cảm xúc tốt hơn"
    T["🏁 最后说两句"] = "🏁 Lời kết"
    T["Seedance 2.0 的多模态能力正处于不断进化中，我们会持续更新能力、支持更多种输入组合方式。希望这份使用手册能帮你更自由地发挥创意！"] = "Khả năng đa phương thức của Seedance 2.0 đang không ngừng tiến hóa, chúng tôi sẽ liên tục cập nhật năng lực, hỗ trợ nhiều cách kết hợp đầu vào hơn. Hy vọng hướng dẫn sử dụng này giúp bạn tự do phát huy sáng tạo hơn!"
    T["如果你遇到了 Bug，或者有用法建议、需求场景，欢迎留言、私信、敲锣打鼓告诉我们！我们会持续优化，一起把即梦变成真正让你们开心、方便的生产力工具 ❤️"] = "Nếu bạn gặp Bug, hoặc có đề xuất sử dụng, tình huống nhu cầu, hãy để lại bình luận, nhắn tin riêng, hãy cho chúng tôi biết! Chúng tôi sẽ tiếp tục tối ưu, cùng nhau biến JiMeng thành công cụ năng suất thực sự khiến các bạn vui vẻ và tiện lợi ❤️"

    if text in T:
        return T[text]
    return text


def main():
    with open('original_blocks.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    translated = copy.deepcopy(data)
    total_elements = 0
    translated_count = 0
    untranslated = []

    for i, block in enumerate(translated['blocks']):
        for elem in block.get('elements', []):
            content = elem.get('content', '')
            if not content.strip():
                continue
            total_elements += 1
            new_content = translate_text(content)
            if new_content != content:
                elem['content'] = new_content
                translated_count += 1
            elif has_chinese(content):
                untranslated.append({
                    'block_index': i,
                    'block_id': block.get('block_id', ''),
                    'content': content[:100]
                })

    with open('translated_blocks.json', 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)

    # Report
    print("=" * 60)
    print("       BÁO CÁO DỊCH THUẬT - LARK DOCUMENT")
    print("=" * 60)
    print(f"  Tổng số block:           {len(translated['blocks'])}")
    print(f"  Tổng số đoạn text:       {total_elements}")
    print(f"  Đã dịch thành công:      {translated_count}")
    print(f"  Giữ nguyên (EN/emoji):   {total_elements - translated_count - len(untranslated)}")
    print(f"  Chưa dịch (còn TQ):      {len(untranslated)}")
    print("=" * 60)

    if untranslated:
        print("\n⚠️  Các đoạn chưa dịch (còn tiếng Trung):")
        for item in untranslated:
            print(f"  Block [{item['block_index']}] {item['block_id']}:")
            print(f"    {item['content']}")
    else:
        print("\n✅ TẤT CẢ đoạn tiếng Trung đã được dịch sang tiếng Việt!")

    print(f"\n📄 File đã lưu: translated_blocks.json")
    return len(untranslated)


if __name__ == '__main__':
    remaining = main()
    sys.exit(0 if remaining == 0 else 1)
