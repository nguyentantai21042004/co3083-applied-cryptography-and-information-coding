# Tóm tắt Cập nhật Guide - Summary of Updates

## Những gì đã được cập nhật / What Has Been Updated

### 1. ✅ Cập nhật Vị trí APK / APK Location Updated

**Trước đây / Before:**
- Guide chỉ nói về clone từ GitHub
- Không đề cập đến APK có sẵn

**Bây giờ / Now:**
- ✅ Giải thích rõ về APK tại: `~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/burp-suite/assigment.apk`
- ✅ Hướng dẫn cài đặt APK trực tiếp
- ✅ Giải thích khi nào dùng APK, khi nào dùng source code
- ✅ Cảnh báo: APK KHÔNG ĐỦ để hoàn thành bài tập (cần source code!)

**Nơi tìm thấy trong guide / Where to find in guide:**
- Section "Điều kiện Tiên quyết" → Mục 4
- Section "Bước 3: Cài đặt SMC Client App" → TÙY CHỌN A

---

### 2. ✅ Giải thích về Temporary vs Project on Disk / Burp Project Persistence

**Câu hỏi của bạn / Your Question:**
> "some place tell me start temporary project, so if i out and in again, it still have ??"

**Trước đây / Before:**
- Guide chỉ nói "Chọn Temporary project"
- Không giải thích điều gì xảy ra khi thoát

**Bây giờ / Now:**
- ✅ Giải thích CHI TIẾT về Temporary Project vs Project on Disk
- ✅ Cảnh báo: Temporary Project **MẤT TẤT CẢ DỮ LIỆU** khi thoát
- ✅ Khuyến nghị: Dùng "New Project on Disk" để lưu dữ liệu
- ✅ Hướng dẫn cách lưu project: `~/Desktop/burp-setup/projects/smc-task-3.1.burp`
- ✅ Hướng dẫn cách mở lại project đã lưu

**Nơi tìm thấy trong guide / Where to find in guide:**
- Section "Bước 1: Cài đặt và Cấu hình Burp Suite" → Mục 1.2

---

## Câu trả lời cho Câu hỏi của Bạn / Answers to Your Questions

### Q1: APK ở đâu và dùng như thế nào?

**A:** APK của bạn ở đây:
```
~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/burp-suite/assigment.apk
```

**Cài đặt nhanh:**
```bash
adb install -r ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/burp-suite/assigment.apk
```

**Nhưng nhớ:** APK này CHỈ để test nhanh. Bạn VẪN CẦN clone source code để hoàn thành bài tập!

---

### Q2: Nếu dùng Temporary Project, thoát ra vào lại còn dữ liệu không?

**A:** ❌ **KHÔNG!** Temporary Project sẽ **MẤT TẤT CẢ DỮ LIỆU** khi bạn thoát Burp Suite!

**Những gì bị mất:**
- ❌ HTTP history (tất cả requests/responses)
- ❌ Intercepted traffic logs
- ❌ Saved items
- ❌ Tất cả công việc của bạn!

**Giải pháp:**

**Cách 1: Dùng Project on Disk (TỐT NHẤT)**
```bash
# Lần đầu khởi động Burp:
1. Chọn "New project on disk"
2. Lưu vào: ~/Desktop/burp-setup/projects/smc-task-3.1.burp
3. Click Next → Start Burp

# Lần sau:
1. Chọn "Open existing project"
2. Chọn file: ~/Desktop/burp-setup/projects/smc-task-3.1.burp
3. Click Next → Start Burp

# ✅ Tất cả dữ liệu vẫn còn!
```

**Cách 2: Nếu đã dùng Temporary Project, SAVE trước khi thoát**
```bash
# Trong Burp Suite:
1. Proxy → HTTP history
2. Chọn tất cả requests (Cmd+A)
3. Right-click → "Save items"
4. Lưu vào file để backup

# Nhưng cách này KÉM HƠN vì phải save thủ công mỗi lần!
```

---

## So Sánh / Comparison

### APK vs Source Code

| Tiêu chí | APK có sẵn | Source Code |
|----------|------------|-------------|
| **Thời gian cài đặt** | < 1 phút | 15-30 phút |
| **Có thể test app?** | ✅ Có | ✅ Có |
| **Chặn bắt traffic?** | ✅ Có | ✅ Có |
| **Ánh xạ đến code?** | ❌ Không | ✅ Có |
| **Hoàn thành Task 3.1?** | ❌ Không đủ | ✅ Đủ |
| **Khi nào dùng?** | Test nhanh | Làm bài tập |

