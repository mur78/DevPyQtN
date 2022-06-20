from PySide2 import QtCore, QtWidgets, QtGui
from ui import form_2048


# noinspection PyCallingNonCallable
class MyWidgetsForm2048(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWidgetsForm2048, self).__init__(parent)
        self.ui = form_2048.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMouseTracking(True)
        self.ui.lineEdit_1.setText(self.getdata())
        self.ui.lineEdit_2.setText(self.getdata())
        self.ui.lineEdit_3.setText(self.getdata())
        self.ui.lineEdit_4.setText(self.getdata())
        self.ui.lineEdit_5.setText(self.getdata())
        self.ui.lineEdit_6.setText(self.getdata())
        self.ui.lineEdit_7.setText(self.getdata())
        self.ui.lineEdit_8.setText(self.getdata())
        self.ui.lineEdit_9.setText(self.getdata())
        self.ui.lineEdit_10.setText(self.getdata())
        self.ui.lineEdit_11.setText(self.getdata())
        self.ui.lineEdit_12.setText(self.getdata())
        self.ui.lineEdit_13.setText(self.getdata())
        self.ui.lineEdit_14.setText(self.getdata())
        self.ui.lineEdit_15.setText(self.getdata())
        self.ui.lineEdit_16.setText(self.getdata())
        self.ui.right.clicked.connect(self.click_right)
        self.ui.left.clicked.connect(self.click_left)
        self.ui.down.clicked.connect(self.click_down)
        self.ui.up.clicked.connect(self.click_up)
        self.ui.init.clicked.connect(self.click_init)
        self.ui.lineEdit_score.setText(self.total_score())

    def getdata(self):
        value_str = "5"
        return value_str

    def total_score(self):
        total_str = "2048"
        return total_str

    def click_init(self):
        pass

    def click_right(self):
        pass

    def click_left(self):
        pass

    def click_up(self):
        pass

    def click_down(self):
        pass




if __name__ == "__main__":
    app = QtWidgets.QApplication()
    myapp = MyWidgetsForm2048()
    myapp.show()

    app.exec_()
