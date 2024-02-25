import threading
import queue

class PriorityQueue:
    def __init__(self):
        self._ = []
        self.mutex_ = threading.Lock()
        self.cond_ = threading.Condition(self.mutex_)

    def enqueue(self,, message):
        self.mutex_:
            self.messages_.append((priority, message))
            self.cond_.notify_all()

    def dequeue(self):
        with self.mutex_:
            self.cond_.wait(self, lambda: bool(self.messages_))
            message = self.messages_.pop(0)
            return message

    def peek(self):
        with self.mutex_:
            self.cond_.wait(self, lambda: bool(self.messages_))
            message = self.messages_[0]
            return message

    def empty(self):
        with self.mutex_:
            return not bool(self.messages_)