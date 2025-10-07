# Problem Set 2: Symmetric Cryptography

## 1 Pseudorandomness

### 1. (10 points) Pseudorandom Generators

(a) (5 điểm) Giải thích những hạn chế của one-time pad trong việc mã hóa thực tiễn và lý do tại sao cần bộ sinh số giả ngẫu nhiên (PRG) trong các hệ thống mật mã hiện đại.

(b) (5 điểm) Phân tích các tác động về mặt an toàn của cấu trúc PRG sau, trong đó 𝐺 là một PRG an toàn:
$$
H(S) = A \| B \| C \| D \quad \text{với} \quad A \| B = G(S),\; C \| D = G(B)
$$
Xác định xem 𝐻 có phải là một PRG an toàn không. Nếu không, hãy đưa ra một bộ phân biệt (distinguisher) có thể phân biệt 𝐻(𝑆) với một chuỗi thực sự ngẫu nhiên với xác suất thành công không tầm thường (non-negligible advantage).

### 2. (10 điểm) Hàm giả ngẫu nhiên (PRF) và hoán vị giả ngẫu nhiên (PRP)

(a) (5 điểm) Xét hàm PRF được xây dựng như sau: 𝐹(𝐾, 𝑋) = 𝐺(𝐾) ⊕ 𝑋, trong đó 𝐺 là một bộ sinh số giả ngẫu nhiên (PRG) an toàn.
Liệu 𝐹 có phải là một PRF an toàn không? Nếu không, hãy mô tả một bộ phân biệt (distinguisher) có thể phân biệt 𝐹 với một hàm ngẫu nhiên thực sự.

(b) (5 điểm) So sánh và đối chiếu giữa PRF và PRP:
i. Giải thích sự khác biệt chính trong định nghĩa và tính chất của chúng.
ii. Mô tả cách PRP có thể được "giáng cấp" thành PRF, nhưng điều ngược lại không nhất thiết đúng.
iii. Giải thích tại sao va chạm (collision) là điều không thể tránh khỏi đối với PRF nhưng lại không xảy ra với PRP.

---

## 2 Chosen-Plaintext and Chosen-Ciphertext Attacks

### 1. (10 điểm) An toàn với CPA (Chosen-Plaintext Attack)

#### (a) (5 điểm) Định nghĩa an toàn CPA

**Mô hình CPA-thực (CPA-real World):**
\[
\mathcal{L}^{\Sigma}_{cpa\text{-}real} :
\begin{cases}
  K \leftarrow \Sigma.\mathcal{K} \\
  \text{CPA.ENC}(M): \\
  \quad C := \Sigma.\text{Enc}(K, M) \\
  \quad \text{return } C
\end{cases}
\]

**Mô hình CPA-ngẫu nhiên (CPA-rand World):**
\[
\mathcal{L}^{\Sigma}_{cpa\text{-}rand} :
\begin{cases}
  \text{CPA.ENC}(M): \\
  \quad C \leftarrow \Sigma.\mathcal{C}(|M|) \\
  \quad \text{return } C
\end{cases}
\]

Yêu cầu: 
\[
\mathcal{L}^{\Sigma}_{cpa\text{-}real} \;\approx\; \mathcal{L}^{\Sigma}_{cpa\text{-}rand}
\]
(tức là hai mô hình này không thể phân biệt được bởi bất kỳ kẻ tấn công hiệu quả nào)

**Câu hỏi:**

i. Giải thích tại sao các hệ mã hóa xác định (deterministic encryption) luôn thất bại với an toàn CPA.

ii. Xây dựng một chương trình phân biệt (distinguisher) đơn giản có thể phá vỡ an toàn CPA của bất kỳ hệ mã hóa xác định nào.

iii. Phân tích các lỗ hổng bảo mật thực tiễn có thể xảy ra trong các hệ thống sử dụng mã hóa không đạt an toàn CPA.

#### (b) (5 điểm) Đối với mỗi hệ mã hóa sau, hãy xác định xem nó có đạt được an toàn CPA hay không. Nếu không, hãy chỉ ra một tấn công cụ thể:

i. Enc(𝐾, 𝑀) = (𝑅, 𝐹(𝐾, 𝑅) ⊕ 𝑀) với 𝑅 được chọn ngẫu nhiên từ {0, 1}^𝜆 và 𝐹 là một hàm giả ngẫu nhiên (PRF) an toàn.

ii. Enc(𝐾, 𝑀) = (𝑅, 𝐹(𝐾, 𝑀) ⊕ 𝑅) với 𝑅 được chọn ngẫu nhiên từ {0, 1}^𝜆 và 𝐹 là một hàm giả ngẫu nhiên (PRF) an toàn.

