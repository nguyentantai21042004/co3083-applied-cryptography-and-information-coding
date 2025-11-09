# Những Kiến Thức Lý Thuyết Cần Thiết Cho Bài 1b

## Giới Thiệu

Bài tập 1b yêu cầu tìm một đa thức tối tiểu $f(x)$ của $\alpha = 7 + \sqrt{29}$ bằng cách tái lập công thức bài toán thành một bài toán lưới (lattice problem). Để hoàn thành bài tập này, bạn cần nắm vững một số khái niệm toán học quan trọng.

---

## 1. KIẾN THỨC TOÁN HỌC CƠ BẢN (TIỀN ĐOÀN)

### 1.1 Đại Số Tuyến Tính

#### Vector Spaces (Không Gian Vectơ)
- **Định nghĩa**: Một tập hợp $V$ các phần tử gọi là vectơ với hai phép toán (cộng và nhân vô hướng) thỏa mãn các tiên đề
- **Ví dụ**: $\mathbb{R}^n$ là không gian vectơ trên trường thực
- **Ứng dụng**: Lattice là một loại không gian vectơ đặc biệt

#### Tổ Hợp Tuyến Tính (Linear Combinations)
- **Định nghĩa**: Cho vectơ $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k$, một tổ hợp tuyến tính là:
  $$\mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k$$
  trong đó $c_i$ là các hệ số vô hướng
- **Trường hợp đặc biệt**: Khi $c_i \in \mathbb{Z}$, ta có tổ hợp tuyến tính nguyên (integer linear combination)

#### Độc Lập Tuyến Tính (Linear Independence)
- **Định nghĩa**: Các vectơ $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k$ độc lập tuyến tính nếu:
  $$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \Rightarrow c_1 = c_2 = \cdots = c_k = 0$$
- **Ý nghĩa**: Không có vectơ nào có thể biểu diễn được thông qua các vectơ khác
- **Ứng dụng**: Xác định tính "độc lập" của cơ sở lattice

#### Cơ Sở (Basis)
- **Định nghĩa**: Một tập hợp vectơ $\{\mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_n\}$ gọi là cơ sở của không gian $V$ nếu:
  - Các vectơ độc lập tuyến tính
  - Mọi vectơ trong $V$ đều có thể biểu diễn được thành tổ hợp tuyến tính của chúng
- **Ví dụ**: Cơ sở tiêu chuẩn của $\mathbb{R}^2$ là $\{(1,0), (0,1)\}$
- **Ứng dụng**: Lattice có thể được biểu diễn bằng một cơ sở cụ thể

#### Hạng (Rank)
- **Định nghĩa**: Số lượng vectơ độc lập tuyến tính tối đa trong một tập hợp
- **Công thức**: Rank bằng số cột độc lập tuyến tính trong ma trận

### 1.2 Lý Thuyết Số

#### Số Hữu Tỉ vs Số Vô Tỉ
- **Số hữu tỉ**: Có thể viết dưới dạng $\frac{p}{q}$ với $p, q \in \mathbb{Z}, q \neq 0$
- **Số vô tỉ**: Không thể viết dưới dạng phân số; ví dụ: $\sqrt{29}, \pi, e$
- **Ý nghĩa**: $\sqrt{29}$ là số vô tỉ, nên $\alpha = 7 + \sqrt{29}$ cũng là số vô tỉ
- **Xấp xỉ**: Số vô tỉ có thể được xấp xỉ bằng một số thập phân với độ chính xác hữu hạn

#### Modular Arithmetic (Số Học Modular)
- **Định nghĩa**: Số học với phép toán mod; $a \equiv b \pmod{n}$ nghĩa là $a - b$ chia hết cho $n$
- **Ứng dụng**: Thường dùng trong mật mã, ít sử dụng trực tiếp trong bài 1b nhưng hữu ích trong các bài toán lattice khác

#### Ước Chung Lớn Nhất (GCD - Greatest Common Divisor)
- **Định nghĩa**: $\gcd(a, b)$ là số dương lớn nhất chia hết cả $a$ lẫn $b$
- **Thuật toán Euclidean**: Cách tính GCD hiệu quả
  ```
  gcd(a, b):
    while b ≠ 0:
      temp = b
      b = a mod b
      a = temp
    return a
  ```
- **Ứng dụng**: Xác định độc lập tuyến tính, tính định thức lattice

### 1.3 Đa Thức

