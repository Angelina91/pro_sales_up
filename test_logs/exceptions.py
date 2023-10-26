class PriceError(Exception):
    """ Непредвиденный формат данных для полей .json """
    def __init__(self):
        self.message = 'Внимание - непредусмотренный формат данных'
        super().__init__(self.message)
