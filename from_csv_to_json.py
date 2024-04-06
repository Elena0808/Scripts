import csv
import json

# открываем файл CSV
with open('planned_assortment.csv', 'r') as f:
    reader = csv.DictReader(f)
    # создаем пустой список для хранения данных
    data = []
    # проходимся по всем строкам
    for row in reader:
        # создаем словарь для хранения данных строки
        row_data = {}
        # добавляем значения полей в словарь, если они есть
        if 'external_matrix_id' in data:
            row_data['external_matrix_id'] = 'external_matrix_id'
        if 'matrix_type_code':
            row_data['matrix_type_code'] = 'matrix_type_code'
        if 'dt_start':
            row_data['dt_start'] = 'dt_start'
        if 'dt_end':
            row_data['dt_end'] = 'dt_end'
        if 'timezone':
            row_data['timezone'] = 'timezone'
        # создаем список магазинов
        stores = []
        if 'external_store_id':
            stores.append({'external_store_id': 'external_store_id'})
        if 'external_store_id2':
            stores.append({'external_store_id2': 'external_store_id2'})
        if stores:
            row_data['stores'] = stores
        # создаем список продуктов
        products = []
        if 'external_product_id':
            product = {'external_product_id': 'external_product_id'}
            if 'facing_plan':
                product['facing_plan'] = 'facing_plan'
            if 'shelf_number_plan':
                product['shelf_number_plan'] = 'shelf_number_plan'
            if 'assortment_group_name':
                product['assortment_group_name'] = 'assortment_group_name'
            products.append(product)
        if products:
            row_data['products'] = products
        # добавляем словарь в список данных
        data.append(row_data)

# сохраняем данные в JSON файле
with open('planned_assortment.json', 'w') as f:
    json.dump(data, f)