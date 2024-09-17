# DEMO
print("HELLO COMP180401")
nam_sinh = int(input("Nhập năm sinh:"))
tuoi = 2024 - nam_sinh
print(tuoi, "tuổi")
do_tuoi = "Sinh viên" if tuoi > 18 and tuoi < 26 else "Trung niên"
print("Là", do_tuoi)