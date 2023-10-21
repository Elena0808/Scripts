import csv
import json

# открываем файл CSV
with open('name.csv', 'r') as f:
    reader = csv.DictReader(f)
    # создаем пустой список для хранения данных
    data = []
    # проходимся по всем строкам
    for row in reader:
        # создаем словарь для хранения данных строки
        row_data = {}
        # добавляем значения полей в словарь, если они есть
        if row['external_matrix_id']:
            row_data['external_matrix_id'] = row['external_matrix_id']

        if row['matrix_type_code']:
            row_data['matrix_type_code'] = row['matrix_type_code']
        if row['dt_start']:
            row_data['dt_start'] = row['dt_start']
        if row['dt_end']:
            row_data['dt_end'] = row['dt_end']
        if row['timezone']:
            row_data['timezone'] = row['timezone']
        # создаем список магазинов
        stores = []
        if row['external_store_id']:
            stores.append({'external_store_id': row['external_store_id']})
        if row['external_store_id2']:
            stores.append({'external_store_id2': row['external_store_id2']})
        if stores:
            row_data['stores'] = stores
        # создаем список продуктов
        products = []
        if row['external_product_id']:
            product = {'external_product_id': row['external_product_id']}
            if row['facing_plan']:
                product['facing_plan'] = int(row['facing_plan'])
            if row['shelf_number_plan']:
                product['shelf_number_plan'] = int(row['shelf_number_plan'])
            if row['assortment_group_name']:
                product['assortment_group_name'] = row['assortment_group_name']
            products.append(product)
        if products:
            row_data['products'] = products
        # добавляем словарь в список данных
        data.append(row_data)

# сохраняем данные в JSON файле
with open('file.json', 'w') as f:
    json.dump(data, f)