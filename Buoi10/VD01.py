import matplotlib.pyplot as plt
import numpy as np

# Định nghĩa hàm vẽ
x = np.arange(0, 5 * np.pi, 0.01)
y = np.cos(x)

# Vẽ
plt.plot(x, y)

# Custom: tiêu đề, label trục
plt.xlabel = "Trục X"
plt.ylabel = "Trục Y"
plt.title = "Bảng giá vàng"
plt.legend(['Cos(x)'])

# Hiển thị lên màn hình
plt.show()