import threading
import queue

class ThreadPool:
    def __init__(self, num_threads):
        self.stop_ = False
        self.threads_ = []
        self.queue_ = queue.Queue()
        for i in range(num_threads):
            t = threading.Thread(target=self.worker)
            t.start()
            self.threads_.append(t)

    def worker(self):
        while True:
            task = self.queue_.get()
            if task is None:
                break
            task()
            self.queue_.task_done()

    def add_task(self, task):
        self.queue_.put(task)

    def stop(self):
        for i in range(len(self.threads_)):
            self.queue_.put(None)
        for t in self.threads_:
            t.join()