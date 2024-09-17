'''
Input:
- Mảng điểm thi của thí sinh [20, 19, 27, 23.4]
- Số lượng chỉ tiêu n=20
Output:
- Điểm chuẩn (cho phép vượt tối đa 10%)
- Thống kê từng điểm
'''
from audioop import reverse
from itertools import count


arr_marks = [19, 13, 23, 29, 27.6, 19, 20, 20, 23.5, 23, 27, 29, 25, 20, 20]
n = 10
mark_stat = {}
for mark in arr_marks:
    mark_stat[mark] = mark_stat.get(mark, 0) + 1
print(mark_stat)

m_diem = set(arr_marks)
print(len(m_diem))
mark_stat2 = {}
for mark in m_diem:
    mark_stat2[mark] = arr_marks.count(mark)
print(mark_stat2)

# Sắp dict
new_dict = sorted(mark_stat.items())
new_dict = dict(reversed(new_dict))
print("+++\n", new_dict)
diem_chuan = 0
max_num = int(n * 1.1)
num = 0 # Số lượng sv lấy
print('Lấy tối đa:', max_num)
for k,v in new_dict.items():
    if num + v > max_num:
        break
    else:
        num += v
        diem_chuan = k

print('Điểm chuẩn', diem_chuan, 'có', num, ' TS trúng tuyển')