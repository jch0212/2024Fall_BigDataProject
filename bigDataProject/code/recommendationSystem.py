import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# Prepare Data
columns_to_load = ['eFiling Filed', 'SPECIAL_ACTION_STATUS', 'Total Est. Fee', 'Job Type', 'Professional Cert', 'Owner Type', 'Job Status']
chunk_size = 10000

# 读取数据，分块处理
chunks = pd.read_csv('DOB_Job_Application_Filings_20240228.csv', chunksize=chunk_size, usecols=columns_to_load, low_memory=False)

processed_chunks = []
hash_modulo = 2 ** 16  # 使用一个较小的模数来控制哈希值的大小

for chunk in chunks:
    chunk['eFiling Filed'] = chunk['eFiling Filed'].apply(lambda x: 1 if x == 'Y' else 0)
    special_action_status_mapping = {'N': 4, 'W': 3, 'C': 2, 'A': 1, '': 0, None: 0}
    chunk['SPECIAL_ACTION_STATUS'] = chunk['SPECIAL_ACTION_STATUS'].fillna('').map(special_action_status_mapping)

    chunk['Total Est. Fee'] = chunk['Total Est. Fee'].replace('[\$,]', '', regex=True).astype(float)
    chunk['Job Type Hash'] = chunk['Job Type'].apply(lambda x: hash(x) % hash_modulo)
    chunk.drop('Job Type', axis=1, inplace=True)

    chunk['Professional Cert'] = chunk['Professional Cert'].apply(lambda x: 1 if x == 'Y' else 0)
    chunk['Owner Type Hash'] = chunk['Owner Type'].apply(lambda x: hash(x) % hash_modulo)
    chunk.drop(['Owner Type'], axis=1, inplace=True)

    chunk['approved'] = (chunk['Job Status'] == 'U') | (chunk['Job Status'] == 'R')
    chunk['approved'] = chunk['approved'].astype(int)
    chunk.drop('Job Status', axis=1, inplace=True)

    processed_chunks.append(chunk)

# 合并所有处理过的数据块
final_df = pd.concat(processed_chunks)
final_df.to_csv('dataForTraining.csv', index=False)

# Model Training
data = pd.read_csv('dataForTraining.csv')
X = data.drop('approved', axis=1)
y = data['approved']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

# Model Evaluation
predictions = dtree.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')

# Visualization of Decision Tree
plt.figure(figsize=(20,10))
plot_tree(dtree, filled=True, feature_names=X.columns, class_names=['Not Approved', 'Approved'])
plt.title('Decision Tree Structure')
plt.show()

# Feature Importance
feature_importances = pd.Series(dtree.feature_importances_, index=X.columns)
feature_importances.nlargest(10).plot(kind='barh')
plt.title('Feature Importances')
plt.show()

# Confusion Matrix
cm = confusion_matrix(y_test, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not Approved', 'Approved'])
disp.plot()
plt.title('Confusion Matrix')
plt.show()