#### Đa Thức Tối Tiểu (Minimal Polynomial)
- **Định nghĩa chính thức**: Cho phần tử đại số $\alpha$ trong một trường, đa thức tối tiểu là:
  - Một đa thức $f(x)$ với hệ số nguyên (hoặc hữu tỉ)
  - $f(\alpha) = 0$ (tức $\alpha$ là nghiệm của $f$)
  - Bậc của $f$ là nhỏ nhất có thể
  - Hệ số cao nhất bằng 1 (monic polynomial)

#### Ví Dụ Đa Thức Tối Tiểu
- Cho $\alpha = \sqrt{2}$:
  - $f(x) = x^2 - 2$ vì $(\sqrt{2})^2 - 2 = 0$
  - Bậc là 2 (nhỏ nhất có thể vì $\sqrt{2}$ không phải hữu tỉ)

- Cho $\alpha = 7 + \sqrt{29}$:
  - Đặt $\alpha - 7 = \sqrt{29}$
  - Bình phương: $(\alpha - 7)^2 = 29$
  - Khai triển: $\alpha^2 - 14\alpha + 49 = 29$
  - Rút gọn: $\alpha^2 - 14\alpha + 20 = 0$
  - Vậy $f(x) = x^2 - 14x + 20$

#### Trường Số Đại Số (Algebraic Number Fields)
- **Định nghĩa**: Mở rộng hữu hạn của trường $\mathbb{Q}$ (số hữu tỉ)
- **Ví dụ**: $\mathbb{Q}(\sqrt{29}) = \{a + b\sqrt{29} : a, b \in \mathbb{Q}\}$ là trường các số có dạng "hữu tỉ cộng với hữu tỉ nhân $\sqrt{29}$"
- **Ý nghĩa**: $\alpha = 7 + \sqrt{29}$ thuộc trường $\mathbb{Q}(\sqrt{29})$

#### Đặc Trưng Nguyên (Algebraic Integer)
- **Định nghĩa**: Một số đại số là đặc trưng nguyên nếu nó là nghiệm của một đa thức có hệ số nguyên và hệ số cao nhất bằng 1
- **Ví dụ**: $\alpha = 7 + \sqrt{29}$ là đặc trưng nguyên vì nó thỏa $x^2 - 14x + 20 = 0$ (hệ số nguyên, monic)
- **Ý nghĩa**: Đặc trưng nguyên là các "số nguyên" trong lý thuyết số đại số

---

## 2. KIẾN THỨC LATTICE (CỐT LÕI)

### 2.1 Định Nghĩa Lattice

#### Lattice Là Gì?
- **Định nghĩa hình thức**: Cho một tập hợp vectơ $\mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_k \in \mathbb{R}^n$ độc lập tuyến tính, lattice $\Lambda$ sinh bởi chúng là:
  $$\Lambda = \{n_1 \mathbf{b}_1 + n_2 \mathbf{b}_2 + \cdots + n_k \mathbf{b}_k : n_i \in \mathbb{Z}\}$$
  Tức là tập tất cả các tổ hợp tuyến tính nguyên của các vectơ cơ sở

#### Ví Dụ Lattice
- **Lattice 1D**: $\Lambda = \{n \cdot 1 : n \in \mathbb{Z}\} = \mathbb{Z}$ (các số nguyên)
- **Lattice 2D**: $\Lambda = \{(n, m) : n, m \in \mathbb{Z}\} = \mathbb{Z}^2$ (lưới điểm nguyên trên mặt phẳng)
- **Lattice tổng quát**: Có thể có cơ sở không trực giao

#### Cơ Sở Lattice (Basis)
- **Định nghĩa**: Một cơ sở của lattice $\Lambda$ là một tập hợp các vectơ sinh ra $\Lambda$ thông qua tổ hợp tuyến tính nguyên
- **Tính chất quan trọng**: Một lattice có thể có nhiều cơ sở khác nhau
- **Mối liên hệ**: Nếu $\mathbf{B}$ và $\mathbf{B}'$ là hai cơ sở của cùng một lattice, thì chúng liên hệ bởi một ma trận unimodular (có định thức ±1)

#### Định Thức Lattice (Determinant / Volume)
- **Định nghĩa**: Nếu lattice $\Lambda$ sinh bởi ma trận cơ sở $B$ (các vectơ cơ sở là các hàng), thì:
  $$\det(\Lambda) = |\det(B)|$$
