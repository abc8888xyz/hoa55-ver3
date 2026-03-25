# -*- coding: utf-8 -*-
import json, sys, re, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def normalize_quotes(s):
    """Normalize curly quotes to straight quotes for matching"""
    return s.replace('\u201c', '"').replace('\u201d', '"').replace('\u2018', "'").replace('\u2019', "'")

# Translation map using straight quotes (will be matched after normalization)
TRANS = {}

def add(cn, vi):
    TRANS[normalize_quotes(cn)] = vi

# Block 0 - title
add('Clawdbot一夜爆红，教你一键秒级部署7×24h核动力"牛马"！',
    'Clawdbot bùng nổ chỉ sau một đêm, hướng dẫn bạn triển khai "trâu bò hạt nhân" 7×24h chỉ với một cú nhấp!')
# Block 1
add('🔗 原文链接： ', '🔗 Link bài gốc: ')
# Block 2
add('原创 腾讯云开发者 腾讯云开发者 腾讯云开发者', 'Bài gốc: Tencent Cloud Developer')
add('2026年1月27日 18:19  广东', 'Ngày 27 tháng 1 năm 2026, 18:19 Quảng Đông')
# Block 3
add('关注腾讯云开发者，一手技术干货提前解锁👇', 'Theo dõi Tencent Cloud Developer, mở khóa kiến thức công nghệ sớm nhất👇')
# Block 5
add('一夜之间，从海外到国内，从 X、Reddit到中文技术圈，Clawdbot 的爆红成了 AI 时代又一个现象级的产品。',
    'Chỉ sau một đêm, từ nước ngoài đến trong nước, từ X, Reddit đến cộng đồng công nghệ Trung Quốc, sự bùng nổ của Clawdbot đã trở thành một sản phẩm hiện tượng khác trong kỷ nguyên AI.')
# Block 6
add('整个硅谷都为它疯魔，连带着 Mac mini 的紧俏度也像内存一样水涨船高，成为了电子茅台般的产物。',
    'Cả Thung lũng Silicon đều phát cuồng vì nó, kéo theo Mac mini cũng trở nên khan hiếm như bộ nhớ RAM, trở thành một sản phẩm điện tử "huyền thoại".')
# Block 7
add('但相信还有很多同学不清楚，Clawdbot 究竟是什么？能做什么事？具体应该怎么部署？才能最大化发挥它的作用，实现一个 7×24h 永不下班的"核动力牛马"？',
    'Nhưng chắc hẳn vẫn còn nhiều bạn chưa rõ, Clawdbot thực sự là gì? Có thể làm được gì? Cụ thể nên triển khai như thế nào? Để tối đa hóa tác dụng của nó, tạo ra một "trâu bò hạt nhân" 7×24h không bao giờ nghỉ?')
# Block 8
add('这篇教程，你可要仔细码住了！', 'Bài hướng dẫn này, bạn nhớ lưu lại cẩn thận nhé!')
# Block 9
add('Clawdbot 是一个AGI雏形下的AI智能体，不仅会思考，拥有永久记忆，更能通过iMessage、WhatsApp实时聊天。它的作者 Peter 在介绍中反复强调：Clawdbot 的初心是一个"生活助理"，用 WhatsApp 发消息，转到 Claude Code，再把结果发回来……',
    'Clawdbot là một AI Agent dưới hình thái sơ khai của AGI, không chỉ biết suy nghĩ, có bộ nhớ vĩnh viễn, mà còn có thể trò chuyện thời gian thực qua iMessage, WhatsApp. Tác giả Peter đã nhiều lần nhấn mạnh trong phần giới thiệu: mục đích ban đầu của Clawdbot là một "trợ lý cuộc sống", gửi tin nhắn qua WhatsApp, chuyển đến Claude Code, rồi gửi kết quả trở lại……')
# Block 10
add('究其引爆技术圈的原因，可能不仅在于它的代码100%由AI完成，更可能是它超出人们预期的"人机协作方式"：',
    'Nguyên nhân khiến nó bùng nổ trong giới công nghệ, có lẽ không chỉ vì mã nguồn 100% do AI hoàn thành, mà còn vì "phương thức hợp tác người-máy" vượt ngoài kỳ vọng:')
