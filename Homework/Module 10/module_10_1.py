from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то число № {i + 1} \n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start_func = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end_func = datetime.now()
res_time_func = time_end_func - time_start_func

thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

time_start_thr = datetime.now()

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end_thr = datetime.now()
res_time_thr = time_end_thr - time_start_thr

print(f'Время работы функций: {res_time_func}')
print(f'Время работы потоков: {res_time_thr}')
