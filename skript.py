import csv
import json

CSV_PRICE_FILE = './data/price.csv'
CSV_INVENTORY1_FILE = './data/inventory1.csv'
CSV_INVENTORY2_FILE = './data/inventory2.csv'
JSON_PRICE_FILE = './data/price.json'
JSON_INVENTORY1_FILE = './data/inventory1.json'
JSON_INVENTORY2_FILE = './data/inventory2.json'

SPECIFICATION_PRICERUNNER = 'https://support.heado.ru/api/management/#method_inventoryUpdateBatch'
SPECIFICATION_INVENTORYRUNNER = 'https://support.heado.ru/api/management/#method_priceupdatebatch'


FORMATS_PRICE = {
    CSV_PRICE_FILE: JSON_PRICE_FILE,
}

FORMATS_INVENTORY = {
    CSV_INVENTORY1_FILE: JSON_INVENTORY1_FILE,
    CSV_INVENTORY2_FILE: JSON_INVENTORY2_FILE,
}


def csv_to_json_price(csv_file_path, json_file_path):
    """Получение данных .csv и преобразование в формат .json"""

    json_list = [SPECIFICATION_PRICERUNNER]

    with open(csv_file_path, encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler, )

        for row in csv_reader:
            json_list.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(
            json.dumps(
                json_list,
                ensure_ascii=False,
                skipkeys=True,
                check_circular=True,
                allow_nan=False,
                cls=None,
                default=None,
                indent=9
            )
        )


def csv_to_json_inventory(csv_file_path, json_file_path):
    """Получение данных .csv и преобразование в формат .json"""

    json_list = [SPECIFICATION_INVENTORYRUNNER]

    with open(csv_file_path, encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler, )

        for row in csv_reader:
            json_list.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(
            json.dumps(
                json_list,
                ensure_ascii=False,
                skipkeys=True,
                check_circular=True,
                allow_nan=False,
                cls=None,
                default=None,
                indent=9
            )
        )


for keys, values in FORMATS_PRICE.items():
    csv_to_json_price(keys, values)


for keys, values in FORMATS_INVENTORY.items():
    csv_to_json_inventory(keys, values)
