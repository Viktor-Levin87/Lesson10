import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power, enimes=100):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enimes = enimes

    def battle(self, *args):
        started_at = time.time()
        while self.enimes:
            self.enimes -= self.power
            time.sleep(1)
            ended_at = time.time()
            print(f'{self.name} сражается {format((ended_at-started_at), '.0f')} дней(дня), осталось '
                  f'{self.enimes} войнов!')
        print(f'{self.name} одержал победу спустя {format((ended_at-started_at), '.0f')} дней(дня)!')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle(self.name, self.power, self.enimes)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
