import pandas as pd
import json

# чтение данных из файла Excel
df = pd.read_excel('assortment_matrices_со_структурой.xlsx', sheet_name='Sheet 1')

# преобразование данных в словарь
data = []
for index, row in df.iterrows():
    if row['external_matrix_id'] not in [d.get('external_matrix_id') for d in data]:
        matrix_data = {
            'external_matrix_id': row['external_matrix_id'] if not pd.isna(row['external_matrix_id']) else None,
            'matrix_type_code': row['matrix_type_code'] if not pd.isna(row['matrix_type_code']) else None,
            'dt_start': str(row['dt_start']) if not pd.isna(row['dt_start']) else None,
            'dt_end': str(row['dt_end']) if not pd.isna(row['dt_end']) else None,
            'timezone': row['timezone'] if not pd.isna(row['timezone']) else None,
            'stores': [],
            'products': []
        }
        data.append(matrix_data)
    store = {
        'external_store_id': row['external_store_id'] if not pd.isna(row['external_store_id']) else None,
        'external_store_id2': row['external_store_id2'] if not pd.isna(row['external_store_id2']) else None
    }
    if store not in data[-1]['stores']:
        data[-1]['stores'].append(store)
    product = {
        'external_product_id': row['external_product_id'] if not pd.isna(row['external_product_id']) else None,
        'facing_plan': int(row['facing_plan']) if not pd.isna(row['facing_plan']) else None,
        'shelf_number_plan': int(row['shelf_number_plan']) if not pd.isna(row['shelf_number_plan']) else None,
        'assortment_group_name': row['assortment_group_name'] if not pd.isna(row['assortment_group_name']) else None
    }
    if product not in data[-1]['products']:
        data[-1]['products'].append(product)

# преобразование списка словарей в JSON
json_data = json.dumps(data)

# запись данных в файл
with open('file.json', 'w') as f:
    f.write(json_data)