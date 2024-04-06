import base64
import openpyxl

with open('decode.txt', 'r') as f:
    encoded_data = f.read()
decoded_bytes = base64.b64decode(encoded_data)

# декодирование байтов из UTF-8 в строку
decoded_string = decoded_bytes.decode("utf-8")

# открываем файл для записи декодированных данных в формате UTF-8
with open('decoded_data.txt', 'w') as f:
    f.write(decoded_string)
