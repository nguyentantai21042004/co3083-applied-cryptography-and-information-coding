# 3. SMC Exploitation

## Liên kết (Links)

- **Burp Suite (Community Edition):**  
  https://portswigger.net/burp/releases/professional-community-2025-8-7?requestededition=community&requestedplatform=

- **Source code SMC (Github Release):**  
  https://github.com/dangduongminhnhat/Client-Assignment-Advance-Cryptography-and-Coding-Theory/releases/tag/v1.0.0

## Tổng quan (Overview)

Burp Suite được sử dụng làm proxy chặn chính (primary intercepting proxy) cho bài tập này. Bằng cách hoạt động như một man-in-the-middle (xen giữa) được kiểm soát, Burp bắt giữ mọi yêu cầu (request) và phản hồi (response) HTTP/HTTPS được trao đổi giữa client Android và máy chủ (server) trong các giai đoạn trao đổi khóa (key exchange) và nhắn tin (messaging). Việc bắt giữ các dấu vết (traces) này cho phép chúng ta:

- Kiểm tra các trường (fields) được sử dụng trong quá trình dẫn xuất khóa (key derivation) và xác thực (authentication).
- Ánh xạ (map) các thông báo mạng (network messages) đến các vị trí trong mã nguồn (source code locations).
- Soạn thảo các bài kiểm tra phát lại (replay) hoặc sửa đổi (modification) có mục tiêu để xác minh và khai thác các điểm yếu trong việc triển khai (implementation weaknesses).

Bài tập này hướng dẫn bạn thực hiện một phân tích từ đầu đến cuối (end-to-end analysis) và khai thác Thành phần Nhắn tin An toàn (Secure Messaging Component - SMC) được phát hành trong liên kết Github này. Mục tiêu của Vấn đề này là áp dụng phân tích giao thức (protocol analysis), tái cấu trúc client (client reconstruction) và phát triển khai thác có trách nhiệm (responsible exploit development) để chứng minh các điểm yếu thực tế trong một triển khai SMC đã được kiểm tra.

### 3.1 Chặn bắt & Phân tích API (Sử dụng Burp Suite) (0.5 điểm)

#### Mục tiêu
Xây dựng một proxy man-in-the-middle (xen giữa) để chặn bắt và lập tài liệu về mọi cuộc gọi API được trao đổi giữa client và server, từ giai đoạn Trao đổi Khóa (Key Exchange) cho đến giai đoạn Trao đổi tin nhắn (Message Exchange).

#### Các Nhiệm vụ Yêu cầu (Required Tasks)

1. **Cấu hình Burp Suite** làm proxy chặn cho client Android (thiết bị thật hoặc trình giả lập). Đảm bảo client tin tưởng chứng chỉ CA của Burp nếu lưu lượng truy cập được bảo vệ bằng TLS.

2. **Chặn bắt tất cả các yêu cầu** (requests) và phản hồi (responses) HTTP/HTTPS liên quan đến:
   - Trao đổi/bắt tay khóa ban đầu (Initial key exchange / handshake)
   - Thiết lập phiên (Session establishment)
   - Các tin nhắn được mã hóa tiếp theo (Subsequent encrypted messaging)

3. **Đối với mỗi cuộc gọi API đã chặn bắt, tạo ra:**
   - Một ảnh chụp màn hình của yêu cầu và phản hồi như hiển thị trong Burp (bao gồm URL, tiêu đề - headers, và nội dung - body)
   - Một giải thích ngắn gọn, chính xác về mọi trường/tham số (field/parameter) trong yêu cầu và phản hồi
   - Đối chiếu (Correlate) mỗi dấu vết Burp với các tệp mã nguồn (source files) và đường dẫn code (code paths) trong repository đã triển khai API đó

#### Sản phẩm (Deliverables)
Tài liệu chứa: Ảnh chụp màn hình Burp, một bảng liệt kê từng điểm cuối API (API endpoint), các trường yêu cầu/phản hồi, và ánh xạ đến các vị trí mã nguồn (mapping to code locations).

### 3.2 Tái triển khai & Tái cấu trúc Giao thức (Re-implementation & Protocol Reconstruction) (1 điểm)

#### Mục tiêu
Đóng vai trò là một client: tái cấu trúc toàn bộ luồng giao thức (protocol flow) từ đầu và cung cấp một mã giả (pseudocode) rõ ràng, từng bước cho logic của client (đăng nhập → trao đổi khóa → kênh an toàn → nhắn tin).

#### Các Nhiệm vụ Yêu cầu (Required Tasks)

1. **Sử dụng các dữ liệu chặn bắt** từ Burp và mã nguồn, liệt kê trình tự chính xác của các thông báo giao thức được trao đổi: các loại thông báo, thứ tự và ngữ nghĩa của các trường (field semantics).

2. **Tạo ra mã giả gọn gàng** (clean pseudocode) thể hiện: xây dựng/phân tích thông báo (message construction/parsing), dẫn xuất và sử dụng khóa (key derivation and use), các bước ký/xác minh (signature/verification steps), và chuyển đổi trạng thái (state transitions).

3. **Giải thích từng bước** của mã giả để người đánh giá có thể hiểu được cách kênh an toàn (secure channel) được dự định xây dựng và sử dụng.

