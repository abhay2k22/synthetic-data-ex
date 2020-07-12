from sdv import SDV
import pandas as pd
import json
sdv = SDV()
users = pd.DataFrame({
    'user_id': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'country': ['USA', 'UK', 'ES', 'UK', 'USA', 'DE', 'BG', 'ES', 'FR', 'UK'],
    'gender': ['M', 'F', None, 'M', 'F', 'M', 'F', None, 'F', None],
    'age': [34, 23, 44, 22, 54, 57, 45, 41, 23, 30]
})
'''
Original Data
'''
print(users)
tables = {
    'users': users
}
with open('./single_table_metadata.json') as metadata_file:
    metadata = json.load(metadata_file)
    sdv.fit(metadata, tables)
    sdv.save('SingleTablesdv.pkl')
sdv = SDV.load('./SingleTablesdv.pkl')
samples = sdv.sample_all(10)
df = pd.DataFrame(samples['users'])
'''
Print Synthetsized Data
'''
print(df)

