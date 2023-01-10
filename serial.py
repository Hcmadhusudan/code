from PyQt5 import QtSerialPort
from PyQt5.QtCore import (
    pyqtSlot, QByteArray, QObject, pyqtSignal, QRunnable, Qt, QTimer, QTime, QSettings, QSize, QThread, QEventLoop, QIODevice,
)
import time
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
)
import sys
import re

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.serial = QtSerialPort.QSerialPort('COM3')
        self.serial.setBaudRate(115200)
        self.serial.readyRead.connect(self.receive)
        a = self.serial.open(QIODevice.ReadWrite)
        print(a)

    @pyqtSlot()
    def receive(self):
        try:
            while self.serial.canReadLine():
                text = self.serial.readLine().data().decode()
                text = text.rstrip('\r\n')
                result = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", text)

                if "Received" in text:
                    flow_index = int(result[1])
                    flow_voltage = float(result[2])
                    print(flow_voltage)
                    # print("Received Serial:", value)
                    # self.new_data.emit(value)
                elif "Temperature" in text:
                    pass
                    temp_index = int(result[1])
                    temp_voltage = float(result[2])
                else:
                    print(text)

        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MainWindow()
    # w.show()
    sys.exit(app.exec())
#serial = QtSerialPort.QSerialPort('COM7', QtSerialPort.QSerialPort.Baud115200, receive)
#serial