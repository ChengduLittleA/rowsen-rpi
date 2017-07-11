import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import spi

class MyTimer(QWidget):
    def __init__(self, parent = None):
        super(MyTimer, self).__init__(parent)      
        self.resize(400, 400)      
        self.setWindowTitle("QTimerDemo")
        
        self.lcd1 = QLCDNumber()      
        self.lcd1.setDigitCount(10)      
        self.lcd1.setMode(QLCDNumber.Dec)
        self.lcd1.setSegmentStyle(QLCDNumber.Flat)
        self.lcd1.display(0)

        self.lcd2 = QLCDNumber()      
        self.lcd2.setDigitCount(10)      
        self.lcd2.setMode(QLCDNumber.Dec)
        self.lcd2.setSegmentStyle(QLCDNumber.Flat)
        self.lcd2.display(0)

        layout = QVBoxLayout()
        layout.addWidget(self.lcd1)
        layout.addWidget(self.lcd2) 
        self.setLayout(layout)
               
        self.timer = QTimer()      
        self.timer.setInterval(200)       
        self.timer.start()
            
        self.timer.timeout.connect(self.onTimerOut)

        self.rw = spi.AD770X()
        
    def onTimerOut(self):
        a = self.rw.readADResultRaw(spi.CHN_AIN1)
        b = self.rw.readADResultRaw(spi.CHN_AIN2)
        self.lcd1.display(str(a))
        self.lcd2.display(str(b))


        
app = QApplication(sys.argv)
t = MyTimer()
t.show()
sys.exit(app.exec_())