4. **Cung cấp một bản tái triển khai client** tối thiểu, có thể chạy được (minimal, runnable client reimplementation) bằng bất kỳ ngôn ngữ lập trình nào để chứng minh rằng bạn có thể tái tạo hành vi của giao thức. Điều này sẽ hữu ích khi phát triển Bằng chứng Khái niệm (PoC).

#### Sản phẩm (Deliverables)

- **Tài liệu chứa:** chuỗi thông báo đã tái cấu trúc (sử dụng sơ đồ hoặc ASCII), mã giả chi tiết cho phía client, và giải thích từng bước cho mỗi hoạt động.
- **Mã nguồn có thể chạy được:** đính kèm (các) tệp nguồn và hướng dẫn đơn giản để chạy chúng với server được cung cấp.

### 3.3 Khai thác & Bằng chứng Khái niệm (Exploitation & Proof-of-Concept) (3.5 điểm)

#### Mục tiêu
Dựa trên các phân tích từ các Phần trên, xác định và chứng minh một lỗ hổng trong triển khai SMC gây ảnh hưởng đến một trong các mục tiêu sau, tùy thuộc vào nhóm của bạn: khôi phục bí mật của server, mạo danh server, hoặc làm rò rỉ thông tin độ dài tin nhắn.

#### Mục tiêu Cụ thể của Nhóm (Group-specific objectives)

- **Nhóm 1:** Tìm một điểm yếu phía server làm phá vỡ tính bảo mật (confidentiality). Mục tiêu ưu tiên là khôi phục Khóa Bí mật của Server (ServerSecretKey) hoặc chứng minh khả năng giải mã hay làm lộ văn bản thô (plaintext) của tin nhắn.

- **Nhóm 2:** Nghiên cứu các điểm yếu của server cho phép mạo danh server (ví dụ: kẻ tấn công có được khóa ký bí mật của server) — thiết kế, triển khai và chứng minh một khai thác (exploit) khiến client chấp nhận và tương tác với một điểm cuối server giả mạo (forged server endpoint) cho ID người dùng được chỉ định.

- **Nhóm 3:** Nghiên cứu các điểm yếu của server làm rò rỉ siêu dữ liệu (metadata) của tin nhắn. Với mục đích của bài tập này, việc chứng minh rằng bạn có thể xác định độ dài của tin nhắn được người dùng gửi là đủ. Việc khôi phục thêm nội dung tin nhắn là được phép nhưng không bắt buộc.

#### Phân phối ID Người dùng (User ID distribution)
Mỗi nhóm sẽ được chỉ định một ID người dùng duy nhất trong Google Sheet "Assignment" này. Chỉ sử dụng ID người dùng được phân bổ cho nhóm của bạn trong quá trình kiểm thử.

#### Môi trường Client và Yêu cầu Demo (Client environment and demo requirements)

- Client là một ứng dụng Android. Bạn có thể kiểm thử bằng thiết bị Android thật hoặc trình giả lập. Khuyến nghị mạnh mẽ: chạy các kiểm thử trên một trình giả lập trong một môi trường cô lập.
- Buổi demo chấm điểm phải trình bày một PoC trực tiếp (live PoC) trên trình giả lập để đảm bảo đánh giá nhất quán giữa các nhóm.
- Ngoài bản demo trực tiếp, hãy quay một video dự phòng (tải lên Google Drive hoặc YouTube) và đính kèm liên kết vào báo cáo của bạn.

#### Hạn chế và Quy tắc An toàn (bắt buộc) (Constraints and safety rules - mandatory)

- Nghiêm ngặt giới hạn việc kiểm thử chỉ trong phạm vi server kiểm thử được cung cấp. Không tấn công các hệ thống bên ngoài.
- Server kiểm thử là miễn phí và bị giới hạn tốc độ (rate-limited). Không thực hiện các cuộc tấn công vét cạn (brute-force) mù quáng. Nếu việc vét cạn có vẻ cần thiết, phải có sự cho phép rõ ràng từ TA trước khi tiến hành.
- Các script tự động phải thực thi độ trễ ít nhất 1 giây giữa hai yêu cầu liên tiếp bất kỳ. Việc không triển khai độ trễ này sẽ dẫn đến bị phạt.
- Thông báo cho các TA ngay lập tức khi bạn tìm thấy một khai thác hoạt động và cung cấp các vật phẩm PoC để xác minh, để họ có thể xác thực các phát hiện và giám sát môi trường kiểm thử.

#### Sản phẩm (Deliverables)

- **Script khai thác** (mã nguồn) kèm theo tệp README mô tả cách cấu hình và chạy chúng.
- **Bằng chứng PoC:** đầu ra của khai thác (stdout/logs), dấu vết Burp (nếu liên quan), ảnh chụp màn hình và liên kết video dự phòng.
- **Một báo cáo ngắn** bao gồm: loại lỗ hổng đã khai thác, các bước cấp cao để tái tạo khai thác, bằng chứng cho thấy khai thác hoạt động (khôi phục bí mật / độ dài tin nhắn / kết quả mạo danh), và các khuyến nghị khắc phục (sửa lỗi giao thức hoặc các bản vá code cụ thể).
