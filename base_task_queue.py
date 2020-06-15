import queue
import threading
from base_app import App

class TaskQueue(threading.Thread):

    tasks = None

    def __init__(self):
        self.tasks = queue.Queue()
        super(TaskQueue, self).__init__()

    def run(self):
        while App.instance.running:
            try:
                function, args, kwargs = self.tasks.get(timeout=1.0/60)
                function(*args, **kwargs)
            except queue.Empty:
                pass

    def submit(self, function, *args, **kwargs):
        self.tasks.put((function, args, kwargs))