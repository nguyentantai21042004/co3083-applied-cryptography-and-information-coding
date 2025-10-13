# Hướng Dẫn Thực Hiện Bài Tập Lớn An ninh Mật mã học

## Tổng Quan Dự Án

**Thời gian dự kiến:** 45-50 ngày (1.5 tháng)
**Tổng điểm:** 10 điểm
**Cấu trúc:** 4 phần chính với 3 mức độ khó tăng dần
**Nhóm:** 5 thành viên với vai trò ngang nhau

---

## PHẦN 1: NGHIÊN CỨU LÝ THUYẾT (3 điểm)

### 2.1 Vấn đề 1: Lattice - Lưới (3 điểm)

#### Kiến Thức Cần Có Trước Khi Bắt Đầu

**Toán học cơ bản:**
- Đại số tuyến tính (vector spaces, linear combinations, bases)
- Lý thuyết số (modular arithmetic, finite fields)
- Đa thức và nghiệm của đa thức
- Hình học Euclid

**Mật mã học cơ bản:**
- Khái niệm về lattice trong mật mã học
- Các bài toán khó trong lattice (SVP, CVP)
- Thuật toán LLL và ứng dụng

#### Thứ Tự Thực Hiện

**Bước 1: Nghiên cứu Lý Thuyết (1 điểm) - Ngày 1-12**
- Đọc và hiểu **[HPS08]** (Chương 6)
- Tạo báo cáo chi tiết về 12 thuật ngữ:
  - Không gian vectơ (vector spaces)
  - Tổ hợp tuyến tính (linear combinations)
  - Độc lập tuyến tính (independence)
  - Cơ sở (bases)
  - Cơ sở trực giao và cơ sở trực chuẩn (orthogonal and orthonormal basis)
  - Lưới (lattices)
  - Miền cơ bản (fundamental domains)
  - Bài toán Vectơ Ngắn nhất (SVP)
  - Bài toán Vectơ Gần nhất (CVP)
  - Hình cầu Euclid (Euclidean ball)
  - Chiều dài ngắn nhất kỳ vọng theo Gauss (Gaussian expected shortest length)
  - Thuật toán LLL (LLL algorithm)

**Bước 2: Tìm Đa Thức Tối Thiểu (1 điểm) - Ngày 13-20**
- Tính toán $\alpha = 7 + \sqrt{29}$ với 10 chữ số thập phân
- Xây dựng lattice phù hợp để tìm đa thức tối tiểu
- Áp dụng thuật toán LLL
- Kiểm tra kết quả bằng chiều dài ngắn nhất kỳ vọng theo Gauss

**Bước 3: Khái Quát Hóa Bài Toán (1 điểm) - Ngày 21-25**
- Phát triển phương pháp tổng quát cho trường hợp biết $d$ chữ số đầu tiên
- Xây dựng lattice tương ứng
- Viết thuật toán tổng quát

#### Kiến Thức Đạt Được Sau Khi Hoàn Thành

**Kỹ năng toán học:**
- Hiểu sâu về cấu trúc lattice và ứng dụng
- Thành thạo thuật toán LLL và các biến thể
- Kỹ năng xây dựng lattice cho các bài toán cụ thể

**Kỹ năng lập trình:**
- Sử dụng các thư viện lattice (SageMath, fpylll)
- Viết thuật toán tối ưu cho bài toán lattice
- Xử lý số học độ chính xác cao

---

## PHẦN 2: PHÁT TRIỂN CÔNG CỤ (2 điểm)

### 2.2 Vấn đề 2: Tấn công Mã Vigenère (2 điểm)

#### Kiến Thức Cần Có Trước Khi Bắt Đầu

**Mật mã học cổ điển:**
- Hiểu cơ chế mã hóa Vigenère
- Các phương pháp tấn công cổ điển
- Phân tích tần số và thống kê ngôn ngữ

**Lập trình:**
- Python cơ bản (xử lý chuỗi, file I/O)
- Thư viện thống kê (numpy, scipy)
- Thuật toán tìm kiếm và tối ưu

#### Thứ Tự Thực Hiện

**Bước 1: Nghiên Cứu Phương Pháp Tấn Công (Ngày 26-30)**
- Tìm hiểu về Index of Coincidence
- Nghiên cứu Kasiski examination
- Phân tích tần số trong ngôn ngữ tiếng Anh
- Các phương pháp tấn công khác

**Bước 2: Thiết Kế Thuật Toán (Ngày 31-35)**
- Xác định độ dài khóa có thể
- Phân đoạn ciphertext theo độ dài khóa
- Phân tích tần số cho từng đoạn
- Tìm kiếm khóa tối ưu

**Bước 3: Lập Trình Script (Ngày 36-40)**
- Viết chương trình tấn công hoàn chỉnh
- Test trên các ciphertext ngắn
- Tối ưu hóa thuật toán
- Xử lý các trường hợp đặc biệt

**Bước 4: Áp Dụng Thực Tế (Ngày 41-45)**
- Giải mã ciphertext thử thách được cung cấp
- Đánh giá độ chính xác của kết quả
- Viết báo cáo chi tiết về phương pháp

