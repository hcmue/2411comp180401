# In thông tin mỗi NV gồm mã, tên, tổng số giờ làm, trung bình
result = []
with open("hours.txt", "r") as my_file:
    for line in my_file:
        line = line.replace("\n", "")
        my_arr = line.split(" ")
        # print(my_arr)
        mark_arr = my_arr[2:]
        total_hours = sum(float(x) for x in mark_arr)
        print(my_arr[0], my_arr[1], "total hours:", total_hours)
        result.append(f"{my_arr[0]} {my_arr[1]} tổng cộng: {total_hours}g\n")
print(result)
with open("workinghours.txt", "w", encoding="utf8") as f:
    for line in result:
        f.write(line)