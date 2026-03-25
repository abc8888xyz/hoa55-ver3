# -*- coding: utf-8 -*-
"""Translate art37 CN->VI"""
import json, sys, copy

sys.stdout.reconfigure(encoding='utf-8')

with open('_art37_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

trans = copy.deepcopy(data)

# Translation map: Chinese -> Vietnamese
# We'll translate block by block
translations = {
    # Block 0 - page title
    "MiniMax出了个「零部署」OpenClaw小龙虾，我们一起试一下（胎教级教程）":
        "MiniMax ra mắt OpenClaw Tôm Hùm「Không cần triển khai」, cùng thử nhé (Hướng dẫn siêu chi tiết)",
    # Block 1 - quote
    "🔗 原文链接： ": "🔗 Link bài gốc: ",
    # Block 2
    "原创 Albert Lsk Albert Lsk 数字牧民-Lsk": "Bài gốc Albert Lsk Albert Lsk Digital Nomad-Lsk",
    "2026年2月26日 09:18  广东": "26/02/2026 09:18  Quảng Đông",
    # Block 3
    "MiniMax出了个「零部署」OpenClaw小龙虾，我们一起试一下（保姆级教程）":
        "MiniMax ra mắt OpenClaw Tôm Hùm「Không cần triển khai」, cùng thử nhé (Hướng dẫn cầm tay chỉ việc)",
    # Block 4
    "嗨，我是ALSKai，让我们一起用AI做点有趣的事。🌿":
        "Xin chào, mình là ALSKai, cùng nhau dùng AI làm những điều thú vị nhé. 🌿",
    # Block 5
    "今天刷到个新鲜事。": "Hôm nay lướt thấy một tin mới.",
    # Block 6
    "MiniMax 上了个东西，叫 MaxClaw。 ": "MiniMax ra mắt một thứ mới, gọi là MaxClaw. ",
    # Block 7
    "说是「零部署」OpenClaw。": "Nói là OpenClaw「không cần triển khai」.",
    # Block 8
    "这话我听过很多次了。通常意思是：你还得配环境、还得写代码、还得调半天。":
        "Câu này mình nghe nhiều lần rồi. Thường có nghĩa là: bạn vẫn phải cấu hình môi trường, vẫn phải viết code, vẫn phải chỉnh sửa cả buổi.",
    # Block 9
    "但这次好像有点不一样。": "Nhưng lần này có vẻ hơi khác.",
    # Block 10 - heading2
    "MaxClaw是个啥": "MaxClaw là cái gì",
    # Block 11
    "MaxClaw = OpenClaw × MiniMax Agent × M2.5": "MaxClaw = OpenClaw × MiniMax Agent × M2.5",
    # Block 12
    "拆开来看：": "Phân tích từng phần:",
    # Block 13
    "「 OpenClaw 」 ": "「 OpenClaw 」 ",
    "：一个开源的 AI Agent 框架，GitHub 19 万+ star，MIT 许可证。支持 20 多个平台——Telegram、WhatsApp、Slack、Discord，甚至 iMessage 和微信（感谢苍何老师的开源）。":
        ": một framework AI Agent mã nguồn mở, GitHub 190K+ star, giấy phép MIT. Hỗ trợ hơn 20 nền tảng — Telegram, WhatsApp, Slack, Discord, thậm chí cả iMessage và WeChat (cảm ơn thầy Thương Hà đã mở nguồn).",
    # Block 14
    "「 MiniMax M2.5 」 ": "「 MiniMax M2.5 」 ",
    "：MiniMax 自家的 100 亿参数模型，说是旗舰级 Agent 性能。":
        ": mô hình 10 tỷ tham số của chính MiniMax, được cho là hiệu năng Agent hàng đầu.",
    # Block 15
    "核心卖点就三个：零部署（是真的点一下就用）、不用额外付 API 费、7×24 小时挂着。":
        "Ba điểm bán hàng cốt lõi: không cần triển khai (thực sự chỉ cần click là dùng), không cần trả thêm phí API, chạy 7×24 giờ liên tục.",
    # Block 16 - heading2
    "为什么值得注意": "Tại sao đáng chú ý",
    # Block 17
    "市面上做 AI 助手的挺多。": "Trên thị trường có khá nhiều AI assistant.",
    # Block 18
    "但大部分有仨问题：": "Nhưng đa phần có ba vấn đề:",
    # Block 19
    "「 第一，得自己搭。 」 ": "「 Thứ nhất, phải tự dựng. 」 ",
    "本地部署？显卡够不够？云服务器？每月开销多少？劝退一大半。":
        "Triển khai local? Card đồ họa có đủ không? Cloud server? Chi phí hàng tháng bao nhiêu? Khiến đa số bỏ cuộc.",
    # Block 20
    "「 第二，平台割裂。 」 ": "「 Thứ hai, nền tảng bị chia cắt. 」 ",
    "Telegram 一个、WhatsApp 一个、Discord 一个。每个都要单独配，维护成本高。":
        "Telegram một cái, WhatsApp một cái, Discord một cái. Mỗi cái đều phải cấu hình riêng, chi phí bảo trì cao.",
    # Block 21
    "「 第三，费钱。 」 ": "「 Thứ ba, tốn tiền. 」 ",
    "用着用着发现 API 账单哗哗涨（我有一阵子就这么\u201c破产\u201d的hhhhhhh再也不敢用Claude的api了！！）。":
        "Dùng một thời gian phát hiện hóa đơn API tăng vèo vèo (mình có một dạo \u201cphá sản\u201d kiểu này hhhhhhh không dám dùng API của Claude nữa!!).",
    # Block 22
    "MaxClaw 的打法是：你直接用，剩下的我搞定。 ":
        "Cách chơi của MaxClaw là: bạn cứ dùng, phần còn lại để tôi lo. ",
    "国内版链接在 https://agent.minimaxi.com 不需要魔法 ":
        "Link phiên bản nội địa tại https://agent.minimaxi.com không cần VPN ",
    # Block 23 - heading2
    "具体能干啥": "Cụ thể làm được gì",
    # Block 24
    "根据官网介绍，MaxClaw 可以多平台同时在线（一个账号，Telegram、WhatsApp 都能用），能记住你们的对话（持久化记忆，不是聊完就忘），还能自定义性格（SOUL.md 文件，你可以给它设定「人设」）。":
        "Theo giới thiệu trên trang chủ, MaxClaw có thể online đồng thời trên nhiều nền tảng (một tài khoản, Telegram, WhatsApp đều dùng được), có thể nhớ cuộc trò chuyện của bạn (bộ nhớ lâu dài, không phải chat xong là quên), còn có thể tùy chỉnh tính cách (file SOUL.md, bạn có thể thiết lập「nhân vật」cho nó).",
    # Block 25
    "但有两个限制：仅支持 MiniMax Agent 模型（不能接其他模型，这点要提前说清楚），也不支持 MiniMax 的 Coding Plan":
        "Nhưng có hai hạn chế: chỉ hỗ trợ mô hình MiniMax Agent (không thể kết nối mô hình khác, điểm này cần nói rõ trước), cũng không hỗ trợ Coding Plan của MiniMax",
    # Block 26
    "这东西看着挺有意思，我打算实测一下。":
        "Thứ này nhìn khá thú vị, mình định thử nghiệm thực tế.",
    # Block 27
    "「 下面正式开始我们的教程啦！ 」 ": "「 Dưới đây chính thức bắt đầu hướng dẫn nhé! 」 ",
    "（虽然下面看起来步骤不少，但是操作起来可能十分钟都不需要":
        "(Tuy nhìn bên dưới có vẻ nhiều bước, nhưng thao tác thực tế có thể không cần đến mười phút",
    # Block 28
    "先登录这个网站： https://agent.minimaxi.com 不需要魔法~":
        "Đầu tiên đăng nhập trang web này: https://agent.minimaxi.com không cần VPN~",
    # Block 29
    "「 点击登录 」 ": "「 Nhấn đăng nhập 」 ",
    # Block 30
    "「 有微信扫码登录和手机号登录 」 ": "「 Có đăng nhập bằng quét mã WeChat và số điện thoại 」 ",
    "我是懒狗我直接微信扫码哈哈哈哈哈哈 ": "Mình lười nên quét mã WeChat luôn hahahaha ",
    # Block 31
    "「 新注册用户送1000积分 」 ": "「 Người dùng đăng ký mới được tặng 1000 điểm 」 ",
    # Block 32
    "「 点击MaxClaw 」 ": "「 Nhấn vào MaxClaw 」 ",
    # Block 33
    "「 点立即开始 」 ": "「 Nhấn Bắt đầu ngay 」 ",
    # Block 34
    "「 这里就任君选择了 」 ": "「 Ở đây tùy bạn lựa chọn 」 ",
    "为了方便我们快速教程，我这里选了默认配置 ":
        "Để tiện cho hướng dẫn nhanh, mình chọn cấu hình mặc định ",
    # Block 35
    "选好之后点击 ": "Chọn xong rồi nhấn ",
    "「 准备好了 」 ": "「 Sẵn sàng rồi 」 ",
    # Block 36
    "「 直接就连接？？这也太快了吧喂 」 ": "「 Kết nối luôn?? Nhanh quá vậy 」 ",
    # Block 37
    "这就开始干活了，自己在后台配置链接飞书的节点 ":
        "Bắt đầu làm việc luôn, tự cấu hình node kết nối Feishu ở backend ",
    # Block 38
    "「 行！这下我都不用出教程了，都给你说完了😭 」 ":
        "「 Được! Giờ mình không cần viết hướng dẫn nữa, nó nói hết rồi 😭 」 ",
    # Block 39
    "点击给出的 ": "Nhấn vào link ",
    "「 飞书开发平台 」 ": "「 Nền tảng phát triển Feishu 」 ",
    "链接，来到企业自建应用 ": "đã cho, đến phần ứng dụng tự xây dựng doanh nghiệp ",
    # Block 40
    "「 点击创建企业自建应用 」 ": "「 Nhấn tạo ứng dụng tự xây dựng doanh nghiệp 」 ",
    # Block 41
    "ok，我这里填好了 ": "OK, mình đã điền xong ",
    # Block 42
    "好了之后来到 ": "Xong rồi đến phần ",
    "「 凭证与基础信息 」 ": "「 Thông tin xác thực và cơ bản 」 ",
    "，把 ": ", sao chép ",
    "「 App ID 」 ": "「 App ID 」 ",
    "和 ": "và ",
    "「 App Secret 」 ": "「 App Secret 」 ",
    "复制，粘贴到MaxClaw里面 ": "rồi dán vào MaxClaw ",
    # Block 43
    "然后就稍微等一下，让maxclaw通过你的id和密钥链接上你的飞书 ":
        "Sau đó đợi một chút, để MaxClaw kết nối với Feishu của bạn qua ID và mật khẩu ",
    "然后MaxClaw会回你这段，我们把他给的 ":
        "Sau đó MaxClaw sẽ trả lời đoạn này, chúng ta sao chép phần ",
    "「 JSON 」 ": "「 JSON 」 ",
    "复制一下，等会儿会用到 ": "lại, lát nữa sẽ dùng đến ",
    # Block 44
    "现在回到飞书，点击 ": "Bây giờ quay lại Feishu, nhấn ",
    "「 添加机器人 」 ": "「 Thêm bot 」 ",
    # Block 45
    "点击 ": "Nhấn ",
    "「 权限管理 」 ": "「 Quản lý quyền 」 ",
    "，点 ": ", nhấn ",
    "「 批量导入/导出权限 」 ": "「 Nhập/Xuất quyền hàng loạt 」 ",
    # Block 46
    "还记得我们刚复制的那段代码不？粘贴进来之后点击确认。 ":
        "Còn nhớ đoạn code vừa sao chép không? Dán vào rồi nhấn xác nhận. ",
    # Block 47
    "注意⚠️我们还需要再添加一个没有提到的权限 ":
        "Lưu ý ⚠️ chúng ta còn cần thêm một quyền chưa được đề cập ",
    "「 contact:contact.base:readonly 」 ": "「 contact:contact.base:readonly 」 ",
    # Block 48
    "ok，确认好之后我们可以点击创建版本啦 ":
        "OK, xác nhận xong thì chúng ta có thể nhấn tạo phiên bản rồi ",
    # Block 49
    "写一下版本号，我喜欢从0.0.1开始（因为不是正式版 ":
        "Viết số phiên bản, mình thích bắt đầu từ 0.0.1 (vì chưa phải bản chính thức ",
    # Block 50
    "然后点击保存，确认创建就可以了。":
        "Sau đó nhấn lưu, xác nhận tạo là xong.",
    # Block 51
    "回到MaxClaw，跟它说一声完成了之后重启一下（就在右上角 ":
        "Quay lại MaxClaw, báo cho nó biết đã hoàn thành rồi khởi động lại (ngay góc trên bên phải ",
    # Block 52
    "完成重启后说一下，然后把他给的 ":
        "Sau khi khởi động lại xong thì nói một tiếng, rồi sao chép phần ",
    "「 im.message.receive_v1 」 ": "「 im.message.receive_v1 」 ",
    "复制一下 ": "mà nó đưa ",
    # Block 53
    "现在再回到飞书 ": "Bây giờ quay lại Feishu ",
    "来到 ": "đến phần ",
    "「 事件与回调 」 ": "「 Sự kiện và Callback 」 ",
    # Block 54
    "「 点击保存 」 ": "「 Nhấn Lưu 」 ",
    # Block 55
    "然后 ": "Sau đó ",
    "「 添加事件 」 ": "「 Thêm sự kiện 」 ",
    "，把刚刚复制的 ": ", dán phần vừa sao chép ",
    "粘贴进去然后勾选保存。 ": "vào rồi tích chọn và lưu. ",
    # Block 56
    "然后添加 ": "Sau đó thêm ",
    "「 回调配置 」 ": "「 Cấu hình Callback 」 ",
    "，保存一下（这是为了让我们能够在飞书上接收到MaxClaw发给我们的消息） ":
        ", lưu lại (việc này để chúng ta có thể nhận tin nhắn MaxClaw gửi cho chúng ta trên Feishu) ",
    # Block 57
    "创建新版本保存，然后发布 ": "Tạo phiên bản mới, lưu lại, rồi phát hành ",
    # Block 58
    "再回到MaxClaw跟它说一声 ": "Quay lại MaxClaw báo cho nó biết ",
    # Block 59
    "现在回到飞书应用，打开刚刚创建的应用。 ":
        "Bây giờ quay lại ứng dụng Feishu, mở ứng dụng vừa tạo. ",
    # Block 60
    "给应用发一句话，然后把它发送过来的匹配码复制一下发给MaxClaw ":
        "Gửi một tin nhắn cho ứng dụng, rồi sao chép mã xác thực nó gửi lại và gửi cho MaxClaw ",
    # Block 61
    "匹配上之后，就可以在飞书应用里面对话啦。":
        "Sau khi khớp thành công, có thể trò chuyện trong ứng dụng Feishu rồi.",
    # Block 62
    "这是我之前配置好了的小开🦞 ": "Đây là con Tôm Hùm nhỏ mình đã cấu hình trước đó 🦞 ",
    # Block 63
    "整体跑下来还是挺流畅的，服务器偶尔会停止不动的情况，这个时候就停止对话，再重新发一遍信息给它。 ":
        "Nhìn chung chạy khá mượt, server thỉnh thoảng bị đứng, lúc đó thì dừng cuộc trò chuyện rồi gửi lại tin nhắn. ",
    "还有两个坑得避雷——MaxClaw 只能接 MiniMax Agent，其他模型免谈。也不支持 Coding Plan，我这种开了年度 coding plan 的就有点亏，还得重新开一个 agent 的套餐。":
        "Còn hai cái bẫy cần tránh — MaxClaw chỉ kết nối được MiniMax Agent, các mô hình khác miễn bàn. Cũng không hỗ trợ Coding Plan, người như mình đã mua gói coding plan hàng năm thì hơi lỗ, phải mua thêm gói agent mới.",
    # Block 64 - heading2
    "一点观察": "Một vài nhận xét",
    # Block 65
    "OpenClaw 这个项目，挺有意思。": "Dự án OpenClaw này khá thú vị.",
    # Block 66
    "创建者叫 Peter Steinberger，今年 2 月加入了 OpenAI。":
        "Người tạo ra nó là Peter Steinberger, tháng 2 năm nay đã gia nhập OpenAI.",
    # Block 67
    "一个开源项目做到 19 万 star，然后被大厂招安……这剧本，还挺硅谷的。":
        "Một dự án mã nguồn mở đạt 190K star, rồi được công ty lớn mời về... kịch bản này khá Silicon Valley.",
    # Block 68
    "但开放开源的东西，不会因为他加入 OpenAI 就消失。MIT 许可证摆在那里，分叉、社区、迭代——开源的韧性就在这。":
        "Nhưng thứ mã nguồn mở sẽ không biến mất chỉ vì anh ấy gia nhập OpenAI. Giấy phép MIT vẫn còn đó, fork, cộng đồng, cập nhật — sức bền của mã nguồn mở nằm ở chỗ này.",
    # Block 69
    "「 零部署 」 ": "「 Không cần triển khai 」 ",
    "这个卖点，击中的是「不想折腾但想要 AI 助手」的人群。":
        "điểm bán hàng này nhắm đúng vào nhóm người「không muốn vọc vạch nhưng muốn có AI assistant」.",
    # Block 70
    "这个人群，比我们想象的大得多。":
        "Nhóm người này lớn hơn nhiều so với chúng ta tưởng.",
    # Block 71
    "如果你也试了 MaxClaw，评论区聊聊体验。":
        "Nếu bạn cũng đã thử MaxClaw, hãy chia sẻ trải nghiệm ở phần bình luận.",
    # Block 72
    "如果你没用过但想试试，我可以把实测流程详细写出来（配图密集，胎教级）。":
        "Nếu bạn chưa dùng nhưng muốn thử, mình có thể viết chi tiết quy trình thử nghiệm thực tế (nhiều hình ảnh, siêu chi tiết).",
    # Block 73
    "如果觉得有用，欢迎关注「数字牧民-Lsk」":
        "Nếu thấy hữu ích, hãy theo dõi「Digital Nomad-Lsk」",
    # Block 74
    "让我们一起用AI做点有趣的事 🌿": "Cùng nhau dùng AI làm những điều thú vị nhé 🌿",
    # Block 75
    "也欢迎直接私聊我呀 ": "Cũng hoan nghênh nhắn tin riêng cho mình nhé ",
}

# Apply translations
translated_count = 0
kept_count = 0

for block in trans['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run':
            content = el['content']
            if content in translations:
                el['content'] = translations[content]
                if content != translations[content]:
                    translated_count += 1
                else:
                    kept_count += 1
            elif content.strip() == '' or content == '\n':
                kept_count += 1
            else:
                # Check if we missed any
                print(f"WARNING: Untranslated text: {repr(content[:80])}")
                kept_count += 1

print(f"Translated: {translated_count}, Kept: {kept_count}")

with open('_art37_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, ensure_ascii=False, indent=2)

print("Saved _art37_trans.json")
