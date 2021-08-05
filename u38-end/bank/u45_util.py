class Account:
    def __init__(self,*bank):
        self.ano=bank[0]
        self.owner=bank[1]
        self.__balance=bank[2]
     
    def deposit(self,amount):
        if (self.__balance+amount) >= 10000000:
            print(f'잔액인 {self.__balance}이 천만원 이상이랑 입금불가')
            return
        self.__balance+=amount
        print(f'입급 후 잔액 : {self.__balance}')

    def withdraw(self,amount):
        if (self.__balance-amount)<0 :
            print(f'{self.__balance}-{amount} 0보다 작아 출금 불가') 
            return 
        self.__balance-=amount 
        print(f'출금 후 잔액 : {self.__balance}')

    def __str__(self):
        return f'ano:{self.ano}, owner:{self.owner}, balance:{self.__balance}'
         
    