#### Kiến Thức Đạt Được Sau Khi Hoàn Thành

**Kỹ năng phân tích mật mã:**
- Hiểu sâu về điểm yếu của mật mã cổ điển
- Thành thạo các kỹ thuật phân tích thống kê
- Kỹ năng thiết kế thuật toán tấn công

**Kỹ năng lập trình:**
- Xử lý dữ liệu văn bản và thống kê
- Tối ưu hóa thuật toán
- Debug và test các chương trình phức tạp

---

## PHÂN CHIA CÔNG VIỆC CHO NHÓM 5 NGƯỜI

### Nguyên Tắc Chia Việc

**Vai trò ngang nhau:** Mỗi thành viên đều có trách nhiệm như nhau và đóng góp 20% vào dự án
**Làm việc song song:** Các phần có thể làm đồng thời để tối ưu thời gian
**Hỗ trợ lẫn nhau:** Mọi người cần hiểu và hỗ trợ công việc của nhau

### Cấu Trúc Nhóm

| Thành viên | Vai trò chính | Trách nhiệm | Thời gian |
|------------|---------------|-------------|-----------|
| **Thành viên 1** | Lattice Theory Lead | Nghiên cứu lý thuyết lattice, hướng dẫn nhóm | Ngày 1-25 |
| **Thành viên 2** | Lattice Implementation | Lập trình thuật toán LLL, tìm đa thức | Ngày 13-25 |
| **Thành viên 3** | Vigenère Research | Nghiên cứu phương pháp tấn công | Ngày 26-35 |
| **Thành viên 4** | Vigenère Implementation | Lập trình script tấn công | Ngày 36-45 |
| **Thành viên 5** | Documentation & Integration | Tổng hợp, báo cáo, presentation | Suốt dự án |

### Chi Tiết Phân Công

#### GIAI ĐOẠN 1: NGHIÊN CỨU LÝ THUYẾT (Ngày 1-25)

**Thành viên 1 - Lattice Theory Lead (Ngày 1-25)**
- **Nhiệm vụ chính:**
  - Đọc và phân tích [HPS08] Chương 6
  - Tạo báo cáo chi tiết về 12 thuật ngữ lattice
  - Hướng dẫn nhóm hiểu về lý thuyết lattice
  - Chuẩn bị presentation về lý thuyết

- **Deliverables:**
  - Báo cáo lý thuyết hoàn chỉnh (20-30 trang)
  - Slides presentation cho nhóm
  - Glossary thuật ngữ chuyên môn

**Thành viên 2 - Lattice Implementation (Ngày 13-25)**
- **Nhiệm vụ chính:**
  - Tính toán $\alpha = 7 + \sqrt{29}$ với 10 chữ số thập phân
  - Xây dựng lattice cho bài toán đa thức tối tiểu
  - Implement thuật toán LLL
  - Kiểm tra và validate kết quả

- **Deliverables:**
  - Code Python/SageMath hoàn chỉnh
  - Kết quả tính toán chi tiết
  - Báo cáo kỹ thuật implementation

**Thành viên 3,4,5 - Hỗ trợ (Ngày 1-25)**
- **Nhiệm vụ:**
  - Học và hiểu lý thuyết lattice từ thành viên 1
  - Review và feedback cho code của thành viên 2
  - Chuẩn bị cho giai đoạn tiếp theo

#### GIAI ĐOẠN 2: PHÁT TRIỂN CÔNG CỤ (Ngày 26-45)

**Thành viên 3 - Vigenère Research (Ngày 26-35)**
- **Nhiệm vụ chính:**
  - Nghiên cứu Index of Coincidence
  - Phân tích Kasiski examination
  - Tìm hiểu các phương pháp tấn công khác
  - Thiết kế thuật toán tổng thể

- **Deliverables:**
  - Báo cáo nghiên cứu phương pháp (15-20 trang)
  - Pseudocode cho thuật toán
  - Test cases và expected results

**Thành viên 4 - Vigenère Implementation (Ngày 36-45)**
- **Nhiệm vụ chính:**
  - Implement script tấn công theo thiết kế
  - Test trên các ciphertext ngắn
  - Tối ưu hóa thuật toán
  - Giải mã ciphertext thử thách

- **Deliverables:**
  - Script Python hoàn chỉnh
  - Test results và analysis
  - Plaintext được giải mã

**Thành viên 1,2,5 - Hỗ trợ (Ngày 26-45)**
- **Nhiệm vụ:**
  - Review thiết kế thuật toán
  - Test và debug code
  - Chuẩn bị documentation

#### GIAI ĐOẠN 3: TỔNG HỢP VÀ NỘP BÀI (Ngày 41-50)

**Thành viên 5 - Documentation & Integration (Suốt dự án)**
- **Nhiệm vụ chính:**
  - Tổng hợp tất cả kết quả
  - Viết báo cáo tổng thể
  - Chuẩn bị presentation slides
  - Quản lý GitHub repository
  - Tạo demo videos

