import requests
import threading
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WorkWithReq(QObject):
    for_progress_bar = pyqtSignal(int)
    results = pyqtSignal(dict)

    def __init__(self, resource, num_products):
        super(WorkWithReq, self).__init__()
        self.base_url = resource
        self.num_products = num_products
        self.all_data = {}

    def get_data(self, product_url, i):
        response = requests.get(product_url, timeout=10)
        if response.status_code == 200:
            product_data = response.json()
            self.all_data[i] = product_data
        progress_percentage = int((len(self.all_data) / self.num_products) * 100)
        self.for_progress_bar.emit(progress_percentage)

    def run_with_threads(self):
        threads = []
        for i in range(1, self.num_products + 1):
            thread = threading.Thread(target=self.get_data, args=(f"{self.base_url}/{i}", i,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        self.results.emit(self.all_data)

    def run_without_threads(self):
        for i in range(1, self.num_products + 1):
            self.get_data(f"{self.base_url}/{i}", i)
        self.results.emit(self.all_data)
