# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiMaster.ui'
#
# Created: Tue Mar 18 06:28:33 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(894, 578)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 251, 521))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.txtPath = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.txtPath.setObjectName(_fromUtf8("txtPath"))
        self.horizontalLayout_2.addWidget(self.txtPath)
        self.cmdSelectPath = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.cmdSelectPath.setMaximumSize(QtCore.QSize(30, 16777215))
        self.cmdSelectPath.setObjectName(_fromUtf8("cmdSelectPath"))
        self.horizontalLayout_2.addWidget(self.cmdSelectPath)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lstFiles = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.lstFiles.setObjectName(_fromUtf8("lstFiles"))
        self.verticalLayout.addWidget(self.lstFiles)
        self.lblSelect = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.lblSelect.setMinimumSize(QtCore.QSize(255, 255))
        self.lblSelect.setMaximumSize(QtCore.QSize(300, 300))
        self.lblSelect.setStyleSheet(_fromUtf8("border-color: rgb(255, 58, 58); border: 1px solid; "))
        self.lblSelect.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblSelect.setObjectName(_fromUtf8("lblSelect"))
        self.verticalLayout.addWidget(self.lblSelect)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(260, 0, 631, 521))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblGraph = QtGui.QLabel(self.horizontalLayoutWidget)
        self.lblGraph.setAlignment(QtCore.Qt.AlignCenter)
        self.lblGraph.setObjectName(_fromUtf8("lblGraph"))
        self.horizontalLayout.addWidget(self.lblGraph)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSelectPath.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSelect.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGraph.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

