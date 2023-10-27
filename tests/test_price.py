import json
import logging


JSON_PRICE_FILE = './data/price.json'


def price_json_excep_logging(file_path):
    """ Сбор исключений и логгирование price.json """
    logger = logging.getLogger('json_processing')
    logger.setLevel(logging.WARNING)
    log_file = './logs/price.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.WARNING)
    logger.addHandler(file_handler)

    with open(file_path, 'r') as json_file:
        for line_num, line in enumerate(json_file, start=1):
            try:
                json_data = json.loads(line)
                isinstance(json_data, str)
            except json.JSONDecodeError as e:
                logger.warning(f'Error in line {line_num}: {str(e)}')
            finally:
                continue


price_json_excep_logging(JSON_PRICE_FILE)
