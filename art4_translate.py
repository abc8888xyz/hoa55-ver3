import json, re

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

with open('art4_original.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

t = {
    "B0E0": "Nhật ký nuôi dưỡng OpenClaw, bắt đầu từ 0! Phải đọc sau khi cài đặt! (40 ngày kinh nghiệm thực chiến + kèm prompt vai trò)",
    "B1E0": "🔗 Link bài gốc: ",
    "B2E0": "Tuyên bố: Bài viết này đến từ 𝕏",
    "B3E0": "Đại thần Saboo, tôi dịch và biên tập sang tiếng Trung! Mọi người có thể follow!",
    "B4E0": "Điều duy nhất tôi làm, là nói chuyện với chúng.",
    "B5E0": "Không phải chỉnh prompt, không phải đổi model, không phải tái cấu trúc kiến trúc. Chỉ là nói chuyện, cho phản hồi, nhìn chúng ghi lại nội dung. ",
    "B6E0": "Tuyên bố: Bài viết gốc của đại thần hải ngoại Shubham Saboo, có thể follow! x:",
    "B7E0": "40 ngày trước, agent nội dung của tôi viết tweet còn chất đầy emoji và hashtag, agent nghiên cứu chìm thông tin giá trị trong nhiễu. Thời gian tôi sửa lỗi còn nhiều hơn tự làm.",
    "B8E0": "Hôm nay, Kelly soạn nội dung bằng giọng của tôi, Dwight mỗi sáng gửi 7 câu chuyện, mỗi cái đều đáng đọc. 8 agent chạy 24 giờ. Tôi mở Telegram, xem bản nháp, uống ly cà phê.",
    "B9E0": "Ngày 1 và ngày 40 dùng cùng một model. Sự khác biệt nằm ở một loạt file Markdown mỗi tuần càng phong phú hơn.",
    "B10E0": "Đây chính là hệ thống file đó.",
    "B11E0": "Làm rõ một điều trước",
    "B12E0": "Agent không thông minh hơn vì bạn dùng lâu hơn. Nhưng các file xung quanh nó trở nên phong phú hơn, chính xác hơn, phù hợp hơn với nhu cầu của bạn. Bối cảnh tích lũy này mới là lợi thế cạnh tranh.",
    "B13E0": "Nhiều người dành nhiều thời gian chỉnh prompt, đổi model, nghiên cứu các framework orchestration. Nhưng sự khác biệt thực sự không nằm ở model, mà ở hệ thống file.",
    "B14E0": "Không có message queue, không có database, không có framework orchestration phức tạp. Toàn bộ hệ thống chỉ là file Markdown trên đĩa. Hệ thống file chính là lớp tích hợp.",
    "B15E0": "Nghe có vẻ thô sơ? Đọc xong bạn sẽ hiểu tại sao nó hiệu quả hơn bất kỳ framework nào.",
    "B16E0": "Kiến trúc ba tầng, rõ ràng một cái nhìn ",
    "B17E0": "Toàn bộ hệ điều hành gồm ba tầng:",
    "B18E0": "Hình 1: Kiến trúc file ba tầng",
    "B19E0": "Mỗi tầng giải quyết một vấn đề cốt lõi:",
    "B20E0": "Tầng|Vấn đề cốt lõi|File Tầng danh tính|Đây là ai? Phục vụ ai?|SOUL.md, IDENTITY.md, USER.md Tầng vận hành|Làm việc thế nào? Tự phục hồi thế nào?|AGENTS.md, HEARTBEAT.md Tầng tri thức|Đã học được gì?|MEMORY.md, nhật ký hàng ngày, bối cảnh chia sẻ",
    "B21E0": "Dưới đây phân tích từng tầng.",
    "B22E0": "Tầng 1: Tầng danh tính",
    "B23E0": "SOUL.md -- Agent là ai?",
    "B24E0": 'Đây là "file nhân cách" của agent. Định nghĩa danh tính, trách nhiệm, cách hành xử.',
    "B25E0": "Ví dụ về agent nghiên cứu Dwight:",
    "B27E0": "IDENTITY.md -- Thẻ tham khảo nhanh",
    "B28E0": "SOUL.md là nhân cách đầy đủ, IDENTITY.md là danh thiếp.",
    "B30E0": "File rất nhỏ, nhưng khi bạn chạy đồng thời 8 agent, thiết kế này sẽ cải thiện trải nghiệm đáng kể. Đây cũng là nội dung hiển thị khi agent gửi tin nhắn cho bạn trên Telegram.",
    "B31E0": "USER.md -- Đối tượng mà agent phục vụ",
    "B32E0": "Mỗi agent đều cần biết nó đang giúp ai.",
    "B34E0": "Chi tiết cá nhân quan trọng hơn bạn nghĩ. Múi giờ nghĩa là agent sẽ không sắp lịch cho bạn lúc 3 giờ sáng. Sở thích ăn uống nghĩa là khi Pam soạn thông báo bữa tối nhóm, sẽ không gợi ý nhà hàng steak. Những chi tiết này tạo hiệu ứng lãi kép.",
    "B35E0": "Viết một lần, tất cả agent đều đọc.",
    "B36E0": "Tầng 2: Tầng vận hành",
    "B37E1": "Quy tắc hành vi",
    "B38E0": "SOUL.md định nghĩa agent là ai, AGENTS.md định nghĩa nó vận hành thế nào: quy trình khởi động phiên, thứ tự đọc file, quản lý bộ nhớ, quy tắc bảo mật.",
    "B39E0": "AGENTS.md cấp gốc mà tất cả agent kế thừa:",
    "B41E0": "Agent không có bộ nhớ giữa các phiên, mỗi lần bắt đầu từ số không.",
    "B41E1": "Nếu một sửa chữa không được ghi vào file, phiên tiếp theo nó sẽ không tồn tại. AGENTS.md làm rõ điều này, đảm bảo agent ghi lại mọi thứ.",
    "B42E0": "Mỗi agent có thể mở rộng thêm quy tắc riêng. AGENTS.md của Kelly bổ sung 6 file: hướng dẫn phong cách viết, mẫu format bài đăng, ví dụ thực tế, nhiệm vụ hàng ngày...",
    "B43E0": "HEARTBEAT.md -- Cơ chế tự phục hồi",
    "B44E0": "Đội agent là hạ tầng, hạ tầng sẽ gặp sự cố.",
    "B45E0": "HEARTBEAT.md của Monica giám sát hai điều:",
    "B46E0": "Trình duyệt có sống không",
    "B46E1": " -- Quét tình báo của Dwight phụ thuộc vào nó",
    "B47E0": "Nhiệm vụ định kỳ có chạy không",
    "B47E1": " -- Nếu bỏ lỡ, Kelly và Rachel sẽ làm việc dựa trên tình báo cũ",
    "B48E0": "Tuần thứ 3 tôi đã bị dính. Scheduler có bug, nhiệm vụ đẩy vào hàng đợi nhưng không bao giờ thực thi. Tôi mấy tiếng không phát hiện. Sau đó tôi mới xây cơ chế heartbeat, đưa failure mode vào giám sát.",
    "B49E0": "Ngày đầu không cần cái này, sau lần gặp sự cố đầu tiên hãy xây. Bạn sẽ biết rõ cần giám sát gì, vì đã tận mắt thấy cái gì sẽ sập.",
    "B50E0": "Tầng 3: Tầng tri thức",
    "B51E0": "Đây là hệ thống bộ nhớ thực sự hiệu quả -- hệ thống ba cấp dựa trên file.",
    "B52E0": "Cấp 1: MEMORY.md (Bộ nhớ dài hạn tinh hoa)",
    "B53E0": "Không phải log thô, không phải mọi thứ đã xảy ra, mà là nội dung thực sự quan trọng.",
    "B54E0": 'Chú ý phần "Bài học xương máu" và "Ví dụ sai". Monica đã xóa một thư mục dự án, lỗi này từ đó vĩnh viễn ghi vào bộ nhớ dài hạn của cô ấy. Cô ấy sẽ không bao giờ mắc lại.',
    "B55E0": "Sửa một lần, lưu một lần, ngăn cùng một lỗi lặp lại trong mọi phiên tương lai. Chỉ riêng phần này, đã đáng giá hơn bất kỳ hướng dẫn prompt engineering nào.",
    "B56E0": "Cấp 2: Nhật ký hàng ngày (Bản ghi thô)",
    "B57E0": "Nhật ký hàng ngày là nguyên liệu thô, MEMORY.md là sản phẩm tinh lọc, cả hai đều không thể thiếu.",
    "B58E0": "Quy tắc bảo trì: Nhật ký hàng ngày tích lũy rất nhanh, không cắt tỉa thì context của agent sẽ phình to. Nhật ký của Kelly có lúc đạt 161,000 token, chất lượng output giảm mạnh, phải nén xuống 40,000. Mỗi lần chỉ tải nhật ký hôm nay và hôm qua.",
    "B59E0": "Cấp 3: shared-context/ (Tầng tri thức xuyên agent)",
    "B60E0": "Đây là phần mới nhất được thêm vào, và cũng là",
    "B60E1": "phần thay đổi tất cả",
    "B60E2": ".",
    "B61E0": "THESIS.md là khung tư duy hiện tại của tôi: tôi quan tâm điều gì, đã viết gì, còn khoảng trống nào. Dwight đọc nó để xác định ưu tiên nghiên cứu, Kelly đọc để khớp với dòng suy nghĩ của tôi. Mỗi agent đều căn chỉnh theo cùng một nguồn sự thật.",
    "B62E0": 'FEEDBACK-LOG.md là tầng sửa chữa xuyên agent. Khi tôi nói Kelly "đừng dùng gạch ngang", phản hồi này cũng áp dụng cho Rachel, Ryan và Pam. Thay vì sửa từng agent một, tôi viết một lần, tất cả đều đọc.',
    "B63E0": "Sự thay đổi đơn lẻ này tiết kiệm thời gian nhiều hơn bất kỳ prompt optimization nào tôi từng làm.",
    "B64E0": "Cách agent phối hợp",
    "B65E0": "Không có API call, không có message queue, chỉ có file.",
    "B66E0": "Dwight ghi nghiên cứu vào intel/DAILY-INTEL.md, Kelly đọc, Rachel đọc, Pam đọc. Phối hợp chính là hệ thống file.",
    "B67E0": "Hình 2: Quy trình phối hợp dựa trên file",
    "B68E0": "Nguyên tắc đơn ghi",
    "B68E1": ": Không bao giờ để hai agent đồng thời ghi cùng một file. Thiết kế mỗi file chia sẻ thành một người ghi, nhiều người đọc. Điều này ngăn chặn mọi xung đột phối hợp mà bạn cần debug.",
    "B69E0": "Lập lịch khiến tất cả trở nên khả thi",
    "B69E1": ": Dwight chạy lúc 8 sáng và 4 chiều, Kelly và Rachel chạy lúc 5 chiều.",
    "B69E2": "Dwight chạy trước, vì tất cả đều phụ thuộc output của anh ấy.",
    "B69E3": "Sai thứ tự, agent phía sau đọc được file đã cũ hoặc trống.",
    "B70E0": "Cấu trúc thư mục hoàn chỉnh",
    "B71E0": "Tại sao phương pháp này hiệu quả",
    "B72E0": "File không phải tĩnh, chúng đang tiến hóa.",
    "B73E0": "SOUL.md của Kelly ngày đầu chỉ là bản nháp sơ sài. Đến ngày 40, nó đã có ví dụ giọng điệu cụ thể, danh sách pattern bị từ chối do chính cô ấy viết, và một khu vực \"không bao giờ gợi ý lại\".",
    "B74E0": 'Nguyên tắc của Dwight ngày đầu viết "tìm xu hướng hot". Ngày 10 thành "nếu Alex hôm nay không thể hành động, bỏ qua". Ngày 20, anh ấy thêm bước xác minh.',
    "B75E0": "Tầng bối cảnh chia sẻ đến ngày 20 mới tồn tại. Lúc đó tôi đang lặp lại cùng sửa chữa cho nhiều agent. Sau đó tôi xây THESIS.md và FEEDBACK-LOG.md, đột nhiên, một lần sửa lan truyền đến khắp nơi.",
    "B76E0": "Model ngày 1 và ngày 40 giống nhau. Nó không thông minh hơn vì bạn dùng lâu hơn.",
    "B77E0": "Nhưng các file xung quanh nó trở nên phong phú hơn, chính xác hơn, phù hợp hơn với nhu cầu cụ thể của bạn.",
    "B78E0": "Bối cảnh tích lũy này mới là lợi thế cạnh tranh. Không ai có thể sao chép nó bằng cách dùng cùng một model.",
    "B79E0": "Bạn phải kiếm được nó bằng cách xuất hiện mỗi ngày, trò chuyện với agent.",
    "B80E0": "Cách bắt đầu (đừng cố xây xong trong một cuối tuần)",
    "B81E0": "Thời gian|Hành động Hôm nay|Cài OpenClaw, viết SOUL.md, IDENTITY.md, USER.md. Chọn nhiệm vụ hàng ngày lặp lại nhất, đặt cron cho nó chạy 3 ngày sau|Bắt đầu cho phản hồi cụ thể, đảm bảo phản hồi ghi vào file bộ nhớ, chứ không chỉ nằm trong lịch sử chat 1 tuần sau|Tạo AGENTS",
    "B82E0": "Lúc này bạn sẽ cảm nhận lãi kép bắt đầu xảy ra 3 tuần sau|Thêm agent thứ hai, xây phối hợp dựa trên file. Khi pattern xuất hiện, thêm hướng dẫn chuyên biệt cho vai trò Khoảng cùng lúc|Xây tầng bối cảnh chia sẻ. Dùng THESIS.md ghi suy nghĩ hiện tại, dùng FEEDBACK-LOG.md quản lý sửa chữa xuyên agent 4 tuần sau|Sau sự cố đầu tiên",
    "B83E0": "Viết ở cuối",
    "B84E0": "Điều duy nhất bạn cần làm, là trò chuyện với agent của bạn. File sẽ hoàn thành phần còn lại.",
    "B85E0": "Không phải chỉnh prompt, không phải đổi model, không phải tái cấu trúc kiến trúc.",
    "B86E0": "Chỉ là nói chuyện. Cho phản hồi. Nhìn chúng ghi lại nội dung.",
    "B87E0": "Rồi một ngày bạn mở Telegram, xem bản nháp, uống ly cà phê.",
    "B88E0": "Agent của bạn đã học được cách giúp bạn làm việc.",
    "B89E0": 'Tham khảo: Shubham Saboo "How to Build OpenClaw Agents That Actually Evolve Over Time"',
    "B90E0": "Từ:",
    "B92E0": "Biên tập dịch thuật:",
}

stats = {"total_blocks": len(data["blocks"]), "translated": 0, "kept": 0, "total_text": 0, "errors": []}
for i, block in enumerate(data["blocks"]):
    for j, elem in enumerate(block.get("elements", [])):
        content = elem.get("content", "")
        if not content.strip():
            continue
        stats["total_text"] += 1
        key = f"B{i}E{j}"
        if key in t:
            elem["content"] = t[key]
            stats["translated"] += 1
        elif not has_chinese(content):
            stats["kept"] += 1
        else:
            stats["errors"].append(key)

with open("art4_translated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Stats: translated={stats['translated']}, kept={stats['kept']}, errors={len(stats['errors'])}, total={stats['total_text']}")
if stats["errors"]:
    for key in stats["errors"]:
        parts = key.split("E")
        i, j = int(parts[0][1:]), int(parts[1])
        c = data["blocks"][i]["elements"][j].get("content", "")
        print(f"  MISSING {key}: {repr(c[:80])}")
