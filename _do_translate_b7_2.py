"""Translate _art_b7_2_orig.json CN->VI"""
import sys, json, re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art_b7_2_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation mapping
T = {}
T['小白必看！彻底终结 OpenClaw 安装难的问题 🦞'] = 'Người mới phải xem! Giải quyết triệt để vấn đề cài đặt OpenClaw khó khăn 🦞'
T['🔗 原文链接： '] = '🔗 Link bài gốc: '
T['原创 贾克斯的平行世界 贾克斯的平行世界 贾克斯的平行世界'] = 'Nguyên tác Thế giới song song của Jax Thế giới song song của Jax Thế giới song song của Jax'
T['2026年3月8日 14:39  上海'] = 'Ngày 8 tháng 3 năm 2026 14:39 Thượng Hải'
T['贾克斯的平行世界'] = 'Thế giới song song của Jax'
T['读完需要'] = 'Đọc hết cần'
T['5分钟'] = '5 phút'
T['速读仅需 2 分钟'] = 'Đọc nhanh chỉ cần 2 phút'
T['OpenClaw 本身安装并不复杂,但是由于各个操作系统上存在差异，导致很多 Windows 系统的用户在安装时候出现了各种各样的问题。'] = 'Bản thân việc cài đặt OpenClaw không phức tạp, nhưng do sự khác biệt giữa các hệ điều hành, nhiều người dùng Windows đã gặp phải đủ loại vấn đề khi cài đặt.'
T['我所创建的群聊中，因为 Windows /Mac 系统安装异常碰到各种各样问题的人，简直是数不胜数，惨不忍睹。'] = 'Trong nhóm chat mà tôi tạo, số người gặp đủ loại vấn đề do lỗi cài đặt trên hệ thống Windows/Mac thực sự là không đếm xuể, thảm hại vô cùng.'
T['今天我们彻底把这个问题给终结掉：'] = 'Hôm nay chúng ta sẽ giải quyết triệt để vấn đề này:'
T['第一：不再需要让用户输入任何命令！'] = 'Thứ nhất: Không cần người dùng nhập bất kỳ lệnh nào nữa!'
T['而是直接采用开源的自动化安装工具，通过鼠标点击就能一键安装 OpenClaw！Mac 和 Windows 实测下来准确率可以高达 80% 直接做到一键安装。'] = 'Mà sử dụng trực tiếp công cụ cài đặt tự động mã nguồn mở, chỉ cần click chuột là có thể cài đặt OpenClaw một chạm! Thực tế kiểm tra trên Mac và Windows, tỷ lệ thành công có thể lên đến 80% cài đặt một chạm.'
T['第二：如果因为系统差异，你在使用自动化工具安装的过程中，也出现了异常，不要慌！'] = 'Thứ hai: Nếu do sự khác biệt hệ thống, bạn gặp lỗi trong quá trình sử dụng công cụ cài đặt tự động, đừng hoảng!'
T['这里把我调试了一下午的系统提示词分享给你，把这个系统提示词，直接丢给 AI，AI 会一步步引导你选择你想使用的小龙虾模型，以及是否需要卸载重装，并且碰到任何异常问题时，全部自动化进行处理。相信 AI 的力量！'] = 'Ở đây tôi chia sẻ cho bạn prompt hệ thống mà tôi đã debug cả buổi chiều, hãy đưa prompt hệ thống này trực tiếp cho AI, AI sẽ hướng dẫn bạn từng bước chọn mô hình tôm hùm mà bạn muốn sử dụng, cũng như có cần gỡ cài đặt và cài lại không, và khi gặp bất kỳ vấn đề bất thường nào, tất cả đều được xử lý tự động. Hãy tin vào sức mạnh của AI!'
T['两套组合拳打下来，保证你的安装成功率高达 99.99 %'] = 'Hai bộ combo đánh xuống, đảm bảo tỷ lệ cài đặt thành công của bạn lên đến 99,99%'
T['结合一键部署的自动化能力以及 AI 驱动安装 OpenClaw 的能力，说是现阶段业内首创，没毛病。'] = 'Kết hợp khả năng tự động hóa triển khai một chạm và khả năng AI điều khiển cài đặt OpenClaw, nói là đầu tiên trong ngành ở giai đoạn hiện tại, không sai.'
T['接下来，我们按照顺序一个一个来。'] = 'Tiếp theo, chúng ta sẽ đi theo thứ tự từng bước một.'
T['安装自动化部署工具/'] = 'Cài đặt công cụ triển khai tự động/'
T['Cherry Studio 是一款国产开源的 AI 助手平台，集成了多模型对话、知识库管理等一系列功能。'] = 'Cherry Studio là một nền tảng trợ lý AI mã nguồn mở trong nước, tích hợp hàng loạt tính năng như đối thoại đa mô hình, quản lý kho tri thức và nhiều hơn nữa.'
T['由于 Cherry Studio 是开源工具，所以你不需要担心在使用这个工具时的隐私泄露等问题。'] = 'Vì Cherry Studio là công cụ mã nguồn mở, nên bạn không cần lo lắng về vấn đề rò rỉ quyền riêng tư khi sử dụng công cụ này.'
T['访问： '] = 'Truy cập: '
T['我们直接选择适合自己系统的版本进行安装，安装完成后页面效果如下。'] = 'Chúng ta trực tiếp chọn phiên bản phù hợp với hệ thống của mình để cài đặt, sau khi cài đặt xong giao diện sẽ như sau.'
T['此时我们点击点击右上角的设置按钮，配置对应的模型 API KEY'] = 'Lúc này chúng ta nhấp vào nút cài đặt ở góc trên bên phải, cấu hình API KEY của mô hình tương ứng'
T['关于什么是模型的 API KEY，以及如何购买 API KEY，可以参考之前的这篇文章： '] = 'Về API KEY của mô hình là gì, cũng như cách mua API KEY, bạn có thể tham khảo bài viết trước đây: '
T['OpenClaw 保姆级教程：你要知道的都在这里了！'] = 'Hướng dẫn chi tiết OpenClaw: Tất cả những gì bạn cần biết đều ở đây!'
T['这篇文章详细列出了国内模型的购买方式，以及什么是 API KEY，如何获取 API KEY，所以这里就不赘述了。'] = 'Bài viết đó đã liệt kê chi tiết cách mua mô hình trong nước, API KEY là gì, cách lấy API KEY, nên ở đây sẽ không nhắc lại nữa.'
T['上面我们配置完 API KEY 后，直接点击下面截图的 + 号'] = 'Sau khi cấu hình xong API KEY ở trên, trực tiếp nhấp vào dấu + trong ảnh chụp bên dưới'
T['此时我们直接点击 OpenClaw 就会开始引导进入后续的自动化安装流程。'] = 'Lúc này chúng ta trực tiếp nhấp vào OpenClaw sẽ bắt đầu hướng dẫn vào quy trình cài đặt tự động tiếp theo.'
T['我们直接点击下面的安装 OpenClaw，然后全程跟着引导进行点击执行即可'] = 'Chúng ta trực tiếp nhấp vào Cài đặt OpenClaw bên dưới, sau đó làm theo hướng dẫn nhấp thực hiện trong toàn bộ quá trình'
T['安装过程会显示对应的安装进度'] = 'Quá trình cài đặt sẽ hiển thị tiến trình cài đặt tương ứng'
T['安装完成后，会提示你选择你要使用的模型，还记得最开始我们在设置界面填写过模型的 Key 吗，此处直接下拉框选择对应的模型即可，然后点击启动。'] = 'Sau khi cài đặt xong, sẽ nhắc bạn chọn mô hình muốn sử dụng, còn nhớ lúc đầu chúng ta đã điền Key của mô hình trong giao diện cài đặt không, ở đây trực tiếp chọn mô hình tương ứng từ danh sách thả xuống, sau đó nhấp Khởi động.'
T['接下来就会看到对应的启动成功页面'] = 'Tiếp theo sẽ thấy trang khởi động thành công tương ứng'
T['以及对应的 OpenClaw 的控制台页面'] = 'Và trang bảng điều khiển OpenClaw tương ứng'
T['恭喜你，这个时候就安装完成了，Mac 和 Windows 的安装步骤都类似，中间需要人工下载其他依赖的时候，我们直接按照程序的安装引导进行安装即可。'] = 'Xin chúc mừng, lúc này đã cài đặt xong, các bước cài đặt trên Mac và Windows đều tương tự, khi cần tải thủ công các dependency khác ở giữa, chúng ta chỉ cần làm theo hướng dẫn cài đặt của chương trình.'
T['但是，我说过，Cherry Studio 的自动部署，并不能解决所有系统的安装问题，大家可以先使用上面的安装步骤进行安装，如果没有任何异常，恭喜你。'] = 'Tuy nhiên, như tôi đã nói, việc triển khai tự động của Cherry Studio không thể giải quyết tất cả vấn đề cài đặt trên mọi hệ thống, mọi người có thể thử cài đặt theo các bước ở trên trước, nếu không có lỗi gì, xin chúc mừng bạn.'
T['但是如果安装过程中有异常，不要急，我说了，剩下 20% 碰到安装问题的用户，这篇文章也会通通给解决掉的，那就是！'] = 'Nhưng nếu có lỗi trong quá trình cài đặt, đừng vội, tôi đã nói, 20% người dùng còn lại gặp vấn đề cài đặt, bài viết này cũng sẽ giải quyết hết, đó chính là!'
T['上黑科技，上 AI ！'] = 'Dùng công nghệ đen, dùng AI!'
T['AI 来驱动安装 OpenClaw '] = 'AI điều khiển cài đặt OpenClaw '
T['我们直接点击左上角添加助手，这里选择添加 Agent'] = 'Chúng ta trực tiếp nhấp vào Thêm trợ lý ở góc trên bên trái, ở đây chọn thêm Agent'
T['这里选择我们前面在 Cherry Studio 设置中已经填写好的模型，以及权限模型必须给放开到\u201c全自动模式\u201d，这样 AI 会自驱解决安装过程中的所有问题。'] = 'Ở đây chọn mô hình mà chúng ta đã điền trước đó trong cài đặt Cherry Studio, và quyền hạn mô hình phải được mở đến \u201cchế độ tự động hoàn toàn\u201d, như vậy AI sẽ tự chủ giải quyết tất cả vấn đề trong quá trình cài đặt.'
T['新建完成后，我们直接把自己的系统提示词发给该 AI Agent'] = 'Sau khi tạo mới xong, chúng ta trực tiếp gửi prompt hệ thống của mình cho AI Agent đó'
T['然后模型就会问你，你要使用哪一款模型来驱动 OpenClaw，因为前面我选择的智谱来自动安装的，所以这里我选择基于阿里百炼进行验证。'] = 'Sau đó mô hình sẽ hỏi bạn muốn sử dụng mô hình nào để điều khiển OpenClaw, vì trước đó tôi đã chọn Zhipu để cài đặt tự động, nên ở đây tôi chọn xác minh dựa trên Alibaba Bailian.'
T['接下来AI 检测到我本机已经安装过 OpenClaw，所以提示我是否要卸载重装！我选择是，卸载重装！'] = 'Tiếp theo AI phát hiện máy tôi đã cài OpenClaw trước đó, nên nhắc tôi có muốn gỡ cài đặt và cài lại không! Tôi chọn có, gỡ cài đặt và cài lại!'
T['如果你本机前面用自动化安装失败了，那么这里可能也会有残留的 OpenClaw 文件在你本地，所以你也直接选择卸载重装即可！'] = 'Nếu trước đó máy bạn cài đặt tự động thất bại, thì ở đây có thể vẫn còn tệp OpenClaw tồn đọng trên máy, nên bạn cũng trực tiếp chọn gỡ cài đặt và cài lại!'
T['如果你是首次安装，AI 是不会提示你是否要卸载重装的，而是直接给你进行自动安装了。'] = 'Nếu bạn cài đặt lần đầu, AI sẽ không nhắc bạn có muốn gỡ cài đặt và cài lại không, mà trực tiếp tiến hành cài đặt tự động cho bạn.'
T['接下来 AI 就会进入自驱安装的过程了，遇到的所有问题他会自行进行解决。'] = 'Tiếp theo AI sẽ bắt đầu quá trình cài đặt tự chủ, mọi vấn đề gặp phải AI sẽ tự giải quyết.'
T['这里安装完成后，会提示让你输入模型的 API KEY，直接发给他即可。'] = 'Sau khi cài đặt xong ở đây, sẽ nhắc bạn nhập API KEY của mô hình, trực tiếp gửi cho nó là được.'
T['然后 AI 开始再次进入自动配置 OpenClaw 的阶段'] = 'Sau đó AI bắt đầu bước vào giai đoạn tự động cấu hình OpenClaw lần nữa'
T['这里可以看到 AI 已经在启动 OpenClaw 的网关服务了'] = 'Ở đây có thể thấy AI đã đang khởi động dịch vụ gateway của OpenClaw'
T['恭喜，OpenClaw 安装配置完成！接下来我们直接在浏览器打开该访问地址，即可开始使用 OpenClaw ！'] = 'Xin chúc mừng, cài đặt cấu hình OpenClaw hoàn tất! Tiếp theo chúng ta trực tiếp mở địa chỉ truy cập đó trong trình duyệt, là có thể bắt đầu sử dụng OpenClaw!'
T['上面我们演示了如何通过 AI 来驱动部署 OpenClaw，这种场景，非常适合大家采用自动部署脚本，依然碰到问题的情况。'] = 'Ở trên chúng ta đã demo cách sử dụng AI để điều khiển triển khai OpenClaw, tình huống này rất phù hợp khi mọi người đã sử dụng script triển khai tự động mà vẫn gặp vấn đề.'
T['而上述流程中，AI 之所以可以一整套流程一气呵成，先问你要使用什么模型来驱动 OpenClaw，再问你的 API Key 是什么，最后帮你配置并启动 OpenClaw，就是因为最开始我们丢给他的第一套系统提示词。'] = 'Trong quy trình trên, lý do AI có thể thực hiện trọn vẹn cả một quy trình liền mạch, trước tiên hỏi bạn muốn dùng mô hình nào để điều khiển OpenClaw, sau đó hỏi API Key của bạn là gì, cuối cùng giúp bạn cấu hình và khởi động OpenClaw, chính là nhờ bộ prompt hệ thống đầu tiên mà chúng ta đã đưa cho nó.'
T['AI 提示词 '] = 'Prompt AI '
T['下面就是该提示词的详细信息，大家直接按照上述流程拷贝到你的 Agent 里面，让 AI 自动驱动安装部署即可！'] = 'Dưới đây là thông tin chi tiết của prompt đó, mọi người trực tiếp copy vào Agent của mình theo quy trình trên, để AI tự động điều khiển cài đặt triển khai!'
T['写到这里，感觉 Cherry Studio 应该打钱才对，但是讲真，本文纯分享，无任何广告！'] = 'Viết đến đây, cảm giác Cherry Studio nên trả tiền mới đúng, nhưng nói thật, bài viết này thuần chia sẻ, không có bất kỳ quảng cáo nào!'
T['AI 时代已经到来，但是没想到今年竟然是龙虾年！'] = 'Thời đại AI đã đến, nhưng không ngờ năm nay lại là năm tôm hùm!'
T['大家抓紧按照上述流程部署好小龙虾，接下来会继续更新关于小龙虾更多的实战技巧！'] = 'Mọi người nhanh chóng triển khai tôm hùm theo quy trình trên, tiếp theo sẽ tiếp tục cập nhật thêm nhiều kỹ thuật thực chiến về tôm hùm!'
T['部署好小龙虾只是第一步，如何真正用好小龙虾！用爽小龙虾！让小龙虾真正的为你服务！这才是王道！'] = 'Triển khai tôm hùm chỉ là bước đầu tiên, làm thế nào để thực sự dùng tốt tôm hùm! Dùng sướng tôm hùm! Để tôm hùm thực sự phục vụ bạn! Đó mới là vương đạo!'
T['为什么本文说可以解决 99.99% 的部署问题，而不是 100% ，因为这核心取决于 AI Agent 模型的上限。'] = 'Tại sao bài viết nói có thể giải quyết 99,99% vấn đề triển khai, chứ không phải 100%, vì điều cốt lõi phụ thuộc vào giới hạn trên của mô hình AI Agent.'
T['如果遇到非常非常复杂的问题，其实只要你配置的 AI 模型能力足够强，AI 也是可以解决的，但是这需要你不断的和 AI 会话进行调试才行。'] = 'Nếu gặp vấn đề rất rất phức tạp, thực ra chỉ cần mô hình AI bạn cấu hình đủ mạnh, AI cũng có thể giải quyết, nhưng điều này cần bạn liên tục hội thoại với AI để debug.'
T['并且，大家后续使用龙虾遇到任何问题，也可以在上述的 AI Agent 窗口中，直接告诉你的 Agent，让他帮你修复对应的问题，不单单是帮你部署，还能帮你更好的用好小龙虾。'] = 'Và sau này mọi người sử dụng tôm hùm gặp bất kỳ vấn đề gì, cũng có thể trong cửa sổ AI Agent ở trên, trực tiếp nói với Agent của bạn, để nó giúp bạn sửa vấn đề tương ứng, không chỉ giúp bạn triển khai, mà còn giúp bạn dùng tốt tôm hùm hơn.'
T['上述玩龙虾内容有任何疑问，也欢迎进群交流。'] = 'Nếu có bất kỳ thắc mắc nào về nội dung chơi tôm hùm ở trên, cũng hoan nghênh vào nhóm trao đổi.'
T['欢迎日常交流'] = 'Hoan nghênh trao đổi hàng ngày'
T['AI 时代，单打独斗不如抱团成长， 欢迎大家加微信互相交流心得。 '] = 'Thời đại AI, chiến đấu một mình không bằng cùng nhau phát triển, hoan nghênh mọi người kết bạn WeChat trao đổi kinh nghiệm. '
T['👉 想要进群的朋友，扫码时备注 \u201cAI实验群\u201d，看到消息后会第一时间拉你进群。'] = '👉 Bạn nào muốn vào nhóm, khi quét mã hãy ghi chú \u201cNhóm thí nghiệm AI\u201d, sau khi thấy tin nhắn sẽ kéo bạn vào nhóm ngay.'
T['群定位： '] = 'Định vị nhóm: '
T['AI工具提效/实战经验互助'] = 'Nâng cao hiệu suất công cụ AI / Hỗ trợ kinh nghiệm thực chiến'
T['群规则： '] = 'Quy tắc nhóm: '
T['不水群、不广告、干货优先'] = 'Không spam, không quảng cáo, ưu tiên nội dung chất lượng'
T['好文章值得被更多人看见！既然看到这里了，随手点个赞👍和关注，并转发给更多的朋友吧！感谢。'] = 'Bài viết hay đáng được nhiều người thấy hơn! Đã đọc đến đây rồi, tiện tay bấm like 👍 và theo dõi, rồi chia sẻ cho nhiều bạn bè hơn nhé! Cảm ơn.'
T['> 作者：贾克斯的平行世界、微信：x_h886688'] = '> Tác giả: Thế giới song song của Jax, WeChat: x_h886688'

