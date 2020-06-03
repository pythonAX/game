from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Lock



def product(q,lock, str, count):
    lock.acquire()
    product_name = '%s执行的任务%d' % (str, count)
    q.put(product_name)   #  把执行的结果全部发到了队列
    lock.release()


def customer(q):
    while not q.empty():
        cus = q.get()
        print('消费者拿了%s' % cus)


if __name__ == '__main__':
    q = Queue()
    count = 1
    lock = Lock()
    while count <= 100:
        ps = []
        for i in range(1, 33):  #
            if count > 100:
                break
            p = Process(target=product, args=(q,lock, '进程%d' % i, count))
            ps.append(p)  ## 进程列表
            count += 1
        for i in range(len(ps)):
            ps[i].start()
            ps[i].join()
    p2 = Process(target=customer,args=(q,))   #  p2是消费者 在队列里面取数据
    p2.start()
    p2.join()
