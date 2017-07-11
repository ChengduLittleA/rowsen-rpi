import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import spi

GLOBAL_Zero1=0
GLOBAL_Zero2=0

class MyTimer(QWidget):
    def __init__(self, parent = None):
        super(MyTimer, self).__init__(parent)      
        self.resize(400, 400)      
        self.setWindowTitle("QTimerDemo")
        
        self.lcd1 = QLCDNumber()      
        self.lcd1.setDigitCount(6)      
        self.lcd1.setMode(QLCDNumber.Dec)
        self.lcd1.setSegmentStyle(QLCDNumber.Flat)
        self.lcd1.display(0)

        self.lcd2 = QLCDNumber()      
        self.lcd2.setDigitCount(6)      
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

        self.ZeroOut()
    
    def ZeroOut(self):
        time.sleep(1)
        GLOBAL_Zero1 = self.rw.readADResultRaw(spi.CHN_AIN1)
        time.sleep(0.1)
        GLOBAL_Zero2 = self.rw.readADResultRaw(spi.CHN_AIN2)
        
    def onTimerOut(self):
        a = self.rw.readADResultRaw(spi.CHN_AIN1)
        a-=GLOBAL_Zero1
        a/=134.21

        time.sleep(0.1)

        b = self.rw.readADResultRaw(spi.CHN_AIN2)
        b-=GLOBAL_Zero2
        b/=134.21
        
        self.lcd1.display("%.1f"%a)
        self.lcd2.display("%.1f"%b)


        
app = QApplication(sys.argv)
t = MyTimer()
t.show()
sys.exit(app.exec_())