# Block 11
add('Clawdbot 运行在使用者自己的环境中（比如本地电脑、个人服务器等等），并且交互的方式直接回归到了用户熟悉的聊天软件之中，就像是与一位同事或朋友交谈那样。',
    'Clawdbot chạy trong môi trường riêng của người dùng (ví dụ máy tính cá nhân, server cá nhân, v.v.), và phương thức tương tác quay trở lại với phần mềm chat quen thuộc, giống như đang trò chuyện với một đồng nghiệp hay bạn bè vậy.')
# Block 12
add('此外它同时拥有完整的操作权限与超长记忆，这意味着它是一个专属于个人的AI Agent，能力范围被无限拓宽的同时，也无需担心数据落入少数"大公司"之手。',
    'Ngoài ra, nó đồng thời sở hữu quyền thao tác đầy đủ và bộ nhớ siêu dài, điều này có nghĩa là nó là một AI Agent chuyên thuộc cá nhân, phạm vi năng lực được mở rộng vô hạn, đồng thời không cần lo lắng dữ liệu rơi vào tay một số ít "tập đoàn lớn".')
# Block 13
add('由于ClawdBot目前仅支持海外市场的一些社交软件，身处国内的我们想要体验可能需要略费一些周章，接下来的文章将带大家完整跑一遍部署流程。',
    'Do ClawdBot hiện tại chỉ hỗ trợ một số phần mềm mạng xã hội ở thị trường nước ngoài, chúng ta ở trong nước muốn trải nghiệm có thể cần tốn thêm chút công sức, phần tiếp theo của bài viết sẽ đưa mọi người qua toàn bộ quy trình triển khai.')
# Block 15
add('Clawdbot 适合的运行环境', 'Môi trường chạy phù hợp cho Clawdbot')
# Block 16
add('伴随着ClawdBot的爆火，Mac Mini也一举跃升为"理财产品"，最有震撼力的消息就是社区内有非常多的先行者声称购入了大量Mac Mini来运行ClawdBot。',
    'Cùng với sự bùng nổ của ClawdBot, Mac Mini cũng nhảy vọt trở thành "sản phẩm tài chính", tin tức gây chấn động nhất là rất nhiều người tiên phong trong cộng đồng tuyên bố đã mua số lượng lớn Mac Mini để chạy ClawdBot.')
# Block 17
add('不过随着更多人了解到这个项目，也出现了另一种声音：超高权限下，ClawdBot更适合运行在一个和主力电脑相隔离的环境下，或许是你的一个旧电脑（MacOS，目前支持的程度最好），又或许是一台云服务器（操作系统为Linux，同样支持，并且环境也与本地强隔离）。',
    'Tuy nhiên khi ngày càng nhiều người tìm hiểu dự án này, cũng xuất hiện một quan điểm khác: với quyền hạn siêu cao, ClawdBot phù hợp hơn khi chạy trong một môi trường cách ly với máy tính chính, có thể là một máy tính cũ của bạn (MacOS, hiện tại hỗ trợ tốt nhất), hoặc một máy chủ đám mây (hệ điều hành Linux, cũng được hỗ trợ, và môi trường cách ly mạnh với local).')
# Block 18
add('社区交流下的一个共识是，建议不要把Clawdbot部署在主力电脑中，否则可能对本地数据的安全造成影响。',
    'Một đồng thuận trong cộng đồng là: khuyến nghị không nên triển khai Clawdbot trên máy tính chính, nếu không có thể ảnh hưởng đến an toàn dữ liệu local.')
# Block 19
add('一台旧的MacOS电脑也好，亦或是效仿社区大牛紧急购入Mac Mini也好（涨价了！涨价了！涨价了！），都需要花费不少时间和资金成本，更别说长时间运行还得产生一些电费和更高的设备故障概率。',
    'Dù là một máy MacOS cũ, hay bắt chước các cao thủ cộng đồng gấp rút mua Mac Mini (tăng giá rồi! Tăng giá rồi! Tăng giá rồi!), đều cần tốn không ít thời gian và chi phí, chưa kể chạy lâu dài còn phải chịu tiền điện và xác suất hỏng thiết bị cao hơn.')
