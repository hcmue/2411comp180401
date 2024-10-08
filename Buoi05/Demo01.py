from cProfile import label
import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
# Custom màn hình chính
root.title('Tkinter Window Demo')
root.geometry("500x500")

# Gắn control + Gắn sự kiện
tk.Label(root, text="Hello World", padx=10, pady=10).pack()
tk.Button(
    root, text="Click me",
    command=showinfo('Thanks for click me')
).pack()

# Hiện màn hình chính
root.mainloop()