- **Deliverables:**
  - Báo cáo cuối cùng (40-50 trang)
  - Presentation slides (20-25 slides)
  - GitHub repository hoàn chỉnh
  - Demo videos

**Tất cả thành viên (Ngày 41-50)**
- **Nhiệm vụ:**
  - Review và hoàn thiện báo cáo
  - Chuẩn bị presentation
  - Test toàn bộ system
  - Submit final deliverables

### Lịch Họp Nhóm

**Họp hàng tuần (30-45 phút):**
- **Thứ 2:** Review tiến độ tuần trước
- **Thứ 4:** Thảo luận vấn đề và hỗ trợ
- **Thứ 6:** Demo kết quả và feedback

**Họp đặc biệt:**
- **Ngày 12:** Review lý thuyết lattice
- **Ngày 25:** Demo implementation lattice
- **Ngày 35:** Review thiết kế Vigenère
- **Ngày 45:** Demo script tấn công
- **Ngày 50:** Final review và chuẩn bị nộp bài

### Công Cụ Làm Việc Nhóm

**Communication:**
- **Discord/Teams:** Chat hàng ngày
- **Google Meet:** Họp online
- **Email:** Gửi documents và updates

**Collaboration:**
- **GitHub:** Quản lý code và documents
- **Google Drive:** Share files và báo cáo
- **Notion/Trello:** Quản lý tasks và timeline

**Documentation:**
- **Overleaf:** Viết báo cáo LaTeX
- **Google Docs:** Collaborate viết báo cáo
- **Miro/Figma:** Vẽ diagrams và flowcharts

### Phân Bổ Điểm Số

**Mỗi thành viên sẽ được đánh giá dựa trên:**
- **50%** - Hoàn thành nhiệm vụ được giao
- **30%** - Đóng góp cho công việc chung
- **20%** - Presentation và communication skills

**Bonus points:**
- Đóng góp ý tưởng sáng tạo
- Hỗ trợ thành viên khác
- Quality của deliverables

---

## HOÀN THIỆN VÀ NỘP BÀI (Ngày 41-50)

### Công Việc Chung (Tất cả thành viên)

**Ngày 41-45:**
- Hoàn thiện tất cả implementations
- Test và debug toàn bộ system
- Review và cập nhật documentation

**Ngày 46-48:**
- Viết báo cáo cuối cùng
- Chuẩn bị presentation slides
- Tạo demo videos

**Ngày 49-50:**
- Final review và polish
- Submit deliverables
- Chuẩn bị presentation

### Deliverables Cuối Cùng

1. **GitHub Repository** với tất cả source code
2. **PDF Report** chi tiết về toàn bộ dự án (40-50 trang)
3. **Presentation Slides** cho buổi thuyết trình (20-25 slides)
4. **Demo Videos** backup cho presentation
5. **Individual Contribution Report** - Báo cáo đóng góp từng thành viên

---

## CÔNG CỤ VÀ TÀI NGUYÊN CẦN THIẾT

### Software Tools:
- **SageMath** hoặc **Python** với thư viện lattice
- **Burp Suite Professional**
- **Android Studio** và emulator
- **Git** và GitHub
- **LaTeX** hoặc **Word** cho báo cáo

### Learning Resources:
- **[HPS08]** - Hoffstein, Pipher, Silverman - "An Introduction to Mathematical Cryptography"
- **Cryptohack.org** - Practice platform
- **OWASP** documentation
- **Burp Suite** official documentation

### Hardware Requirements:
- Computer với RAM ít nhất 8GB
- Stable internet connection
- Storage space ít nhất 50GB

---

## LƯU Ý QUAN TRỌNG

### Thời Gian:
- **Bắt đầu ngay** - Dự án 45-50 ngày cần làm việc hiệu quả
- **Tuân thủ timeline** - Mỗi giai đoạn có deadline rõ ràng
- **Backup thường xuyên** - Lưu trữ code và documents

### Làm Việc Nhóm:
- **Communication** - Giao tiếp thường xuyên và rõ ràng
- **Collaboration** - Hỗ trợ lẫn nhau, không để ai bị tụt lại
- **Accountability** - Mỗi người chịu trách nhiệm về phần việc của mình

### Chất Lượng:
- **Documentation** - Ghi chú chi tiết mọi bước
- **Code quality** - Viết code sạch, có comments
- **Testing** - Test kỹ lưỡng trước khi submit
- **Peer review** - Review code và báo cáo của nhau

---

## MỤC TIÊU HỌC TẬP

Sau khi hoàn thành dự án này, nhóm sẽ có:

1. **Kiến thức sâu về lattice-based cryptography**
2. **Kỹ năng phân tích và tấn công mật mã cổ điển**
3. **Kinh nghiệm làm việc nhóm hiệu quả**
4. **Kỹ năng quản lý dự án và timeline**
5. **Khả năng viết báo cáo kỹ thuật chuyên nghiệp**
6. **Kỹ năng presentation và communication**

---

**Chúc bạn thành công với dự án này!**
