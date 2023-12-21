from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt

# 生成一些样本数据
# x = np.array([0, 1, 2, 3, 4, 5])
# y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])
stop = 100
x = np.arange(0, stop, 1, int)
# y = np.sin(np.linspace(-np.pi, np.pi, stop))
y = np.random.randint(0,100,size=(stop,1))

# 转换输入数据为多项式特征
poly = PolynomialFeatures(degree=3, include_bias=False)
X = poly.fit_transform(x[:, np.newaxis])

# 使用线性回归模型拟合多项式特征数据
model = LinearRegression()
model.fit(X, y)

# 打印模型系数
print(model.coef_)

# 绘制原始数据
plt.scatter(x, y)

# 生成一些用于绘制拟合曲线的数据
x_plot = np.linspace(0, stop, stop*10)
X_plot = poly.fit_transform(x_plot[:, np.newaxis])
y_plot = model.predict(X_plot)

# 绘制拟合曲线
plt.plot(x_plot, y_plot, 'r')

# 添加标题和标签
plt.title('Polynomial Regression')
plt.xlabel('x')
plt.ylabel('y')

# 显示图形
plt.savefig('highLinear.png', dpi=1000)
plt.show()

