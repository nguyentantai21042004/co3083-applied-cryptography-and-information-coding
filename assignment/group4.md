# Bài Tập Lớn An ninh Mật mã học

## 1. Mục tiêu và Phạm vi Dự án

**Mục tiêu:** Cung cấp giới thiệu toàn diện, thực tế về trách nhiệm của chuyên gia an ninh thông tin chuyên về mật mã học.

**Cấu trúc:** Dự án được chia thành ba phần rõ rệt: Lý thuyết, Thiết kế Công cụ, và Khai thác thực tế.

### Ba Phần Chính của Bài tập

| Phần | Nội dung Chính | Mục đích Thực tế |
|------|---------------|------------------|
| **Phần 1: Lý thuyết** | Hiểu biết nền tảng vững chắc về mật mã | Chứng minh tính đúng đắn và sự hiểu biết các khái niệm cốt lõi |
| **Phần 2: Phát triển** (Cầu nối Lý thuyết & Thực hành) | Thiết kế và triển khai một công cụ để xác định và khai thác điểm yếu của các hệ thống mật mã yếu | Phục vụ cả người kiểm thử xâm nhập (Penetration Testers) và nhà mật mã học bằng cách tự động hóa việc khám phá lỗ hổng |
| **Phần 3: Khai thác** | Mô phỏng một cuộc tấn công xen giữa (Man-in-the-Middle - MITM) | Thực hiện trinh sát, khám phá lỗ hổng, và tạo ra bằng chứng khái niệm (Proof-of-Concept) |

## 2. Nghiên cứu và Phát triển

| Vấn đề | Mô tả | Số điểm |
|--------|-------|---------|
| **Vấn đề 1** | Nghiên cứu | 3 |
| **Vấn đề 2** | Phát triển | 2 |

### 2.1 Vấn đề 1: Lattice - Lưới

#### Định nghĩa 2.5: Trường con và Phần mở rộng trường

- **Trường con** (subfield) $K$ của trường (field) $L$ là một tập con $K\subset L$ mà $K$ cũng là một trường.
- Nếu $K$ là trường con của $L$, thì $L$ là **phần mở rộng trường** (extension field) của $K$, và ký hiệu là $L/K$ (đọc là "L trên K").

#### Định nghĩa 2.6: Đa thức tối tiểu

- Cho $\alpha\in K$ với $F$ là một trường và $L/K$ là một phần mở rộng trường.
- **Đa thức tối tiểu** (minimal polynomial) của $\alpha$ là một đa thức đơn tố (monic polynomial) có bậc nhỏ nhất trong $F[x]$ mà $\alpha$ là nghiệm (root).

#### a) (1 điểm)

Đọc trong **[HPS08]** (Chương 6) và trình bày trong báo cáo các thuật ngữ sau:

- **Không gian vectơ** (*vector spaces*)
- **Tổ hợp tuyến tính** (*linear combinations*)
- **Độc lập tuyến tính** (*independence*)
- **Cơ sở** (*bases*)
- **Cơ sở trực giao và cơ sở trực chuẩn** (*orthogonal and orthonormal basis*)
- **Lưới** (*lattices*)
- **Miền cơ bản** (*fundamental domains*)
- **Bài toán Vectơ Ngắn nhất (SVP)** (*Shortest Vector Problem – SVP*)
- **Bài toán Vectơ Gần nhất (CVP)** (*Closest Vector Problem – CVP*)
- **Hình cầu Euclid** (*Euclidean ball*)
- **Chiều dài ngắn nhất kỳ vọng theo Gauss** (*Gaussian expected shortest length*)
- **Thuật toán LLL** (*LLL algorithm*)

#### b) (1 điểm)

Cho một giá trị $\alpha = 7 + \sqrt{29}$, với một xấp xỉ $\beta$ của $\alpha$ đến 10 chữ số thập phân. Tìm một đa thức tối tiểu $f(x)$ của $\alpha$ bằng cách sử dụng xấp xỉ $\beta$, thông qua việc tái lập công thức (*reformulating*) bài toán này thành một bài toán lưới (*lattice problem*).

> **Gợi ý:**
> - Phỏng đoán ban đầu về bậc (*degree*) của đa thức tối tiểu mà bạn muốn tìm là gì?
> - Bạn có thể nói gì về $f(\beta)$ khi biết $f(\alpha) = 0$?
> - Tìm một lưới thích hợp sao cho một vectơ nhất định là nhỏ và có thể dễ dàng tìm thấy.
> - Có thể kiểm tra kết quả tìm được bằng cách so sánh chiều dài của vectơ đó với chiều dài ngắn nhất kỳ vọng theo Gauss của lưới.

#### c) (1 điểm)

Giả sử bạn biết $d$ chữ số đầu tiên sau dấu thập phân của $X$. Hãy chỉ ra rằng bạn có thể tìm được $X$ bằng cách tái lập công thức bài toán này thành một bài toán lưới.

> **Lưu ý:** Sinh viên nên làm phần b) trước để hiểu được tư duy tiếp cận một bài toán lưới.