# Apply translations
translated_count = 0
kept_count = 0
warnings = []

for block in data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run':
            content = el['content']
            if content in T:
                el['content'] = T[content]
                translated_count += 1
            else:
                if re.match(r'^https?://', content) or content.strip() in ['/', '/ ']:
                    kept_count += 1
                else:
                    has_chinese = bool(re.search(r'[\u4e00-\u9fff]', content))
                    if has_chinese:
                        warnings.append(f'WARN: untranslated: {content[:80]}')
                    else:
                        kept_count += 1

# Add spaces between adjacent Vietnamese text_runs
for block in data['blocks']:
    elements = block['elements']
    for i in range(len(elements) - 1):
        el = elements[i]
        next_el = elements[i + 1]
        if el['type'] == 'text_run' and next_el['type'] == 'text_run':
            if el['content'] and next_el['content']:
                if not el['content'].endswith(' ') and not next_el['content'].startswith(' '):
                    if not next_el['content'].startswith('http') and not next_el['content'].startswith('/'):
                        el['content'] = el['content'] + ' '

# Update title
data['title'] = 'Người mới phải xem! Giải quyết triệt để vấn đề cài đặt OpenClaw khó khăn 🦞'

with open('_art_b7_2_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Translated: {translated_count} text_runs')
print(f'Kept as-is: {kept_count} text_runs')
print(f'Total blocks: {len(data["blocks"])}')
for w in warnings:
    print(w)
print('Saved to _art_b7_2_trans.json')
