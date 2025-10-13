# Bài Tập 2: Mật Mã Đối Xứng

## 1. Tính Giả Ngẫu Nhiên (Pseudorandomness)

### Câu 1. (10 điểm) Bộ Sinh Giả Ngẫu Nhiên (Pseudorandom Generators - PRGs)

**(a) (5 điểm)** Giải thích các hạn chế của mã hóa một lần (one-time pad) đối với việc mã hóa thực tế và tại sao các bộ sinh giả ngẫu nhiên (PRGs) lại cần thiết trong các hệ thống mật mã hiện đại.

**(b) (5 điểm)** Phân tích các tác động bảo mật của cấu trúc PRG sau đây, trong đó G là một PRG an toàn:

```
H(S) = A‖B‖C‖D trong đó A‖B = G(S) và C‖D = G(B)
```

Xác định xem H có phải là một PRG an toàn hay không. Nếu không, hãy cung cấp một bộ phân biệt (distinguisher) có thể phân biệt H(S) với một chuỗi thực sự ngẫu nhiên với lợi thế không đáng kể (non-negligible advantage).

### Câu 2. (10 điểm) Hàm Giả Ngẫu Nhiên và Hoán Vị (Pseudorandom Functions and Permutations)

**(a) (5 điểm)** Xét cấu trúc PRF sau: `F(K, X) = G(K) ⊕ X`, trong đó G là một PRG an toàn. F có phải là một PRF an toàn không? Nếu không, hãy mô tả một bộ phân biệt có thể phân biệt hiệu quả F với một hàm ngẫu nhiên.

**(b) (5 điểm)** So sánh và đối chiếu PRFs và PRPs:

1. Giải thích các khác biệt chính trong định nghĩa và thuộc tính của chúng.
2. Mô tả cách PRPs có thể được "hạ cấp" thành PRFs, nhưng không nhất thiết ngược lại.
3. Giải thích tại sao va chạm (collisions) là không thể tránh khỏi đối với PRFs nhưng không phải đối với PRPs.


## 2. Tấn Công Văn Bản Rõ Đã Chọn và Văn Bản Mã Hóa Đã Chọn

### Câu 1. (10 điểm) Bảo Mật CPA (Chosen-Plaintext Attack)

**(a) (5 điểm)** Xét định nghĩa bảo mật CPA:

```
ℒ_Σ^cpa-real                    ℒ_Σ^cpa-rand
K ↞ Σ.𝒦                         cpa.enc(M):
cpa.enc(M):                       C ↞ Σ.𝒞(|M|)
  C ≔ Σ.Enc(K, M)                 return C
  return C
```

1. Giải thích tại sao các lược đồ mã hóa xác định (deterministic) luôn thất bại với bảo mật CPA.
2. Xây dựng một chương trình phân biệt đơn giản có thể phá vỡ bảo mật CPA của bất kỳ lược đồ mã hóa xác định nào.
3. Phân tích các lỗ hổng bảo mật thực tế tồn tại trong các hệ thống sử dụng mã hóa không an toàn CPA.

**(b) (5 điểm)** Đối với mỗi lược đồ mã hóa sau đây, xác định xem nó có đạt được bảo mật CPA hay không. Nếu không, hãy cung cấp một cuộc tấn công cụ thể:

1. `Enc(K, M) = (R, F(K, R) ⊕ M)` trong đó `R ↞ {0, 1}^λ` và F là một PRF an toàn.
2. `Enc(K, M) = (R, F(K, M) ⊕ R)` trong đó `R ↞ {0, 1}^λ` và F là một PRF an toàn.
3. AES ở chế độ Electronic Codebook (ECB).
4. AES ở chế độ Counter (CTR) với IV được chọn ngẫu nhiên.

### Câu 2. (10 điểm) Bảo Mật CCA và Mã Hóa Xác Thực

**(a) (3 điểm)** Tấn công oracle định dạng (Format oracle attacks):

