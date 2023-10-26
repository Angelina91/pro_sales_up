class PriceError(Exception):
    """ Непредвиденный формат данных для полей price.json """
    def __init__(self):
        self.message = 'Внимание - непредусмотренный формат данных price.json'
        super().__init__(self.message)


class InventoryError(Exception):
    """ Непредвиденный формат данных для полей .json """
    def __init__(self):
        self.message = 'Непредусмотренный формат данных inventory1.json'
        super().__init__(self.message)