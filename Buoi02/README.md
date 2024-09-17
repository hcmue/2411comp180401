# range(start, end, step)

- range(n): 0 ==> n - 1
- range(x, y): x ==> y - 1
- range(x, y, 3): x < y - 1, mỗi phần tử tăng 3

# print(v1,v2,v3, sep=" ", end="\n")

# LIST

- Khai báo v = [] hoặc v = list()
- slicing: Lấy mảng con

  - name[start:end] # end is exclusive (lấy từ index start tới index end-1)
  - name[start:] # to end of list
  - name[:end] # from start of list (lấy tứ đầu - index=0 đến end-1)

## Đổi mảng sang chuỗi và ngược lại

- Mảng sang chuỗi: <kí_tự_phân_cách>.join(list)
- Chuổi sang mảng: chuoi.split()

- Thêm phần tử: mylist.append(item)
- Kiểm tra có phần rử: mylist.contains(value) hoặc value in mylist
- Xóa phần tử: mylist.del(value)

# DICT (key ==> value)

- Tạo mydict = {} hoặc mydict = dict()
- Thêm phần tử: mydict[mykey] = value
- Kiểm tra có key hay chưa: mykey in mydict
- Lấy giá trị: item_value = mydict[mykey]
  - nên lấy: item_value = mydict.get(mykey, default_value)
