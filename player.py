
class Player(object):

    STARTING_BALANCE: int = 10000

    def __init__(self):
        self.__balance = self.STARTING_BALANCE
        self.is_broke = False
        self.__in_trade = False

    
    def get_balance(self) -> int:
        return self.__balance


    def is_in_trade(self) -> bool:
        return self.__in_trade


    