### Temporary Project vs Project on Disk

| Tiêu chí | Temporary Project | Project on Disk |
|----------|-------------------|-----------------|
| **Khởi động** | Rất nhanh | Hơi chậm |
| **Lưu dữ liệu?** | ❌ Không | ✅ Có |
| **Thoát ra vào lại?** | ❌ Mất hết | ✅ Giữ nguyên |
| **HTTP History?** | ❌ Mất | ✅ Lưu |
| **Cho bài tập?** | ❌ Nguy hiểm | ✅ An toàn |

---

## Khuyến nghị Cuối cùng / Final Recommendations

### Để Hoàn thành Bài tập Thành công:

```
✅ PHẢI LÀM:
1. Tạo Burp project on disk (không dùng temporary!)
   → Lưu tại: ~/Desktop/burp-setup/projects/smc-task-3.1.burp

2. Dùng APK để test nhanh ban đầu (ngày 1)
   → File: ~/Workspaces/.../burp-suite/assigment.apk

3. Clone source code để phân tích đầy đủ (ngày 2)
   → Git clone từ GitHub

4. Làm bài tập với source code (ngày 3-4)
   → Ánh xạ API calls đến code locations

❌ KHÔNG NÊN:
1. Dùng Temporary Project (sẽ mất dữ liệu!)
2. Chỉ dùng APK mà không clone source (không đủ!)
3. Thoát Burp mà không save (nếu dùng temporary)
```

---

## Nơi Đọc Chi tiết / Where to Read Details

### Trong Guide Đã Cập nhật:

1. **Về APK:**
   - Mục "Điều kiện Tiên quyết" → Phần mềm Cần thiết → Mục 4
   - Section "Bước 3" → TÙY CHỌN A

2. **Về Burp Project:**
   - Section "Bước 1" → Mục 1.2
   - Có bảng so sánh chi tiết
   - Có hướng dẫn từng bước

3. **Tài liệu Thêm:**
   - `about-apk.md` - Giải thích chi tiết về APK
   - `task-3.1-concepts.md` - Giải thích khái niệm tổng thể

---

## Câu hỏi Thường gặp / FAQ

### Q: Tôi đã dùng Temporary Project và thoát ra, làm sao lấy lại dữ liệu?
**A:** ❌ Không thể. Dữ liệu đã mất vĩnh viễn. Phải chặn bắt lại từ đầu.

### Q: Tôi có thể chỉ dùng APK để hoàn thành bài tập không?
**A:** ❌ Không. Bài tập yêu cầu ánh xạ đến source code. APK không cung cấp điều này.

### Q: Project on Disk lưu ở đâu?
**A:** Bất kỳ đâu bạn muốn. Khuyến nghị: `~/Desktop/burp-setup/projects/smc-task-3.1.burp`

### Q: File .burp có bị mất không?
**A:** Không, nó là file bình thường trên đĩa. Chỉ mất nếu bạn xóa thủ công.

### Q: Tôi nên dùng APK hay Source Code?
**A:** Dùng **CẢ HAI**:
- APK: Test nhanh ngày đầu
- Source Code: Phân tích và làm bài tập

### Q: Project on Disk chiếm bao nhiêu dung lượng?
**A:** Khoảng 10-100 MB tùy vào số lượng traffic bạn chặn bắt.

---

## Tóm tắt Ngắn gọn / Quick Summary

**2 Cập nhật chính:**

1. **APK Location:**
   - ✅ Đã thêm hướng dẫn cài đặt APK có sẵn
   - ✅ Giải thích khi nào dùng APK vs Source Code
   - ✅ Cảnh báo: APK không đủ cho bài tập hoàn chỉnh

2. **Burp Project:**
   - ✅ Giải thích Temporary vs Project on Disk
   - ✅ Cảnh báo: Temporary **MẤT DỮ LIỆU** khi thoát
   - ✅ Khuyến nghị: Dùng Project on Disk
   - ✅ Hướng dẫn save và reopen project

**Đọc guide đầy đủ tại:**
```
/Users/tantai/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/burp-suite/document/guide.md
```

---

Chúc bạn thành công với bài tập! 🚀
