# coding=utf-8
import Queue
import threading
import time
# from add_data import get_list_by_url, get_url_list
from csv_data import get_list
from test import KunMing


class WorkManager(object):
    def __init__(self, jobs, thread_num=2):
        self.work_queue = Queue.Queue()
        self.threads = []
        self.__init_work_queue(jobs)
        self.__init_thread_pool(thread_num)

    """
        初始化线程
    """
    def __init_thread_pool(self, thread_num):
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))

    """
        初始化工作队列
    """
    def __init_work_queue(self, jobs):
        url_jobs = iter(jobs)
        for i in url_jobs:
            self.add_job(do_job, i)

    """
        添加一项工作入队
    """
    def add_job(self, func, *args):
        self.work_queue.put((func, list(args)))  # 任务入队，Queue内部实现了同步机制
    """
        检查剩余队列任务
    """
    def check_queue(self):
        return self.work_queue.qsize()

    """
        等待所有线程运行完毕
    """
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()


class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self):
        # 死循环，从而让创建的线程在一定条件下关闭退出
        while True:
            try:
                do, args = self.work_queue.get(block=False)  # 任务异步出队，Queue内部实现了同步机制
                do(args)
                self.work_queue.task_done()  # 通知系统任务完成
            except Exception, e:
                print str(e)
                break

# 具体要做的任务


def do_job(args):
    print args
    # get_list_by_url(args[0])
    km = KunMing(args[0])
    km.session.add(km)
    km.session.commit()


if __name__ == '__main__':
    start = time.time()
    work_manager = WorkManager(get_list(), 8)  # 或者work_manager =  WorkManager(10000, 20)
    work_manager.wait_allcomplete()
    end = time.time()
    print "cost all time: %s" % (end-start)
