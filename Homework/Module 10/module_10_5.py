import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


list_files = [f'./file {number}.txt' for number in range(1, 5)]

start0 = datetime.datetime.now()

for file in list_files:
    read_info(file)

end0 = datetime.datetime.now()
print(end0 - start0)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start1 = datetime.datetime.now()
        pool.map(read_info, list_files)
    end1 = datetime.datetime.now()
    print(end1 - start1)


