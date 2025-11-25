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