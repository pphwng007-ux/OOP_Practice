class Money:
    def __init__(self, amount: int, currency: str = 'USD'):
        self.__amount = amount
        self.__currency = currency
        
    def __str__(self):
        return f"{self.__amount} {self.__currency}"
    
    def __eq__(self, value):
        if isinstance(value, Money):
            return self.__amount == value.__amount and self.__currency == value.__currency
        return False
    
    