import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 建立随机森林模型
random_forest = RandomForestClassifier(n_estimators=10, random_state=42)
random_forest.fit(X_train, y_train)

# 预测并计算准确率
y_pred = random_forest.predict(X_test)
accuracy = np.mean(y_pred == y_test)
print(f'Accuracy: {accuracy:.2f}')

# 可视化随机森林中的决策树
n_trees = len(random_forest.estimators_)

fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(20, 10), dpi=100)

for index, tree in enumerate(random_forest.estimators_):
    ax = axes[index // 5, index % 5]
    plot_tree(tree, filled=True, ax=ax, feature_names=iris.feature_names, class_names=iris.target_names, rounded=True, proportion=True)
    ax.set_title(f'Tree {index + 1}')

plt.tight_layout()
plt.savefig('random_forest_iris.png', dpi=1000)
plt.show()
