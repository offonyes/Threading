import json
import time

from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Utils.utils import WorkWithReq
from Windows.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.started = None
        self.thread = QThread()
        self.worker = None
        self.closeEvent = self.on_close_event
        self.setupUi(self)
        self.num_pages = int(self.doubleSpinBox.value())
        self.resourse = self.resourse_cb.currentText()
        self.thread_status = True
        self.start_btn.clicked.connect(self.start_function)
        self.resourse_cb.currentIndexChanged.connect(self.on_combo_box_text_changed)
        self.threads_btn.clicked.connect(self.button_ckecking)

    def on_combo_box_text_changed(self, index):
        resourse_dct = {0: 100, 1: 20, 2: 100, 3: 50}
        value = resourse_dct[index]
        self.pages_lbl.setText(f"Pages:\n(MAX {value})")
        self.doubleSpinBox.setMaximum(value)
        self.doubleSpinBox.setValue(value)
        self.resourse = self.resourse_cb.currentText()

    def start_function(self):
        self.started = time.time()
        self.start_btn.setEnabled(False)
        self.frame.setEnabled(False)

        self.num_pages = int(self.doubleSpinBox.value())

        self.worker = WorkWithReq(self.resourse, self.num_pages)
        self.worker.moveToThread(self.thread)

        if self.thread_status:
            self.thread.started.connect(self.worker.run_with_threads)
        else:
            self.thread.started.connect(self.worker.run_without_threads)
        self.thread.start()
        self.worker.for_progress_bar.connect(self.handle_progressbar)
        self.worker.results.connect(self.handle_results)

    def handle_progressbar(self, percentage):
        self.progressBar.setValue(percentage)

    def handle_results(self, result):
        finished = time.time()
        with open(f"{self.resourse.split("/")[-1]}_{self.num_pages}.json", 'w') as file:
            result = dict(sorted(result.items(), key=lambda item: int(item[0])))
            json.dump(result, file, indent=2)
        self.finished(finished - self.started)

    def button_ckecking(self, status):
        self.thread_status = status
        if status:
            self.threads_btn.setStyleSheet("background-color: green;")
            self.threads_btn.setText("ON")
        else:
            self.threads_btn.setStyleSheet("background-color:red")
            self.threads_btn.setText("OFF")

    def finished(self, time_needed):
        self.thread.quit()
        self.thread.wait()
        self.start_btn.setEnabled(True)
        self.frame.setEnabled(True)
        QMessageBox.information(self, "Done", f"Operation completed successfully in {time_needed:.3f} sec.")

    @staticmethod
    def on_close_event(event):
        event.accept()
