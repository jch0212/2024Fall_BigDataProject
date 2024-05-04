import pandas as pd



### jobParam Data Processing

# columns_to_load = ['Doc #', 'Street Name', 'Job Type', 'Plumbing', 'Mechanical', 'Boiler', 'Fuel Burning',
#                    'Fuel Storage', 'Standpipe', 'Sprinkler', 'Fire Alarm', 'Equipment', 'Fire Suppression', 'Curb Cut',
#                    'Total Est. Fee', 'Job Status']
# chunk_size = 10000
#
# chunks = pd.read_csv('DOB_Job_Application_Filings_20240228.csv', chunksize=chunk_size, usecols=columns_to_load,
#                      low_memory=False)
#
# processed_chunks = []
# hash_modulo = 2**20
#
# for chunk in chunks:
#     # 去掉Total Est. Fee列的"$"符号并转换为浮点数
#     chunk['Total Est. Fee'] = chunk['Total Est. Fee'].replace('[\$,]', '', regex=True).astype(float)
#
#     # 将街道名称转换为规范化的哈希值
#     chunk['Street Name Vec'] = chunk['Street Name'].apply(lambda x: hash(x) % hash_modulo)
#     chunk.drop('Street Name', axis=1, inplace=True)
#
#     # 使用哈希技术处理Job Type并规范化
#     chunk['Job Type Hash'] = chunk['Job Type'].apply(lambda x: hash(x) % hash_modulo)
#     chunk.drop('Job Type', axis=1, inplace=True)
#
#     # 二分化其他列
#     cols_to_convert = ['Plumbing', 'Mechanical', 'Boiler', 'Fuel Burning', 'Fuel Storage',
#                        'Standpipe', 'Sprinkler', 'Fire Alarm', 'Equipment', 'Fire Suppression', 'Curb Cut']
#     for col in cols_to_convert:
#         chunk[col] = chunk[col].apply(lambda x: 1 if x == 'X' else 0)
#
#     # 创建二元分类目标列
#     chunk['approved'] = (chunk['Job Status'] == 'U') | (chunk['Job Status'] == 'R')
#     chunk['approved'] = chunk['approved'].astype(int)
#     chunk.drop('Job Status', axis=1, inplace=True)
#
#     processed_chunks.append(chunk)
#
# # 合并所有处理过的数据
# final_df = pd.concat(processed_chunks)
#
# # 保存处理后的数据到CSV文件
# final_df.to_csv('D:/bigDataProject/processedDataForJobParam.csv', index=False)
#


# ### Admin Management Data Processing
#
# import pandas as pd
#
# columns_to_load = ['Little e', 'Loft Board', 'eFiling Filed', 'Fee Status', 'SPECIAL_ACTION_STATUS', 'JOB_NO_GOOD_COUNT',
#                    'Job Status']
# chunk_size = 10000
#
# chunks = pd.read_csv('DOB_Job_Application_Filings_20240228.csv', chunksize=chunk_size, usecols=columns_to_load,
#                      low_memory=False)
#
# processed_chunks = []
#
# for chunk in chunks:
#     # 转换 Fee Status
#     fee_status_mapping = {'EXEMPT': 1, 'STANDARD': 2, 'DEFERRED': 3}
#     chunk['Fee Status'] = chunk['Fee Status'].map(fee_status_mapping)
#
#     # 转换 SPECIAL_ACTION_STATUS
#     special_action_status_mapping = {'N': 4, 'W': 3, 'C': 2, 'A': 1, '': 0, None: 0}
#     chunk['SPECIAL_ACTION_STATUS'] = chunk['SPECIAL_ACTION_STATUS'].fillna('').map(special_action_status_mapping)
#
#
#     # 转换其他列
#     cols_to_convert = ['Little e', 'Loft Board', 'eFiling Filed']
#     for col in cols_to_convert:
#         chunk[col] = chunk[col].apply(lambda x: 1 if x == 'Y' else 0)
#
#     # 创建二元分类目标列
#     chunk['approved'] = (chunk['Job Status'] == 'U') | (chunk['Job Status'] == 'R')
#     chunk['approved'] = chunk['approved'].astype(int)
#     chunk.drop('Job Status', axis=1, inplace=True)
#
#     processed_chunks.append(chunk)
#
# # 合并所有处理过的数据块
# final_df = pd.concat(processed_chunks)
#
# # 保存处理后的数据到CSV文件
# final_df.to_csv('D:/bigDataProject/processedDataForAdmin.csv', index=False)

### Owner Chara Data



columns_to_load = ['Applicant Professional Title', 'Professional Cert', 'Owner Type', 'Non-Profit', 'Job Status']
chunk_size = 10000

# 读取数据，分块处理
chunks = pd.read_csv('DOB_Job_Application_Filings_20240228.csv', chunksize=chunk_size, usecols=columns_to_load,
                     low_memory=False)

processed_chunks = []
hash_modulo = 2 ** 16  # 使用一个较小的模数来控制哈希值的大小

for chunk in chunks:
    # 将特定列的字符串哈希化并取模
    chunk['Applicant Professional Title Hash'] = chunk['Applicant Professional Title'].apply(
        lambda x: hash(x) % hash_modulo)
    chunk['Owner Type Hash'] = chunk['Owner Type'].apply(lambda x: hash(x) % hash_modulo)

    # 删除原始的字符串列
    chunk.drop(['Applicant Professional Title', 'Owner Type'], axis=1, inplace=True)

    # 转换其他列
    cols_to_convert = ['Professional Cert', 'Non-Profit']
    for col in cols_to_convert:
        chunk[col] = chunk[col].apply(lambda x: 1 if x == 'Y' else 0)

    # 创建二元分类目标列
    chunk['approved'] = (chunk['Job Status'] == 'U') | (chunk['Job Status'] == 'R')
    chunk['approved'] = chunk['approved'].astype(int)
    chunk.drop('Job Status', axis=1, inplace=True)

    processed_chunks.append(chunk)

# 合并所有处理过的数据块
final_df = pd.concat(processed_chunks)

# 保存处理后的数据到CSV文件
final_df.to_csv('D:/bigDataProject/processedDataForOwner.csv', index=False)