- **Ý nghĩa**: Đo "kích thước" của lattice; giá trị càng nhỏ thì lattice càng "dày đặc"
- **Ứng dụng**: Dùng để ước lượng kích thước của vectơ ngắn nhất

### 2.2 Các Bài Toán Lattice

#### Bài Toán Vectơ Ngắn Nhất (SVP - Shortest Vector Problem)
- **Định nghĩa**: Cho một lattice $\Lambda$, tìm vectơ khác không $\mathbf{v} \in \Lambda$ sao cho:
  $$\|\mathbf{v}\| \leq \|\mathbf{w}\| \text{ với mọi } \mathbf{w} \in \Lambda, \mathbf{w} \neq \mathbf{0}$$
  Tức là tìm vectơ có độ dài nhỏ nhất

- **Độ khó**: SVP là bài toán NP-hard (khó giải quyết cho lattice có chiều cao)
- **Ứng dụng**: Là nền tảng của nhiều mật mã lattice-based

#### Bài Toán Vectơ Gần Nhất (CVP - Closest Vector Problem)
- **Định nghĩa**: Cho một lattice $\Lambda$ và một điểm $\mathbf{t} \notin \Lambda$, tìm vectơ $\mathbf{v} \in \Lambda$ gần nhất với $\mathbf{t}$:
  $$\|\mathbf{t} - \mathbf{v}\| \leq \|\mathbf{t} - \mathbf{w}\| \text{ với mọi } \mathbf{w} \in \Lambda$$

- **Mối liên hệ với SVP**: CVP là tổng quát hơn SVP
- **Ứng dụng**: Giải mã các mã lỗi, cryptanalysis

#### Approximate-SVP
- **Định nghĩa**: Tìm một vectơ $\mathbf{v} \in \Lambda$ sao cho:
  $$\|\mathbf{v}\| \leq \gamma \cdot \lambda_1$$
  trong đó $\lambda_1$ là độ dài của vectơ ngắn nhất, và $\gamma > 1$ là một hệ số xấp xỉ

- **Ý nghĩa**: Bài toán dễ hơn SVP, nhưng vẫn hữu ích thực tế
- **Ứng dụng**: Thuật toán LLL giải quyết Approximate-SVP với $\gamma \approx 2^{n/2}$

### 2.3 Chuẩn Euclid

#### Định Nghĩa Chuẩn Euclid
- **Công thức**: Cho vectơ $\mathbf{v} = (v_1, v_2, \ldots, v_n) \in \mathbb{R}^n$:
  $$\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}$$

- **Tính chất**: 
  - $\|\mathbf{v}\| \geq 0$ với mọi $\mathbf{v}$, và $\|\mathbf{v}\| = 0$ khi và chỉ khi $\mathbf{v} = \mathbf{0}$
  - $\|c\mathbf{v}\| = |c| \|\mathbf{v}\|$ (tính nhất quán)
  - $\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$ (bất đẳng thức tam giác)

#### Ví Dụ Tính Chuẩn
- $\mathbf{v} = (3, 4)$: $\|\mathbf{v}\| = \sqrt{9 + 16} = \sqrt{25} = 5$
- $\mathbf{v} = (1, 1, 1)$: $\|\mathbf{v}\| = \sqrt{1 + 1 + 1} = \sqrt{3} \approx 1.732$

#### Chiều Dài Kỳ Vọng Theo Gauss (Gaussian Expected Shortest Length)
- **Công thức gần đúng**: Cho một lattice $\Lambda$ có rank $n$ và định thức $d = \det(\Lambda)$, chiều dài kỳ vọng của vectơ ngắn nhất là:
  $$\lambda_1 \approx \sqrt{\frac{n}{2\pi e}} \cdot d^{1/n}$$

- **Ý nghĩa**: Dự đoán kích thước vectơ ngắn nhất trong một lattice tương ứng
- **Ứng dụng**: Dùng để kiểm tra kết quả sau khi chạy thuật toán LLL
  - Nếu vectơ tìm được có độ dài gần bằng Gaussian heuristic, thì nó gần như chắc chắn là vectơ ngắn nhất thực sự

---

## 3. THUẬT TOÁN LLL (CHÍNH)

### 3.1 Giới Thiệu Thuật Toán LLL

#### Lịch Sử
- **Được phát triển**: Năm 1982 bởi Lenstra, Lenstra, và Lovász
- **Tên gọi**: LLL viết tắt từ ba tên của các tác giả
- **Ý nghĩa**: Một bước ngoặt trong lý thuyết lattice, làm cho việc giải Approximate-SVP trở nên khả thi trong thực tế

