import time
from multiprocessing import Pool
#import os
#print (f'Текущая рабочая директория: {os.getcwd()}')

def read_info(name):
    all_data = []
    with open (name, 'r', encoding='utf8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

print ('Линейное выполнение:')
start_time = time.time()
for file in filenames:
    read_info(file)
end_time = time.time()
print (f'Время: {end_time - start_time} секунд')

print ('Многопроцессное выполнение:')
start_time = time.time()
with Pool() as pool:
    pool.map(read_info, filenames)
end_time = time.time()
print (f'Время: {end_time - start_time} секунд')
