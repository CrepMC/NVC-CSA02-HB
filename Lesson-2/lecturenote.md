# Ghi chú bài học Lesson 2

## 1. Tính toán trung vị (Median)

- Trung vị là giá trị ở giữa của một tập hợp số liệu đã được sắp xếp.
- Nếu số lượng phần tử là lẻ, trung vị là phần tử ở giữa.
- Nếu số lượng phần tử là chẵn, trung vị là trung bình của hai phần tử ở giữa.

### Ví dụ

```python
if (len(mathq) % 2 == 1):
    mid = len(mathq) // 2
    median = mathq[mid]
else:
    mid = len(mathq) // 2 - 1
    median = (mathq[mid] + mathq[mid + 1]) / 2
```

## 2. Danh sách và các thao tác

- Danh sách cho phép lưu trữ và thao tác với nhiều giá trị.
- Có thể thêm, xóa, và truy cập các phần tử trong danh sách.

## 3. Sử dụng thư viện statistics

- Thư viện `statistics` cung cấp các hàm hữu ích để tính toán các giá trị thống kê như trung bình, trung vị và mode.

## 4. Cấu trúc lặp

- Sử dụng vòng lặp `for` và `while` để lặp qua các phần tử trong danh sách hoặc thực hiện các hành động nhiều lần.

## Kết luận

- Bài học này đã giúp củng cố kiến thức về danh sách, các phép toán thống kê, và cách tính toán trung vị trong Python. Hãy thực hành thêm để nắm vững các khái niệm này!