iii. AES ở chế độ Electronic Codebook (ECB).

iv. AES ở chế độ Counter (CTR) với IV (vector khởi tạo) được chọn ngẫu nhiên.

### 2. (10 điểm) An toàn CCA và Mã hóa xác thực (Authenticated Encryption)

#### (a) (3 điểm) Tấn công oracle định dạng (Format oracle attacks):

i. Giải thích cách tấn công null-oracle hoạt động đối với mã hóa chế độ CTR và tại sao nó lại nguy hiểm dù CTR đạt an toàn CPA.

ii. Mô tả một kịch bản thực tế mà trong đó một format oracle có thể vô tình bị lộ ra trong một hệ thống mật mã.

iii. Tính toán xấp xỉ số lượng truy vấn oracle cần thiết để khôi phục một tệp 1 KB bằng tấn công null-oracle, và giải thích tại sao điều này lại thực tế đối với kẻ tấn công.

#### (b) (4 điểm) Với các phương pháp xây dựng hệ mã hóa sau, hãy xác định xem mỗi phương pháp có đạt được an toàn CCA và/hoặc mã hóa xác thực (AE) hay không. Giải thích ngắn gọn lý do:

i. Encrypt-then-MAC: 𝐶 = Enc(𝐾ₑ, 𝑀), 𝑇 = MAC(𝐾ₘ, 𝐶), xuất ra (𝐶, 𝑇)

ii. Encrypt-and-MAC: 𝐶 = Enc(𝐾ₑ, 𝑀), 𝑇 = MAC(𝐾ₘ, 𝑀), xuất ra (𝐶, 𝑇)

iii. MAC-then-encrypt: 𝑇 = MAC(𝐾ₘ, 𝑀), 𝐶 = Enc(𝐾ₑ, 𝑀‖𝑇), xuất ra 𝐶

iv. Giải thích một tình huống mà tấn công phát lại (replay attack) có thể thành công ngay cả khi hệ thống sử dụng mã hóa xác thực, và cách dữ liệu liên kết (Associated Data - AD) giải quyết lỗ hổng này.

#### (c) (3 điểm) AES-GCM (Galois/Counter Mode):

i. Giải thích cách AES-GCM kết hợp mã hóa chế độ CTR với phép nhân trường Galois để xác thực. Lợi thế bảo mật của phương pháp này so với việc sử dụng riêng biệt mã hóa và MAC là gì?

ii. Mô tả các hệ quả bảo mật nghiêm trọng khi tái sử dụng nonce trong AES-GCM. Những lỗ hổng cụ thể nào sẽ xuất hiện nếu cùng một nonce được dùng cho nhiều bản tin?

iii. AES-GCM đôi khi được triển khai với các độ dài thẻ xác thực (tag) khác nhau. Phân tích sự đánh đổi về bảo mật khi sử dụng tag 128-bit so với 64-bit hoặc 32-bit.

iv. Ngoài việc tái sử dụng nonce, hãy nêu một lỗ hổng bất ngờ trong AES-GCM mà các lập trình viên và kỹ sư có thể không nhận ra, nhưng có thể ảnh hưởng nghiêm trọng đến an toàn phần mềm của họ.

## 3. Hàm băm chống va chạm (Collision-Resistant Hash Functions)

### 1. (15 điểm) Các tính chất của hàm băm

#### (a) (5 điểm) Tính chống va chạm:
i. Giải thích tại sao va chạm (collision) chắc chắn tồn tại trong bất kỳ hàm băm nào ánh xạ đầu vào có độ dài tùy ý sang đầu ra có độ dài cố định.

ii. Sử dụng nghịch lý ngày sinh (birthday paradox), hãy tính xấp xỉ số lượng phép băm cần thực hiện để tìm được một va chạm với xác suất 50% đối với một hàm băm an toàn 256-bit.

iii. Mô tả một kịch bản tấn công thực tế mà việc tìm ra va chạm hàm băm sẽ làm tổn hại đến một hệ thống bảo mật.

#### (b) (5 điểm) Cấu trúc hàm băm:
i. So sánh và đối chiếu giữa cấu trúc Merkle-Damgård (được sử dụng trong SHA-2) và cấu trúc Sponge (được sử dụng trong SHA-3).

ii. Giải thích cách thức tấn công mở rộng độ dài (length extension attack) hoạt động đối với các hàm băm Merkle-Damgård và lý do tại sao cấu trúc Sponge lại chống được kiểu tấn công này.

