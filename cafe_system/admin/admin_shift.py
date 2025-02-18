# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_shift.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import bd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from admin.admin_order import Ui_adminPanelOrder
from admin.modal_shift import Ui_createShiftModal
from admin.staff_in_shift import Ui_StaffInShift
import assets.resources


class Ui_adminPanelShift(object):
    def setupUi(self, adminPanelShift):
        self.admin_panel =adminPanelShift
        self.main = adminPanelShift
        adminPanelShift.setObjectName("adminPanelShift")
        adminPanelShift.resize(971, 713)
        self.frame = QtWidgets.QFrame(adminPanelShift)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 991, 731))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.staffPageButton = QtWidgets.QPushButton(self.frame)
        self.staffPageButton.setGeometry(QtCore.QRect(10, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.staffPageButton.setFont(font)
        self.staffPageButton.setAutoFillBackground(False)
        self.staffPageButton.setStyleSheet("border: 1px solid rgb(153, 102, 51); ")
        self.staffPageButton.setAutoDefault(False)
        self.staffPageButton.clicked.connect(adminPanelShift.close)
        self.staffPageButton.setObjectName("staffPageButton")
        self.shiftPageButton = QtWidgets.QPushButton(self.frame)
        self.shiftPageButton.setGeometry(QtCore.QRect(260, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.shiftPageButton.setFont(font)
        self.shiftPageButton.setAutoFillBackground(False)
        self.shiftPageButton.setStyleSheet("border: 1px solid rgb(153, 102, 51);\n"
"background-color: rgb(209, 207, 207);")
        self.shiftPageButton.setAutoDefault(False)
        self.shiftPageButton.setObjectName("shiftPageButton")
        
        self.orderPageButton = QtWidgets.QPushButton(self.frame)
        self.orderPageButton.clicked.connect(adminPanelShift.close)
        self.orderPageButton.setGeometry(QtCore.QRect(510, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.orderPageButton.setFont(font)
        self.orderPageButton.setAutoFillBackground(False)
        self.orderPageButton.setStyleSheet("border: 1px solid rgb(153, 102, 51);")
        self.orderPageButton.setAutoDefault(False)
        self.orderPageButton.setObjectName("orderPageButton")
        self.orderPageButton.clicked.connect(self.openOrderPanel)
        self.orderPageButton.clicked.connect(adminPanelShift.close)
        self.createShiftButton = QtWidgets.QPushButton(self.frame)
        self.createShiftButton.clicked.connect(self.openAddShiftModal)
        self.createShiftButton.setGeometry(QtCore.QRect(30, 80, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.createShiftButton.setFont(font)
        self.createShiftButton.setAutoFillBackground(False)
        self.createShiftButton.setStyleSheet("background-color: rgb(153, 102, 51);")
        self.createShiftButton.setAutoDefault(False)
        self.createShiftButton.setObjectName("createShiftButton")
        self.shiftTable = QtWidgets.QTableWidget(self.frame)
        self.shiftTable.setGeometry(QtCore.QRect(30, 140, 731, 531))
        self.shiftTable.setAutoFillBackground(True)
        self.shiftTable.setStyleSheet("border: 1px solid rgb(153, 102, 51);")
        self.shiftTable.setRowCount(5)
        self.shiftTable.setAutoScroll( True)
        self.shiftTable.itemDoubleClicked.connect(self.showStaffOnShift)
        self.shiftTable.setColumnCount(4)
        self.shiftTable.itemClicked.connect(self.editingShift)
        self.shiftTable.setObjectName("shiftTable")
        item = QtWidgets.QTableWidgetItem()
        self.shiftTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.shiftTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.shiftTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.shiftTable.setHorizontalHeaderItem(3, item)
        self.shiftTable.horizontalHeader().setVisible(True)
        self.shiftTable.horizontalHeader().setCascadingSectionResizes(False)
        self.icon = QtWidgets.QLabel(self.frame)
        self.icon.setGeometry(QtCore.QRect(790, 30, 161, 191))
        self.icon.setText("")
        self.icon.setTextFormat(QtCore.Qt.RichText)
        self.icon.setPixmap(QtGui.QPixmap(":assets/icon.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.saveShift = QtWidgets.QPushButton(self.frame)
        self.saveShift.setGeometry(QtCore.QRect(790, 630, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.saveShift.setFont(font)
        self.saveShift.setAutoFillBackground(False)
        self.saveShift.setStyleSheet("background-color: rgb(153, 102, 51);")
        self.saveShift.setAutoDefault(False)
        self.saveShift.setObjectName("saveShift")
        self.saveShift.setVisible(False)
        self.saveShift.clicked.connect(self.saveEditingShift)

        self.retranslateUi(adminPanelShift)
        QtCore.QMetaObject.connectSlotsByName(adminPanelShift)

    def retranslateUi(self, adminPanelShift):
        _translate = QtCore.QCoreApplication.translate
        adminPanelShift.setWindowTitle(_translate("adminPanelShift", "Панель администратора. Смены"))
        self.staffPageButton.setText(_translate("adminPanelShift", "Сотрудники"))
        self.shiftPageButton.setText(_translate("adminPanelShift", "Смены"))
        self.orderPageButton.setText(_translate("adminPanelShift", "Заказы"))
        self.createShiftButton.setText(_translate("adminPanelShift", "Создать смену"))
        self.shiftTable.setSortingEnabled(False)
        item = self.shiftTable.horizontalHeaderItem(0)
        item.setText(_translate("adminPanelShift", "id"))
        item = self.shiftTable.horizontalHeaderItem(1)
        item.setText(_translate("adminPanelShift", "Дата"))
        item = self.shiftTable.horizontalHeaderItem(2)
        item.setText(_translate("adminPanelShift", "Начало"))
        item = self.shiftTable.horizontalHeaderItem(3)
        item.setText(_translate("adminPanelShift", "Конец"))
        self.saveShift.setText(_translate("adminPanelShift", "Сохранить"))
    
    def editingShift(self):
        self.saveShift.setVisible(True)

    def openOrderPanel(self):
            self.order = QWidget()
            self.ui = Ui_adminPanelOrder()
            self.ui.setupUi(self.order)
            self.ui.loadOredersTable()
            self.order.show()
            self.ui.shiftPageButton.clicked.connect(self.main.show)
            self.ui.staffPageButton.clicked.connect(self.admin_panel.show)
            self.main.close()

    def openAddShiftModal(self):
            self.modal = QWidget()
            self.ui = Ui_createShiftModal()
            self.ui.setupUi(self.modal)
            self.modal.show()
            self.ui.saveShiftModalButton.clicked.connect(self.loadShifttaffTable)
            self.ui.loadStaffInComboBox()


    def loadShifttaffTable(self):
        connection = bd.connectBd()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Work_shift;")
        data_staff = cursor.fetchall()
        self.shiftTable.setRowCount(0)
        self.shiftTable.setColumnCount(4)
        self.shiftTable.hideColumn(0)
        for row_number, row_data in enumerate(data_staff):
            self.shiftTable.insertRow(row_number)
            for c_number, data in enumerate(row_data):
                self.shiftTable.setItem(
                    row_number,
                    c_number,
                    QtWidgets.QTableWidgetItem(str(row_data[data])),
                )
        self.shiftTable.setHorizontalHeaderLabels(
           ["id", "Дата","Начало", "Конец"]
        )
        self.shiftTable.resizeColumnsToContents()
        connection.close()

    def saveEditingShift(self):
        connection = bd.connectBd()
        cursor = connection.cursor()
        for i in range(self.shiftTable.rowCount()):
            id = self.shiftTable.item(i, 0).text()
            date = self.shiftTable.item(i, 1).text()
            start = self.shiftTable.item(i, 2).text()
            end = self.shiftTable.item(i, 3).text()
            cursor.execute(
                "UPDATE Work_shift SET date = '{}', start ='{}', stop = '{}' WHERE shift_id = {} ;".format(date, start,end,id)
            )
        connection.commit()
        cursor.execute("SELECT * FROM Work_shift;")
        data_staff = cursor.fetchall()
        self.shiftTable.setRowCount(0)
        self.shiftTable.setColumnCount(4)
        self.shiftTable.hideColumn(0)
        for row_number, row_data in enumerate(data_staff):
            self.shiftTable.insertRow(row_number)
            for c_number, data in enumerate(row_data):
                self.shiftTable.setItem(
                    row_number,
                    c_number,
                    QtWidgets.QTableWidgetItem(str(row_data[data])),
                )
        self.shiftTable.setHorizontalHeaderLabels(
           ["id", "Дата","Начало", "Конец"]
        )
        self.shiftTable.resizeColumnsToContents()
        connection.close()
        self.saveShift.setVisible(False)

    def showStaffOnShift(self):
            row = self.shiftTable.selectionModel().selectedIndexes()[0].row()
            print(row)
            id = self.shiftTable.item(row,0).text()
            print(id)
            self.modal = QWidget()
            self.ui = Ui_StaffInShift()
            self.ui.setupUi(self.modal)
            self.ui.idShift.setText(id)
            self.ui.loadStaffInShift()
            self.modal.show()
            self.ui.closeStaffInShift.clicked.connect(self.modal.close)
