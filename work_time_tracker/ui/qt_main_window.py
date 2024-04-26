# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 351, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.weeklyWorkTimeLabel = QLabel(self.verticalLayoutWidget)
        self.weeklyWorkTimeLabel.setObjectName(u"weeklyWorkTimeLabel")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(18)
        font.setBold(True)
        self.weeklyWorkTimeLabel.setFont(font)

        self.verticalLayout.addWidget(self.weeklyWorkTimeLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.dailyWorkTimeLabel = QLabel(self.verticalLayoutWidget)
        self.dailyWorkTimeLabel.setObjectName(u"dailyWorkTimeLabel")
        self.dailyWorkTimeLabel.setFont(font)

        self.verticalLayout.addWidget(self.dailyWorkTimeLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.currentWorkTimeLabel = QLabel(self.verticalLayoutWidget)
        self.currentWorkTimeLabel.setObjectName(u"currentWorkTimeLabel")
        self.currentWorkTimeLabel.setFont(font)

        self.verticalLayout.addWidget(self.currentWorkTimeLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.startTimerButton = QPushButton(self.verticalLayoutWidget)
        self.startTimerButton.setObjectName(u"startTimerButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTimerButton.sizePolicy().hasHeightForWidth())
        self.startTimerButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.startTimerButton.setFont(font1)

        self.verticalLayout.addWidget(self.startTimerButton, 0, Qt.AlignHCenter)

        self.currentDateTimeLabel = QLabel(self.verticalLayoutWidget)
        self.currentDateTimeLabel.setObjectName(u"currentDateTimeLabel")
        self.currentDateTimeLabel.setFont(font)

        self.verticalLayout.addWidget(self.currentDateTimeLabel, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.weeklyWorkTimeLabel.setText("")
        self.dailyWorkTimeLabel.setText("")
        self.currentWorkTimeLabel.setText("")
        self.label.setText("")
        self.startTimerButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443", None))
        self.currentDateTimeLabel.setText("")
    # retranslateUi

