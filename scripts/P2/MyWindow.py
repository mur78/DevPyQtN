from PySide2 import QtCore, QtWidgets, QtGui
from ui import Form1
import time

# Задания:
# ВЫВОД В ЛОГ
# 1. Перемещение окна по заданным координатам
#
#screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
#screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()

# 2. Получение параметров экрана + установить для элемента shortCut (горячую клавишу)
#     a. Кол-во экранов
#     b. Текущее основное окно
#     c. Разрешение экрана
#     d. На каком экране окно находится
#     e. Размеры окна
#     f. Минимальные размеры окна
#     g. Текущее положение (координаты) окна
#     h. Координаты центра приложения
# 3. Отслеживани bе состояния окна (свернуто/развёрнуто/активно/отображено + время)
# ВЫВОД В ТЕРМИНАЛ
# 4. Информация о координатах при перемещении окна
# 5. Информиция о размерах окна при изменении размера
# 6. Значение кнопки когда она была нажата
#
# eventFilter
# 7. Добавить в dial возможность установки значений кнопками клавиатуры(+ и -), выводить новые значения в лог
#
# slots
# 8. Законектить между собой QDial, QSlider, QLCDNumber
# 9. Для QLCDNumber сделать отображение в различных системах счисления
#
# QSettings
# 10. Сохранять значение и режима LCDNumber в системные настройки, при перезапуске программы выводить в него
# соответствующие значения


# noinspection PyCallingNonCallable
class MyWidgetsForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWidgetsForm, self).__init__(parent)
        self.ui = Form1.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setMouseTracking(True)

        self.ui.HexLable.addItems(["HEX", "DEC", "OCT", "BIN"])
        self.ui.HexLable.currentIndexChanged.connect(self.changeLCDview)
        self.ui.GetData.clicked.connect(self.getScreenInfo)
        self.ui.RightUp.clicked.connect(self.editPosition)
        self.ui.LeftUp.clicked.connect(self.editPosition)
        self.ui.LeftDown.clicked.connect(self.editPosition)
        self.ui.RightDown.clicked.connect(self.editPosition)
        self.ui.Center.clicked.connect(self.editPosition)

        self.ui.GetData.setShortcut(QtGui.QKeySequence("F1"))

        self.ui.dial.valueChanged.connect(self.showLCD)
        self.ui.horizontalSlider.valueChanged.connect(self.showLCD)

        self.ui.dial.installEventFilter(self)


    # ===== #
    # SLOTS #
    # ===== #

    @QtCore.Slot()
    def getScreenInfo(self):
        """Получение параметров экрана"""
        screens_count = QtWidgets.QApplication.screens()
        log = self.ui.textEdit.appendPlainText

        log(time.ctime())
        log(f"{11*'='} SystemInfo {11*'='}")
        log(f"Кол-во экранов:           {len(screens_count)}")
        log(f"Основное окно:            {QtWidgets.QApplication.primaryScreen().name()}")
        for cur_screen in screens_count:
            log(f"Разрешение экрана         {cur_screen.name()} составляет {cur_screen.size().width()} на {cur_screen.size().height()}")
        log(f"Окно находится на экране  {QtWidgets.QApplication.screenAt(self.pos()).name()}")
        log(f"Размеры окна:             Ширина {self.size().width()} Высота {self.size().height()}")
        log(f"Минимальные размеры окна: Ширина {self.minimumWidth()} Высота {self.minimumHeight()}")
        log(f"Текущее положение:        x = {self.pos().x()} y = {self.pos().y()}")
        log(f"Центр приложения:         x = {self.pos().x() + self.width()/2} y = {self.pos().y() + self.height()/2}")
        log(f"{30 * '='}\n")


    def editPosition(self):
        """Перемещение экрана на заданную позицию"""
        print(self.sender())
        buttonText = self.sender().text()
        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()

        position = {"Лево/Верх":(0, 0),
                    "Лево/Низ": (0, screenHeight-self.height()-75),
                    "Центр": (screenWidth/2 - self.width()/2, screenHeight/2 - self.height()/2),
                    "Право/Верх": (screenWidth - self.width(), 0),
                    "Право/Низ": (screenWidth- self.width(), screenHeight-self.height()-75)}

        self.move(position.get(buttonText)[0], position.get(buttonText)[1])

    def showLCD(self):
        if self.sender().objectName() == "dial":
            value = self.ui.dial.value()

        elif self.sender().objectName() == "horizontalSlider":
            value = self.ui.horizontalSlider.value()

        self.ui.lcdNumber.display(value)
        self.ui.horizontalSlider.setValue(value)
        self.ui.dial.setValue(value)

    def changeLCDview(self):
        # print(123)

        a = {"HEX": self.ui.lcdNumber.setHexMode, "BIN": self.ui.lcdNumber.setBinMode,
             "OCT": self.ui.lcdNumber.setOctMode, "DEC": self.ui.lcdNumber.setDecMode}

        a[self.ui.HexLable.currentText()]()
        print(self.ui.lcdNumber.mode())



    # ====== #
    # EVENTS #
    # ====== #

    def changeEvent(self, event: QtCore.QEvent) -> None:
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                self.ui.textEdit.appendPlainText(time.ctime() + ": window is minimized")
            elif self.isMaximized():
                self.ui.textEdit.appendPlainText(time.ctime() + ": window is maximized")
        if event.type() == QtCore.QEvent.ActivationChange:
            self.ui.textEdit.append(time.ctime() + ": window is active")

        QtWidgets.QWidget.changeEvent(self, event)

    def showEvent(self, event:QtGui.QShowEvent) -> None:
        self.ui.textEdit.append(time.ctime() + ": window is show")

        QtWidgets.QWidget.showEvent(self, event)

    def hideEvent(self, event:QtGui.QHideEvent) -> None:
        self.ui.textEdit.append(time.ctime() + ": window is hide")
        QtWidgets.QWidget.hideEvent(self, event)

    def moveEvent(self, event:QtGui.QMoveEvent) -> None:
        print(f"moveEvent:   x = {event.pos().x()}, y = {event.pos().y()}")
        QtWidgets.QWidget.moveEvent(self, event)

    def resizeEvent(self, event:QtGui.QResizeEvent) -> None:
        print(f"resizeEvent: w = {event.size().width()}, h = {event.size().height()}")
        QtWidgets.QWidget.resizeEvent(self, event)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно",
                                                     "Вы хотите закрыть окно?",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.KeyPress:
            print(f"{event.text()} is pressed")

        return QtWidgets.QWidget.event(self, event)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:

        if watched == self.ui.dial and event.type() == QtCore.QEvent.KeyPress:
            if event.text() == "+":
                self.ui.dial.setValue(self.ui.dial.value()+1)
            if event.text() == "-":
                self.ui.dial.setValue(self.ui.dial.value()-1)

            self.ui.textEdit.appendPlainText(f"dial value {self.ui.dial.value()}")


        return super(MyWidgetsForm, self).eventFilter(watched, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyWidgetsForm()
    myapp.show()

    app.exec_()
