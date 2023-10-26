import json
import logging


JSON_INVENTORY1_FILE = './data/inventory1.json'


def inventory1_json_excep_logging(file_path):
    """ Сбор исключений и логгирование inventory1.json """
    logger = logging.getLogger('json_processing_1')
    logger.setLevel(logging.WARNING)
    log_file = './logs/inventory1.log'
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


inventory1_json_excep_logging(JSON_INVENTORY1_FILE)
