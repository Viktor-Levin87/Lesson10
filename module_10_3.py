import threading
from random import randint
import time


class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(0, 100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            x = randint(50, 500)
            self.balance += x
            print(f'Пополнение: {x}. Баланс {self.balance} ')
            time.sleep(0.001)

    def take(self):
        for i in range(0, 100):
            if self.lock.locked():
                self.lock.release()
            x = randint(50, 5000)
            print(f'Запрос на {x}')
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие: {x}. Баланс {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
