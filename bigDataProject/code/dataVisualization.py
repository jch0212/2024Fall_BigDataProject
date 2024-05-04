
import pandas as pd
import matplotlib.pyplot as plt

# # 1
# data = pd.read_csv('shap_values_positive_class.txt', header=None, sep=" ")  # 根据实际的分隔符调整 sep 参数
# print(data[0])
# shap = []
# for i in range(len(data[0])):
#     shap.append(data[0][i])
#
# first_column = ['Doc #', 'Plumbing', 'Mechanical', 'Boiler', 'Fuel Burning',
#        'Fuel Storage', 'Standpipe', 'Sprinkler', 'Fire Alarm', 'Equipment',
#        'Fire Suppression', 'Curb Cut', 'Total Est. Fee', 'Street Name Vec',
#        'Job Type Hash']
#
# # 绘制直方图
# plt.figure(figsize=(10, 8))  # 设置图形大小
# plt.bar(first_column, shap)  # bins 控制条形的数量
# plt.title('jobParam')
# plt.xticks(rotation=45)  # 旋转45度
# plt.xticks(fontsize=8)
# plt.xlabel('Param')  # 可以根据需要更改标签
# plt.ylabel('SHAP Value')
# plt.show()





# # 2
# data = pd.read_csv('shap_values_positive_class_admin.txt', header=None, sep=" ")  # 根据实际的分隔符调整 sep 参数
# print(data[0])
# shap = []
# for i in range(len(data[0])):
#     shap.append(data[0][i])
#
# first_column = ['Loft Board', 'Little e', 'eFiling Filed', 'Fee Status',
#        'SPECIAL_ACTION_STATUS', 'JOB_NO_GOOD_COUNT']
#
# # 绘制直方图
# plt.figure(figsize=(10, 8))  # 设置图形大小
# plt.bar(first_column, shap)  # bins 控制条形的数量
# plt.title('Admin Management')
# plt.xticks(rotation=45)  # 旋转45度
# plt.xticks(fontsize=8)
# plt.xlabel('Param')  # 可以根据需要更改标签
# plt.ylabel('SHAP Value')
# plt.show()

# 3
data = pd.read_csv('shap_values_positive_class_Owner.txt', header=None, sep=" ")  # 根据实际的分隔符调整 sep 参数
print(data[0])
shap = []
for i in range(len(data[0])):
    shap.append(data[0][i])

first_column = ['Professional Cert', 'Non-Profit', 'Applicant Professional Title Hash',
       'Owner Type Hash']

# 绘制直方图
plt.figure(figsize=(10, 8))  # 设置图形大小
plt.bar(first_column, shap)  # bins 控制条形的数量
plt.title('OwnerInformation')
plt.xticks(rotation=45)  # 旋转45度
plt.xticks(fontsize=8)
plt.xlabel('Param')  # 可以根据需要更改标签
plt.ylabel('SHAP Value')
plt.show()