1. Giải thích cách tấn công null-oracle hoạt động chống lại mã hóa chế độ CTR và tại sao nó lại tàn phá mặc dù chế độ CTR an toàn CPA.
2. Mô tả một kịch bản thực tế trong đó một oracle định dạng có thể bị lộ vô tình trong một hệ thống mật mã.
3. Tính toán số lượng truy vấn oracle gần đúng cần thiết để khôi phục một tệp 1 KB bằng cách sử dụng tấn công null-oracle, và giải thích tại sao điều này khả thi đối với kẻ tấn công.

**(b) (4 điểm)** Đối với các cấu trúc lược đồ mã hóa sau, xác định xem mỗi cấu trúc có cung cấp bảo mật CCA và/hoặc mã hóa xác thực (AE) hay không. Biện minh cho câu trả lời của bạn với giải thích ngắn gọn:

1. **Encrypt-then-MAC**: `C = Enc(K_e, M), T = MAC(K_m, C)`, đầu ra `(C, T)`
2. **Encrypt-and-MAC**: `C = Enc(K_e, M), T = MAC(K_m, M)`, đầu ra `(C, T)`
3. **MAC-then-encrypt**: `T = MAC(K_m, M), C = Enc(K_e, M‖T)`, đầu ra `C`
4. Giải thích một kịch bản trong đó các cuộc tấn công phát lại (replay attacks) có thể thành công ngay cả đối với một hệ thống sử dụng mã hóa xác thực, và cách dữ liệu liên kết (associated data - AD) giải quyết lỗ hổng này.

**(c) (3 điểm)** AES-GCM (Galois/Counter Mode):

1. Giải thích cách AES-GCM kết hợp mã hóa chế độ CTR với phép nhân trường Galois để xác thực. Điều này cung cấp những lợi thế bảo mật gì so với việc sử dụng các thuật toán mã hóa và MAC riêng biệt?
2. Mô tả các tác động bảo mật nghiêm trọng của việc tái sử dụng nonce trong AES-GCM. Những lỗ hổng cụ thể nào phát sinh khi cùng một nonce được sử dụng cho nhiều thông điệp?
3. AES-GCM đôi khi được triển khai với các độ dài thẻ (tag) khác nhau. Phân tích sự đánh đổi bảo mật khi sử dụng thẻ 128-bit so với thẻ 64-bit hoặc 32-bit.
4. Ngoài việc tái sử dụng nonce, lỗ hổng bất ngờ nào trong AES-GCM mà các nhà phát triển và kỹ sư có thể không biết, nhưng có thể ảnh hưởng đáng kể đến bảo mật phần mềm của họ?


## 3. Hàm Băm Chống Va Chạm (Collision-Resistant Hash Functions)

### Câu 1. (15 điểm) Thuộc Tính Hàm Băm

**(a) (5 điểm)** Khả năng chống va chạm (Collision resistance):

1. Giải thích tại sao va chạm phải tồn tại trong bất kỳ hàm băm nào ánh xạ đầu vào có độ dài tùy ý sang đầu ra có độ dài cố định.
2. Sử dụng nghịch lý sinh nhật (birthday paradox), tính toán xấp xỉ số lượng băm phải được tính để tìm va chạm với xác suất 50% trong một hàm băm an toàn 256-bit.
3. Mô tả một kịch bản tấn công thực tế trong đó việc tìm va chạm băm sẽ làm tổn hại đến một hệ thống bảo mật.

**(b) (5 điểm)** Cấu trúc hàm băm:

1. So sánh và đối chiếu cấu trúc Merkle-Damgård (được sử dụng trong SHA-2) và cấu trúc Sponge (được sử dụng trong SHA-3).
2. Giải thích cách các cuộc tấn công mở rộng độ dài (length extension attacks) hoạt động chống lại các hàm băm Merkle-Damgård và tại sao cấu trúc Sponge lại kháng được các cuộc tấn công này.
3. Mô tả cấu trúc HMAC và giải thích cách nó bảo vệ chống lại các cuộc tấn công mở rộng độ dài.

**(c) (5 điểm)** Sự phát triển của hàm băm:

1. Mô tả các cuộc tấn công thành công chống lại MD5 và SHA-1 dẫn đến việc chúng bị loại bỏ.
2. Giải thích khái niệm va chạm tiền tố đã chọn (chosen-prefix collisions) và tại sao chúng đặc biệt nguy hiểm đối với các cơ quan cấp chứng chỉ.
3. So sánh bảo mật của SHA-2 và SHA-3 chống lại các kỹ thuật phân tích mật mã đã biết.

