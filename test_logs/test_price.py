import decimal
import json
import logging
import sys

import exceptions


JSON_PRICE_FILE = '../data/price.json'


def main():
    """ Собирание логгов для непредвиденного формата данных в .json """
    logging_format = "%(asctime)s, %(levelname)s, %(message)s"
    logging.basicConfig(
        level=logging.DEBUG,
        format=logging_format,
        handlers=[
            logging.FileHandler('logs.txt', encoding='UTF-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )

    price_data = json.loads(JSON_PRICE_FILE)
    price_volume = price_data['unit_ratio']

    for volume in price_volume:

        try:
            isinstance(volume, (decimal, str))
        except exceptions.PriceError as error:
            message = f'Непредусмотренный формат значения поля {error}'
            logging.warning(message)
        finally:
            continue


if __name__ == "__main__":
    main()