#### Mục Tiêu
- **Input**: Một cơ sở tùy ý của một lattice (có thể không "tốt")
- **Output**: Một cơ sở "giảm" (reduced basis) với các tính chất:
  - Các vectơ gần như trực giao với nhau
  - Vectơ đầu tiên có độ dài gần bằng vectơ ngắn nhất của lattice

#### Tính Chất Quan Trọng
- **Độ phức tạp**: Chạy trong thời gian đa thức: $O(n^4 m \log B)$ (n = chiều, m = số vectơ, B = bit-length)
- **Tính thực tế**: Chạy nhanh trên thực tế, là thuật toán chuẩn được sử dụng rộng rãi
- **Ưu điểm**: Không cần giải bất kỳ bài toán khó nào, chỉ sử dụng phép toán đại số tuyến tính

### 3.2 Cơ Sở Trực Giao (Orthogonal Basis)

#### Định Nghĩa Cơ Sở Trực Giao
- **Định nghĩa**: Một tập hợp vectơ $\{\mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_n\}$ gọi là trực giao nếu:
  $$\mathbf{b}_i \cdot \mathbf{b}_j = 0 \text{ với mọi } i \neq j$$
  Tức là các vectơ vuông góc với nhau

#### Cơ Sở Trực Chuẩn (Orthonormal Basis)
- **Định nghĩa**: Một cơ sở vừa trực giao vừa có mỗi vectơ có độ dài bằng 1
- **Ví dụ**: Cơ sở tiêu chuẩn $\{(1,0), (0,1)\}$ của $\mathbb{R}^2$ là trực chuẩn

#### Quá Trình Gram-Schmidt
- **Mục đích**: Chuyển một cơ sở tùy ý thành cơ sở trực giao
- **Công thức**: Cho cơ sở $\{\mathbf{b}_1, \mathbf{b}_2, \ldots\}$, cơ sở trực giao $\{\mathbf{b}_1^*, \mathbf{b}_2^*, \ldots\}$ được tính như sau:
  - $\mathbf{b}_1^* = \mathbf{b}_1$
  - $\mathbf{b}_2^* = \mathbf{b}_2 - \frac{\mathbf{b}_2 \cdot \mathbf{b}_1^*}{\mathbf{b}_1^* \cdot \mathbf{b}_1^*} \mathbf{b}_1^*$
  - $\mathbf{b}_i^* = \mathbf{b}_i - \sum_{j=1}^{i-1} \frac{\mathbf{b}_i \cdot \mathbf{b}_j^*}{\mathbf{b}_j^* \cdot \mathbf{b}_j^*} \mathbf{b}_j^*$

- **Ý nghĩa**: Loại bỏ thành phần "dư thừa" từ các vectơ

### 3.3 Điều Kiện Giảm LLL

#### Điều Kiện δ-LLL (delta-LLL)
- **Công thức**: Một cơ sở được gọi là δ-LLL reduced (với $0.25 < \delta < 1$, thường $\delta = 0.75$) nếu:
  - **Điều kiện 1 (Lovász condition)**: 
    $$\|\mathbf{b}_{i+1}^* + \mu_{i+1,i} \mathbf{b}_i^*\|^2 \geq \delta \|\mathbf{b}_i^*\|^2$$
    trong đó $\mu_{i+1,i}$ là hệ số trong quá trình Gram-Schmidt
  - **Điều kiện 2**: Các vectơ được sắp xếp theo độ dài tăng dần (gần như)

#### Ý Nghĩa Điều Kiện
- Đảm bảo rằng các vectơ gần như trực giao
- Đảm bảo rằng vectơ đầu tiên không quá dài

### 3.4 Đặc Tính của LLL-Reduced Basis

#### Tính Chất 1: Vectơ Đầu Tiên Ngắn
- **Định lý**: Cho lattice $\Lambda$ với cơ sở LLL-reduced, vectơ đầu tiên $\mathbf{b}_1$ thỏa mãn:
  $$\|\mathbf{b}_1\| \leq 2^{(n-1)/2} \cdot \lambda_1$$
  trong đó $\lambda_1$ là độ dài của vectơ ngắn nhất trong $\Lambda$

- **Ý nghĩa**: Vectơ đầu tiên không quá dài so với vectơ ngắn nhất thực sự

