# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 266)
        self.label_sort = QtWidgets.QLabel(Dialog)
        self.label_sort.setGeometry(QtCore.QRect(10, 12, 161, 21))
        self.label_sort.setObjectName("label_sort")
        self.label_price = QtWidgets.QLabel(Dialog)
        self.label_price.setGeometry(QtCore.QRect(10, 130, 161, 21))
        self.label_price.setObjectName("label_price")
        self.label_description = QtWidgets.QLabel(Dialog)
        self.label_description.setGeometry(QtCore.QRect(10, 100, 161, 21))
        self.label_description.setObjectName("label_description")
        self.lineEdit_frying = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_frying.setGeometry(QtCore.QRect(180, 40, 321, 21))
        self.lineEdit_frying.setObjectName("lineEdit_frying")
        self.comboBox_ground = QtWidgets.QComboBox(Dialog)
        self.comboBox_ground.setGeometry(QtCore.QRect(180, 70, 321, 22))
        self.comboBox_ground.setObjectName("comboBox_ground")
        self.pushButton_no_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_no_ok.setGeometry(QtCore.QRect(310, 190, 141, 61))
        self.pushButton_no_ok.setObjectName("pushButton_no_ok")
        self.lineEdit_price = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price.setGeometry(QtCore.QRect(180, 130, 321, 21))
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(74, 190, 141, 61))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.label_ground = QtWidgets.QLabel(Dialog)
        self.label_ground.setGeometry(QtCore.QRect(10, 70, 161, 21))
        self.label_ground.setObjectName("label_ground")
        self.label_volume = QtWidgets.QLabel(Dialog)
        self.label_volume.setGeometry(QtCore.QRect(10, 160, 161, 21))
        self.label_volume.setObjectName("label_volume")
        self.lineEdit_description = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_description.setGeometry(QtCore.QRect(180, 100, 321, 21))
        self.lineEdit_description.setObjectName("lineEdit_description")
        self.lineEdit_sort = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_sort.setGeometry(QtCore.QRect(180, 10, 321, 21))
        self.lineEdit_sort.setObjectName("lineEdit_sort")
        self.lineEdit_volume = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_volume.setGeometry(QtCore.QRect(180, 160, 321, 21))
        self.lineEdit_volume.setObjectName("lineEdit_volume")
        self.label_frying = QtWidgets.QLabel(Dialog)
        self.label_frying.setGeometry(QtCore.QRect(10, 40, 161, 21))
        self.label_frying.setObjectName("label_frying")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_sort.setText(_translate("Dialog", "Сорт"))
        self.label_price.setText(_translate("Dialog", "Цена"))
        self.label_description.setText(_translate("Dialog", "Описание вкуса"))
        self.pushButton_no_ok.setText(_translate("Dialog", "NO OK"))
        self.pushButton_ok.setText(_translate("Dialog", "OK"))
        self.label_ground.setText(_translate("Dialog", "Молотый или в зернах"))
        self.label_volume.setText(_translate("Dialog", "Объем"))
        self.label_frying.setText(_translate("Dialog", "Степень обжарки"))
