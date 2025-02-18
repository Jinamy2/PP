# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order_kitchen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import bd


class Ui_kitchenPanel(object):
    def setupUi(self, kitchenPanel):
        kitchenPanel.setObjectName("kitchenPanel")
        kitchenPanel.resize(971, 713)
        self.frame = QtWidgets.QFrame(kitchenPanel)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 991, 731))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.orderPageButton = QtWidgets.QPushButton(self.frame)
        self.orderPageButton.setGeometry(QtCore.QRect(10, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.orderPageButton.setFont(font)
        self.orderPageButton.setAutoFillBackground(False)
        self.orderPageButton.setStyleSheet("border: 1px solid rgb(153, 102, 51);\n"
"background-color: rgb(209, 207, 207);")
        self.orderPageButton.setAutoDefault(False)
        self.orderPageButton.setObjectName("orderPageButton")
        self.orderTable = QtWidgets.QTableWidget(self.frame)
        self.orderTable.setGeometry(QtCore.QRect(30, 140, 731, 531))
        self.orderTable.setAutoFillBackground(True)
        self.orderTable.setStyleSheet("border: 1px solid rgb(153, 102, 51);")
        self.orderTable.setRowCount(5)
        self.orderTable.setColumnCount(4)
        self.orderTable.itemClicked.connect(self.showSave)
        self.orderTable.setObjectName("orderTable")
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(3, item)
        self.orderTable.horizontalHeader().setVisible(True)
        self.orderTable.horizontalHeader().setCascadingSectionResizes(False)
        self.icon = QtWidgets.QLabel(self.frame)
        self.icon.setGeometry(QtCore.QRect(790, 30, 161, 191))
        self.icon.setText("")
        self.icon.setTextFormat(QtCore.Qt.RichText)
        self.icon.setPixmap(QtGui.QPixmap(":/assets/:assets/icon.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.saveOrderButton = QtWidgets.QPushButton(self.frame)
        self.saveOrderButton.setGeometry(QtCore.QRect(30, 70, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.saveOrderButton.setFont(font)
        self.saveOrderButton.setAutoFillBackground(False)
        self.saveOrderButton.setStyleSheet("background-color: rgb(153, 102, 51);")
        self.saveOrderButton.setAutoDefault(False)
        self.saveOrderButton.setObjectName("saveOrderButton")
        self.saveOrderButton.setVisible(False)
        self.saveOrderButton.clicked.connect(self.saveOrder)

        self.retranslateUi(kitchenPanel)
        QtCore.QMetaObject.connectSlotsByName(kitchenPanel)

    def retranslateUi(self, kitchenPanel):
        _translate = QtCore.QCoreApplication.translate
        kitchenPanel.setWindowTitle(_translate("kitchenPanel", "Панель повара. Заказы"))
        self.orderPageButton.setText(_translate("kitchenPanel", "Заказы"))
        self.orderTable.setSortingEnabled(False)
        item = self.orderTable.horizontalHeaderItem(0)
        item.setText(_translate("kitchenPanel", "id"))
        item = self.orderTable.horizontalHeaderItem(1)
        item.setText(_translate("kitchenPanel", "Заказ"))
        item = self.orderTable.horizontalHeaderItem(2)
        item.setText(_translate("kitchenPanel", "Статус зала"))
        item = self.orderTable.horizontalHeaderItem(3)
        item.setText(_translate("kitchenPanel", "Статус кухни"))
        self.saveOrderButton.setText(_translate("kitchenPanel", "Сохранить"))

    def showSave(self):
        self.saveOrderButton.setVisible(True)

    def loadOrder(self):
        connection = bd.connectBd()
        cursor = connection.cursor()
        cursor.execute("SELECT  Orders.order_id,Orders.description,Orders.table_number,Orders.count_customer,Status_order_waiter.name,Status_order_kitchen.name FROM `Orders` join Status_order_waiter on Orders.status_waiter=Status_order_waiter.status_waiter_id left join Status_order_kitchen on Orders.status_kitchen=Status_order_kitchen.status_kitchen_id;")
        data_staff = cursor.fetchall()
        self.orderTable.setRowCount(0)
        self.orderTable.setColumnCount(6)
        self.orderTable.hideColumn(0)
        for row_number, row_data in enumerate(data_staff):
            self.orderTable.insertRow(row_number)
            for c_number, data in enumerate(row_data):
                self.orderTable.setItem(
                    row_number,
                    c_number,
                    QtWidgets.QTableWidgetItem(str(row_data[data])),
                )
        self.orderTable.setHorizontalHeaderLabels(
           ["id", "Описание заказа","Номер столика", "Кол-во гостей", "Статус зала", "Статус кухни"]
        )
        self.orderTable.resizeColumnsToContents()
        connection.close()
    
    def saveOrder(self):
        connection = bd.connectBd()
        cursor = connection.cursor()
        for i in range(self.orderTable.rowCount()):
            id = self.orderTable.item(i, 0).text()
            status_kitchen = self.orderTable.item(i, 5).text()
            cursor.execute(
                "UPDATE `Orders` SET `status_kitchen` = (SELECT status_kitchen_id FROM Status_order_kitchen WHERE name = '{}') WHERE `Orders`.`order_id` = {};".format(status_kitchen,id)
            )
        connection.commit()
        cursor.execute("SELECT  Orders.order_id,Orders.description,Orders.table_number,Orders.count_customer,Status_order_waiter.name,Status_order_kitchen.name FROM `Orders` join Status_order_waiter on Orders.status_waiter=Status_order_waiter.status_waiter_id left join Status_order_kitchen on Orders.status_kitchen=Status_order_kitchen.status_kitchen_id;")
        data_order = cursor.fetchall()
        self.orderTable.setRowCount(0)
        self.orderTable.setColumnCount(6)
        self.orderTable.hideColumn(0)
        for row_number, row_data in enumerate(data_order):
            self.orderTable.insertRow(row_number)
            for c_number, data in enumerate(row_data):
                self.orderTable.setItem(
                    row_number,
                    c_number,
                    QtWidgets.QTableWidgetItem(str(row_data[data])),
                )
        self.orderTable.setHorizontalHeaderLabels(
           ["id", "Описание заказа","Номер столика", "Кол-во гостей", "Статус зала", "Статус кухни"]
        )
        self.orderTable.resizeColumnsToContents()
        connection.close()
        self.saveOrderButton.setVisible(False)