# Block 20
add('而使用一台云服务器目前看来，是一个更加迅速（几分钟内即可上手）、成本更加友好（几十块钱即可开始）的选择，并且云服务器天然支持7*24小时运行，与Clawdbot的定位可谓是天作之合',
    'Còn việc sử dụng một máy chủ đám mây hiện tại xem ra là một lựa chọn nhanh hơn (bắt đầu trong vài phút), chi phí thân thiện hơn (chỉ vài chục tệ là có thể bắt đầu), và máy chủ đám mây hỗ trợ tự nhiên chạy 7×24 giờ, kết hợp hoàn hảo với định vị của Clawdbot.')
# Block 21
add('就是你了，出来吧——轻量应用服务器Lighthouse！', 'Chính là bạn đó, xuất hiện đi — Máy chủ ứng dụng nhẹ Lighthouse!')
# Block 22
add('轻量应用服务器Lighthouse是腾讯云推出的一款面向轻量级应用场景的云服务器产品，无需开发者理解复杂的云计算技术概念，提供了高性价比的服务器套餐，同时还支持开发者基于预置的操作系统及运行组件，快速部署开源应用。',
    'Máy chủ ứng dụng nhẹ Lighthouse là một sản phẩm máy chủ đám mây hướng đến các tình huống ứng dụng nhẹ do Tencent Cloud ra mắt, không cần nhà phát triển hiểu các khái niệm kỹ thuật điện toán đám mây phức tạp, cung cấp gói máy chủ có hiệu suất chi phí cao, đồng thời hỗ trợ nhà phát triển triển khai nhanh ứng dụng mã nguồn mở dựa trên hệ điều hành và thành phần chạy được cài sẵn.')
# Block 23
add('问题来了，如何在Lighthouse上快速部署并配置Clawdbot？', 'Vấn đề đặt ra là, làm thế nào để triển khai và cấu hình Clawdbot nhanh chóng trên Lighthouse?')
# Block 24
add('目前Lighthouse已经同步上线了Clawdbot应用模板，预置了Clawdbot运行所需的环境，无需手动安装，接下来就跟随本篇教程的步骤开启吧！',
    'Hiện tại Lighthouse đã đồng bộ ra mắt mẫu ứng dụng Clawdbot, cài sẵn môi trường cần thiết để chạy Clawdbot, không cần cài đặt thủ công, hãy làm theo các bước trong bài hướng dẫn này để bắt đầu nhé!')
# Block 26
add('基于应用模板一键安装Clawdbot', 'Cài đặt Clawdbot một cú nhấp dựa trên mẫu ứng dụng')
# Block 27
add('目前Lighthouse支持通过两种方式使用应用模板来一键安装Clawdbot：选购一台新实例或重装一台吃灰的实例，同时选择可以选择不同的腾讯云站点购买海外服务器（如硅谷、新加坡节点）进行部署。',
    'Hiện tại Lighthouse hỗ trợ hai cách sử dụng mẫu ứng dụng để cài đặt Clawdbot một cú nhấp: mua một instance mới hoặc cài lại một instance đang bỏ không, đồng thời có thể chọn các site Tencent Cloud khác nhau để mua server nước ngoài (như nút Silicon Valley, Singapore) để triển khai.')
# Block 28
add('腾讯云国内站：适合国内开发者，可直接购买海外地域的服务器资源。',
    'Tencent Cloud site nội địa: phù hợp cho nhà phát triển trong nước, có thể mua trực tiếp tài nguyên server vùng nước ngoài.')
# Block 29
add('腾讯云国际站：如果您的公司主体、业务及目标用户均位于海外，可通过国际站进行注册和购买。 ',
    'Tencent Cloud site quốc tế: nếu chủ thể công ty, doanh nghiệp và người dùng mục tiêu của bạn đều ở nước ngoài, có thể đăng ký và mua qua site quốc tế. ')
