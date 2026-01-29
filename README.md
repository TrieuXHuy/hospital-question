# Công cụ Chuyển đổi Câu hỏi Trắc nghiệm Y khoa sang Định dạng Azota

## Mô tả

Công cụ này chuyển đổi danh sách câu hỏi trắc nghiệm y khoa từ định dạng bảng Word (cột phân cách bằng Tab) sang định dạng chuẩn Azota để dễ dàng copy-paste ngược lại vào Word.

## Yêu cầu hệ thống

- Python 3.x

## Cách sử dụng

### Bước 1: Chuẩn bị dữ liệu

Đảm bảo file dữ liệu nguồn của bạn có định dạng:
- Các cột được phân cách bằng ký tự Tab
- Cấu trúc: STT, Mã câu, Nội dung câu hỏi, các lựa chọn A-D, Đáp án

### Bước 2: Chạy script chuyển đổi

```bash
python3 convert_to_azota.py "PHẦN NHỚ.ini"
```

hoặc với file của bạn:

```bash
python3 convert_to_azota.py "đường_dẫn_đến_file_của_bạn.txt"
```

### Bước 3: Copy kết quả

Kết quả sẽ được hiển thị trong một code block để bạn dễ dàng copy toàn bộ.

## Định dạng đầu ra

Mỗi câu hỏi được chuyển đổi theo định dạng Azota:

```
Câu [STT] ([Mã câu]): [Nội dung câu hỏi]
A. [Lựa chọn A]
B. [Lựa chọn B]
C. [Lựa chọn C]
D. [Lựa chọn D]
Đáp án: [Chữ cái]
```

## Ví dụ

### Dữ liệu đầu vào (Tab-separated):
```
1	N1-1-001	Nguyên nhân nào dưới đây phù hợp nhất gây viêm ruột thừa cấp?
A. Nhiễm ký sinh trùng đường tiêu hoá
B. Sỏi phân trong ruột thừa và vi khuẩn
C. Viêm hạch mạc treo ruột non và vi khuẩn
D. Polip ruột và vi khuẩn	B
```

### Kết quả đầu ra (Azota format):
```
Câu 1 (N1-1-001): Nguyên nhân nào dưới đây phù hợp nhất gây viêm ruột thừa cấp?
A. Nhiễm ký sinh trùng đường tiêu hoá
B. Sỏi phân trong ruột thừa và vi khuẩn
C. Viêm hạch mạc treo ruột non và vi khuẩn
D. Polip ruột và vi khuẩn
Đáp án: B
```

## Đặc điểm

✓ Giữ nguyên nội dung chuyên môn y khoa - không tự ý sửa đổi  
✓ Định dạng chuẩn Azota  
✓ Xuất kết quả trong code block duy nhất để dễ copy  
✓ Tự động xử lý tất cả câu hỏi trong file  

## Lưu ý

- Script tự động bỏ qua dòng header
- Tất cả thuật ngữ y khoa được giữ nguyên như trong file gốc
- Kết quả được in ra stdout (màn hình) trong code block để dễ dàng copy

## Hỗ trợ

Nếu gặp vấn đề, vui lòng kiểm tra:
1. File nguồn có đúng định dạng Tab-separated không
2. Python version >= 3.x
3. File nguồn có encoding UTF-8