#### Tính Chất 2: Định Thức Không Đổi
- **Tính chất**: LLL không thay đổi định thức của lattice, chỉ thay đổi cơ sở
- **Giải thích**: Phép biến đổi cơ sở sử dụng ma trận unimodular (định thức ±1)

### 3.5 Thuật Toán LLL (Pseudocode)

```
Thuật toán LLL(B, δ):
  Input: Ma trận cơ sở B, tham số 0.25 < δ < 1
  Output: Ma trận cơ sở LLL-reduced
  
  n = số hàng của B
  Tính Gram-Schmidt: B* và μ
  
  i = 2
  while i ≤ n:
    for j = i-1 down to 1:
      if |μ[i][j]| > 0.5:
        B[i] = B[i] - round(μ[i][j]) * B[j]
        Cập nhật μ
    
    if i == 1 or Lovász condition thỏa mãn:
      i = i + 1
    else:
      Hoán đổi B[i] và B[i-1]
      Cập nhật μ
      i = max(2, i-1)
  
  return B
```

### 3.6 Ứng Dụng LLL

#### Ứng Dụng 1: Tìm Các Quan Hệ Tuyến Tính Nguyên
- **Bài toán**: Cho các số $a_1, a_2, \ldots, a_n$ (thường là số thực/xấp xỉ), tìm các hệ số nguyên $c_1, c_2, \ldots, c_n$ (không đồng thời bằng 0) sao cho $c_1 a_1 + c_2 a_2 + \cdots + c_n a_n \approx 0$
- **Phương pháp LLL**: Xây dựng lattice phù hợp và sử dụng LLL để tìm vectơ ngắn nhất

#### Ứng Dụng 2: Tìm Đa Thức Tối Tiểu (Bài 1b)
- **Bài toán**: Cho xấp xỉ số $\beta$ của $\alpha = 7 + \sqrt{29}$, tìm đa thức tối tiểu
- **Phương pháp**: Xây dựng lattice sao cho một vector trong lattice tương ứng với hệ số đa thức

#### Ứng Dụng 3: Integer Relation Finding
- **Bài toán**: Tương tự ứng dụng 1, nhưng có thể áp dụng cho nhiều số
- **Công cụ**: PSLQ algorithm (cũng dựa trên LLL)

---

## 4. CÁC KHÁI NIỆM TRỰC TIẾP LIÊN QUAN ĐẾN BÀI 1b

### 4.1 Phương Pháp Tìm Đa Thức Tối Tiểu Bằng Lattice

#### Ý Tưởng Chính

**Bài toán**: Cho $\alpha = 7 + \sqrt{29}$ và xấp xỉ $\beta$ của $\alpha$ (10 chữ số thập phân), tìm đa thức $f(x) = a_0 + a_1 x + a_2 x^2 + \cdots$ sao cho $f(\alpha) = 0$

**Quan sát**:
- Nếu $f(\alpha) = 0$, thì $f(\beta)$ sẽ rất nhỏ (gần bằng 0) vì $\beta \approx \alpha$
- Do đó: $a_0 + a_1 \beta + a_2 \beta^2 + \cdots \approx 0$

**Chuyển thành bài toán lattice**:
- Tìm các hệ số nguyên $(a_0, a_1, a_2, \ldots)$ (không đồng thời bằng 0) sao cho tổ hợp tuyến tính của chúng nhỏ
- Đây chính là bài toán SVP trên một lattice được xây dựng từ $\beta$

#### Xây Dựng Lattice Basis

**Phương pháp**:
Xây dựng ma trận cơ sở $B$ có dạng:

$$B = \begin{pmatrix}
M & 0 & 0 & 0 & \cdots \\
M\beta & 1 & 0 & 0 & \cdots \\
M\beta^2 & 0 & 1 & 0 & \cdots \\
M\beta^3 & 0 & 0 & 1 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}$$

**Giải thích**:
- $M$ là một hệ số chuẩn hóa lớn (thường là $10^{10}$ hoặc lũy thừa của 10), dùng để "phóng to" độ dài
- Hàng đầu tiên: $(M, 0, 0, \ldots)$ tương ứng với "hệ số tự do" $a_0$
- Hàng thứ i: $(M\beta^{i-1}, 0, \ldots, 0, 1, 0, \ldots)$ tương ứng với "hệ số" $a_{i-1}$

