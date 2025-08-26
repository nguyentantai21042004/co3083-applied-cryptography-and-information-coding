# CO3083 - Applied Cryptography and Information Coding

## Giới thiệu

Đây là repository cá nhân chứa toàn bộ tài liệu, code và writeup cho môn học **CO3083 - Applied Cryptography and Information Coding**.

## Cấu trúc repository

### 1. Overleaf Sync (`overleaf-sync/`)
Chứa tất cả file LaTeX để sync với Overleaf:
- `current-project/` - Project hiện tại (main.tex, contents, images, outro)
- `templates/` - Templates LaTeX cho các loại tài liệu
  - `assignments/` - Templates cho bài tập
  - `reports/` - Templates cho báo cáo  
  - `presentations/` - Templates cho slide thuyết trình
  - `thesis/` - Templates cho luận văn/đồ án
- `common/` - Styles, packages và macros dùng chung

### 2. CryptoHack Writeups (`cryptohack-writeups/`)
Chứa lời giải chi tiết cho các challenge trên CryptoHack.org:
- `introduction/` - Các bài cơ bản
- `general/` - Kỹ thuật tổng quát
- `mathematics/` - Toán học mật mã
- `symmetric-ciphers/` - Mã hóa đối xứng
- `rsa/` - Thuật toán RSA
- `elliptic-curves/` - Đường cong elliptic
- `misc/` - Các bài khác
- `common/` - Utilities và templates

### 3. Test Source Code (`test-code/`)
Chứa các implementation và test code:
- `cryptography/` - Implementation các thuật toán mật mã
- `algorithms/` - Thuật toán và cấu trúc dữ liệu liên quan
- `implementations/` - Code thực hành
- `experiments/` - Thí nghiệm và benchmark
- `common/` - Libraries, configs và data dùng chung

### 4. References (`references/`)
Chứa tài liệu tham khảo và học liệu:
- `books/` - Sách giáo khoa, tham khảo (PDF/EPUB)
- `papers/` - Bài báo khoa học, research papers
- `slides/` - Slide bài giảng, presentations
- `notes/` - Ghi chú cá nhân, summaries

### 5. Other Content
- `keyword-contents/` - Báo cáo từ project cũ (có thể xóa sau)

## Cách sử dụng

1. **Overleaf Sync**: Copy toàn bộ folder `overleaf-sync/` vào Overleaf project
2. **CryptoHack**: Thêm writeup mới vào thư mục tương ứng trong `cryptohack-writeups/`
3. **Test Code**: Lưu code test và implementation vào `test-code/`
4. **References**: Lưu sách, papers, slides vào `references/` theo chủ đề

## Quy ước

- Mỗi writeup CryptoHack nên có format: `challenge-name.md` với code đi kèm
- LaTeX templates nên có documentation rõ ràng về cách sử dụng
- Test code nên có comment và README trong từng thư mục

---

*Repository này được tổ chức để hỗ trợ việc học tập môn Applied Cryptography and Information Coding.*
