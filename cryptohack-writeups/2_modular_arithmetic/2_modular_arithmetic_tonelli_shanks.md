# Tonelli–Shanks: Square roots mod prime (p ≡ 1 mod 4)

**File name:** `modular_arithmetic_tonelli_shanks.md`

## 1) Bối cảnh & lý thuyết
- Với prime \(p\), kiểm tra \(a\) có là bình phương mod \(p\) không bằng ký hiệu **Legendre**:
  \((a/p) \equiv a^{(p-1)/2} \ (\bmod\ p)\).
- Nếu \(p \equiv 3 \ (\bmod\ 4)\): căn bậc hai của \(a\) (QR) là \(r \equiv a^{(p+1)/4} \pmod p\).
- Nếu \(p \equiv 1 \ (\bmod\ 4)\): dùng **Tonelli–Shanks** để tính \(r\) với độ phức tạp đa thức (rất nhanh trong thực tế).
- Hai nghiệm luôn là \(r\) và \(p-r\). Bài yêu cầu **nghiệm nhỏ hơn**.

## 2) Dữ liệu
- \(p\): prime 2048-bit (ở đây \(p \equiv 1 \pmod 4\)).
- \(a\): số cần lấy căn bậc hai mod \(p\).

## 3) Cách làm
1. Dùng **Legendre** để khẳng định \(a\) là **quadratic residue**.
2. Chạy **Tonelli–Shanks** để tìm một nghiệm \(r\).
3. Hai nghiệm là \(r\) và \(p-r\). Chọn **nghiệm nhỏ hơn** làm flag.
4. Kiểm chứng: \((\text{root})^2 \equiv a \pmod p\).

## 4) Kết quả
- Tính được hai nghiệm \(r\) và \(p-r\); nghiệm nhỏ hơn là:

**root_small (flag):**
2362339307683048638327773298580489298932137505520500388338271052053734747862351779647314176817953359071871560041125289919247146074907151612762640868199621186559522068338032600991311882224016021222672243139362180461232646732465848840425458257930887856583379600967761738596782877851318489355679822813155123045705285112099448146426755110160002515592418850432103641815811071548456284263507805589445073657565381850521367969675699760755310784623577076440037747681760302434924932113640061738777601194622244192758024180853916244427254065441962557282572849162772740798989647948645207349737457445440405057156897508368531939120

(Đã kiểm chứng \(\text{root\_small}^2 \equiv a \ (\bmod\ p)\).)