from PyQt5 import QtSerialPort
from PyQt5.QtCore import (
    pyqtSlot, QByteArray, QObject, pyqtSignal, QRunnable, Qt, QTimer, QTime, QSettings, QSize, QThread, QEventLoop, QIODevice,
)
import time


def receive():
    while serial.canReadLine():
        text = serial.readLine().data().decode()
        text = text.rstrip('\r\n')
        result = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", text)

        # print(text.split())
        # print(result)
        if "Received" in text:
            flow_index = int(result[1])
            flow_voltage = float(result[2])
            # print("Received Serial:", value)
            # self.new_data.emit(value)
        elif "Temperature" in text:
            temp_index = int(result[1])
            temp_voltage = float(result[2])

        else:
            print(text)
        #
        if flow_index == self.temp_index:
            add_data_point(flow_voltage, None, [temp_voltage, 0.0, 0.0, 0.0])
serial = QtSerialPort.QSerialPort('COM7')
serial.setBaudRate(115200)
serial.readyRead.connect(receive)
a=serial.open(QIODevice.ReadWrite)
print(a)

#serial = QtSerialPort.QSerialPort('COM7', QtSerialPort.QSerialPort.Baud115200, receive)
#serial