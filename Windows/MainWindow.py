from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 323)
        MainWindow.setMinimumSize(QtCore.QSize(515, 323))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"    background-color: rgba(0,0,0, 80)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame#frame {\n"
"    background-color: rgba(0, 0, 0, 90);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(5)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.threads_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.threads_btn.setFont(font)
        self.threads_btn.setStyleSheet("background-color: green;")
        self.threads_btn.setObjectName("pushButton")
        self.threads_btn.setCheckable(True)
        self.threads_btn.setChecked(True)
        self.gridLayout_2.addWidget(self.threads_btn, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(90, 30))
        self.label_3.setMaximumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.resourse_cb = QtWidgets.QComboBox(self.frame)
        self.resourse_cb.setMinimumSize(QtCore.QSize(277, 30))
        self.resourse_cb.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resourse_cb.setFont(font)
        self.resourse_cb.setObjectName("comboBox")
        self.resourse_cb.addItem("")
        self.resourse_cb.addItem("")
        self.resourse_cb.addItem("")
        self.resourse_cb.addItem("")

        self.gridLayout_2.addWidget(self.resourse_cb, 0, 1, 1, 1)
        self.pages_lbl = QtWidgets.QLabel(self.frame)
        self.pages_lbl.setMinimumSize(QtCore.QSize(90, 50))
        self.pages_lbl.setMaximumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pages_lbl.setFont(font)
        self.pages_lbl.setObjectName("pages_lbl")
        self.gridLayout_2.addWidget(self.pages_lbl, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(90, 30))
        self.label.setMaximumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(0, 25))
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setProperty("value", 100.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_2.addWidget(self.doubleSpinBox, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet("QProgressBar::chunk {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 160, 255, 255), stop:1 rgba(0, 160, 180, 255));\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 2)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.start_btn.setSizeIncrement(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 238, 0, 255);\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 9px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 190, 0, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(0, 190, 0, 255); \n"
"}\n"
"")
        self.start_btn.setObjectName("start_btn")
        self.gridLayout.addWidget(self.start_btn, 3, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 2)
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.stop_btn.setSizeIncrement(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stop_btn.setFont(font)
        self.stop_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 0, 0, 255); \n"
"    color: rgba(255, 255, 255, 210); \n"
"    border-radius: 9px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(178, 0, 0, 200); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgbargba(178, 0, 0, 255); \n"
"}\n"
"")
        self.stop_btn.setObjectName("stop_btn")
        self.stop_btn.hide()
        self.gridLayout.addWidget(self.stop_btn, 3, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Threading APP"))
        self.threads_btn.setText(_translate("MainWindow", "ON"))
        self.label_3.setText(_translate("MainWindow", "Threads:"))
        self.resourse_cb.setCurrentText(_translate("MainWindow", "https://dummyjson.com/products"))
        self.resourse_cb.setItemText(0, _translate("MainWindow", "https://dummyjson.com/products"))
        self.resourse_cb.setItemText(1, _translate("MainWindow", "https://dummyjson.com/carts"))
        self.resourse_cb.setItemText(2, _translate("MainWindow", "https://dummyjson.com/users"))
        self.resourse_cb.setItemText(3, _translate("MainWindow", "https://dummyjson.com/recipes"))
        self.pages_lbl.setText(_translate("MainWindow", "Pages: \n"
"(MAX 100)"))
        self.label.setText(_translate("MainWindow", "Resourse:"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))