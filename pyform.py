# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdestest.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(255, 191, 101, 81))
        self.listView.setObjectName("listView")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 260, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(90, 200, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.SHOWButton = QtWidgets.QPushButton(Dialog)
        self.SHOWButton.setGeometry(QtCore.QRect(310, 110, 75, 23))
        self.SHOWButton.setObjectName("SHOWButton")
        self.labelshow = QtWidgets.QLabel(Dialog)
        self.labelshow.setGeometry(QtCore.QRect(140, 130, 81, 31))
        self.labelshow.setObjectName("labelshow")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 120, 80))
        self.widget.setObjectName("widget")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(40, 10, 69, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SHOWButton.setText(_translate("Dialog", "SHOW"))
        self.labelshow.setText(_translate("Dialog", "show here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
