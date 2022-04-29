# Class for stock

class Stock:

    def __init__(self, name: str, share_price: int) -> None:
        self.tick = self.__check_tick(name)
        self.price = share_price

    

    def __check_tick(self, word: str) -> str:

        if len(word) > 5:
            word = word[0:5]

        return word.upper()
    