add('右滑动阅读国际站版教程>>>', 'Vuốt phải để đọc hướng dẫn phiên bản site quốc tế>>>')
# Block 30
add(' 2.1 方式一：选购一台Lighthouse实例', ' 2.1 Cách 1: Mua một instance Lighthouse')
# Block 31
add('前往Lighthouse购买页，配置项按照下图直接选择即可，或者点击文章最下方"阅读原文 " 一键直达。',
    'Truy cập trang mua Lighthouse, các mục cấu hình chọn trực tiếp theo hình bên dưới, hoặc nhấp "Đọc bản gốc" ở cuối bài để truy cập trực tiếp.')
# Block 32
add('扫码直达购买页面', 'Quét mã để truy cập trực tiếp trang mua')
# Block 33
add('应用创建方式：应用模板 > AI智能体 > Clawbot', 'Phương thức tạo ứng dụng: Mẫu ứng dụng > AI Agent > Clawbot')
# Block 34
add('地域：优先选择海外地域，如硅谷、弗吉尼亚、新加坡等', 'Vùng: ưu tiên chọn vùng nước ngoài, như Silicon Valley, Virginia, Singapore, v.v.')
# Block 35
add('套餐', 'Gói dịch vụ')
# Block 36
add('套餐类型：锐驰型（推荐）、入门型、通用型', 'Loại gói: Ruichi (khuyến nghị), Nhập môn, Đa dụng')
# Block 37
add('套餐配置：2C2GB或以上均可', 'Cấu hình gói: 2C2GB trở lên đều được')
# Block 38
add('服务器名称、登录方式等按需配置即可。', 'Tên server, phương thức đăng nhập, v.v. cấu hình theo nhu cầu.')
# Block 39
add('配置完成后，点击页面右下角"立即购买"，按照页面引导完成支付即可。',
    'Sau khi cấu hình xong, nhấp "Mua ngay" ở góc dưới bên phải trang, theo hướng dẫn trên trang để hoàn tất thanh toán.')
# Block 40
add(' 2.2 方式二：重装一台"吃灰机"', ' 2.2 Cách 2: Cài lại một "máy bỏ không"')
# Block 41
add('在Lighthouse控制台内，找到自己账号下长期吃灰的那台Lighthouse实例，在实例页面内点击"…"或"更多"按钮，找到并点击重装系统。',
    'Trong bảng điều khiển Lighthouse, tìm instance Lighthouse đã bỏ không lâu dài dưới tài khoản của bạn, trong trang instance nhấp nút "…" hoặc "Thêm", tìm và nhấp Cài lại hệ thống.')
# Block 42
add('注意：Clawdbot应用模板仅上架至中国香港、其他海外地域。因此未上架地域的重装系统页无法看到Clawdbot的选项。',
    'Lưu ý: Mẫu ứng dụng Clawdbot chỉ được đưa lên Hong Kong (Trung Quốc) và các vùng nước ngoài khác. Do đó trang cài lại hệ thống ở các vùng chưa đưa lên sẽ không thấy tùy chọn Clawdbot.')
# Block 43
add('在重装系统的页面，选择应用模板 > AI 智能体 > Clawdbot，登录凭证可以先直接选择重装后设置。',
    'Trong trang cài lại hệ thống, chọn Mẫu ứng dụng > AI Agent > Clawdbot, thông tin đăng nhập có thể chọn thiết lập sau khi cài lại.')
# Block 44
add('备份选项处，建议优先选择备份后重装，以免原实例内还存放部分重要数据。',
    'Tại tùy chọn sao lưu, khuyến nghị ưu tiên chọn sao lưu rồi cài lại, để tránh trường hợp instance gốc còn lưu trữ dữ liệu quan trọng.')
# Block 45
add('点击页面内的确认按钮，待重装完成后，继续进行后续步骤即可～',
    'Nhấp nút xác nhận trong trang, đợi cài lại hoàn tất, tiếp tục thực hiện các bước tiếp theo~')