**Lý do này hoạt động**:
Nếu $(a_0, a_1, a_2, \ldots) = n_1 B_1 + n_2 B_2 + \cdots$ (một vectơ trong lattice), thì:
- Từ cột thứ nhất: $a_0 \approx M(n_1 + n_2 \beta + n_3 \beta^2 + \cdots)$
- Từ các cột khác: $a_1 = n_2$, $a_2 = n_3$, ...
- Để làm cho vectơ này ngắn, cần $n_1 + n_2 \beta + n_3 \beta^2 + \cdots \approx 0$
- Điều này chính là điều kiện $a_0 + a_1 \beta + a_2 \beta^2 + \cdots \approx 0$ !

#### Quy Trình Đầy Đủ

**Bước 1: Tính xấp xỉ $\beta$**
- Tính $\alpha = 7 + \sqrt{29}$ với độ chính xác cao (10 chữ số thập phân hoặc hơn)
- Ví dụ: $\alpha \approx 12.3852813742$

**Bước 2: Quyết định bậc của đa thức**
- Phỏng đoán bậc của đa thức tối tiểu là gì?
- Với $\alpha = 7 + \sqrt{29}$: vì $\alpha - 7 = \sqrt{29}$ và $\sqrt{29}$ là căn bậc 2 (không phải căn bậc 1), nên bậc tối thiểu là 2
- Thường bắt đầu với bậc 2 hoặc 3, hoặc theo gợi ý bài toán

**Bước 3: Xây dựng ma trận lattice**
- Cho $\beta \approx 12.3852813742$ và bậc $d = 2$:
  
$$B = \begin{pmatrix}
10^{10} & 0 & 0 \\
10^{10} \times 12.3852813742 & 1 & 0 \\
10^{10} \times 12.3852813742^2 & 0 & 1
\end{pmatrix}$$

Tức là:
$$B = \begin{pmatrix}
10^{10} & 0 & 0 \\
1.23852813742 \times 10^{11} & 1 & 0 \\
1.53599768... \times 10^{11} & 0 & 1
\end{pmatrix}$$

**Bước 4: Áp dụng LLL**
- Nhập ma trận $B$ vào thuật toán LLL
- Nhận được cơ sở LLL-reduced $B'$
- Vectơ đầu tiên của $B'$ (hoặc những vectơ ngắn nhất) chứa thông tin về hệ số đa thức

**Bước 5: Trích xuất đa thức**
- Từ vectơ ngắn nhất $(v_1, v_2, v_3, \ldots)$:
  - $a_1 = v_2$ (hoặc scaling)
  - $a_2 = v_3$ (hoặc scaling)
  - $a_0 = v_1 / M$ (hoặc scaling)
- Vậy đa thức tối tiểu là $f(x) = a_0 + a_1 x + a_2 x^2$

**Bước 6: Kiểm tra**
- Kiểm tra $f(\alpha) \approx 0$:
  - $f(7 + \sqrt{29}) = a_0 + a_1(7 + \sqrt{29}) + a_2(7 + \sqrt{29})^2$
  - Nên bằng hoặc rất gần 0

- Kiểm tra với Gaussian heuristic:
  - Tính $d = \det(\Lambda)$
  - Tính $\lambda_{gauss} = \sqrt{\frac{d}{2\pi e}}$
  - So sánh với độ dài vectơ tìm được: nên gần bằng

### 4.2 Ví Dụ Cụ Thể

#### Ví Dụ: Tìm Đa Thức Tối Tiểu của $\sqrt{2}$

Cho $\alpha = \sqrt{2}$, xấp xỉ $\beta = 1.4142135623$

**Xây dựng lattice**:
$$B = \begin{pmatrix}
10^{10} & 0 \\
1.4142135623 \times 10^{10} & 1
\end{pmatrix}$$

**Áp dụng LLL**: Sẽ tìm được vectơ ngắn nhất gần như $(-2, 1)$ (sau scaling)

**Kết quả**: $(a_0, a_1, a_2) = (−2, 0, 1)$ → $f(x) = x^2 - 2$

#### Ví Dụ: Tìm Đa Thức Tối Tiểu của $7 + \sqrt{29}$

Cho $\alpha = 7 + \sqrt{29}$, xấp xỉ $\beta = 12.3852813742$

**Xây dựng lattice**: (như trên)

**Áp dụng LLL**: Sẽ tìm được vectơ ngắn nhất tương ứng với $(a_0, a_1, a_2) = (20, -14, 1)$

**Kết quả**: $f(x) = x^2 - 14x + 20$

**Kiểm tra**: $(7 + \sqrt{29})^2 - 14(7 + \sqrt{29}) + 20 = 0$ ✓

