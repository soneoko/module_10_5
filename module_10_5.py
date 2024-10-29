from multiprocessing import Process
from time import  time
def read_info(name):
    all_data = []
    file = open(name, 'r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line.strip():
            break
        all_data.append(line)
    file.close()

filenames = [f'./file {number}.txt' for number in range(1, 5)]



if __name__ == '__main__':
    start_time = time()
    for i in filenames:
        read_info(i)

    print(f'{time() - start_time} (линейный)')
    start_time1 = time()
    process1 = Process(target=read_info, args=(filenames[0],))
    process2 = Process(target=read_info, args=(filenames[1],))
    process3 = Process(target=read_info, args=(filenames[2],))
    process4 = Process(target=read_info, args=(filenames[3],))
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    print(f'{time() - start_time1} (многопроцессный)')