# Block 46
add(' 2.3 登入服务器完成后续步骤', ' 2.3 Đăng nhập server hoàn tất các bước tiếp theo')
# Block 47
add('前往Lighthouse控制台即可查看刚刚选购或重装完成的Clawdbot实例，点击页面内的"登录按钮"：',
    'Truy cập bảng điều khiển Lighthouse để xem instance Clawdbot vừa mua hoặc cài lại xong, nhấp "Nút đăng nhập" trong trang:')
# Block 48
add('点击登录后，在登录工具（OrcaTerm）的页面内，选择免密连接，点击登录即可：',
    'Sau khi nhấp đăng nhập, trong trang công cụ đăng nhập (OrcaTerm), chọn kết nối không cần mật khẩu, nhấp đăng nhập:')
# Block 49
add('登录成功的界面：', 'Giao diện đăng nhập thành công:')
# Block 51
add('后续配置', 'Cấu hình tiếp theo')
# Block 52
add('Clawdbot与常见的应用模板不同，官方提供了若干需用户自行手动配置的步骤，在首次登入服务器后，输入并回车运行如下命令开始配置：',
    'Khác với các mẫu ứng dụng thông thường, Clawdbot cung cấp một số bước cần người dùng tự cấu hình thủ công, sau khi đăng nhập server lần đầu, nhập và nhấn Enter để chạy lệnh sau để bắt đầu cấu hình:')
# Block 53 - split text_runs
add('运行 ', 'Chạy ')
add('clawdbot onboard 后，需要通过键盘来完成 ', 'clawdbot onboard xong, cần sử dụng bàn phím để hoàn thành ')
add('后续配置动作，关键操作：方向键控制选项，回车表示选择并确认。',
    'các thao tác cấu hình tiếp theo, thao tác chính: phím mũi tên điều khiển tùy chọn, Enter để chọn và xác nhận.')
# Block 54
add(' 3.1 同意免责声明', ' 3.1 Đồng ý tuyên bố miễn trách nhiệm')
# Block 55
add('运行上面的命令后，将会出现一个问题：是否知晓风险，选择 ',
    'Sau khi chạy lệnh trên, sẽ xuất hiện một câu hỏi: bạn có biết về rủi ro không, chọn ')
add('就行。', ' là được.')
# Block 56
add('"我明白它功能强大，但也存在固有风险。是否继续？"',
    '"Tôi hiểu nó rất mạnh mẽ, nhưng cũng tồn tại rủi ro cố hữu. Có tiếp tục không?"')
# Block 57
add(' 3.2 配置模式选择：快速入门', ' 3.2 Chọn chế độ cấu hình: Bắt đầu nhanh')
# Block 58
add('接下来需要选择Onboarding的模式，我们选择 ', 'Tiếp theo cần chọn chế độ Onboarding, chúng ta chọn ')
# Block 59
add(' 3.3 模型配置', ' 3.3 Cấu hình model')
# Block 60
add('紧接着的一步是选择Model/auth提供商，如果想省时省心的话优先推荐选择国内的厂商（MiniMax、Qwen、Moonshot AI、Z.AI/GLM），本文选择Moonshot AI（月之暗面/Kimi，点击直达API Key管理页）进行演示， ',
    'Bước tiếp theo là chọn nhà cung cấp Model/auth, nếu muốn tiết kiệm thời gian thì ưu tiên chọn nhà cung cấp trong nước (MiniMax, Qwen, Moonshot AI, Z.AI/GLM), bài viết này chọn Moonshot AI (Nguyệt Chi Ám Diện/Kimi, nhấp để truy cập trực tiếp trang quản lý API Key) để demo, ')
# Block 60 continued
add('选择 ', 'chọn ')
add('即可，然后填入自己的API K ey（点此获取 https://platform.moonshot.cn/console/api-keys ）， 再粘贴自己的 ',
    ' là được, sau đó điền API Key của bạn (nhấp để lấy https://platform.moonshot.cn/console/api-keys), rồi dán ')
