import json
import copy

with open('C:/Users/ADMIN/hoa55_ ver3/original_blocks.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create a deep copy for translation
translated = copy.deepcopy(data)

# Translation mapping: original Chinese content -> Vietnamese translation
# Only translate content fields in text_run elements
# Do NOT translate: URLs, links, numbers, proper names, code/technical terms, emoji,
# content already in Vietnamese/English, Korean text

translations = {
    "🎬 Seedance 2.0 使用手册（全新多模态创作体验）": "🎬 Seedance 2.0 Hướng dẫn sử dụng (Trải nghiệm sáng tạo đa phương thức hoàn toàn mới)",
    "🌀 ": "🌀 ",
    "视频 Seedance 2.0 正式上线！": "Video Seedance 2.0 chính thức ra mắt!",
    "还记得从只能用文字和首/尾帧「讲故事」的那天起，我们就想做出一个真正听得懂你表达的视频模型。今天，它真的来了！": "Còn nhớ từ ngày chỉ có thể dùng văn bản và khung hình đầu/cuối để \"kể chuyện\", chúng tôi đã muốn tạo ra một mô hình video thực sự hiểu được cách bạn diễn đạt. Hôm nay, nó thực sự đã đến!",
    "Seedance 2.0 现在支持图像、视频、音频、文本四种模态输入，表达方式更丰富，生成也更可控": "Seedance 2.0 hiện hỗ trợ bốn loại đầu vào đa phương thức: hình ảnh, video, âm thanh, văn bản - cách diễn đạt phong phú hơn, việc tạo nội dung cũng dễ kiểm soát hơn",
    "你可以用一张图定下画面风格，用一个视频指定角色的动作和镜头的变化，再用几秒音频带起节奏氛围……搭配提示词，让创作过程变得更自然、更高效，也更像真正的"导演"。": "Bạn có thể dùng một bức ảnh để định phong cách hình ảnh, dùng một video để chỉ định hành động nhân vật và chuyển động camera, rồi dùng vài giây âm thanh để tạo nhịp điệu và bầu không khí... kết hợp với prompt, giúp quá trình sáng tạo trở nên tự nhiên hơn, hiệu quả hơn, và giống một \"đạo diễn\" thực thụ hơn.",
    "这次升级中，": "Trong lần nâng cấp này, ",
    ""参考能力"是最大亮点": "\"khả năng tham chiếu\" là điểm nổi bật nhất",
    "：": ":",
    "📷 参考图像可精准还原画面构图、角色细节": "📷 Hình ảnh tham chiếu có thể tái hiện chính xác bố cục hình ảnh và chi tiết nhân vật",
    "🎥 参考视频支持镜头语言、复杂的动作节奏、创意特效的复刻": "🎥 Video tham chiếu hỗ trợ tái tạo ngôn ngữ ống kính, nhịp điệu hành động phức tạp và hiệu ứng sáng tạo",
    "⏱ 视频支持平滑延长与衔接，可按用户提示生成连续镜头，不止生成，还能"接着拍"": "⏱ Video hỗ trợ kéo dài mượt mà và nối tiếp, có thể tạo cảnh quay liên tục theo gợi ý của người dùng - không chỉ tạo mới mà còn \"quay tiếp\"",
    "✂️ 编辑能力同步增强，支持对已有视频进行角色更替、删减、增加": "✂️ Khả năng chỉnh sửa cũng được nâng cấp đồng bộ, hỗ trợ thay thế, cắt bỏ và thêm nhân vật trong video hiện có",
    "我们知道，视频创作从来不仅是"生成"，更是对表达的控制。2.0 不只是多模态，更是一种真正可控的创作方式": "Chúng tôi biết rằng sáng tạo video không chỉ là \"tạo ra\", mà còn là kiểm soát cách diễn đạt. 2.0 không chỉ là đa phương thức, mà còn là một phương thức sáng tạo thực sự có thể kiểm soát",
    "Seedance 2.0，多模态创作，从这里启程。请你们大胆想象，其余的交给它": "Seedance 2.0, sáng tạo đa phương thức, khởi hành từ đây. Hãy mạnh dạn tưởng tượng, phần còn lại để nó lo",
    "参数预览": "Xem trước thông số",
    "核心维度": "Các thông số cốt lõi",
    "图片输入": "Đầu vào hình ảnh",
    "≤ 9 张": "≤ 9 ảnh",
    "视频输入": "Đầu vào video",
    "≤ 3 个，总时长不超过15s": "≤ 3 video, tổng thời lượng không quá 15s",
    "（有参考视频会贵一点哦）": "(Có video tham chiếu sẽ tốn thêm một chút nhé)",
    "音频输入": "Đầu vào âm thanh",
    "支持 MP3 上传，数量≤ 3 个，总时长不超过15s": "Hỗ trợ tải lên MP3, số lượng ≤ 3, tổng thời lượng không quá 15s",
    "文本输入": "Đầu vào văn bản",
    "自然语言": "Ngôn ngữ tự nhiên",
    "生成时长": "Thời lượng tạo",
    "≤ 15s，可自由选择4-15s": "≤ 15s, tự do chọn từ 4-15s",
    "声音输出": "Đầu ra âm thanh",
    "自带音效/配乐": "Tự động có âm thanh/nhạc nền",
    "交互限制：": "Giới hạn tương tác: ",
    "目前支持的混合输入总上限是 12 个文件": "Hiện tại tổng giới hạn đầu vào hỗn hợp là 12 tệp",
    "。建议优先上传对画面或节奏影响最大的素材，合理分配不同模态的文件数量": ". Nên ưu tiên tải lên các tài liệu ảnh hưởng lớn nhất đến hình ảnh hoặc nhịp điệu, phân bổ hợp lý số lượng tệp cho từng loại đầu vào",
    "交互形式": "Hình thức tương tác",
    "⚠️注意：": "⚠️Lưu ý:",
    "Seedance 2.0 支持": "Seedance 2.0 hỗ trợ",
    "「首尾帧」": "\"Khung hình đầu-cuối\"",
    "和": "và",
    "「全能参考」": "\"Tham chiếu toàn năng\"",
    "入口，": ", ",
    "智能多帧和主体参考无法选中": "không thể chọn Đa khung hình thông minh và Tham chiếu chủ thể",
    "。若你只上传首帧图 + prompt，可走首尾帧入口；如需多模态（图、视频、音频、文本）组合输入，则需进入全能参考入口": ". Nếu bạn chỉ tải lên ảnh khung hình đầu + prompt, có thể dùng cổng Khung hình đầu-cuối; nếu cần kết hợp đa phương thức (ảnh, video, âm thanh, văn bản), thì cần vào cổng Tham chiếu toàn năng",
    "当前支持的交互方式是通过"@素材名"来指定每个图片、视频、音频的用途，例如：@图片1 作为首帧，@视频1 参考镜头语言，@音频1 用于配乐": "Cách tương tác hiện tại là thông qua \"@tên tài liệu\" để chỉ định công dụng của từng ảnh, video, âm thanh, ví dụ: @hình ảnh 1 làm khung hình đầu, @video 1 tham chiếu ngôn ngữ ống kính, @âm thanh 1 dùng làm nhạc nền",
    "主界面：": "Giao diện chính:",
    "入口：Seedance 2.0 - 全能参考/首尾帧": "Cổng vào: Seedance 2.0 - Tham chiếu toàn năng/Khung hình đầu-cuối",
    "唤起本地文件弹窗": "Mở hộp thoại chọn tệp từ máy tính",
    "选定文件，添加至输入框": "Chọn tệp, thêm vào ô nhập liệu",
    "全能参考模式下如何@：": "Cách dùng @ trong chế độ Tham chiếu toàn năng:",
    "方法1：输入"@"唤起参考调用": "Cách 1: Nhập \"@\" để gọi tham chiếu",
    "输入"@"": "Nhập \"@\"",
    "选择参考，落入输入框": "Chọn tham chiếu, đưa vào ô nhập liệu",
    "输入prompt": "Nhập prompt",
    "方法2：点击参数工具"@"唤起参考调用": "Cách 2: Nhấn vào công cụ \"@\" để gọi tham chiếu",
    "点击"@"": "Nhấn \"@\"",
    "上传素材后，": "Sau khi tải lên tài liệu, ",
    "图片、视频、音频": "hình ảnh, video, âm thanh",
    "都支持": "đều hỗ trợ",
    "悬停预览": "xem trước khi di chuột qua",
    "下面是一些不同场景下的用法和玩法，帮助你更好地理解 Seedance 2.0 在生成质量上、控制能力和创意表现上的升级。如果你还不知道从哪开始，不如先看看这些例子，激发灵感～": "Dưới đây là một số cách sử dụng và thủ thuật trong các tình huống khác nhau, giúp bạn hiểu rõ hơn về sự nâng cấp của Seedance 2.0 về chất lượng tạo nội dung, khả năng kiểm soát và biểu hiện sáng tạo. Nếu bạn chưa biết bắt đầu từ đâu, hãy xem qua các ví dụ này để lấy cảm hứng~",
    "Seedance 2.0 能力 / 提升预览": "Seedance 2.0 Năng lực / Xem trước các cải tiến",
    "基础能力显著增强：更稳、更顺、更像真的！ ": "Năng lực cơ bản được nâng cấp rõ rệt: Ổn định hơn, mượt mà hơn, chân thực hơn! ",
    "不只是多模态，Seedance 2.0 在基础层面显著增强，": "Không chỉ là đa phương thức, Seedance 2.0 được nâng cấp rõ rệt ở tầng nền tảng, ",
    "物理规律更合理": "quy luật vật lý hợp lý hơn",
    "、": ", ",
    "动作表现更自然流畅": "biểu hiện hành động tự nhiên và mượt mà hơn",
    "指令理解更精准": "hiểu lệnh chính xác hơn",
    "风格保持更稳定": "giữ phong cách ổn định hơn",
    "，不仅能稳定完成复杂动作、连续运动等高难度生成任务，也让整体视频效果更真实、更顺滑，是一次底层能力的全面进化！": ", không chỉ hoàn thành ổn định các tác vụ tạo nội dung khó như hành động phức tạp, chuyển động liên tục, mà còn làm cho hiệu ứng video tổng thể chân thực hơn, mượt mà hơn - đây là một bước tiến toàn diện về năng lực nền tảng!",
    "女孩在优雅的晒衣服，晒完接着在桶里拿出另一件，用力抖一抖衣服。": "Cô gái đang phơi quần áo một cách duyên dáng, phơi xong lại lấy một chiếc khác từ trong xô ra, rũ mạnh chiếc áo.",
    "超强真实感": "Cảm giác chân thực cực mạnh",
    "画里面的人物心虚的表情，眼睛左右看了看探出画框，快速的将手伸出画框拿起可乐喝了一口，然后露出一脸满足的表情，这时传来脚步声，画中的人物赶紧将可乐放回原位，此时一位西部牛仔拿起杯子里的可乐走了，最后镜头前推画面慢慢变得纯黑背景只有顶光照耀的罐装可乐，画面最下方出现艺术感字幕和旁白："宜口可乐，不可不尝！"": "Nhân vật trong tranh với vẻ mặt bất an, mắt nhìn trái phải rồi thò ra khỏi khung tranh, nhanh chóng duỗi tay ra ngoài khung tranh lấy lon cola uống một ngụm, rồi lộ vẻ mặt mãn nguyện. Lúc này có tiếng bước chân vang lên, nhân vật trong tranh vội vàng đặt cola lại chỗ cũ. Một tay cao bồi miền Tây nhặt lon cola trong cốc rồi đi. Cuối cùng ống kính đẩy tới, màn hình dần trở nên đen hoàn toàn, chỉ có ánh sáng từ trên chiếu xuống lon cola, phía dưới cùng xuất hiện phụ đề nghệ thuật và lời bình: \"Cola tuyệt hảo, không thể bỏ lỡ!\"",
    "镜头小幅度拉远（露出街头全景）并跟随女主移动，风吹拂着女主的裙摆，女主走在19世纪的伦敦大街上；女主走着走着右边街道驶来一辆蒸汽机车，快速驶过女主身旁，风将女主的裙摆吹起，女主一脸震惊的赶忙用双手向下捂住裙摆；背景音效为走路声，人群声，汽车声等等": "Ống kính kéo ra nhẹ (lộ toàn cảnh đường phố) và theo dõi nữ chính di chuyển, gió thổi tà váy nữ chính, nữ chính đi trên đường phố London thế kỷ 19; đang đi thì bên phải đường có một chiếc xe hơi chạy bằng hơi nước lao qua, vượt nhanh qua nữ chính, gió thổi tung tà váy, nữ chính kinh ngạc vội dùng hai tay giữ chặt váy xuống; âm thanh nền là tiếng bước chân, tiếng đám đông, tiếng xe cộ v.v.",
    "镜头跟随黑衣男子快速逃亡，后面一群人在追，镜头转为侧面跟拍，人物惊慌撞倒路边的水果摊爬起来继续逃，人群慌乱的声音。": "Ống kính bám theo người đàn ông mặc đồ đen chạy trốn nhanh chóng, phía sau một đám người đang truy đuổi, ống kính chuyển sang quay bám từ bên hông, nhân vật hoảng hốt va đổ quầy hoa quả bên đường rồi bò dậy tiếp tục chạy, tiếng đám đông hoảng loạn.",
    "多模态全面升级：视频创作进入"自由组合"时代！": "Đa phương thức nâng cấp toàn diện: Sáng tạo video bước vào kỷ nguyên \"tổ hợp tự do\"!",
    "Seedance 2.0 多模态介绍": "Giới thiệu đa phương thức Seedance 2.0",
    "支持上传文本、图片、视频、音频，这些素材都可以被用作使用对象或参考对象。你可以参考任何内容的动作、特效、形式、运镜、人物、场景、声音，": "Hỗ trợ tải lên văn bản, hình ảnh, video, âm thanh - tất cả tài liệu này đều có thể được dùng làm đối tượng sử dụng hoặc đối tượng tham chiếu. Bạn có thể tham chiếu hành động, hiệu ứng, hình thức, chuyển động camera, nhân vật, bối cảnh, âm thanh từ bất kỳ nội dung nào, ",
    "只要提示词写得清楚": "chỉ cần viết prompt rõ ràng",
    "，模型都能理解。": ", mô hình đều có thể hiểu.",
    "Seedance 2.0 = 多模态参考能力（可参考万物） + 强创意生成 + 指令响应精准（理解力很棒）": "Seedance 2.0 = Khả năng tham chiếu đa phương thức (có thể tham chiếu mọi thứ) + Tạo nội dung sáng tạo mạnh mẽ + Phản hồi lệnh chính xác (khả năng hiểu rất tốt)",
    "用自然语言描述你想要的画面和动作就可以啦，明确是参考，还是编辑～素材多的时候，建议你多检查一下各个 @对象有没有标清楚，别把图、视频、角色搞混了哦": "Chỉ cần dùng ngôn ngữ tự nhiên mô tả hình ảnh và hành động bạn muốn là được, nêu rõ là tham chiếu hay chỉnh sửa~ Khi có nhiều tài liệu, nên kiểm tra kỹ xem các @đối tượng đã được ghi rõ chưa, đừng nhầm lẫn giữa ảnh, video và nhân vật nhé",
    "特殊使用方式（不设限，仅供参考）：": "Cách sử dụng đặc biệt (không giới hạn, chỉ mang tính tham khảo):",
    "有首帧/尾帧图？还想参考视频动作？": "Có ảnh khung hình đầu/cuối? Còn muốn tham chiếu hành động video?",
    " → 提示词中写清楚，如："@图1为首帧，参考@视频1的打斗动作"": " → Viết rõ trong prompt, ví dụ: \"@ảnh 1 làm khung hình đầu, tham chiếu hành động đánh nhau của @video 1\"",
    "想延长一个已有的视频？": "Muốn kéo dài một video đã có?",
    " → 说明延长时间，如"将@视频1延长 5s"，": " → Nêu rõ thời gian kéo dài, ví dụ \"Kéo dài @video 1 thêm 5s\", ",
    "注意：此时选择的生成时长应为"新增部分"的时长": "Lưu ý: lúc này thời lượng tạo được chọn nên là thời lượng của \"phần thêm mới\"",
    "（例如延长 5s，生成长度也选 5s": "(ví dụ kéo dài 5s, thời lượng tạo cũng chọn 5s",
    "想融合多个视频？": "Muốn kết hợp nhiều video?",
    " → 提示词中说明合成逻辑，如："我要在@视频1和@视频2之间加一个场景，内容为xxx"": " → Nêu rõ logic ghép nối trong prompt, ví dụ: \"Tôi muốn thêm một cảnh giữa @video 1 và @video 2, nội dung là xxx\"",
    "没音频素材？可以直接参考视频里的声音": "Không có tài liệu âm thanh? Có thể tham chiếu trực tiếp âm thanh trong video",
    "想生成连续动作？": "Muốn tạo hành động liên tục?",
    " → 可以在提示词中加入连续性描述，如："角色从跳跃直接过渡到翻滚，保持动作连贯流畅"@图1@图2@图3...": " → Có thể thêm mô tả tính liên tục trong prompt, ví dụ: \"Nhân vật chuyển trực tiếp từ nhảy sang lăn, giữ hành động liền mạch\" @ảnh 1@ảnh 2@ảnh 3...",
    "那些一直很难做的视频问题，现在真的能搞定了！": "Những vấn đề video khó giải quyết bấy lâu nay, giờ thực sự có thể xử lý được!",
    "做视频总会碰到一些让人头疼的地方：比如人脸换了、动作不像、视频延长不自然、改着改着整个节奏都变了……这次多模态能把这些"老大难"问题一口气解决了，下面就是具体的使用案例👇": "Làm video luôn gặp những vấn đề đau đầu: ví dụ khuôn mặt bị đổi, hành động không giống, kéo dài video không tự nhiên, sửa mãi mà cả nhịp điệu đều thay đổi... Lần nâng cấp đa phương thức này có thể giải quyết hết các vấn đề \"nan giải\" này cùng lúc, dưới đây là các trường hợp sử dụng cụ thể👇",
    "一致性全面提升": "Nâng cao toàn diện tính nhất quán",
    "你可能遇到过这些烦恼：画面里人物前后长得不一样、商品细节丢了、小字模糊、场景跳变、镜头风格无法统一……这些在创作中常见的一致性问题，现在在 2.0 中都能被解决。从人脸到服装，再到字体细节，整体一致性更稳、更准": "Bạn có thể đã gặp những phiền toái này: nhân vật trong hình trước sau trông khác nhau, chi tiết sản phẩm bị mất, chữ nhỏ bị mờ, cảnh nhảy đột ngột, phong cách ống kính không thống nhất... Những vấn đề nhất quán thường gặp trong sáng tạo này, giờ đây đều có thể được giải quyết trong phiên bản 2.0. Từ khuôn mặt đến trang phục, đến chi tiết phông chữ, tính nhất quán tổng thể ổn định hơn, chính xác hơn",
    "生成结果": "Kết quả tạo",
    "男人@图片1下班后疲惫的走在走廊，脚步变缓，最后停在家门口，脸部特写镜头，男人深呼吸，调整情绪，收起了负面情绪，变得轻松，然后特写翻找出钥匙，插入门锁，进入家里后，他的小女儿和一只宠物狗，欢快的跑过来迎接拥抱，室内非常的温馨，全程自然对话": "Người đàn ông @hình ảnh 1 sau giờ làm mệt mỏi đi trong hành lang, bước chân chậm dần, cuối cùng dừng lại trước cửa nhà, cận cảnh khuôn mặt, người đàn ông hít thở sâu, điều chỉnh cảm xúc, gạt bỏ cảm xúc tiêu cực, trở nên thoải mái, rồi cận cảnh tìm chìa khóa, cắm vào ổ khóa, sau khi vào nhà, cô con gái nhỏ và một chú chó cưng vui vẻ chạy ra đón ôm, trong nhà rất ấm cúng, toàn bộ hội thoại tự nhiên",
    "将@视频1中的女生换成戏曲花旦，场景在一个精美的舞台上，参考@视频1的运镜和转场效果，利用镜头匹配人物的动作，极致的舞台美感，增强视觉冲击力": "Thay cô gái trong @video 1 thành đào hát tuồng, bối cảnh trên một sân khấu tinh xảo, tham chiếu chuyển động camera và hiệu ứng chuyển cảnh của @video 1, dùng ống kính phù hợp với động tác nhân vật, vẻ đẹp sân khấu đỉnh cao, tăng cường sức hấp dẫn thị giác",
    "使用参考图片人物的形象生成一段古装穿越剧的预告短片。\n 0-3秒画面：参考图片1人物形象的男主手里举起一个篮球，抬头望向镜头。说话"我只是想喝杯酒，该不会要穿越了吧……" \n": "Sử dụng hình ảnh nhân vật từ ảnh tham chiếu để tạo một đoạn trailer phim cổ trang xuyên không.\n 0-3 giây: Nam chính với hình tượng nhân vật tham chiếu từ ảnh 1, tay giơ một quả bóng rổ, ngẩng đầu nhìn vào ống kính. Nói \"Tôi chỉ muốn uống ly rượu, chẳng lẽ sắp xuyên không rồi sao...\" \n",
    "4-8秒画面：镜头突然剧烈晃动，操场的场景开始剧烈震动，瞬间切换成古宅的雨夜。一个穿着古装，长相清秀的女主，冷冽的目光穿透雨幕，望向镜头方向。雷鸣声，衣袂猎猎声。女主说话"何人擅闯我永宁侯府？" 9-13秒画面：镜头切到一个穿着明官服的男子坐在衙门里，眼神锐利如刀，愤怒说话"来人！即刻拿下此'妖人'！" 画面闪回：男主穿着不合身的粗布麻衣；在官差的围堵下慌不择路；与女主的身影在雨巷里交错；男主穿着官服走在皇宫里。 14-15秒画面：黑屏，打出片名《醉梦惊华》，伴随着沉重的鼓点。": "4-8 giây: Ống kính đột ngột rung lắc mạnh, cảnh sân vận động bắt đầu rung chấn dữ dội, chuyển ngay sang đêm mưa trong ngôi nhà cổ. Một nữ chính mặc cổ trang, gương mặt thanh tú, ánh mắt lạnh lẽo xuyên qua màn mưa, nhìn về phía ống kính. Tiếng sấm, tiếng vạt áo phần phật. Nữ chính nói \"Ai dám tự tiện xông vào phủ Vĩnh Ninh Hầu?\" 9-13 giây: Ống kính chuyển sang một người đàn ông mặc quan phục triều Minh ngồi trong nha môn, ánh mắt sắc như dao, tức giận nói \"Người đâu! Lập tức bắt lấy 'yêu nhân' này!\" Hồi tưởng: Nam chính mặc áo vải thô không vừa; hoảng loạn chạy trốn trước sự vây bắt của quan binh; bóng dáng nam chính và nữ chính giao nhau trong con hẻm mưa; nam chính mặc quan phục đi trong hoàng cung. 14-15 giây: Màn hình đen, hiện tên phim \"Túy Mộng Kinh Hoa\", kèm theo tiếng trống nặng nề.",
    "参考 @视频1的所有转场和运镜，一镜到底，画面以棋局为起始，镜头左移，展示地板的黄色沙砾，镜头上移来到一个沙滩，沙滩上有足印，一个穿着白色素衣的女生在沙滩上渐行渐远，镜头切到空中的俯拍视角，海水在冲刷（不要出现人物），无缝渐变转场，冲刷的海浪变成飘动的窗帘，镜头拉远，展示女孩的面部特写，一镜到底": "Tham chiếu tất cả chuyển cảnh và chuyển động camera của @video 1, quay liền mạch một cảnh, hình ảnh bắt đầu từ bàn cờ, ống kính di chuyển sang trái, hiển thị cát vàng trên sàn, ống kính di chuyển lên đến một bãi biển, trên bãi biển có dấu chân, một cô gái mặc đồ trắng giản dị trên bãi biển dần đi xa, ống kính chuyển sang góc quay từ trên cao, nước biển đang xô bờ (không xuất hiện người), chuyển cảnh mờ dần liền mạch, sóng biển biến thành rèm cửa bay, ống kính kéo ra, hiển thị cận cảnh khuôn mặt cô gái, quay liền mạch một cảnh",
    "0-2秒画面：快速四格闪切，红、粉、紫、豹纹四款蝴蝶结依次定格，特写缎面光泽与 "chéri" 品牌字样。画外音"Chéri 자석 리본으로 무궁무진한 아름다움을 연출해 보세요!"": "0-2 giây: Cắt nhanh bốn khung hình, bốn chiếc nơ đỏ, hồng, tím, da báo lần lượt đóng khung, cận cảnh độ bóng satin và chữ thương hiệu \"chéri\". Lời bình ngoài hình \"Chéri 자석 리본으로 무궁무진한 아름다움을 연출해 보세요!\"",
    "3-6秒画面：特写银色磁吸扣 "咔嗒" 吸合，再轻轻一拉分开，展示丝滑质感与便捷性。画外音"단 1초 만에 잠그고, 최고의 스타일을 완성하세요!"": "3-6 giây: Cận cảnh khóa từ tính bạc \"tách\" hút vào nhau, rồi nhẹ nhàng kéo ra, thể hiện chất liệu mượt mà và tính tiện lợi. Lời bình ngoài hình \"단 1초 만에 잠그고, 최고의 스타일을 완성하세요!\"",
    "7-12 秒画面：快速切换佩戴场景：酒红款别在大衣领口，通勤氛围感拉满；粉色款绑在马尾，甜妹出街；紫色款系在包带，小众高级；豹纹款挂在西装领，辣妹气场全开。画外音"코트, 가방, 헤어 액세서리까지, 다재다능하고 개성 넘치는 스타일을 완성하세요!"": "7-12 giây: Chuyển nhanh các cảnh đeo: Kiểu rượu đỏ cài ở cổ áo khoác, đầy phong cách đi làm; kiểu hồng buộc đuôi ngựa, ngọt ngào xuống phố; kiểu tím gắn vào quai túi, tinh tế cao cấp; kiểu da báo treo ở cổ vest, phong thái cá tính bùng nổ. Lời bình ngoài hình \"코트, 가방, 헤어 액세서리까지, 다재다능하고 개성 넘치는 스타일을 완성하세요!\"",
    "13-15秒画面：四款蝴蝶结并排陈列，品牌名 "chéri, 당신에게 즉각적인 아름다움을 선사합니다!"": "13-15 giây: Bốn kiểu nơ xếp hàng trưng bày, tên thương hiệu \"chéri, 당신에게 즉각적인 아름다움을 선사합니다!\"",
    "对@图片2的包包进行商业化的摄像展示，包包的侧面参考@图片1，包包的表面材质参考@图片3，要求将包包的细节均有所展示，背景音恢宏大气，": "Thực hiện quay quảng cáo thương mại cho chiếc túi xách @hình ảnh 2, mặt bên của túi tham chiếu @hình ảnh 1, chất liệu bề mặt túi tham chiếu @hình ảnh 3, yêu cầu thể hiện đầy đủ chi tiết của túi, nhạc nền hoành tráng, ",
    "把@图片1作为画面的首帧图，第一人称视角，参考@视频1的运镜效果，上方场景参考@图片2，左边场景参考@图片3，右边场景参考@图片4。": "Lấy @hình ảnh 1 làm khung hình đầu, góc nhìn người thứ nhất, tham chiếu hiệu ứng chuyển động camera của @video 1, cảnh phía trên tham chiếu @hình ảnh 2, cảnh bên trái tham chiếu @hình ảnh 3, cảnh bên phải tham chiếu @hình ảnh 4.",
    "高难度/可控的运镜和动作精准复刻": "Chuyển động camera khó/có thể kiểm soát và tái tạo chính xác hành động",
    "以前想让模型模仿电影里的走位、运镜或者复杂动作，要么写一堆细节提示词，要么干脆做不到。而现在，只需要上传一段参考视频，就可以了": "Trước đây muốn mô hình bắt chước di chuyển, chuyển động camera hoặc hành động phức tạp trong phim, hoặc phải viết hàng loạt prompt chi tiết, hoặc đơn giản là không thể làm được. Nhưng bây giờ, chỉ cần tải lên một đoạn video tham chiếu là đủ",
    "创意模版 / 复杂特效精准复刻": "Mẫu sáng tạo / Tái tạo chính xác hiệu ứng phức tạp",
    "不止能生图写故事，Seedance 2.0 还支持"照着模仿"——创意转场、广告成片、电影片段、复杂剪辑，只要你有参考图或视频，模型就能识别动作节奏、镜头语言、视觉结构，并精准复刻出来。不懂专业术语也没关系，写清楚你想参考的部分，比如"参考 @视频1 的节奏和运镜，@图1 的角色造型"，模型就能高质量生成属于你的版本。大胆试！它真的能做到": "Không chỉ tạo ảnh viết truyện, Seedance 2.0 còn hỗ trợ \"bắt chước theo mẫu\" — chuyển cảnh sáng tạo, video quảng cáo hoàn chỉnh, đoạn phim, dựng phim phức tạp, chỉ cần bạn có ảnh hoặc video tham chiếu, mô hình có thể nhận diện nhịp điệu hành động, ngôn ngữ ống kính, cấu trúc thị giác, và tái tạo chính xác. Không hiểu thuật ngữ chuyên môn cũng không sao, viết rõ phần bạn muốn tham chiếu, ví dụ \"Tham chiếu nhịp điệu và chuyển động camera của @video 1, hình tượng nhân vật của @ảnh 1\", mô hình sẽ tạo ra phiên bản chất lượng cao của riêng bạn. Cứ thử đi! Nó thực sự làm được",
    "模型的创意性、剧情补全能力": "Tính sáng tạo và khả năng bổ sung cốt truyện của mô hình",
    "视频延长": "Kéo dài video",
    "音色更准，声音更真": "Âm sắc chính xác hơn, giọng nói chân thực hơn",
    "固定镜头，中央鱼眼镜头透过圆形孔洞向下窥视，参考视频1的鱼眼镜头，让@视频2中的马看向鱼眼镜头，参考@视频1中的说话动作，背景BGM参考@视频3中的音效。": "Ống kính cố định, ống kính mắt cá trung tâm nhìn xuống qua lỗ tròn, tham chiếu ống kính mắt cá của video 1, để con ngựa trong @video 2 nhìn vào ống kính mắt cá, tham chiếu hành động nói chuyện trong @video 1, BGM nền tham chiếu âm thanh trong @video 3.",
    "根据提供的写字楼宣传照，生成一段15秒电影级写实风格的地产纪录片，采用2.35:1宽银幕，24fps，细腻的画面风格，其中旁白的音色参考@视频1，拍摄 "写字楼的生态"，呈现楼内不同企业的运作，结合旁白阐述写字楼如何成为一个充满活力的商业生态系统.": "Dựa trên ảnh quảng cáo tòa nhà văn phòng được cung cấp, tạo một đoạn phim tài liệu bất động sản phong cách điện ảnh siêu thực 15 giây, sử dụng màn ảnh rộng 2.35:1, 24fps, phong cách hình ảnh tinh tế, trong đó âm sắc lời bình tham chiếu @video 1, quay \"hệ sinh thái tòa nhà văn phòng\", thể hiện hoạt động của các doanh nghiệp khác nhau trong tòa nhà, kết hợp lời bình trình bày cách tòa nhà trở thành một hệ sinh thái thương mại đầy sức sống.",
    "在"猫狗吐槽间"里的一段吐槽对话，要求情感丰沛，符合脱口秀表演：\n喵酱（猫主持，舔毛翻眼）：\"家人们谁懂啊，我身边这位，每天除了摇尾巴、拆沙发，就只会用那种"我超乖求摸摸"的眼神骗人类零食，明明拆家的时候比谁都凶，还好意思叫旺仔，我看叫"旺拆"还差不多哈哈哈"\n": "Một đoạn hội thoại \"roast\" trong \"Phòng chém gió Chó Mèo\", yêu cầu cảm xúc dồi dào, phù hợp với phong cách talk show:\nMeo-chan (mèo MC, vừa liếm lông vừa trợn mắt): \"Mọi người ai hiểu không, vị bên cạnh tôi đây, hàng ngày ngoài vẫy đuôi, phá sofa, thì chỉ biết dùng ánh mắt kiểu 'con ngoan lắm xin vuốt đầu' để lừa đồ ăn vặt từ người, rõ ràng lúc phá nhà dữ hơn ai hết, mà vẫn tự xưng là Vượng Tài, tôi thấy gọi là 'Vượng Phá' thì đúng hơn hahaha\"\n",
    "旺仔（狗主持，歪头晃尾巴）：\"你还好意思说我？你每天睡18个小时，醒了就蹭人类腿要罐头，掉毛掉得人类黑衣服上全是你的毛，人家扫完地，你转身又在沙发上滚一圈，还好意思装高冷贵族？\"": "Vượng Tài (chó MC, nghiêng đầu vẫy đuôi): \"Mày còn dám nói tao? Mày ngày nào cũng ngủ 18 tiếng, tỉnh dậy là cọ chân người đòi đồ hộp, rụng lông rụng đến nỗi áo đen của người đầy lông mày, người ta vừa quét xong nhà, mày quay lưng lại lăn một vòng trên sofa, còn giả vờ quý tộc cao lạnh?\"",
    "豫剧经前桥段《铡美案》的伴奏响起，左侧的黑衣包拯指着右侧的红衣陈世美，咬牙切齿地唱着豫剧："刀对鞘，真凭实据你敢不招？" 陈世美的眼珠左右滴溜溜乱转，寻找着权宜之策，面色窘迫至极。此时，画面外传来一声豫剧旦角的念白："且慢！"包拯和陈世美一齐向画面右侧看去。": "Nhạc nền đoạn mở đầu vở Dự kịch \"Trảm Mỹ Án\" vang lên, Bao Công áo đen bên trái chỉ tay vào Trần Thế Mỹ áo đỏ bên phải, nghiến răng hát Dự kịch: \"Dao kề vỏ, bằng chứng đanh thép ngươi dám không nhận?\" Mắt Trần Thế Mỹ đảo qua đảo lại tìm kế hoãn binh, vẻ mặt vô cùng lúng túng. Lúc này, từ ngoài hình vang lên một câu niệm bạch của đào nương Dự kịch: \"Khoan đã!\" Bao Công và Trần Thế Mỹ cùng nhìn sang bên phải màn hình.",
    "生成一个15秒的MV视频。关键词：稳重构图 / 轻推拉 / 低角度英雄感 / 纪实但高级A超广角建立镜头，低机位轻微仰拍，悬崖土路与复古旅行车占画面下三分之一，远处海面与地平线拉开空间，夕阳侧逆光体积光穿过尘粒，电影级构图，真实胶片颗粒，微风吹动衣角。": "Tạo một video MV 15 giây. Từ khóa: bố cục vững chãi / đẩy kéo nhẹ / góc thấp cảm giác anh hùng / phong cách tài liệu nhưng cao cấp. Ống kính siêu rộng thiết lập, máy đặt thấp hơi ngửa lên, đường đất vách đá và xe du lịch cổ điển chiếm phần ba dưới hình ảnh, mặt biển xa và đường chân trời mở rộng không gian, ánh nắng hoàng hôn ngược bên sườn với tia sáng xuyên qua hạt bụi, bố cục điện ảnh, hạt phim thực, gió nhẹ thổi vạt áo.",
    "画面中间戴帽子的女孩温柔地唱着说\"I'm so proud of my family!\"，之后转身拥抱中间的黑人女孩。黑人女孩感动地回应\"My sweetie, you're the heart of our family\"，回抱她。左侧的黄衣服男孩开心地说\"Folks, let's dance together to celebrate!" 最右侧的女孩紧接着回复： "I'll bring the music!\"，背景拉美音乐响起，左侧穿橙色裙的女性（朱丽叶塔）笑着点头，右侧扎辫女性（路易莎）握紧拳头挥动手臂。人群中有人开始踏起步子，孩子们跟着节奏拍手，整个家族即将围成圈，伴着欢快的音乐，裙摆飞扬，在五彩的街道上尽情舞动，传递着喜悦与温暖。": "Cô gái đội mũ ở giữa màn hình dịu dàng hát \"I'm so proud of my family!\", sau đó quay lại ôm cô gái da đen ở giữa. Cô gái da đen xúc động đáp lại \"My sweetie, you're the heart of our family\", ôm lại cô ấy. Cậu bé áo vàng bên trái vui vẻ nói \"Folks, let's dance together to celebrate!\" Cô gái ngoài cùng bên phải liền đáp: \"I'll bring the music!\", nhạc Latin vang lên ở phía sau, người phụ nữ mặc váy cam bên trái (Julieta) mỉm cười gật đầu, người phụ nữ tết tóc bên phải (Luisa) nắm chặt tay vung cánh tay. Trong đám đông có người bắt đầu bước nhảy, trẻ em vỗ tay theo nhịp, cả gia đình sắp quây thành vòng tròn, hòa theo âm nhạc vui tươi, tà váy bay bổng, nhảy múa thỏa thích trên con phố rực rỡ sắc màu, lan tỏa niềm vui và sự ấm áp.",
    "固定镜头。站着的壮汉（队长）握拳挥臂用西班牙语说着："三分钟后突袭！"持刀者收刀入鞘，金发队员站在检查枪械，绿发队员握紧战术手电。黑人队员搭肩问同伴用西班牙语说："侧翼包抄？"队长点头用西班牙语说："老规矩，活口留审讯。"全员肃然，装备碰撞声中完成战术手势，默契起身，大家都严阵以待，左侧两个男生也争先站起来准备战斗。": "Ống kính cố định. Người đàn ông vạm vỡ đứng (đội trưởng) nắm chặt tay vung cánh tay nói bằng tiếng Tây Ban Nha: \"Ba phút nữa tập kích!\" Người cầm dao tra dao vào vỏ, đội viên tóc vàng đứng kiểm tra vũ khí, đội viên tóc xanh nắm chặt đèn pin chiến thuật. Đội viên da đen vỗ vai hỏi đồng đội bằng tiếng Tây Ban Nha: \"Bọc sườn?\" Đội trưởng gật đầu nói bằng tiếng Tây Ban Nha: \"Theo quy tắc cũ, giữ người sống để thẩm vấn.\" Toàn đội nghiêm trang, trong tiếng va chạm trang bị hoàn thành hiệu lệnh chiến thuật, đồng loạt đứng dậy, mọi người đều sẵn sàng chiến đấu, hai chàng trai bên trái cũng tranh nhau đứng dậy chuẩn bị chiến đấu.",
    "0-3秒：开头闹钟响起来，画面朦胧中出现画面1； ": "0-3 giây: Mở đầu đồng hồ báo thức kêu, trong hình ảnh mờ ảo xuất hiện hình ảnh 1; ",
    "3-10秒：快速摇镜头，转向对面特写男人面部，男人无奈的叫女生起床，语气和音色参考@视频1； ": "3-10 giây: Ống kính quay nhanh, chuyển sang cận cảnh khuôn mặt người đàn ông đối diện, anh ấy bất lực gọi cô gái dậy, ngữ điệu và âm sắc tham chiếu @video 1; ",
    "10-12秒：女生撅着嘴躲进被子里面； ": "10-12 giây: Cô gái chu môi trốn vào trong chăn; ",
    "12-15秒：切换到男主全身，他叹着气说："真拿你没办法！"": "12-15 giây: Chuyển sang toàn thân nam chính, anh ấy thở dài nói: \"Thật chẳng biết làm gì với em!\"",
    "@图片1的猴子走向奶茶店柜台，镜头跟随在他身后，一位@图片2的比熊服务员正在吧台处擦拭制作工具，猴子向服务员用四川口音点单："幺妹儿，霸王别姬有得没得？"\n切镜，特写。\n服务员放下手里的活，怪异地看了老头一眼后回答："没得，美式要不要得嘛"\n": "Chú khỉ @hình ảnh 1 đi đến quầy tiệm trà sữa, ống kính bám theo phía sau, một nhân viên chó Bichon @hình ảnh 2 đang lau dụng cụ pha chế tại quầy bar, chú khỉ gọi món với giọng Tứ Xuyên: \"Cô em ơi, có Bá Vương Biệt Cơ không vậy?\"\nChuyển cảnh, cận cảnh.\nNhân viên bỏ việc đang làm, nhìn ông lão một cái lạ lùng rồi trả lời: \"Hết rồi, Americano uống không?\"\n",
    "切镜，镜头给到猴子。": "Chuyển cảnh, ống kính quay sang chú khỉ.",
    "他挠了挠头念念有词："没事……？我有事！孙儿叫我来买个奶茶，就叫个撒子霸王别姬嘛"": "Hắn gãi đầu lẩm bẩm: \"Không sao...? Tôi có việc! Cháu bảo tôi đi mua trà sữa, gọi cái gì Bá Vương Biệt Cơ đó mà\"",
    "用科普风格和音色，将": "Dùng phong cách và giọng khoa học thường thức, biến ",
    "图片1": "hình ảnh 1",
    "中的内容演绎出来，内容包括悟空为过火焰山，到翠云山向铁扇公主借芭蕉扇。铁扇公主因红孩儿被悟空降伏拜观音为童子，母子分离，不肯借扇还欲报仇。悟空好言相劝无果，二人随即起了争执的小故事进行讲解。": " nội dung trong đó thành bài diễn giải, nội dung bao gồm Ngộ Không để vượt qua Hỏa Diệm Sơn, đến Thúy Vân Sơn mượn quạt Ba Tiêu từ Thiết Phiến Công Chúa. Thiết Phiến Công Chúa vì Hồng Hài Nhi bị Ngộ Không thu phục phải bái Quan Âm làm đồng tử, mẹ con ly biệt, không chịu cho mượn quạt còn muốn báo thù. Ngộ Không khuyên nhủ không được, hai người liền xảy ra tranh cãi — kể lại câu chuyện nhỏ này.",
    "镜头连贯性（一镜到底）更强": "Tính liên tục ống kính (quay liền mạch một cảnh) mạnh hơn",
    "@图片1@图片2@图片3@图片4@图片5，一镜到底的追踪镜头，从街头跟随跑步者上楼梯、穿过走廊、进入屋顶，最终俯瞰城市。": "@hình ảnh 1@hình ảnh 2@hình ảnh 3@hình ảnh 4@hình ảnh 5, cảnh quay bám theo liền mạch một cảnh, từ đường phố theo người chạy bộ lên cầu thang, đi qua hành lang, lên mái nhà, cuối cùng nhìn toàn cảnh thành phố từ trên cao.",
    "以@图片1为首帧，画面放大至飞机舷窗外，一团团云朵缓缓飘至画面中，其中一朵为彩色糖豆点缀的云朵，始终在画面中居中，然后缓缓变形为@图片2的冰淇淋，镜头推远回到机舱内，坐在窗边的@图片3伸手从窗外拿进冰淇淋，吃了一口，嘴巴上沾满奶油，脸上洋溢出甜蜜的笑容，此时视频配音为@视频1.": "Lấy @hình ảnh 1 làm khung hình đầu, hình ảnh phóng to ra ngoài cửa sổ máy bay, từng đám mây từ từ trôi vào hình, trong đó có một đám mây được trang trí bằng kẹo đường đầy màu sắc, luôn ở giữa hình ảnh, rồi dần biến hình thành kem @hình ảnh 2, ống kính kéo ra trở lại trong khoang máy bay, @hình ảnh 3 ngồi cạnh cửa sổ duỗi tay lấy kem từ ngoài cửa sổ vào, ăn một miếng, miệng dính đầy kem, khuôn mặt nở nụ cười ngọt ngào, lúc này lồng tiếng video là @video 1.",
    "谍战片风格，@图片1作为首帧画面，镜头正面跟拍穿着红风衣的女特工向前走，镜头全景跟随，不断有路人遮挡红衣女子，走到一个拐角处，参考@图片2的拐角建筑，固定镜头红衣女子离开画面，走在拐角处消失，一个戴面具的女孩在拐角处躲着恶狠狠的盯着她，面具女孩形象参考@图片3，只参考形象，女孩站在拐角处。镜头往前摇向红衣女特工，她走进一座豪宅消失不见了，豪宅参考@图片4。全程不要切镜头，一镜到底。": "Phong cách phim gián điệp, @hình ảnh 1 làm khung hình đầu, ống kính quay chính diện bám theo nữ đặc vụ mặc áo gió đỏ đi về phía trước, ống kính toàn cảnh bám theo, liên tục có người đi đường che khuất người phụ nữ áo đỏ, đi đến một góc rẽ, tham chiếu kiến trúc góc rẽ @hình ảnh 2, ống kính cố định người phụ nữ áo đỏ rời khỏi hình ảnh, đi ở góc rẽ biến mất, một cô gái đeo mặt nạ núp ở góc rẽ nhìn cô ấy đầy ác ý, hình tượng cô gái đeo mặt nạ tham chiếu @hình ảnh 3, chỉ tham chiếu hình tượng, cô gái đứng ở góc rẽ. Ống kính quay về phía trước hướng tới nữ đặc vụ áo đỏ, cô ấy đi vào một biệt thự và biến mất, biệt thự tham chiếu @hình ảnh 4. Toàn bộ không cắt cảnh, quay liền mạch một cảnh.",
    "根据@图片1外景的镜头，第一人称主观视角快推镜头到木屋内的环境场景近景，一只小鹿@图片2和一只羊@图片3在围炉旁喝茶聊天，镜头推进特写茶杯的样式参考@图片4.": "Theo cảnh ngoại cảnh @hình ảnh 1, góc nhìn chủ quan người thứ nhất đẩy nhanh ống kính đến cận cảnh môi trường bên trong cabin gỗ, một chú nai nhỏ @hình ảnh 2 và một chú cừu @hình ảnh 3 đang uống trà trò chuyện bên lò sưởi, ống kính đẩy vào cận cảnh kiểu dáng tách trà tham chiếu @hình ảnh 4.",
    "@图片1@图片2@图片3@图片4@图片5，主观视角一镜到底的惊险过山车的镜头，过山车的速度越来越快。": "@hình ảnh 1@hình ảnh 2@hình ảnh 3@hình ảnh 4@hình ảnh 5, góc nhìn chủ quan quay liền mạch một cảnh tàu lượn siêu tốc hồi hộp, tốc độ tàu lượn ngày càng nhanh hơn.",
    "视频编辑可用度高": "Chỉnh sửa video có tính ứng dụng cao",
    "有时候你已经有了一段视频，不想从头再找图或重做一遍，只是希望调整其中一小段动作、延长几秒钟，或让角色表现更贴近你的想法。现在你可以直接用已有视频作为输入，在不改变其它内容的前提下，指定片段、动作或节奏进行定向修改。无需重头生成，也能快速完成调整": "Đôi khi bạn đã có sẵn một đoạn video, không muốn tìm lại ảnh hay làm lại từ đầu, chỉ muốn điều chỉnh một đoạn hành động nhỏ, kéo dài thêm vài giây, hoặc để nhân vật thể hiện gần hơn với ý tưởng của bạn. Bây giờ bạn có thể trực tiếp dùng video có sẵn làm đầu vào, trong khi không thay đổi nội dung khác, chỉ định đoạn clip, hành động hoặc nhịp điệu để sửa đổi có mục tiêu. Không cần tạo lại từ đầu, vẫn có thể hoàn thành điều chỉnh nhanh chóng",
    "颠覆@视频1的整个剧情": "Đảo ngược toàn bộ cốt truyện của @video 1",
    "0–3秒画面：西装男坐在酒吧，神情冷静，手里轻晃酒杯。 镜头缓慢推进，光影高级、氛围严肃。 环境音低沉，西装男小声说"这单生意，很大。"": "0-3 giây: Người đàn ông vest ngồi trong quán bar, vẻ mặt bình tĩnh, tay khẽ lắc ly rượu. Ống kính từ từ đẩy tới, ánh sáng cao cấp, không khí nghiêm túc. Âm thanh môi trường trầm, người đàn ông vest nói nhỏ \"Thương vụ này, rất lớn.\"",
    "3–6秒画面：身后的女人表情紧张问"有多大？"西装男抬眼，压低声音："非常大。"镜头切手部特写——他把酒杯放下，气场拉满。": "3-6 giây: Người phụ nữ phía sau vẻ mặt căng thẳng hỏi \"Lớn cỡ nào?\" Người đàn ông vest ngước mắt, hạ giọng: \"Rất lớn.\" Ống kính chuyển sang cận cảnh bàn tay — anh ta đặt ly rượu xuống, khí chất đỉnh cao.",
    "6–9秒画面：突然西装男从桌下掏出—— 一大包体积夸张的零食礼包，"咚"的一声重重放在桌上。": "6-9 giây: Đột nhiên người đàn ông vest lấy ra từ dưới bàn — một gói quà vặt khổng lồ kích thước cực lớn, \"bịch\" một tiếng đặt nặng trên bàn.",
    "9–12秒画面：身后的女人原本放在腰间的手，肌肉从僵硬到松弛，整个人表情放松。画面氛围轻松起来。": "9-12 giây: Người phụ nữ phía sau, tay vốn đặt ở thắt lưng, cơ bắp từ cứng nhắc chuyển sang thả lỏng, toàn bộ biểu cảm trở nên thoải mái. Bầu không khí hình ảnh nhẹ nhàng hẳn.",
    "13–15秒画面：西装男拿出一包零食给女人，镜头拉远展示酒馆全景，画面变得透明模糊—— 字幕弹出"再忙，也要记得吃点零食~"": "13-15 giây: Người đàn ông vest lấy một gói đồ ăn vặt đưa cho người phụ nữ, ống kính kéo ra hiển thị toàn cảnh quán rượu, hình ảnh trở nên trong suốt mờ ảo — phụ đề hiện lên \"Dù bận đến đâu, cũng nhớ ăn chút đồ ăn vặt nhé~\"",
    "视频1中的女主唱换成图片1的男主唱，动作完全模仿原视频，不要出现切镜，乐队演唱音乐。": "Nữ ca sĩ chính trong video 1 thay thành nam ca sĩ chính trong hình ảnh 1, hành động hoàn toàn bắt chước video gốc, không cắt cảnh, ban nhạc biểu diễn.",
    "将视频1女人发型变成红色长发，图片1中的大白鲨缓缓浮出半个脑袋，在她身后。": "Thay đổi kiểu tóc người phụ nữ trong video 1 thành tóc dài đỏ, cá mập trắng lớn trong hình ảnh 1 từ từ nổi lên nửa đầu, phía sau cô ấy.",
    "视频1镜头右摇，炸鸡老板忙碌地将炸鸡递给排队的客户，用普通话说"做完他的，做你的，大家文明排队。"一说完，就去拿纸袋子去装炸鸡。特写展示老板拿印有图1的纸袋子，特写展示递给客户的手部特写。": "Ống kính video 1 quay sang phải, ông chủ gà rán bận rộn đưa gà rán cho khách xếp hàng, nói bằng tiếng phổ thông \"Làm xong của anh ấy rồi đến của bạn, mọi người xếp hàng văn minh.\" Nói xong liền đi lấy túi giấy đựng gà rán. Cận cảnh ông chủ cầm túi giấy in hình ảnh 1, cận cảnh bàn tay đưa cho khách hàng.",
    "可进行音乐卡点": "Có thể đồng bộ nhịp nhạc",
    "情绪演绎更好": "Diễn xuất cảm xúc tốt hơn",
    "🏁 最后说两句": "🏁 Lời cuối",
    "Seedance 2.0 的多模态能力正处于不断进化中，我们会持续更新能力、支持更多种输入组合方式。希望这份使用手册能帮你更自由地发挥创意！": "Khả năng đa phương thức của Seedance 2.0 đang liên tục phát triển, chúng tôi sẽ tiếp tục cập nhật năng lực, hỗ trợ thêm nhiều cách kết hợp đầu vào. Hy vọng hướng dẫn sử dụng này giúp bạn phát huy sáng tạo tự do hơn!",
    "如果你遇到了 Bug，或者有用法建议、需求场景，欢迎留言、私信、敲锣打鼓告诉我们！我们会持续优化，一起把即梦变成真正让你们开心、方便的生产力工具 ❤️": "Nếu bạn gặp Bug, hoặc có gợi ý sử dụng, tình huống nhu cầu, hãy để lại bình luận, nhắn tin, hãy cho chúng tôi biết! Chúng tôi sẽ liên tục tối ưu hóa, cùng nhau biến Jimeng thành công cụ năng suất thực sự khiến các bạn vui vẻ và thuận tiện ❤️",
}

# Apply translations
for block in translated['blocks']:
    for element in block.get('elements', []):
        if element.get('type') == 'text_run':
            content = element['content']
            if content in translations:
                element['content'] = translations[content]

# Write output
with open('C:/Users/ADMIN/hoa55_ ver3/translated_blocks.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

# Verify
with open('C:/Users/ADMIN/hoa55_ ver3/translated_blocks.json', 'r', encoding='utf-8') as f:
    result = json.load(f)
print(f"Total blocks: {len(result['blocks'])}")

# Check for untranslated Chinese content
import re
untranslated = []
for i, block in enumerate(result['blocks']):
    for element in block.get('elements', []):
        if element.get('type') == 'text_run':
            content = element['content']
            # Check if content has Chinese characters and is not a known keep-as-is
            if re.search(r'[\u4e00-\u9fff]', content):
                untranslated.append((i, content[:80]))

print(f"\nUntranslated blocks with Chinese: {len(untranslated)}")
for idx, content in untranslated:
    print(f"  Block {idx}: {content}")
