import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 构造数据
x = np.array([1, 2, 3, 4, 5])
# x = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
y = np.array([2, 4, 5, 4, 5])

# 拟合线性模型
# model = LinearRegression().fit(x, y)

# 拟合线性模型
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]


# 打印结果
# print("斜率 m =", model.coef_[0])
# print("截距 c =", model.intercept_)
print("斜率 m =", m)
print("截距 c =", c)

plt.scatter(x, y, color='blue')
plt.plot(x, m*x + c, color='red')
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('linear.png', dpi=1000)
plt.show()
