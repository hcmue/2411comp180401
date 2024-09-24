import json

ho_ten = input("Họ tên SV: ")
mssv = input("Mã số SV: ")
diem_gk = float(input("Điểm giữa kỳ: "))
diem_ck = float(input("Điểm cuối kỳ: "))

diem_tong_ket = diem_ck * 0.7 + diem_gk * 0.3
thong_tin_diem = {
    "ho_ten": ho_ten,
    "mssv": mssv,
    "diem": [
        {"ma_mon": "COMP1804", "giua_ky": diem_gk,"cuoi_ky": diem_ck}
    ]
}

print(json.dumps(thong_tin_diem, indent=4))

with open("student.json", "w", encoding="utf8") as myfile:
    json.dump(thong_tin_diem, myfile, indent=4)

with open("student.json", "r", encoding="utf8") as myfile:
    data = json.load(myfile)
    print(data)