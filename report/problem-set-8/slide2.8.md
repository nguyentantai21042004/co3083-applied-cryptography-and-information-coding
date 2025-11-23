# Zero-Knowledge Proofs (Bằng chứng không tiết lộ tri thức)

Tài liệu đi sâu vào lý thuyết, các giao thức cụ thể, và ứng dụng thực tế của Zero-Knowledge Proofs (ZKP).

## 1. Giới thiệu về Zero-Knowledge Proofs
[cite_start]Khái niệm cơ bản giải quyết nghịch lý: "Làm thế nào để chứng minh tôi biết một bí mật mà không cần tiết lộ bí mật đó?"[cite: 19, 23].

### [cite_start]Ba tính chất cốt lõi [cite: 38]
1.  [cite_start]**Completeness (Tính đầy đủ):** Nếu tuyên bố là đúng, một người chứng minh (prover) trung thực luôn có thể thuyết phục được người kiểm tra (verifier) trung thực[cite: 40].
2.  [cite_start]**Soundness (Tính đúng đắn):** Nếu tuyên bố là sai, kẻ gian lận không thể thuyết phục người kiểm tra (trừ xác suất không đáng kể)[cite: 41].
    * [cite_start]*Knowledge Soundness (Tính đúng đắn về tri thức):* Một đảm bảo mạnh hơn, nghĩa là nếu người chứng minh thành công, họ thực sự "biết" nhân chứng (witness) và có thể trích xuất nó ra[cite: 56, 57].
3.  [cite_start]**Zero-Knowledge (Không tiết lộ tri thức):** Người kiểm tra không học được gì thêm ngoài việc tuyên bố đó là đúng[cite: 43].

### [cite_start]Ví dụ: Giao thức Schnorr [cite: 88]
Đây là giao thức nền tảng để chứng minh việc biết một khóa bí mật $a$ tương ứng với khóa công khai $A = g^a$ mà không tiết lộ $a$.

* **Quy trình:**
    1.  [cite_start]**Commitment (Cam kết):** Prover chọn số ngẫu nhiên $y$, gửi $Y = g^y$[cite: 93, 110].
    2.  [cite_start]**Challenge (Thách thức):** Verifier gửi số ngẫu nhiên $c$[cite: 97, 111].
    3.  [cite_start]**Response (Phản hồi):** Prover tính và gửi $r = (y + ca) \pmod n$[cite: 99, 112].
    4.  [cite_start]**Verification (Kiểm tra):** Verifier kiểm tra nếu $g^r \equiv Y \cdot A^c$[cite: 102].
* [cite_start]**Tại sao nó Zero-Knowledge?** Người ta có thể tạo ra một bản ghi (transcript) giả mạo trông y hệt bản ghi thật mà không cần biết $a$ bằng cách chọn $c$ và $r$ trước, sau đó tính ngược ra $Y$[cite: 134, 140]. Điều này chứng tỏ bản ghi thực tế không chứa thông tin gì về $a$.

---

## 2. Giao thức Sigma ($\Sigma$-Protocols)
[cite_start]Giao thức Schnorr là một ví dụ của khung tổng quát gọi là Giao thức Sigma, có cấu trúc 3 bước dạng "zigzag"[cite: 303, 340].

