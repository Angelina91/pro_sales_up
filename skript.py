import csv
import json

CSV_PRICE_FILE = './data/price.csv'
CSV_INVENTORY1_FILE = './data/inventory1.csv'
CSV_INVENTORY2_FILE = './data/inventory2.csv'
JSON_PRICE_FILE = './data/price.json'
JSON_INVENTORY1_FILE = './data/inventory1.json'
JSON_INVENTORY2_FILE = './data/inventory2.json'

FORMATS = {
    CSV_PRICE_FILE: JSON_PRICE_FILE,
    CSV_INVENTORY1_FILE: JSON_INVENTORY1_FILE,
    CSV_INVENTORY2_FILE: JSON_INVENTORY2_FILE,
}


def csv_to_json(csv_file_path, json_file_path):

    data_dict = {}

    with open(csv_file_path, encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler, )

        for rows in csv_reader:

            data_dict = rows

    with open(json_file_path, 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(
            json.dumps(
                data_dict,
                ensure_ascii=False,
                skipkeys=False,
                check_circular=True,
                allow_nan=True,
                cls=None,
                default=None,
                indent=9
            )
        )


for keys, values in FORMATS.items():
    csv_to_json(keys, values)