---

## 5. KIẾN THỨC LẬP TRÌNH CẦN THIẾT

### 5.1 SageMath

#### Giới Thiệu SageMath
- **Định nghĩa**: SageMath (trước gọi là SAGE) là phần mềm toán học miễn phí dựa trên Python
- **Ưu điểm**: Có sẵn hàm LLL, xử lý số đại số, tính toán độ chính xác cao
- **Trang chủ**: https://www.sagemath.org/

#### Cài Đặt
```bash
# Trên macOS với Homebrew
brew install sagemath

# Hoặc tải từ trang chủ
# Hoặc dùng Docker
docker pull sagemath/sagemath
```

#### Sử Dụng LLL trong SageMath
```python
# Tạo ma trận
B = matrix([
    [10^10, 0, 0],
    [int(10^10 * 12.3852813742), 1, 0],
    [int(10^10 * 12.3852813742^2), 0, 1]
])

# Áp dụng LLL
B_reduced = B.LLL()

# Lấy vectơ đầu tiên (vectơ ngắn nhất)
v = B_reduced[0]
print(v)

# Tính độ dài
print(v.norm())
```

### 5.2 fpylll

#### Giới Thiệu fpylll
- **Định nghĩa**: Thư viện Python binding cho fplll (thư viện C++)
- **Ưu điểm**: Nhanh hơn SageMath, có nhiều tùy chọn
- **Trang chủ**: https://github.com/fplll/fpylll

#### Cài Đặt
```bash
pip install fpylll
```

#### Sử Dụng fpylll
```python
from fpylll import IntegerMatrix, LLL

# Tạo ma trận
B = IntegerMatrix.from_matrix([
    [10**10, 0, 0],
    [int(10**10 * 12.3852813742), 1, 0],
    [int(10**10 * 12.3852813742**2), 0, 1]
])

# Áp dụng LLL
LLL.reduction(B)

# Lấy vectơ đầu tiên
v = B[0]
print(list(v))

# Tính độ dài
import math
length = math.sqrt(sum(x**2 for x in v))
print(length)
```

### 5.3 Python Cơ Bản

#### Các Thư Viện Hữu Ích
- **numpy**: Tính toán ma trận, vector
- **scipy**: Các hàm khoa học kỹ thuật
- **decimal**: Tính toán độ chính xác cao

#### Ví Dụ Tính Toán
```python
from decimal import Decimal, getcontext

# Đặt độ chính xác
getcontext().prec = 50

# Tính sqrt(29)
sqrt_29 = Decimal(29).sqrt()
alpha = Decimal(7) + sqrt_29
print(f"α = {alpha}")

# Tính α^2
alpha_squared = alpha ** 2
print(f"α² = {alpha_squared}")
```

---

## 6. BỐ CỤC KIẾN THỨC THEO GIAI ĐOẠN HỌC

### Giai Đoạn Chuẩn Bị (2-3 ngày)

**Mục tiêu**: Hiểu kiến thức toán học cơ bản

**Nội dung**:
- Đại số tuyến tính: vector spaces, basis, rank
- Đa thức và nghiệm
- Số vô tỉ và xấp xỉ

**Tài liệu**:
- Sách giáo khoa đại số tuyến tính
- Phần 1.2-1.3 của hướng dẫn này

**Đánh giá**:
- Có thể giải thích khái niệm basis, linear independence
- Có thể tính được đa thức tối tiểu của $\sqrt{2}$ bằng tay

### Giai Đoạn Lattice Cơ Bản (3-4 ngày)

**Mục tiêu**: Hiểu lattice và các bài toán lattice

**Nội dung**:
- Định nghĩa lattice
- Các bài toán SVP, CVP, Approximate-SVP
- Chuẩn Euclid và Gaussian heuristic

**Tài liệu**:
- Chương 6 của [HPS08]
- Phần 2 của hướng dẫn này

**Đánh giá**:
- Có thể vẽ một lattice 2D cơ bản
- Có thể giải thích ý nghĩa của SVP
- Có thể tính Gaussian heuristic cho một lattice đơn giản

### Giai Đoạn LLL (3-4 ngày)

**Mục tiêu**: Hiểu thuật toán LLL

**Nội dung**:
- Quá trình Gram-Schmidt
- Điều kiện δ-LLL reduced
- Pseudocode của LLL

**Tài liệu**:
- Chương 6 của [HPS08]
- Phần 3 của hướng dẫn này

