import threading
import time

from priority_queue import PriorityQueue
from thread_pool import ThreadPool

class MessageQueue:
    def __init__(self, name, queue):
        self.name_ = name
        self.queue_ = queue
        self.pool_ = ThreadPool(4)

    def send_message(self, priority, message):
        def task():
            self.queue_.enqueue(priority, message)
        self.pool_.add_task(task)

    def receive_message(self):
        def task():
            priority, message = self.queue_.dequeue()
            print(f"{self.name_} received message: {message} with priority: {priority}")
        self.pool_.add_task(task)

    def start(self):
        self.receive_thread_ = threading.Thread(target=self.receive_loop)
        self.receive_thread_.start()

    def receive_loop(self):
        while True:
            self.receive_message()
            time.sleep(1)

    def stop(self):
        self.pool_.stop()
        self.receive_thread_.join()