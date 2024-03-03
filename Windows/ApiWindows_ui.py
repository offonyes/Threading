# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ApiWindows.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QLabel, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(515, 323)
        MainWindow.setMinimumSize(QSize(515, 323))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {\n"
"    background-color: rgba(0,0,0, 80)\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame {\n"
"	background-color: rgba(0, 0, 0, 90);\n"
"}")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(5)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(76, 255, 0);")

        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 30))
        self.label_3.setMaximumSize(QSize(120, 35))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(277, 30))
        self.comboBox.setMaximumSize(QSize(16777215, 35))
        self.comboBox.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 50))
        self.label_2.setMaximumSize(QSize(120, 60))
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 30))
        self.label.setMaximumSize(QSize(120, 35))
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(0, 25))
        self.doubleSpinBox.setMaximumSize(QSize(16777215, 30))
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setValue(100.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar::chunk {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 160, 255, 255), stop:1 rgba(0, 160, 180, 255));\n"
"}")
        self.progressBar.setValue(25)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.progressBar, 2, 1, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 2)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        self.pushButton_2.setSizeIncrement(QSize(0, 45))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 238, 0, 255);\n"
"    color: rgb(255, 255, 255);\n"
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

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setSizeIncrement(QSize(0, 45))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
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
"    background-color: rgba(178, 0, 0, 255); \n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_3, 4, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Turn on", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Threads:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"https://dummyjson.com/products", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"https://dummyjson.com/carts", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"https://dummyjson.com/users", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"https://dummyjson.com/posts", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"https://dummyjson.com/comments", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"https://dummyjson.com/quotes", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"https://dummyjson.com/recipes", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"https://dummyjson.com/todos", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"https://dummyjson.com/products", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pages: \n"
"(MAX 100)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Resourse:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

