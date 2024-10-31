from multiprocessing import Pool
import time


def ead_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        file.seek(0)
        while not line == '':
            line = file.readline().strip('\n')
            all_data += line
        print(f'Прочитал файл {name}')


filenames = [f'./file {number}.txt' for number in range(1, 5)]

'''a1 = time.time()
for i in filenames:
    ead_info(i)
b1 = time.time()
print(b1-a1)'''  # выполнение составляет порядка 4 секунд

if __name__ == '__main__':
    a2 = time.time()
    with Pool(processes=4) as pool:
        pool.map(ead_info, filenames)
    b2 = time.time()
    print(b2-a2)