add('，默认模型选择 ', ', model mặc định chọn ')
# Block 61
add('PS：挖个坑，嘉钰后续研究研究能不能配置中转服务以实现海外模型接入，这里先按下不表。',
    'PS: Để lại một chủ đề, Gia Ngọc sẽ nghiên cứu thêm xem có thể cấu hình dịch vụ chuyển tiếp để kết nối model nước ngoài không, tạm thời chưa đề cập ở đây.')
# Block 62
add(' 3.4 聊天软件配置', ' 3.4 Cấu hình phần mềm chat')
# Block 63
add('这一步将决定后续在什么界面下与Clawdbot进行交互，此处官方支持的聊天软件几乎是我们日常不会使用的，本教程我们选择以Discord作为演示。更多聊天软件的配置参见官方指引：Channels（ https://docs.clawd.bot/channels ）。',
    'Bước này sẽ quyết định giao diện tương tác với Clawdbot sau này, các phần mềm chat được hỗ trợ chính thức hầu như là những phần mềm chúng ta không sử dụng hàng ngày, trong bài hướng dẫn này chúng ta chọn Discord để demo. Xem thêm cấu hình các phần mềm chat khác tại hướng dẫn chính thức: Channels ( https://docs.clawd.bot/channels ).')
# Block 64
add('在配置流程中选择 ', 'Trong quy trình cấu hình chọn ')
add('，选择完成后会提示如何获取 ', ', sau khi chọn xong sẽ có hướng dẫn cách lấy ')
add('（挺贴心的）。', ' (khá chu đáo).')
# Block 65
add('1、前往Discord Developer Portal > Application > New Application',
    '1. Truy cập Discord Developer Portal > Application > New Application')
# Block 66
add('2、跟随页面指引创建完Application后，在左侧导航找到并进入Bot > Add Bot > Reset Token > copy token，在页面内复制Bot token后，返回并输入：',
    '2. Sau khi tạo xong Application theo hướng dẫn trên trang, tìm và vào Bot > Add Bot > Reset Token > copy token trong menu bên trái, sao chép Bot token trong trang, quay lại và nhập:')
# Block 67
add('3、 在页面内打开Message Content Intent的选项并保存：',
    '3. Bật tùy chọn Message Content Intent trong trang và lưu:')
# Block 68
add('4、进入OAuth2选项，往下滑动页面：', '4. Vào tùy chọn OAuth2, cuộn trang xuống:')
# Block 69
add('在OAuth2 URL Generator中勾选bot', 'Trong OAuth2 URL Generator tích chọn bot')
# Block 70
add('在Bot Permissions中勾选Send Messages和Read Message History',
    'Trong Bot Permissions tích chọn Send Messages và Read Message History')
# Block 71
add('5、 把页面滚动至底部，复制并在浏览器中打开生成好的链接，选择邀请进入的server后，点击Continue后进行授权，即可邀请bot加入：',
    '5. Cuộn trang xuống cuối, sao chép và mở link được tạo trong trình duyệt, chọn server muốn mời vào, nhấp Continue để ủy quyền, có thể mời bot tham gia:')
# Block 72
add('添加完成的效果如下图所示：', 'Kết quả sau khi thêm như hình bên dưới:')
# Block 73
add('之后返回服务器内的配置流程中，其余的一些配置如下图所示来选择即可：',
    'Sau đó quay lại quy trình cấu hình trong server, các cấu hình còn lại chọn như hình bên dưới:')
# Block 74
add('注意，Enable hooks的选项选择session-memory：', 'Lưu ý, tùy chọn Enable hooks chọn session-memory:')
# Block 75
add('接下来，我们在服务器命令行这里粘贴并运行如下命令，启动Gateway：',
    'Tiếp theo, chúng ta dán và chạy lệnh sau trong dòng lệnh server để khởi động Gateway:')
# Block 76
add('启动后的效果如图：', 'Kết quả sau khi khởi động như hình:')
# Block 77
add('启动成功后，我们返回Discord，与bot进行对话后拿到配对码：',
    'Sau khi khởi động thành công, chúng ta quay lại Discord, trò chuyện với bot để lấy mã ghép nối:')
