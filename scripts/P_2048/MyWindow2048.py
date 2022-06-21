from PySide2 import QtCore, QtWidgets, QtGui
from ui import form_2048
from Sim_2048 import Simulate2048

# matrix = [[0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0]]
m = Simulate2048()

# noinspection PyCallingNonCallable
class MyWidgetsForm2048(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWidgetsForm2048, self).__init__(parent)
        self.ui = form_2048.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMouseTracking(True)

        self.ui.lineEdit_1.setText(str(m.matrix[0][0]))
        self.ui.lineEdit_2.setText(str(m.matrix[0][1]))
        self.ui.lineEdit_3.setText(str(m.matrix[0][2]))
        self.ui.lineEdit_4.setText(str(m.matrix[0][3]))
        self.ui.lineEdit_5.setText(str(m.matrix[1][0]))
        self.ui.lineEdit_6.setText(str(m.matrix[1][1]))
        self.ui.lineEdit_7.setText(str(m.matrix[1][2]))
        self.ui.lineEdit_8.setText(str(m.matrix[1][3]))
        self.ui.lineEdit_9.setText(str(m.matrix[2][0]))
        self.ui.lineEdit_10.setText(str(m.matrix[2][1]))
        self.ui.lineEdit_11.setText(str(m.matrix[2][2]))
        self.ui.lineEdit_12.setText(str(m.matrix[2][3]))
        self.ui.lineEdit_13.setText(str(m.matrix[3][0]))
        self.ui.lineEdit_14.setText(str(m.matrix[3][1]))
        self.ui.lineEdit_15.setText(str(m.matrix[3][2]))
        self.ui.lineEdit_16.setText(str(m.matrix[3][3]))
        self.ui.right.clicked.connect(m.click_right())
        self.ui.left.clicked.connect(m.click_right())
        self.ui.down.clicked.connect(m.click_down())
        self.ui.up.clicked.connect(m.click_up())
        self.ui.init.clicked.connect(m.click_init())
        self.ui.lineEdit_score.setText(m.total_score())

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    myapp = MyWidgetsForm2048()
    myapp.show()
    app.exec_()
