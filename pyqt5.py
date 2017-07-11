import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import spi

class MyTimer(QWidget):
    def __init__(self, parent = None):
        super(MyTimer, self).__init__(parent)      
        self.resize(200, 100)      
        self.setWindowTitle("QTimerDemo")
        
        self.lcd = QLCDNumber()      
        self.lcd.setDigitCount(10)      
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.display(0)

        layout = QVBoxLayout()
        layout.addWidget(self.lcd)       
        self.setLayout(layout)
               
        self.timer = QTimer()      
        self.timer.setInterval(1000)       
        self.timer.start()
            
        self.timer.timeout.connect(self.onTimerOut)

        self.rw = spi.AD770X()
        
    def onTimerOut(self):
        a = self.rw.readADResultRaw(spi.CHN_AIN1) 
        self.lcd.display(str(a))


        
app = QApplication(sys.argv)
t = MyTimer()
t.show()
sys.exit(app.exec_())