### Câu 2. (15 điểm) Băm Mật Khẩu (Password Hashing)

**(a) (5 điểm)** Đối với mỗi cách lưu trữ mật khẩu sau đây, hãy phân tích các tác động bảo mật nếu cơ sở dữ liệu máy chủ bị xâm phạm:

1. Lưu trữ mật khẩu dưới dạng văn bản thuần túy (plaintext).
2. Mã hóa mật khẩu với khóa được lưu trữ trên cùng một máy chủ.
3. Lưu trữ băm SHA-256 không có muối (unsalted) của mật khẩu.
4. Lưu trữ băm SHA-256 có muối (salted) của mật khẩu.
5. Sử dụng một hàm băm mật khẩu chuyên dụng như Scrypt.

**(b) (5 điểm)** Muối (Salting):

1. Giải thích cách muối bảo vệ chống lại các cuộc tấn công tính toán trước như bảng cầu vồng (rainbow tables).
2. Tính toán yêu cầu lưu trữ cho các băm mật khẩu có muối phù hợp, giả sử có 10.000 người dùng, muối 16-byte và đầu ra băm 32-byte.
3. Mô tả các thực hành tốt nhất để tạo và lưu trữ muối.

**(c) (5 điểm)** Hàm băm mật khẩu chuyên dụng:

1. Giải thích tại sao các hàm khó bộ nhớ (memory-hard functions) như Scrypt cung cấp bảo vệ tốt hơn chống lại các cuộc tấn công phần cứng chuyên dụng so với PBKDF2.
2. Mô tả cách mỗi tham số của Scrypt (N, r, p) ảnh hưởng đến bảo mật và hiệu suất của nó.
3. So sánh tốc độ tương đối của SHA-256, PBKDF2 và Scrypt để băm mật khẩu, và giải thích các tác động bảo mật của những khác biệt về tốc độ này.


## 4. Nghiên Cứu Điển Hình Mật Mã Ứng Dụng

### Câu 1. (10 điểm) Phân Tích Các Chế Độ Mã Khối

Với tham chiếu đến các chế độ mã khối được đề cập trong bài giảng của chúng ta, hãy phân tích các kịch bản sau:

**(a)** Một ứng dụng lưu trữ tệp an toàn cần mã hóa các tệp người dùng lưu trữ. So sánh các chế độ CBC, CTR và AES-GCM cho ứng dụng này, thảo luận về:

- Tác động hiệu suất đối với các tệp lớn.
- Lan truyền lỗi nếu các phần của văn bản mã hóa bị hỏng.
- Các tác động bảo mật của việc tái sử dụng IV/nonce.
- Đảm bảo tính toàn vẹn dữ liệu và lợi thế của mã hóa xác thực với AES-GCM.

**(b)** Một ứng dụng nhắn tin thời gian thực cần mã hóa các tin nhắn ngắn với độ trễ tối thiểu. So sánh các chế độ CBC, CTR và AES-GCM cho ứng dụng này, thảo luận về:

- Khả năng song song hóa cho mã hóa/giải mã.
- Tính phù hợp cho dữ liệu phát trực tuyến (streaming).
- Bảo vệ chống lại các cuộc tấn công văn bản mã hóa đã chọn.
- Cách AES-GCM giải quyết nhu cầu xác thực so với các chế độ không xác thực.

**(c)** Cụ thể đối với AES-GCM:

- Giải thích tác động bảo mật của việc tái sử dụng nonce trong AES-GCM so với việc tái sử dụng nonce trong chế độ CTR.
- Thảo luận về sự đánh đổi hiệu suất của AES-GCM so với việc sử dụng mã hóa riêng biệt (chế độ CTR) và xác thực (HMAC).
- Giải thích cách các thuộc tính mã hóa xác thực của AES-GCM bảo vệ chống lại các cuộc tấn công sẽ thành công chống lại các chế độ CBC hoặc CTR.