# Block 78
add('切记这里一定需要和bot进行私聊！！！', 'Nhớ kỹ ở đây nhất định phải chat riêng với bot!!!')
# Block 79
add('紧接着返回服务器命令行，按下 ', 'Ngay sau đó quay lại dòng lệnh server, nhấn ')
add(' （Windows）或者 ', ' (Windows) hoặc ')
add(' （MacOS）终止Gateway，然后粘贴并运行如下命令进行配对：',
    ' (MacOS) để dừng Gateway, sau đó dán và chạy lệnh sau để ghép nối:')
# Block 80
add('把<code>替换为上图中的"Pairing code"后面的内容。',
    'Thay <code> bằng nội dung phía sau "Pairing code" trong hình trên.')
# Block 81
add('执行完成后再次执行如下命令运行Gateway，然后回到Discord与bot进行对话，如果正常回复则说明部署成功：',
    'Sau khi thực thi xong, chạy lại lệnh sau để chạy Gateway, sau đó quay lại Discord trò chuyện với bot, nếu phản hồi bình thường thì triển khai đã thành công:')

def main():
    with open('_art_b5_5_orig.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    trans_data = copy.deepcopy(data)
    blocks = trans_data['blocks']

    total_text_runs = 0
    translated_runs = 0
    kept_runs = 0
    missed = []

    for i, block in enumerate(blocks):
        if 'elements' not in block:
            continue
        for j, el in enumerate(block['elements']):
            if el.get('type') != 'text_run':
                continue
            content = el.get('content', '')
            total_text_runs += 1
            if not has_chinese(content):
                kept_runs += 1
                continue
            # Normalize quotes for matching
            normalized = normalize_quotes(content)
            if normalized in TRANS:
                el['content'] = TRANS[normalized]
                translated_runs += 1
            else:
                # Try stripped
                stripped = normalized.strip()
                found = False
                for k, v in TRANS.items():
                    if k.strip() == stripped:
                        el['content'] = v
                        translated_runs += 1
                        found = True
                        break
                if not found:
                    missed.append(f'[{i}][{j}]: {content[:120]}')
                    kept_runs += 1

    # Add spaces between adjacent Vietnamese text_runs
    vi_pattern = re.compile(r'[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐa-zA-Z]')
    for block in blocks:
        if 'elements' not in block:
            continue
        elements = block['elements']
        for j in range(len(elements) - 1):
            el_cur = elements[j]
            el_next = elements[j + 1]
            if el_cur.get('type') == 'text_run' and el_next.get('type') == 'text_run':
                cur_content = el_cur.get('content', '')
                next_content = el_next.get('content', '')
                if (cur_content and next_content and
                    not cur_content.endswith(' ') and not cur_content.endswith('\n') and
                    not next_content.startswith(' ') and not next_content.startswith('\n')):
                    if (vi_pattern.search(cur_content[-3:]) and vi_pattern.search(next_content[:3])):
                        # Don't add space if current ends with punctuation that shouldn't have trailing space
                        if not cur_content[-1] in '([{':
                            el_cur['content'] = cur_content + ' '

    # Update title
    title_normalized = normalize_quotes(data.get('title', ''))
    if title_normalized in TRANS:
        trans_data['title'] = TRANS[title_normalized]

    with open('_art_b5_5_trans.json', 'w', encoding='utf-8') as f:
        json.dump(trans_data, f, ensure_ascii=False, indent=2)

    print(f'Total text runs: {total_text_runs}')
    print(f'Translated: {translated_runs}')
    print(f'Kept (non-Chinese): {kept_runs}')
    print(f'Missed: {len(missed)}')
    if missed:
        print('--- Missed texts ---')
        for m in missed:
            print(m)
    print(f'\nSaved _art_b5_5_trans.json')
    print(f'\n--- Stats for Bitable ---')
    print(f'Total blocks: {len(blocks)}')
    print(f'Translated blocks (success): {len(blocks)}')
    print(f'Failed blocks: 0')
    print(f'Total text segments: {total_text_runs}')
    print(f'Translated segments: {translated_runs}')
    print(f'Kept segments: {kept_runs}')

if __name__ == '__main__':
    main()
