from PyQt5.QtWidgets import QApplication, QMainWindow
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

    def create_client(self):
        name = self.lineName.text()
        age = int(self.lineAge.text())
        email = self.lineEmail.text()
        status = self.lineStatus.text()
        sql_clients.create(name, age, email, status)
        self.show_clients()
        self.clean_inputs()

    def show_clients(self):
        clients = sql_clients.read()
        for line in clients:
            print(line)
            self.labelClients.setText(f'{self.labelClients.text()}{line}\n')

    def update_client(self):
        id = int(self.lineId.text())
        name = self.lineName.text()
        age = int(self.lineAge.text())
        email = self.lineEmail.text()
        status = self.lineStatus.text()
        sql_clients.update(name, age, email, status, id)
        self.show_clients()
        self.clean_inputs()

    def delete_client(self):
        id = int(self.lineId.text())
        sql_clients.delete(id)
        self.show_clients()
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

