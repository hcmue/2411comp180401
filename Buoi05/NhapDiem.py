'''
Nhập vào tên môn, loại điểm, điểm số
Xuất ra màn hình và file json
- Môn gì
- Điểm gì? Tỉ lệ? Bao nhiêu? Loại?
'''
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from typing_extensions import IntVar

root = tk.Tk()
# Custom màn hình chính
root.title('Màn hình nhập điểm')
root.geometry("500x500")

mon_hoc = tk.StringVar(value="Python")
diem = tk.IntVar()

# Gắn control + Gắn sự kiện
ttk.Label(
    root, text="NHẬP ĐIỂM",
    font="Arial 15", foreground="blue"
).grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Môn học").grid(column=0, row=1)
ttk.Entry(root, textvariable=mon_hoc).grid(column=1, row=1)

ttk.Label(root, text="Loại điểm").grid(column=0, row=2)
# create a combobox
selected_mark_type = tk.StringVar()
mark_types = ttk.Combobox(root, textvariable=selected_mark_type)
mark_types['values'] = ["Giữa kỳ", "Cuối kỳ"]
mark_types.grid(column=1, row=2)

ttk.Label(root, text="Điểm").grid(column=0, row=3)
ttk.Entry(root, textvariable=diem).grid(column=1, row=3)

ttk.Button(root, text="Click me").grid(column=1, row=4)

# Hiện màn hình chính 
root.mainloop()