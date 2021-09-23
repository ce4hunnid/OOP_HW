class RetailItem:

    def __init__ (self, description, inv, price):
        self.__descr = description
        self.__inv = inv
        self.__price = price
#Setting
    def set_descr(self, description):
        self.__descr = description
    
    def set_inv(self, inv):
        self.__inv = inv

    def set_price(self, price):
        self.__price = price
#Return

    def get_descr(self):
        return self.__descr

    def get_inv(self):
        return self.__inv

    def get_price(self):
        return self.__price
    