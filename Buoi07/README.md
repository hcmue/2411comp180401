# Buổi 07 (05/11/2024)

# FASTAPI

https://fastapi.tiangolo.com/

## Cài FastAPI

```
pip install "fastapi[standard]"
```

Phiên bản FastAPI mới đã bao gồm uvicorn

## Chạy ứng dụng FastAPI

```
fastapi dev <file_main.py>
```

# Restful API

VD thiết kế bộ API thao tác CRUD trên students

```
GET     /students       # Lấy tất cả
GET     /students/{id}  # Lấy theo id
POST    /students       # Tạo mới
PUT     /students/{id}  # Sửa theo id
DELETE  /students/{id}  # Xóa theo id
GET     /students/search # Có thể xem xét gộp chung
```
