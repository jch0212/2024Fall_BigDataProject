import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import shap

# 加载数据
data = pd.read_csv('processedDataForOwner.csv')

# 随机抽取一定数量的样本
sample_size = 100000  # 每个数据集的样本数
if len(data) >= 2 * sample_size:
    sampled_data = data.sample(n=2 * sample_size, random_state=42)
else:
    print("数据量不足以抽取两万条样本")
    sampled_data = data

# 划分数据集
X = sampled_data.drop('approved', axis=1)
print(X.columns)
y = sampled_data['approved']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)  # 确保训练集和测试集都是一万条数据

# 训练随机森林分类器
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
print("Model Training Completed.")

# 初始化SHAP
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)


# 将SHAP值存储到文本文件
np.savetxt('shap_values_positive_class_Owner.txt', shap_values[1], fmt='%f')

print("SHAP values saved to shap_values_positive_class_Owner.txt.")

