# -*- coding: utf-8 -*-
"""Translate _art_b7_10_orig.json CN->VI and save as _art_b7_10_trans.json"""
import json
import copy
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Translation map: Chinese -> Vietnamese
TRANS = {
    "OpenClaw 保姆级教程：你要知道的都在这里了！": "Hướng dẫn OpenClaw từ A-Z: Tất cả những gì bạn cần biết đều ở đây!",
    "🔗 原文链接： ": "🔗 Link bài gốc: ",
    "原创 贾克斯的平行世界 贾克斯的平行世界 贾克斯的平行世界": "Nguyên tác: Thế Giới Song Song Của Jax",
    "2026年3月2日 06:00  上海": "Ngày 2 tháng 3 năm 2026, 06:00 Thượng Hải",
    "贾克斯的平行世界": "Thế Giới Song Song Của Jax",
    "读完需要": "Đọc hết cần ",
    "2分钟": "2 phút",
    "速读仅需 1 分钟": "Đọc lướt chỉ cần 1 phút",
    "小龙虾是什么？ ": "OpenClaw là gì? ",
    "小龙虾（OpenClaw）是什么，简单来说就是你 24 小时的个人助理。": "OpenClaw là gì? Nói đơn giản, nó là trợ lý cá nhân 24 giờ của bạn.",
    "个人助理这个词大家可能听腻了，太多所谓的助理实际用起来傻不拉几的。但这次小龙虾之所以火遍全球，是因为它真的做到了：": "Có lẽ bạn đã nghe chán từ \"trợ lý cá nhân\" rồi, quá nhiều cái gọi là trợ lý nhưng dùng thực tế thì ngu ngốc hết sức. Nhưng lần này OpenClaw nổi khắp toàn cầu, bởi vì nó thực sự làm được:",
    "1. 能自动打开浏览器，操作所有和网页相关的任务，想象空间很大；": "1. Có thể tự động mở trình duyệt, thao tác mọi tác vụ liên quan đến web, không gian tưởng tượng rất lớn;",
    "2. 能操作你的电脑，安装软件、开发程序、帮你监控任务，都没问题；": "2. Có thể thao tác máy tính của bạn, cài phần mềm, phát triển chương trình, giúp bạn giám sát tác vụ, đều không vấn đề;",
    "3. 能 24 小时不间断运行，你给一个任务，它自己拼命干完等你审核；": "3. Có thể chạy 24 giờ không ngừng nghỉ, bạn giao một tác vụ, nó tự làm hết rồi đợi bạn duyệt;",
    "4. 有向量记忆模块，越用越懂你。": "4. Có module bộ nhớ vector, dùng càng nhiều càng hiểu bạn.",
    "这才是真正的个人助理！": "Đây mới thực sự là trợ lý cá nhân!",
    "如果这篇文章你看完不去进行实践，那你真的亏爆了，小龙虾的能力外人介绍太多次，都不如你实际体验一次。": "Nếu đọc xong bài này mà không thực hành, thì bạn thực sự thiệt thòi lớn. Năng lực của OpenClaw được người khác giới thiệu bao nhiêu lần, cũng không bằng bạn tự trải nghiệm một lần.",
    "本文把我养 OpenClaw 近一个月的经验，以及看到的非常优秀的内容，一股脑全部列出来了。": "Bài viết này tổng hợp tất cả kinh nghiệm gần một tháng sử dụng OpenClaw của mình, cùng những nội dung xuất sắc mà mình tìm được.",
    "你只要按照内容来，保证玩小龙虾手拿把掐，千万别一键三连后收藏夹里吃灰了。": "Bạn chỉ cần làm theo nội dung, đảm bảo chơi OpenClaw thuần thục, đừng có like xong rồi để mốc trong bookmark nhé.",
    "接下来我们开始！": "Bắt đầu thôi!",
    "部署前需要知道的 ": "Những điều cần biết trước khi triển khai ",
    "在部署 OpenClaw 前，你需要先了解两个基本概念：": "Trước khi triển khai OpenClaw, bạn cần hiểu hai khái niệm cơ bản:",
    "1. OpenClaw 是一套可运行的开源软件，你可以把它部署到你的 Windows 上也可以是 Mac 上或者 Linux 上。": "1. OpenClaw là một bộ phần mềm mã nguồn mở có thể chạy được, bạn có thể triển khai trên Windows, Mac hoặc Linux.",
    "这里核心是告诉你 OpenClaw 服务的运行消耗的是你自己电脑的资源，这块是免费的，你只要安装好就可以永久使用。": "Điều cốt lõi ở đây là: OpenClaw chạy trên tài nguyên máy tính của chính bạn, phần này miễn phí, chỉ cần cài xong là dùng vĩnh viễn.",
    "2. OpenClaw 本身是开源免费的，但是 OpenClaw 的使用需要对接模型的 API（接口）才行。": "2. Bản thân OpenClaw là mã nguồn mở miễn phí, nhưng để sử dụng OpenClaw cần kết nối với API (giao diện) của model.",
    "打个比方，你家厨房装修完可以永久使用，但要想持续做出精美菜肴，必须要有厨师。": "Ví dụ như nhà bếp của bạn trang trí xong có thể dùng vĩnh viễn, nhưng muốn liên tục nấu ra món ngon thì phải có đầu bếp.",
    "在这里模型就是你的厨师，而雇佣一个顶级厨师则是需要收费的。": "Ở đây model chính là đầu bếp của bạn, và thuê một đầu bếp hàng đầu thì cần trả phí.",
    "国内主流厂商有：智谱 GLM、阿里通义、月之暗面 Kimi、字节豆包、DeepSeek、Minimax。": "Các nhà cung cấp chính tại Trung Quốc gồm: Zhipu GLM, Alibaba Tongyi, Moonshot Kimi, ByteDance Doubao, DeepSeek, Minimax.",
    "这几家产商的模型每一个都各有特点，价格也各异，并且每个厂商都有提供包月套餐，首月最低的是 7.9 元，所以你可以根据自己情况，自由选择。": "Model của các nhà cung cấp này đều có đặc điểm riêng, giá cả khác nhau, và mỗi nhà cung cấp đều có gói thuê bao tháng, tháng đầu thấp nhất là 7,9 tệ, nên bạn có thể tự do lựa chọn theo tình hình của mình.",
    "模型购买及官方部署文档 ": "Mua model và tài liệu triển khai chính thức ",
    "下面我列出了智谱、Kimi、阿里和字节的模型购买链接，以及对应的官方部署文档。": "Dưới đây mình liệt kê link mua model của Zhipu, Kimi, Alibaba và ByteDance, cùng tài liệu triển khai chính thức tương ứng.",
    "每一个厂商的部署文档中，都详细介绍了如何部署 OpenClaw 以及将 OpenClaw 和自家模型进行对接。": "Tài liệu triển khai của mỗi nhà cung cấp đều hướng dẫn chi tiết cách triển khai OpenClaw và kết nối OpenClaw với model của họ.",
    "（厂商比你更想让你学会 OpenClaw，这样就能持续消费 Token 了": "(Nhà cung cấp còn muốn bạn học OpenClaw hơn cả bạn, vì như vậy bạn sẽ tiêu thụ Token liên tục",
    "其中字节的部署文档中，除了教你如何部署 OpenClaw 以及对接模型外，还额外说明了如何把 OpenClaw 和飞书打通。": "Trong đó tài liệu triển khai của ByteDance, ngoài việc hướng dẫn triển khai OpenClaw và kết nối model, còn giải thích thêm cách tích hợp OpenClaw với Feishu (Lark).",
    "所以就算你不打算购买字节的模型套餐，这里对接飞书机器人的文档，你后续需要时也可以看下。": "Nên kể cả bạn không định mua gói model của ByteDance, tài liệu tích hợp bot Feishu (Lark) ở đây, khi cần sau này bạn cũng có thể tham khảo.",
    "智谱 GLM5.0 是现阶段国内模型表现较为优秀的，如果你想从事复杂任务，建议优先选择智谱，包月价格 49 元，购买链接： ": "Zhipu GLM5.0 là model có hiệu suất khá tốt ở Trung Quốc hiện tại, nếu bạn muốn làm tác vụ phức tạp, khuyến nghị ưu tiên chọn Zhipu, giá thuê bao tháng 49 tệ, link mua: ",
    "OpenClaw部署以及如何对接智谱模型文档：": "Triển khai OpenClaw và tài liệu kết nối model Zhipu:",
    "Kimi 的首月价格也是 49 元，购买链接：": "Giá tháng đầu của Kimi cũng là 49 tệ, link mua:",
    "OpenClaw部署以及如何对接Kimi模型文档：": "Triển khai OpenClaw và tài liệu kết nối model Kimi:",
    "如果你只是想轻量尝试，建议阿里的首月 7.9 元套餐。记住是首月 7.9，续费不是这个价格，记得关闭自动续费，购买链接：": "Nếu bạn chỉ muốn dùng thử nhẹ nhàng, khuyến nghị gói 7,9 tệ tháng đầu của Alibaba. Nhớ là chỉ tháng đầu 7,9, gia hạn không phải giá này, nhớ tắt tự động gia hạn, link mua:",
    "OpenClaw部署以及如何对接阿里模型文档：": "Triển khai OpenClaw và tài liệu kết nối model Alibaba:",
    "字节的模型套餐是 9.9 元一个月，购买链接：": "Gói model của ByteDance là 9,9 tệ một tháng, link mua:",
    "OpenClaw部署以及如何对接字节模型文档：": "Triển khai OpenClaw và tài liệu kết nối model ByteDance:",
    "看完上面的内容后，这意味着你已经发现了，如果打算用 OpenClaw，这肯定要消费一波了，多多少少的问题，这里大家根据自己的情况自行评估，适当消费。": "Sau khi đọc xong nội dung trên, bạn chắc đã nhận ra, nếu định dùng OpenClaw thì chắc chắn phải chi một khoản, ít hay nhiều tùy, ở đây mọi người tự đánh giá theo tình hình của mình, chi tiêu hợp lý.",
    "非研发人员如何安装 OpenClaw ": "Người không phải lập trình viên cài OpenClaw như thế nào ",
    "如果你不是研发人员，看不懂上面厂商的文档，不要急。": "Nếu bạn không phải lập trình viên, đọc không hiểu tài liệu của nhà cung cấp ở trên, đừng vội.",
    "Mac/Linux 用户直接执行这个命令：": "Người dùng Mac/Linux chạy trực tiếp lệnh này:",
    "Windows 用户直接执行这个命令：": "Người dùng Windows chạy trực tiếp lệnh này:",
    "上述命令执行后会一键把 Nodejs、NVM、OpenClaw 都安装好。": "Sau khi chạy lệnh trên, Nodejs, NVM, OpenClaw sẽ được cài đặt tự động một lần.",
    "但如果一键部署脚本在你的环境上因为缺少依赖执行异常了，不要想着修复脚本，直接采用下面手动安装的方式。 ": "Nhưng nếu script triển khai một bước bị lỗi trên môi trường của bạn do thiếu dependency, đừng cố sửa script, hãy dùng cách cài đặt thủ công bên dưới. ",
    "直接看下面三个链接，我帮你把整个手动安装过程拼接起来了：": "Xem trực tiếp ba link bên dưới, mình đã ghép nối toàn bộ quy trình cài đặt thủ công cho bạn:",
    "安装 Node.js：": "Cài đặt Node.js:",
    "安装 NVM：": "Cài đặt NVM:",
    "安装 OpenClaw（Mac/Linux）：": "Cài đặt OpenClaw (Mac/Linux):",
    "安装 OpenClaw（Windows）：": "Cài đặt OpenClaw (Windows):",
    "上述步骤执行时，你可能会碰到网络问题，配置国内镜像源就可以解决。": "Khi thực hiện các bước trên, bạn có thể gặp vấn đề mạng, cấu hình mirror source nội địa là giải quyết được.",
    "如果你不知道怎么做，没关系，去问你的 AI 助手：豆包、DeepSeek、千问都可以。": "Nếu bạn không biết làm thế nào, không sao, hỏi trợ lý AI của bạn: Doubao, DeepSeek, Qwen đều được.",
    "如果你本地有安装 Agent，比如 Trae、Qoder、Claude Code、OpenCode、Codex，那问题就更简单了。": "Nếu bạn đã cài Agent trên máy, ví dụ Trae, Qoder, Claude Code, OpenCode, Codex, thì vấn đề còn đơn giản hơn.",
    "直接把上面需要安装的内容和文档链接丢给你的 Agent，让它帮你装，它会解决一切问题。": "Trực tiếp đưa nội dung cần cài và link tài liệu ở trên cho Agent của bạn, để nó giúp bạn cài, nó sẽ giải quyết mọi vấn đề.",
    "到了这里，你就已经安装完成了。": "Đến đây, bạn đã cài đặt xong rồi.",
    "学习资源和必备技能 ": "Tài nguyên học tập và kỹ năng cần thiết ",
    "安装完成后只是开始，接下来给你推荐一些学习资源，以及必装的基础 Skill。": "Cài xong mới chỉ là bắt đầu, tiếp theo giới thiệu cho bạn một số tài nguyên học tập và các Skill cơ bản bắt buộc phải cài.",
    "必装 Skill：": "Skill bắt buộc phải cài:",
    "1. self-improvement：让你的小龙虾自我改进，记录错误和学习。": "1. self-improvement: Giúp OpenClaw của bạn tự cải thiện, ghi nhận lỗi và học hỏi.",
    "2. browser：浏览器自动化，网页交互和截图。": "2. browser: Tự động hóa trình duyệt, tương tác web và chụp ảnh màn hình.",
    "3. desktop-control：桌面自动化，鼠标键盘控制。": "3. desktop-control: Tự động hóa desktop, điều khiển chuột bàn phím.",
    "4. auto-updater：自动更新 Clawdbot 和升级技能。": "4. auto-updater: Tự động cập nhật Clawdbot và nâng cấp kỹ năng.",
    "5. skill-vetter，扫描你安装的技能是否安全，避免安装高风险技能把本地文件上传到非法云端。": "5. skill-vetter: Quét xem kỹ năng bạn cài có an toàn không, tránh cài skill rủi ro cao upload file local lên cloud bất hợp pháp.",
    "6. subagent-driven-development（管理者）：让你的 AI 学会委派，把子任务分配给其他 AI 并审核它们的工作，这样你就能专注于愿景，而不是苦力活。 ": "6. subagent-driven-development (quản lý): Giúp AI của bạn học cách ủy quyền, phân công tác vụ con cho các AI khác và kiểm duyệt công việc của chúng, để bạn tập trung vào tầm nhìn thay vì làm việc chân tay. ",
    "7. vector-memory: 向量记忆搜索，任务上下文太杂，导致记忆不准确的问题，通过它来 解决。": "7. vector-memory: Tìm kiếm bộ nhớ vector, giải quyết vấn đề ngữ cảnh tác vụ quá lộn xộn dẫn đến bộ nhớ không chính xác.",
    "8. clawhub：clawhub 是 OpenClaw 的技能市场，当你有其他需要的时候让小龙虾自行检索并安装 Skill 即可。": "8. clawhub: clawhub là chợ kỹ năng của OpenClaw, khi bạn có nhu cầu khác chỉ cần để OpenClaw tự tìm kiếm và cài Skill là được.",
    "其他的编程类、文案类、自动化流程等大家可以根据需求自行探索。": "Các loại khác như lập trình, viết content, quy trình tự động hóa... mọi người có thể tự khám phá theo nhu cầu.",
    "推荐资料：": "Tài liệu khuyến nghị:",
    "1. OpenClaw 的官网文档： ": "1. Tài liệu chính thức của OpenClaw: ",
    "如果你喜欢看官网文档可以看，不喜欢就不看，因为我一度觉得这文档不是给人看的，更像是给模型看的。": "Nếu bạn thích đọc tài liệu chính thức thì đọc, không thích thì thôi, vì mình từng thấy tài liệu này không phải viết cho người đọc, mà giống viết cho model đọc hơn.",
    "所以你碰到任何使用问题，都可以把官网丢给你的 OpenClaw，让它基于官网的知识来帮你解决。": "Nên khi gặp bất kỳ vấn đề sử dụng nào, bạn đều có thể đưa trang chính thức cho OpenClaw, để nó dựa trên kiến thức từ trang chính thức giúp bạn giải quyết.",
    "2. Awesome-openclaw-skills： clawhub上有上万的 Skill，但是这里只整理了 5000 个左右精挑细算的 Sikill 并给与了分类，当你需要找特定领域的 Skill 的时候直接来这里看看就完事了： ": "2. Awesome-openclaw-skills: Trên clawhub có hàng vạn Skill, nhưng ở đây chỉ tuyển chọn khoảng 5000 Skill tinh chọn và phân loại, khi bạn cần tìm Skill trong lĩnh vực cụ thể thì đến đây xem là xong: ",
    "3. OpenClaw 学习资源聚合网站： ": "3. Website tổng hợp tài nguyên học tập OpenClaw: ",
    "4. OpenClaw 中文社区： ": "4. Cộng đồng OpenClaw tiếng Trung: ",
    "5. OpenClaw 中文教程： ": "5. Hướng dẫn OpenClaw tiếng Trung: ",
    "6. OpenClaw 从新手到中级完整教程： ": "6. Hướng dẫn OpenClaw hoàn chỉnh từ người mới đến trung cấp: ",
    "关于上述这几个社区资源，说实话，每一个都是宝藏，把上述内容看完，执行完，相信我，你将会变成真正的龙虾主人，有这么一个贴心的助手陪着你，世界将会变得如此简单！": "Về các tài nguyên cộng đồng ở trên, nói thật, mỗi cái đều là kho báu. Đọc hết, thực hiện hết nội dung trên, tin mình đi, bạn sẽ trở thành chủ nhân OpenClaw thực thụ, có một trợ lý tận tâm như vậy bên cạnh, thế giới sẽ trở nên đơn giản biết bao!",
    "上述玩龙虾内容有任何疑问，也欢迎进群交流。": "Nếu có bất kỳ thắc mắc nào về nội dung sử dụng OpenClaw ở trên, cũng hoan nghênh vào nhóm trao đổi.",
    "欢迎日常交流": "Chào mừng trao đổi hàng ngày",
    "AI 时代，单打独斗不如抱团成长， 欢迎大家加微信互相交流心得。 ": "Thời đại AI, chiến đấu một mình không bằng cùng nhau phát triển. Hoan nghênh mọi người thêm WeChat để trao đổi kinh nghiệm. ",
    "👉 想要进群的朋友，扫码时备注 \"AI实验群\"，看到消息后会第一时间拉你进群。": "👉 Bạn nào muốn vào nhóm, khi quét mã hãy ghi chú \"Nhóm thí nghiệm AI\", thấy tin nhắn sẽ kéo bạn vào nhóm ngay.",
    "👉 想要进群的朋友，扫码时备注 \u201cAI实验群\u201d，看到消息后会第一时间拉你进群。": "👉 Bạn nào muốn vào nhóm, khi quét mã hãy ghi chú \u201cNhóm thí nghiệm AI\u201d, thấy tin nhắn sẽ kéo bạn vào nhóm ngay.",
    "群定位： ": "Định vị nhóm: ",
    "AI工具提效/实战经验互助": "Tăng hiệu suất công cụ AI / Hỗ trợ kinh nghiệm thực chiến",
    "群规则： ": "Quy tắc nhóm: ",
    "不水群、不广告、干货优先": "Không spam, không quảng cáo, ưu tiên nội dung chất lượng",
    "好文章值得被更多人看见！既然看到这里了，随手点个赞👍和关注，并转发给更多的朋友吧！感谢。": "Bài viết hay đáng được nhiều người thấy hơn! Đã đọc đến đây rồi, tiện tay bấm like 👍 và theo dõi, rồi chia sẻ cho nhiều bạn bè hơn nhé! Cảm ơn.",
    "> 作者：贾克斯的平行世界、微信：x_h886688": "> Tác giả: Thế Giới Song Song Của Jax, WeChat: x_h886688",
}

def has_chinese(text):
    return any('\u4e00' <= ch <= '\u9fff' for ch in text)

def translate_text(text):
    if text in TRANS:
        return TRANS[text]
    # If not found in map, return original
    return text

with open('_art_b7_10_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

translated = copy.deepcopy(data)
translated_count = 0
kept_count = 0
total_text = 0

for block in translated['blocks']:
    new_elements = []
    for el in block['elements']:
        if el['type'] == 'text_run':
            total_text += 1
            content = el['content']
            if has_chinese(content):
                new_content = translate_text(content)
                if new_content != content:
                    el['content'] = new_content
                    translated_count += 1
                else:
                    kept_count += 1
                    print(f"UNTRANSLATED: {content[:80]}")
            else:
                kept_count += 1
        new_elements.append(el)

    # Add space between adjacent Vietnamese text_runs
    final_elements = []
    for i, el in enumerate(new_elements):
        final_elements.append(el)
    block['elements'] = final_elements

with open('_art_b7_10_trans.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f"\nTotal text_run: {total_text}")
print(f"Translated: {translated_count}")
print(f"Kept: {kept_count}")
print(f"Saved to _art_b7_10_trans.json")