### Câu 2. (10 điểm) Phân Tích Bảo Mật Hàm Băm

Một hệ thống cập nhật phần mềm sử dụng hàm băm để xác minh tính toàn vẹn của các tải xuống. Hệ thống hoạt động như sau:

1. Nhà cung cấp phần mềm đăng các băm SHA-1 của các tệp cập nhật hợp pháp trên trang web HTTPS của họ.
2. Người dùng tải xuống tệp cập nhật qua HTTP (không phải HTTPS) để tiết kiệm băng thông.
3. Ứng dụng cập nhật xác minh tệp đã tải xuống bằng cách tính băm SHA-1 của nó và so sánh với băm thu được từ trang web HTTPS.
4. Nếu các băm khớp, bản cập nhật được cài đặt tự động.

**Phân tích hệ thống này:**

**(a)** Xác định ít nhất ba lỗ hổng bảo mật trong thiết kế này.

**(b)** Đối với mỗi lỗ hổng, mô tả một kịch bản tấn công cụ thể.

**(c)** Đề xuất cải tiến để giải quyết từng lỗ hổng trong khi vẫn duy trì hiệu suất và khả năng sử dụng.

**(d)** Thiết kế một hệ thống thay thế an toàn hơn bằng cách sử dụng các nguyên thủy mật mã hiện đại được thảo luận trong lớp.
### Câu 3. (10 điểm) Thiết Kế Hệ Thống Quản Lý Mật Khẩu

Bạn đang thiết kế một hệ thống quản lý mật khẩu cho một ứng dụng web mới với các yêu cầu sau:

- Người dùng phải có khả năng khôi phục tài khoản của họ một cách an toàn nếu họ quên mật khẩu.
- Hệ thống phải kháng được các cuộc tấn công từ điển ngoại tuyến (offline dictionary attacks) nếu cơ sở dữ liệu bị xâm phạm.
- Hệ thống phải hỗ trợ xác thực hiệu suất cao cho một cơ sở người dùng lớn.
- Hệ thống nên phát hiện và ngăn chặn các cuộc tấn công nhồi thông tin đăng nhập (credential stuffing attacks).

**Thiết kế và phân tích một giải pháp hoàn chỉnh:**

**(a)** Chỉ rõ các nguyên thủy mật mã nào bạn sẽ sử dụng để lưu trữ mật khẩu và tại sao.

**(b)** Mô tả cơ chế khôi phục mật khẩu của bạn và phân tích các thuộc tính bảo mật của nó.

**(c)** Giải thích cách hệ thống của bạn cân bằng các yêu cầu về bảo mật và hiệu suất.

**(d)** Phân tích các lỗ hổng tiềm ẩn trong thiết kế của bạn và cách chúng được giảm thiểu.

## Câu Hỏi Thưởng

### Câu 1. (10 điểm (thưởng))

Bảo mật của AES và các mã khối khác phụ thuộc vào khả năng chống lại các hình thức phân tích mật mã khác nhau. Nghiên cứu và phân tích một trong các cuộc tấn công nâng cao sau:

**(a)** **Tấn công kênh bên (Side-channel attacks)**: Giải thích cách các cuộc tấn công thời gian, phân tích công suất hoặc tấn công bộ nhớ đệm có thể rò rỉ thông tin về khóa mã hóa trong các triển khai thực tế của AES.

**(b)** **Tấn công khóa liên quan (Related-key attacks)**: Mô tả cách các cuộc tấn công khóa liên quan hoạt động chống lại mã khối và tại sao chúng quan trọng ngay cả khi việc sử dụng bình thường chỉ liên quan đến các khóa không liên quan.

**(c)** **Tấn công lượng tử (Quantum attacks)**: Phân tích tác động của thuật toán Grover đối với bảo mật của AES với các kích thước khóa khác nhau (128, 192, 256 bit) và thảo luận về các khuyến nghị độ dài khóa hậu lượng tử phù hợp.

**Câu trả lời của bạn nên bao gồm**: mô tả về cuộc tấn công, tính khả thi thực tế của nó, các ví dụ có liên quan về việc triển khai thành công chống lại các hệ thống thực tế, và các biện pháp đối phó phù hợp.