### 2.2 Vấn đề 2: Tấn công Mã Vigenère

#### Mô tả

Hầu hết các hệ mật mã cổ điển hiện nay đều đã bị phá vỡ, bao gồm cả Mã Vigenère (Vigenère Cipher). Để hiểu rõ hơn về cách thức tấn công các hệ mật mã này, sinh viên sẽ thực hiện phân tích và tấn công trên Mã Vigenère.

#### Yêu cầu

- Viết một script/bài chương trình (bằng Python hoặc bất kỳ ngôn ngữ lập trình nào khác) để tấn công một văn bản mã hóa (ciphertext) dài được mã hóa bằng Mã Vigenère.
- Trình bày và giải thích các nguyên tắc cốt lõi đằng sau phương pháp tấn công đã sử dụng.
- Áp dụng script/phương pháp vừa xây dựng để giải mã một ciphertext thử thách (được cung cấp bên dưới, khoá không được cho trước).
- Trình bày plaintext thu được.
- *(Tùy chọn)* Một chương trình mã hóa mẫu cũng được cung cấp để tham khảo.

#### Dữ liệu

- **Ciphertext thử thách:** [đính kèm tại đây hoặc cung cấp link]
- **Chương trình mã hóa mẫu:** [đính kèm tại đây hoặc cung cấp link]

#### Gợi ý

- Có thể tìm hiểu về tấn công dựa vào tần số, chỉ số trùng lặp (Index of Coincidence), Kasiski examination,...
- Nên thử trên các ciphertext ngắn trước để kiểm thử chương trình.

> **Lưu ý:** Báo cáo cần nêu rõ ý tưởng, các bước thực hiện tấn công và nhận xét về kết quả thu được.

## 3. SMC Exploitation

### Tổng quan (Overview)

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

## 4. Kết luận

### 4.1 Tính Liêm chính trong Học thuật (Academic integrity)

Tất cả công việc nộp cho bài tập này phải là của riêng bạn. Hợp tác trong nhóm đã được phân công là được phép và khuyến khích, nhưng chia sẻ giải pháp giữa các nhóm, đăng tải công khai các script khai thác (exploit scripts) hoặc chi tiết PoC theo cách có thể bị lạm dụng trước khi chấm điểm, hoặc tìm cách khác để đạt được lợi thế không công bằng đều bị nghiêm cấm. Bất kỳ bằng chứng nào về gian lận, đạo văn, hoặc lạm dụng môi trường kiểm thử sẽ được xử lý theo chính sách liêm chính học thuật của khóa học và có thể dẫn đến hình phạt như điểm 0 cho bài tập hoặc các hành động kỷ luật tiếp theo. Khi nghi ngờ, hãy hỏi các TA để được hướng dẫn.

### 4.2 Tiết lộ có Trách nhiệm và Kiểm thử An toàn (Responsible disclosure and safe testing)

Tất cả việc kiểm thử phải được giới hạn nghiêm ngặt trong server kiểm thử được cung cấp và phạm vi của bài tập này. Không nhắm mục tiêu vào các hệ thống bên ngoài hoặc các dịch vụ công cộng. Nếu bạn phát hiện ra một lỗ hổng nghiêm trọng có thể ảnh hưởng đến các hệ thống hoặc người dùng khác, hãy thông báo cho các TA ngay lập tức và tuân theo hướng dẫn tiết lộ có trách nhiệm; không công bố chi tiết công khai cho đến khi được ủy quyền.

### 4.3 Liên lạc & Hỗ trợ (Communication & support)

- **Email hỗ trợ:** Đối với các câu hỏi, gợi ý, hoặc làm rõ, vui lòng gửi email cho Trợ giảng (Teaching Assistants) tại:
  - `dangduongminhnhat2003@gmail.com`
  - `tcthang.sdh242@hcmut.edu.vn`
- **Thời gian phản hồi:** Các TA sẽ trả lời trong vòng một ngày làm việc (24 giờ) bất cứ khi nào có thể.
- **Họp trực tiếp:** Nếu bạn muốn thảo luận trực tiếp, bạn có thể lên lịch một cuộc họp trực tuyến với các TA vào các buổi tối ngày thường. Vui lòng đề xuất thời gian trước qua email và các TA sẽ xác nhận khả năng sắp xếp.

### 4.4 Yêu cầu Nộp Bài (Submission requirements)

#### Mã nguồn (Source code)
Tất cả mã nguồn được viết cho bài tập này (tái cấu trúc client, script khai thác, công cụ hỗ trợ, script có thể tái tạo) phải được đặt trong một repository GitHub công khai. Repository phải công khai tại thời điểm nộp bài và chứa một tệp README.md rõ ràng mô tả:

- Cách tái tạo PoC của bạn
- Mọi cấu hình cần thiết
- Cách script của bạn thực thi ràng buộc độ trễ yêu cầu 1 giây
- Mọi ảnh giả lập (emulator images) hoặc hướng dẫn cấu hình cần thiết để chạy bản demo

#### Báo cáo (Report)
Nộp một tệp báo cáo PDF duy nhất bao gồm tất cả các vấn đề. Báo cáo phải bao gồm:

1. **Tóm tắt súc tích** về các mục tiêu và mô hình mối đe dọa (threat model) của bạn cho mỗi phần/nhóm.

2. **Đối với mỗi vấn đề, cung cấp:**
   - **Lý thuyết:** Cơ sở lý thuyết liên quan đến phương pháp tiếp cận của bạn (ví dụ: thiết kế giao thức, các cơ sở mật mã (cryptographic primitives), hoặc mô hình lỗ hổng)
   - **Giải thích chi tiết:** Lý luận và phương pháp luận rõ ràng, từng bước được sử dụng trong phân tích hoặc khai thác của bạn
   - **Bằng chứng:** Ảnh chụp màn hình, nhật ký (logs), lưu lượng truy cập bị chặn bắt, hoặc bằng chứng có thể tái tạo khác chứng minh kết quả của bạn
   - **Các trích dẫn được định dạng đúng** cho tất cả các tài liệu tham khảo (bài báo, sách, trang web, hoặc tài nguyên trực tuyến) (sử dụng một kiểu trích dẫn nhất quán như IEEE, ACM, hoặc APA)

3. **Đóng góp của nhóm & Phân chia công việc:** Một bảng rõ ràng liệt kê từng thành viên trong nhóm và, đối với mỗi thành viên:
   - Các nhiệm vụ cụ thể mà họ chịu trách nhiệm
   - Những gì họ đã thực sự hoàn thành
   - Phần trăm hoàn thành cho các nhiệm vụ được giao
   - Một ghi chú ngắn về bất kỳ mục nào đang chờ xử lý hoặc sự phụ thuộc

4. **Sao lưu Bằng chứng (Evidence backup):** Cung cấp một liên kết đến một hoặc nhiều video ngắn (được lưu trữ trên Google Drive hoặc YouTube với chế độ hiển thị bị giới hạn/không công khai) chứng minh PoC của bạn đang chạy trên môi trường giả lập. Đính kèm các liên kết này trong báo cáo PDF và trong tệp GitHub README.md.

#### Phương pháp Nộp bài (Submission method)
Tải lên báo cáo PDF và cung cấp liên kết repository GitHub công khai qua hệ thống nộp bài của khóa học (hoặc gửi email cả hai cho TA nếu không có cổng nộp bài LMS). Đảm bảo liên kết GitHub có thể truy cập và repo là công khai tại thời điểm nộp bài.

### 4.5 Định dạng & Trích dẫn (Formatting & citations)

Báo cáo phải chuyên nghiệp và có khả năng tái tạo: bao gồm các hướng dẫn từng bước rõ ràng, các tham số cấu hình, và các lệnh tối thiểu để tái tạo PoC. Trích dẫn các nguồn bên ngoài một cách chính xác (bài báo/sách/web) theo một kiểu nhất quán (ví dụ: IEEE hoặc APA). Khi trích dẫn hoặc diễn giải tài liệu đã xuất bản, phải bao gồm đầy đủ chi tiết thư mục.

### 4.6 Hạn chót (Deadline)

Hạn chót nộp bài là hai tháng (60 ngày) kể từ ngày phát hành bài tập. Nộp báo cáo PDF và liên kết GitHub công khai của bạn trước hạn chót đó. Các bài nộp trễ chỉ có thể được chấp nhận với sự chấp thuận trước từ người hướng dẫn/TA và có thể bị trừ điểm.

### 4.7 Khuyến khích (Encouragement)

Bài tập này được thiết kế để mang tính thử thách. Vui lòng mạnh dạn đặt câu hỏi và tìm kiếm sự giúp đỡ sớm. Các TA luôn sẵn lòng hỗ trợ và sẽ phản hồi các yêu cầu chính đáng. Thực hành kỹ thuật tốt, tài liệu rõ ràng và kiểm thử có trách nhiệm sẽ được đánh giá cao.

### 4.8 Thuyết trình và Chứng minh (Presentation and demonstration)

Mỗi nhóm được yêu cầu chuẩn bị một bộ slide súc tích tóm tắt các phát hiện chính, phương pháp luận và các bài học kinh nghiệm từ dự án. Các slide sẽ được sử dụng cho buổi thuyết trình cuối cùng, diễn ra trực tiếp (offline). Trong buổi thuyết trình, mỗi nhóm phải thực hiện một bản demo trực tiếp rõ ràng, có thể tái tạo (PoC) về kết quả khai thác hoặc phân tích của họ trên môi trường giả lập. Bài thuyết trình nên nhấn mạnh sự hiểu biết về giao thức, tính đúng đắn của khai thác và thực hành kiểm thử an toàn.

### 4.9 Lời kết (Final note)

Cảm ơn vì sự làm việc chăm chỉ và cống hiến của bạn trong suốt dự án này. Hãy tự tin, luôn tò mò và hợp tác hiệu quả. Chúng tôi chúc tất cả các nhóm đạt được thành công tốt nhất trong việc hoàn thành bài tập và mang đến một bài thuyết trình cuối cùng sâu sắc.