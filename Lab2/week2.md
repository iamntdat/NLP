# Báo cáo triển khai Vectorizer và CountVectorizer

## Tổng quan
Dự án này triển khai giao diện `Vectorizer` và lớp `CountVectorizer` để chuyển đổi văn bản thành biểu diễn vector đếm, sử dụng `RegexTokenizer` từ Lab 1.

## Các thành phần chính
1. **Vectorizer Interface** (`src/core/interfaces.py`):
   - Xác định giao diện trừu tượng với các phương thức: `fit`, `transform`, và `fit_transform`.
   - Đảm bảo tính mô-đun và khả năng mở rộng cho các triển khai vectorizer khác.

2. **CountVectorizer Implementation** (`src/representations/count_vectorizer.py`):
   - Kế thừa từ `Vectorizer`, sử dụng `RegexTokenizer` để token hóa văn bản.
   - Xây dựng từ vựng (`vocabulary_`) từ các token duy nhất trong tập hợp tài liệu.
   - Chuyển đổi tài liệu thành vector đếm dựa trên từ vựng đã học.

3. **Kiểm tra** (`test/lab2_test.py`):
   - Khởi tạo `CountVectorizer` với `RegexTokenizer`.
   - Kiểm tra trên tập hợp tài liệu mẫu:
     ```
     ["I love NLP.", "I love programming.", "NLP is a subfield of AI."]
     ```
   - In từ vựng đã học và ma trận tài liệu-từ (document-term matrix).

## Kết quả
- Triển khai thành công `CountVectorizer`, tạo ra các vector đếm chính xác.
- Từ vựng được sắp xếp và ánh xạ sang các chỉ số nguyên duy nhất.
- Ma trận tài liệu-từ phản ánh số lần xuất hiện của các token trong từng tài liệu.

## Hướng dẫn chạy
Chạy file kiểm tra:
```bash
python test/lab2_test.py