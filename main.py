from PyQt5.QtWidgets import QApplication, QMainWindow
import design
import sys


class ClientViewer(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    clientViewer = ClientViewer()
    clientViewer.show()
    qapp.exec_()