**Đánh giá**:
- Có thể giải thích ý nghĩa của cơ sở trực giao
- Có thể thực hiện Gram-Schmidt cơ bản
- Có thể giải thích các bước của LLL

### Giai Đoạn Ứng Dụng (2-3 ngày)

**Mục tiêu**: Hiểu cách áp dụng LLL để tìm đa thức tối tiểu

**Nội dung**:
- Xây dựng lattice từ xấp xỉ số
- Áp dụng LLL
- Trích xuất đa thức tối tiểu
- Kiểm tra kết quả

**Tài liệu**:
- Phần 4 của hướng dẫn này
- Ví dụ trong [HPS08]

**Đánh giá**:
- Có thể xây dựng ma trận lattice từ một số xấp xỉ
- Có thể chạy LLL được
- Có thể trích xuất đa thức tối tiểu từ kết quả LLL

### Giai Đoạn Lập Trình (5-7 ngày)

**Mục tiêu**: Cài đặt giải pháp cho bài 1b

**Nội dung**:
- Setup SageMath hoặc fpylll
- Viết code để xây dựng lattice
- Áp dụng LLL
- Kiểm tra và báo cáo kết quả

**Tài liệu**:
- Phần 5 của hướng dẫn này
- Ví dụ code, tài liệu SageMath/fpylll

**Đánh giá**:
- Code chạy được
- Tìm được đa thức tối tiểu của $\alpha = 7 + \sqrt{29}$
- Kiểm tra được kết quả với Gaussian heuristic

---

## 7. TÀI LIỆU THAM KHẢO

### Sách Chính
- **[HPS08]**: Hoffstein, Pipher, Silverman - "An Introduction to Mathematical Cryptography" (Springer, 2008)
  - Chương 6: Lattice Methods
  - Chứa đầy đủ lý thuyết và ví dụ

### Bài Báo
- **Lenstra, A. K.; Lenstra, H. W.; Lovász, L.** - "Factoring polynomials with rational coefficients" (Mathematische Annalen, 1982)
  - Bài báo gốc giới thiệu LLL

### Trang Web
- **Sage Math Documentation**: https://doc.sagemath.org/
  - Hướng dẫn sử dụng SageMath
  
- **fpylll Documentation**: https://fpylll.readthedocs.io/
  - Hướng dẫn sử dụng fpylll

- **Lattice Algorithms**: https://www.lattices.science/
  - Trang tổng hợp về lattice cryptography

### Khóa Học Online
- **MIT OpenCourseWare**: Khóa học về mật mã
- **Coursera**: Cryptography I, II
- **CryptoHack**: https://cryptohack.org/ - Các bài tập thực hành

---

## 8. LƯỚI KIẾN THỨC TÓMIC TẮT

```
┌─────────────────────────────────────────────────────────────┐
│                   BÀI TẬP 1b: TÌM ĐA THỨC TỐI TIỂU          │
└─────────────────────────────────────────────────────────────┘
                              ↑
                    ┌─────────┴─────────┐
                    │                   │
          ┌─────────▼────────┐  ┌──────▼──────────┐
          │  KIẾN THỨC LLL   │  │ XÂY DỰNG LATTICE│
          └─────────▲────────┘  └────────▲────────┘
                    │                    │
          ┌─────────┴────────┐  ┌────────┴─────────┐
          │ LATTICE (SVP)    │  │ ĐA THỨC TỐI TIỂU │
          └────────▲─────────┘  └─────────▲────────┘
                   │                      │
         ┌─────────┴──────────┐  ┌────────┴──────────┐
         │ ĐLTT & CƠNG SỞ     │  │ SỐ VÔ TỈ & XẤP XỈ │
         └────────────────────┘  └───────────────────┘
```

---

## 9. LỜI KHUYÊN CHO VIỆc HỌC

1. **Bắt đầu từ cơ bản**: Không bỏ qua phần đại số tuyến tính, dù có vẻ đơn giản
2. **Hiểu ý tưởng, không chỉ công thức**: Hãy vẽ hình, tính toán bằng tay với các ví dụ nhỏ
3. **Thực hành lập trình sớm**: Chạy các ví dụ trong SageMath/fpylll càng sớm càng tốt
4. **Kiểm tra kết quả**: Luôn kiểm tra đa thức tìm được bằng cách tính $f(\alpha)$
5. **Ghi chú chi tiết**: Viết báo cáo chi tiết, giải thích từng bước

---

**Chúc bạn thành công với bài tập 1b!**
