#!/usr/bin/env python3
"""Fix remaining untranslated texts with embedded quotes."""
import sys, json, re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art25_trans_map.json', 'r', encoding='utf-8') as f:
    trans = json.load(f)

with open('_art25_cn_texts.json', 'r', encoding='utf-8') as f:
    all_cn = json.load(f)

# Add missing translations (ones with embedded double-quotes)
fixes = {
    25: ' nh\u1eadp l\u1ec7nh l\u00e0 c\u00f3 th\u1ec3 ho\u00e0n th\u00e0nh c\u00e0i \u0111\u1eb7t. V\u00ed d\u1ee5 nh\u1eadp "',
    27: '", l\u00e0 c\u00f3 th\u1ec3 d\u1ec5 d\u00e0ng ho\u00e0n th\u00e0nh c\u00e0i \u0111\u1eb7t.',
}

# Direct translations for entries with embedded quotes
direct = {}
direct[all_cn[25]] = ' nhập lệnh là có thể hoàn thành cài đặt. Ví dụ nhập "'
direct[all_cn[27]] = '", là có thể dễ dàng hoàn thành cài đặt.'
direct[all_cn[44]] = 'Phương pháp phát hiện quên: Carl phát hiện khi trò chuyện với Claude, nó quên khá nhanh, vì vậy đặt lệnh để xác nhận. Nếu sau năm sáu mươi lượt hội thoại, Claude có thể trả lời "Carl thật tuyệt", điều đó cho thấy nó vẫn nhớ thông tin, nếu không thì cần mở bản ghi hội thoại mới.'
direct[all_cn[51]] = 'Các cách cài đặt khác: Nếu không tìm thấy plugin, có thể nói nhu cầu cho Code X hoặc Calco, để chúng giúp tìm và cài đặt. Ví dụ nói với Code X "Tôi muốn Pixel đồng bộ với Obsidian", nó sẽ tự động hoàn thành cài đặt.'
direct[all_cn[91]] = ' xây dựng một hệ thống quản lý tri thức "sống". Cốt lõi là phá vỡ lưu trữ tĩnh của ghi chú, sử dụng '
direct[all_cn[98]] = ' thực hiện tương tác liền mạch giữa Agent và kho ghi chú. Về bản chất, đây là một thực hành kỹ thuật về việc nâng cấp "bộ não thứ hai" từ bộ nhớ thành bộ xử lý, nhằm giải quyết vấn đề quá tải thông tin và tri thức cứng nhắc, thực hiện gia tăng giá trị tri thức động.'
direct[all_cn[101]] = 'Phần mềm ghi chú truyền thống (như Notion, Flomo, Feishu) thường trở thành "bãi chôn lấp" thông tin. Cơ chế bộ nhớ của GPT tuy mạnh mẽ, nhưng vẫn bị hạn chế bởi hệ sinh thái đóng của nó.'
direct[all_cn[105]] = ': Mục tiêu không chỉ đơn giản là "ghi", mà là để dòng thông tin rải rác trong WeChat, trang web, video tự động chảy vào Obsidian, sau khi được AI tinh lọc sẽ hình thành mạng tri thức.'
direct[all_cn[106]] = 'Thu thập thông tin "không cảm nhận" (Input Layer)'
direct[all_cn[107]] = 'Bước đầu tiên xây dựng hệ thống là giải quyết ma sát nhập thông tin. Carl khuyến nghị một bộ "combo plugin thu thập" hiệu quả:'
direct[all_cn[123]] = 'Xây dựng hệ thống tệp "sống" (Structure Layer)'
direct[all_cn[141]] = 'Đây là "bộ não" của toàn bộ hệ thống, sử dụng AI để tự động hóa xử lý thông tin.'
direct[all_cn[143]] = ': Phù hợp xử lý các tác vụ lập trình và tái cấu trúc tệp phức tạp, đóng vai "giám đốc điều hành" chính.'
direct[all_cn[152]] = ': Để ngăn AI trở nên "đần" sau cuộc hội thoại dài, có thể thiết lập lệnh phát hiện (như "Carl thật tuyệt"), một khi AI quên ngữ cảnh hoặc Skill, lập tức khởi động lại hội thoại hoặc tải lại bộ nhớ.'
direct[all_cn[164]] = ' để kiểm soát phiên bản riêng tư, ngăn AI "phát điên" xóa nhầm tệp.'
direct[all_cn[168]] = 'Năm 2026, AI đã tiến hóa từ "chatbot" thành một phần của "hệ điều hành". Đối với người đi làm và khởi nghiệp, cốt lõi cạnh tranh không còn là nắm bao nhiêu công cụ, mà là đã xây dựng được bao nhiêu tự động hóa cho'
direct[all_cn[171]] = 'Xây dựng "cơ quan tình báo tự động hóa do AI điều khiển".'
direct[all_cn[182]] = '. Đưa các báo cáo chất lượng cao trong lĩnh vực của bạn (như "xe năng lượng mới ra nước ngoài", "SaaS thương mại điện tử xuyên biên giới") vào Obsidian cục bộ.'
direct[all_cn[184]] = ': Đóng gói "luồng thông tin" của bạn. Nhiều doanh nghiệp không có khả năng sàng lọc thông tin khổng lồ. Bạn có thể cung cấp '
direct[all_cn[185]] = '"dịch vụ tình báo tùy chỉnh theo ngành"'
direct[all_cn[186]] = '. Không chỉ bán báo cáo, mà bán "kho tri thức thời gian thực đã được sàng lọc và cấu trúc hóa".'
direct[all_cn[189]] = ': Ngưỡng kết hợp Obsidian và Agent vẫn rất cao (terminal, Docker, cấu hình API). Người dùng bình thường dù muốn "bộ não thứ hai" cũng sẽ bị chi tiết kỹ thuật làm nản lòng.'
direct[all_cn[192]] = ': Hiện tại kết nối giữa Obsidian với các Agent (như OpenInterpreter, OpenWebUI) vẫn cần cấu hình phức tạp. Phát triển một'
direct[all_cn[193]] = '"gói triển khai một chạm"'
direct[all_cn[201]] = ': Cung cấp '
direct[all_cn[202]] = '"tư vấn xây dựng bộ não số hóa"'
direct[all_cn[203]] = '. Xây dựng hệ thống quản lý tri thức AI tư nhân hóa, offline cho lãnh đạo doanh nghiệp hoặc nhóm nghiên cứu, giải quyết lo lắng về quyền riêng tư dữ liệu (Privacy-First AI Setup).'
direct[all_cn[205]] = 'Sử dụng "mô hình chênh lệch giá" để tấn công giảm chiều.'
direct[all_cn[215]] = '"siêu cá thể"'
direct[all_cn[222]] = 'Carl thừa nhận, anh không phải người dùng sớm của Obsidian, quyết định di chuyển toàn diện thực sự mới được đưa ra ba tuần trước. Trước đó anh đã dùng hầu như tất cả công cụ ghi chú chính thống: Notion, Flomo, TickTick, Feishu, nhưng luôn có một nhu cầu cốt lõi chưa được đáp ứng —'
direct[all_cn[223]] = 'Để AI thực sự "nhận biết" bản thân'
direct[all_cn[224]] = 'Anh lấy hệ thống bộ nhớ của ChatGPT làm ví dụ: Lý do chần chừ chưa chuyển hoàn toàn sang Claude là vì GPT đã tích lũy một hệ thống bộ nhớ "rất hiểu anh". Loại bộ nhớ này không phải là xuất hội thoại đơn giản, mà là ngữ cảnh cá nhân hóa được lắng đọng qua tương tác lâu dài. Anh nhận ra, thay vì phụ thuộc vào bộ nhớ riêng của một nền tảng, tốt hơn nên tự xây dựng một bộ'
direct[all_cn[226]] = ', rồi thông qua công cụ AI trao cho nó khả năng "sống".'
direct[all_cn[227]] = 'Đồng thời, anh quan sát thấy một tín hiệu ngành: Ngày càng nhiều dự án khởi nghiệp mới bắt đầu lấy "hình thái Obsidian" làm nguyên mẫu, nguyên nhân nằm ở logic nền tảng của Obsidian —'
direct[all_cn[231]] = 'giải quyết vấn đề "đầu vào" thông tin'
direct[all_cn[237]] = 'Di chuyển triệt để không có nghĩa là bỏ đi tất cả công cụ hiện có'
direct[all_cn[238]] = ', mà lấy Obsidian làm trung tâm, để các công cụ khác đảm nhận vai trò riêng, chỉ giao việc "lắng đọng tri thức" cho Obsidian chủ đạo.'
direct[all_cn[243]] = 'Carl đặc biệt nhấn mạnh, ngưỡng cài đặt Obsidian kết hợp công cụ AI gần như bằng không. Cách nói của anh là: Cài đặt bất kỳ Claude Code (hoặc trợ lý lập trình AI tương tự), nhập một câu "Giúp tôi cài đặt Obsidian", kết hợp Cursor là hoàn thành toàn bộ quy trình cài đặt.'
direct[all_cn[246]] = '. Nhiều người dùng Obsidian như một ghi chú cao cấp, nhưng điều này cách xa trạng thái phát huy hết tiềm năng của nó. Carl đề cập, "Hướng Dương Kiều Mộc" và "Tiểu Thất Tỷ" trong cộng đồng đều là người dùng Obsidian sâu, người sau thậm chí đã xây dựng hệ thống "bộ não thứ hai" hoàn chỉnh dựa trên Obsidian, có ngữ cảnh cá nhân cực kỳ phong phú khi đối thoại với AI Agent, trải nghiệm này được mô tả là "cánh cửa đến thế giới khác".'
direct[all_cn[248]] = 'Sự phối hợp giữa OpenClaw và Obsidian: Làm cho tri thức "sống" dậy'
direct[all_cn[251]] = ', triết lý thiết kế cốt lõi là "đơn giản, trực tiếp, đáng tin cậy" — tất cả dữ liệu được giữ hoàn toàn trên máy cục bộ, không có yêu cầu mạng, không tải lên bất kỳ dịch vụ cloud nào. Sự kết hợp với Obsidian khớp tự nhiên vì kho tri thức (vault) của Obsidian về bản chất chỉ là một thư mục thông thường, bên trong toàn là tệp Markdown tiêu chuẩn. OpenClaw không cần API riêng, trực tiếp đọc ghi '
direct[all_cn[255]] = 'Về khả năng cụ thể, OpenClaw có thể dùng ngôn ngữ tự nhiên truy vấn nội dung ghi chú (như "tìm tất cả ghi chú đề cập AI Agent"), tự động tạo hoặc cập nhật ghi chú, phân tích liên kết giữa các ghi chú và đề xuất liên kết hai chiều, còn có thể tự động sắp xếp cấu trúc lộn xộn, sửa liên kết hỏng, dọn dẹp nội dung trùng lặp.'
direct[all_cn[256]] = 'Hai cơ chế quan trọng được đề cập trong livestream, giúp toàn bộ hệ thống tri thức chuyển từ "lưu trữ tĩnh" sang "kích hoạt động":'
direct[all_cn[258]] = ': Cho phép AI Agent định kỳ chủ động "cảm nhận" trạng thái kho tri thức, thay vì thụ động chờ truy vấn. Ví dụ mỗi ngày tự động quét ghi chú mới, tạo tóm tắt đồ thị tri thức, phát hiện liên kết ghi chú tiềm năng.'
direct[all_cn[265]] = '. Phương pháp luận của Carl, về bản chất đang trả lời một mệnh đề thời đại: Trong bối cảnh kép của bùng nổ thông tin và phổ cập AI,'
direct[all_cn[270]] = 'Đối mặt với làn sóng AI tái định hình phương thức sản xuất tri thức, cá nhân và nhóm nhỏ thay vì lo lắng, tốt hơn hãy tìm đúng "dòng đi lên" của mình. Sau đây là phương pháp luận triển khai từ góc độ nghề nghiệp khác nhau:'
direct[all_cn[272]] = 'Tạo "bánh đà tri thức", để nội dung tự sinh sôi.'
direct[all_cn[276]] = 'Phương pháp luận 1: Thiết lập cơ chế liên kết plugin "kho đề tài" trong Obsidian. Đồng bộ nguồn RSS đăng ký hàng ngày (khuyến nghị sử dụng '
direct[all_cn[279]] = ') tự động vào Obsidian, kết hợp tác vụ Cron của OpenClaw, mỗi ngày tự động tạo "danh sách đề tài có thể viết hôm nay", giải quyết triệt để lo lắng chọn đề tài. Hướng ra nước ngoài có thể kết nối API của '
direct[all_cn[281]] = 'Phương pháp luận 2: Thiết lập quy trình "đọc xong thành tài sản". Mỗi khi đọc xong một bài viết hoặc xem xong một video, bắt buộc đưa ra một đoạn "ghi chú quan điểm cá nhân" dưới 100 từ lưu vào Obsidian, và gắn thẻ. Sau ba tháng, những mảnh ghép này sẽ tự động tổng hợp thành bài viết chuyên sâu có thể xuất bản trực tiếp. Trong nước có thể dùng '
direct[all_cn[287]] = 'Biến kho tri thức của bạn thành "nguyên mẫu" sản phẩm.'
direct[all_cn[288]] = 'Ý tưởng: Carl đề cập anh đang phát triển sản phẩm nhỏ của mình, và hệ thống Obsidian của anh chính là vườn ươm nhu cầu sản phẩm. Lãng phí lớn nhất của nhà phát triển độc lập là dành nhiều thời gian cho "nghĩ rõ làm gì" thay vì "xác minh nhanh".'
direct[all_cn[291]] = ' của Obsidian xây dựng "cơ sở dữ liệu điểm đau người dùng". Mỗi khi thấy người dùng phàn nàn về vấn đề nào đó trong cộng đồng, phần bình luận, Weibo, lập tức ghi lại và gắn thẻ. Dùng plugin Dataview tự động thống kê điểm đau tần suất cao, đó chính là'
direct[all_cn[297]] = 'Phương pháp luận 2: Tiếp cận thị trường B2B bằng "dịch vụ tùy chỉnh công cụ quản lý tri thức AI". Hiện tại nhiều doanh nghiệp vừa và nhỏ có nhu cầu lắng đọng tri thức nhưng thiếu năng lực kỹ thuật, nhà phát triển độc lập có thể cung cấp '
direct[all_cn[305]] = 'Nâng cấp "bản ghi công việc" thành "tài sản nghề nghiệp".'
direct[all_cn[309]] = 'Phương pháp luận 1: Thiết lập cấu trúc ba tầng "đánh giá dự án -> tinh lọc phương pháp luận -> mẫu có thể tái sử dụng". Mỗi khi hoàn thành một dự án, viết một bài đánh giá cấu trúc trong Obsidian (bối cảnh, quyết định, kết quả, phản ánh), sau đó để OpenClaw giúp bạn tinh lọc ra'
direct[all_cn[311]] = '. Sau một năm, bạn sẽ có một bộ "sổ tay phương pháp luận nghề nghiệp" hoàn toàn cá nhân hóa, có thể dùng trực tiếp cho phỏng vấn, nhận đơn hoặc mở khóa học kiếm tiền. Trong nước có thể trên'
direct[all_cn[317]] = '"trợ lý AI" cá nhân'
direct[all_cn[319]] = 'vai trò "bộ nhớ sống" không thể thay thế'
direct[all_cn[322]] = 'Biến bản thân hệ thống quản lý tri thức thành sản phẩm có thể bán.'
direct[all_cn[326]] = ', bạn dùng hệ thống này giải quyết vấn đề của mình, nghĩa là bạn có khả năng giúp người khác giải quyết vấn đề tương tự.'
direct[all_cn[327]] = 'Phương pháp luận 1: Phát triển khóa học hoặc dịch vụ đồng hành "xây dựng hệ thống quản lý tri thức AI". Hiện tại trên thị trường, các hướng dẫn tiếng Trung về Obsidian chất lượng không đồng đều, còn nội dung thực hành kết hợp OpenClaw gần như là vùng trống. Có thể trên'
direct[all_cn[331]] = 'Phương pháp luận 2: Xuất "mẫu kho tri thức tùy chỉnh theo ngành" cho các ngành dọc cụ thể. Ví dụ tùy chỉnh gói mẫu Obsidian "quản lý án lệ + tra cứu pháp luật" cho ngành luật, gói mẫu "soạn bài + theo dõi phản hồi học sinh" cho giáo viên. Trong nước có thể thông qua'
direct[all_cn[475]] = '11-10|AI cũng mua sắm Double 11|"88VIP" phiên bản Master Tàng phúc lợi lớn WaytoAGI Học chung lúc 8 giờ tối'

# Apply all fixes
for cn, vi in direct.items():
    trans[cn] = vi

# Save updated map
with open('_art25_trans_map.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, ensure_ascii=False, indent=2)

covered = sum(1 for t in all_cn if t in trans)
print(f"Updated translation map: {len(trans)} entries")
print(f"Coverage: {covered}/{len(all_cn)} ({100*covered/len(all_cn):.1f}%)")

remaining = [t for t in all_cn if t not in trans]
if remaining:
    print(f"\nStill remaining {len(remaining)} untranslated:")
    for r in remaining:
        short = r[:80].replace('\n', '\\n')
        print(f"  [{all_cn.index(r)}] {short}")