* [cite_start]**Cấu trúc:** Commit $\to$ Challenge $\to$ Respond[cite: 342].
* [cite_start]**Khả năng mở rộng:** Có thể dùng để chứng minh các quan hệ phức tạp hơn như "Tôi biết một cách tô màu đồ thị" hoặc "Tôi biết cách phân tích thừa số nguyên tố"[cite: 313, 315].
* [cite_start]**Special Soundness (Tính đúng đắn đặc biệt):** Nếu một prover có thể trả lời hai thách thức khác nhau ($c$ và $c'$) cho cùng một cam kết $Y$, ta có thể trích xuất được bí mật (witness)[cite: 476, 482].
    * [cite_start]Ví dụ trong Schnorr: Từ 2 phương trình $r = y + ca$ và $r' = y + c'a$, ta có thể giải tìm $a$[cite: 501].

---

## 3. Composition: Chứng minh AND và OR
Cách kết hợp các giao thức Sigma để chứng minh các mệnh đề logic phức tạp.

### [cite_start]OR Proofs (Chứng minh HOẶC) [cite: 587]
* [cite_start]**Mục tiêu:** Chứng minh "Tôi biết bí mật A **hoặc** bí mật B" mà không tiết lộ tôi biết cái nào[cite: 573].
* **Cơ chế:**
    * Prover thực hiện giao thức thật cho bí mật mình biết.
    * [cite_start]Đồng thời *mô phỏng* (fake) giao thức cho bí mật mình không biết[cite: 634].
    * [cite_start]Điều chỉnh sao cho tổng hai thách thức bằng thách thức của Verifier ($C_0 + C_1 = C$)[cite: 628].
* [cite_start]**Ứng dụng:** Bỏ phiếu điện tử (phiếu bầu hợp lệ là YES hoặc NO), xác thực ẩn danh[cite: 589].

### [cite_start]AND Proofs (Chứng minh VÀ) [cite: 681]
* [cite_start]**Mục tiêu:** Chứng minh nhiều điều kiện cùng đúng đồng thời[cite: 686].
* [cite_start]**Cơ chế:** Sử dụng *cùng một* thách thức $C$ cho tất cả các giao thức con[cite: 692].

---

## 4. Non-Interactive ZK (NIZK) & Fiat-Shamir
Chuyển đổi từ giao thức tương tác sang không tương tác để có thể gửi bằng chứng (proof) đi bất cứ đâu.

### [cite_start]Biến đổi Fiat-Shamir [cite: 766]
* [cite_start]**Ý tưởng:** Thay thế Verifier bằng một hàm băm mật mã (Hash function)[cite: 770].
* [cite_start]**Cách làm:** Thay vì đợi Verifier gửi $c$, Prover tự tính $c = Hash(X, Y)$[cite: 773].
* **Hệ quả:**
    * [cite_start]Tạo ra bằng chứng không cần tương tác (Non-interactive)[cite: 799].
    * [cite_start]**Mất tính chối bỏ (Deniability):** Bằng chứng Fiat-Shamir là vĩnh viễn và có thể chuyển giao, ai cũng có thể kiểm tra được, khác với giao thức tương tác nơi chỉ người tham gia mới tin[cite: 866, 880].

### [cite_start]Mô hình Mạch (Circuits) [cite: 905]
* [cite_start]Thay vì thiết kế giao thức toán học riêng cho từng vấn đề, ta chuyển vấn đề thành một mạch tính toán (circuit)[cite: 915].
* [cite_start]Chứng minh: "Tôi biết đầu vào $w$ sao cho mạch $C(x, w) = y$"[cite: 916].
* 
### [cite_start]Các cuộc tấn công vào Fiat-Shamir [cite: 1009]
* [cite_start]Tài liệu cảnh báo về lỗ hổng thực tế khi áp dụng Fiat-Shamir kết hợp với giao thức GKR (2025 attack)[cite: 1017].
* [cite_start]Kẻ tấn công có thể chèn "backdoor" vào mạch để tạo bằng chứng giả cho các mệnh đề sai[cite: 1056].
* [cite_start]Bài học: Việc triển khai thực tế (hash function, circuit design) quan trọng hơn mô hình lý thuyết Random Oracle[cite: 1087].

---

## 5. zkVMs (Máy ảo Zero-Knowledge)

* [cite_start]**Khái niệm:** Một máy ảo thực thi chương trình và tạo ra bằng chứng ZK cho việc thực thi đó[cite: 1107].
* [cite_start]**Lợi ích:** Lập trình viên có thể viết code bình thường (Rust, C++) mà không cần hiểu về mạch hay toán học mật mã[cite: 1119].
* [cite_start]**Ví dụ:** RISC Zero (cho phép viết code Rust, biên dịch và chứng minh thực thi)[cite: 1178].
* [cite_start]**Thực tế:** Hiện tại zkVM vẫn rất chậm (chậm hơn 100.000 lần so với chạy code thường) và nhiều lỗi, chưa sẵn sàng cho các hệ thống bảo mật quan trọng (Security Theater)[cite: 1231, 1233]. [cite_start]Cần nhiều năm nữa để đạt độ chín muồi[cite: 1314].

---

## 6. ZK trong Thế giới thực
### [cite_start]Zcash [cite: 1336]
* [cite_start]Tiền điện tử đầu tiên ứng dụng zk-SNARKs để ẩn thông tin người gửi, người nhận và số tiền[cite: 1347].
* [cite_start]**Cải tiến:** Từ Sprout (chậm, tốn RAM) $\to$ Sapling (nhanh hơn, dùng được trên mobile) $\to$ Halo 2 (không cần trusted setup)[cite: 1374, 1382].

### [cite_start]Xác thực định danh (Identity) [cite: 1400]
* [cite_start]Google đã mở mã nguồn thư viện ZK cho việc xác minh tuổi[cite: 1400].
* [cite_start]**Ứng dụng:** Chứng minh "Tôi trên 18 tuổi" mà không cần gửi ảnh hộ chiếu hay ngày sinh cụ thể, bảo vệ quyền riêng tư người dùng[cite: 1404].
* [cite_start]**Tương lai:** Ví định danh điện tử Châu Âu (EUDI Wallet)[cite: 1408].

### Tương lai
* [cite_start]Sự đối đầu giữa "Surveillance Capitalism" (tư bản giám sát) và "Privacy Renaissance" (phục hưng quyền riêng tư) nhờ vào công nghệ ZK[cite: 1424].