iii. Mô tả cấu trúc HMAC và giải thích cách nó bảo vệ chống lại tấn công mở rộng độ dài.

#### (c) (5 điểm) Sự phát triển của hàm băm:
i. Mô tả các tấn công thành công vào MD5 và SHA-1 dẫn đến việc chúng bị loại bỏ.

ii. Giải thích khái niệm va chạm với tiền tố được chọn (chosen-prefix collision) và tại sao chúng đặc biệt nguy hiểm đối với các tổ chức cấp chứng chỉ số (certificate authorities).

iii. So sánh mức độ an toàn của SHA-2 và SHA-3 trước các kỹ thuật phân tích mật mã đã biết.

### 2. (15 điểm) Băm mật khẩu (Password Hashing)

### (a) (5 điểm) Phân tích các phương pháp lưu trữ mật khẩu sau đây về mặt an toàn nếu cơ sở dữ liệu máy chủ bị lộ:

i. Lưu mật khẩu ở dạng văn bản thuần túy (plaintext).  
ii. Mã hóa mật khẩu bằng một khóa được lưu trên cùng máy chủ.  
iii. Lưu trữ giá trị băm SHA-256 của mật khẩu mà không có salt.  
iv. Lưu trữ giá trị băm SHA-256 của mật khẩu có sử dụng salt.  
v. Sử dụng hàm băm mật khẩu chuyên dụng như Scrypt.

### (b) (5 điểm) Sử dụng salt:

i. Giải thích cách salt bảo vệ chống lại các tấn công tiền tính toán trước (precomputation) như bảng cầu vồng (rainbow tables).  
ii. Tính toán yêu cầu lưu trữ cho các giá trị băm mật khẩu có salt đúng cách, giả sử có 10.000 người dùng, mỗi salt dài 16 byte và mỗi giá trị băm dài 32 byte.  
iii. Mô tả các thực hành tốt nhất khi sinh và lưu trữ salt.

### (c) (5 điểm) Hàm băm mật khẩu chuyên dụng:

i. Giải thích tại sao các hàm yêu cầu bộ nhớ lớn (memory-hard) như Scrypt bảo vệ tốt hơn trước các tấn công bằng phần cứng chuyên dụng so với PBKDF2.  
ii. Mô tả cách các tham số của Scrypt (N, r, p) ảnh hưởng đến độ an toàn và hiệu năng.  
iii. So sánh tốc độ tương đối của SHA-256, PBKDF2 và Scrypt khi băm mật khẩu, và giải thích ý nghĩa an toàn của sự khác biệt về tốc độ này.

## 4. Các nghiên cứu tình huống về Mật mã ứng dụng

### 1. (10 điểm) Phân tích các chế độ hoạt động của mã khối (Block Cipher Modes)

Dựa trên các chế độ mã khối đã học trong bài giảng, hãy phân tích các tình huống sau:

#### (a) Một ứng dụng lưu trữ tệp an toàn cần mã hóa các tệp người dùng khi lưu trữ (at rest). So sánh các chế độ CBC, CTR và AES-GCM cho ứng dụng này, thảo luận về:
- Ảnh hưởng đến hiệu năng khi xử lý các tệp lớn.
- Sự lan truyền lỗi khi một phần ciphertext bị hỏng.
- Hệ quả về mặt an toàn khi tái sử dụng IV/nonce.
- Đảm bảo toàn vẹn dữ liệu và lợi ích của mã hóa xác thực (authenticated encryption) với AES-GCM.

#### (b) Một ứng dụng nhắn tin thời gian thực cần mã hóa các tin nhắn ngắn với độ trễ tối thiểu. So sánh các chế độ CBC, CTR và AES-GCM cho ứng dụng này, thảo luận về:
- Khả năng song song hóa khi mã hóa/giải mã.
- Mức độ phù hợp với dữ liệu truyền theo luồng (streaming).
- Khả năng bảo vệ trước các tấn công chọn bản mã (chosen-ciphertext attacks).
- Cách AES-GCM đáp ứng nhu cầu xác thực so với các chế độ không xác thực.

#### (c) Đối với riêng AES-GCM:
- Giải thích tác động về mặt an toàn khi tái sử dụng nonce trong AES-GCM so với tái sử dụng nonce trong chế độ CTR.
- Thảo luận về đánh đổi hiệu năng của AES-GCM so với việc sử dụng riêng biệt mã hóa (CTR mode) và xác thực (HMAC).
- Giải thích cách thuộc tính mã hóa xác thực của AES-GCM bảo vệ chống lại các tấn công mà CBC hoặc CTR có thể bị khai thác.