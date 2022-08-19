from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from mysql_connection import connection, cursor
import sql_clients
import design
import sys


class ClientViewer(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnCreate.clicked.connect(self.create_client)
        self.btnRefresh.clicked.connect(self.show_clients)
        self.btnUpdate.clicked.connect(self.update_client)
        self.btnDelete.clicked.connect(self.delete_client)

        self.tableClients.setColumnWidth(1, 200)
        self.tableClients.setColumnWidth(3, 200)

    def create_client(self):
        try:
            name = self.lineName.text()
            age = int(self.lineAge.text())
            email = self.lineEmail.text()
            status = self.lineStatus.text()
            sql_clients.create(name, age, email, status)
            self.show_clients()
            self.clean_inputs()
        except Exception as e:
            print('Something went wrong, error: ', e)
            self.clean_inputs()

    def show_clients(self):
        try:
            clients = sql_clients.read()
            row = 0
            self.tableClients.setRowCount(len(clients))
            for line in clients:
                self.tableClients.setItem(row, 0, QtWidgets.QTableWidgetItem(str(line['id'])))
                self.tableClients.setItem(row, 1, QtWidgets.QTableWidgetItem(line['name']))
                self.tableClients.setItem(row, 2, QtWidgets.QTableWidgetItem(str(line['age'])))
                self.tableClients.setItem(row, 3, QtWidgets.QTableWidgetItem(line['email']))
                self.tableClients.setItem(row, 4, QtWidgets.QTableWidgetItem(line['status']))
                row += 1
        except Exception as e:
            print('Something went wrong, error: ', e)
            self.clean_inputs()

    def update_client(self):
        try:
            if not self.lineId.text():
                print('Id field is required for UPDATE!')
            else:
                id = int(self.lineId.text())
                name = self.lineName.text()
                age = int(self.lineAge.text())
                email = self.lineEmail.text()
                status = self.lineStatus.text()
                sql_clients.update(name, age, email, status, id)
                self.show_clients()
                self.clean_inputs()
        except Exception as e:
            print('Something went wrong, error: ', e)
            self.clean_inputs()

    def delete_client(self):
        try:
            if not self.lineId.text():
                print('Id field is required for DELETE!')
            else:
                id = int(self.lineId.text())
                sql_clients.delete(id)
                self.show_clients()
                self.clean_inputs()
        except Exception as e:
            print('Something went wrong, error: ', e)
            self.clean_inputs()

    def clean_inputs(self):
        self.lineId.setText('')
        self.lineName.setText('')
        self.lineAge.setText('')
        self.lineEmail.setText('')
        self.lineStatus.setText('')


if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    clientViewer = ClientViewer()
    clientViewer.show()
    qapp.exec_()
    cursor.close()
    connection.close()

