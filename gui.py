import sys
import serial

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class UI(QWidget):
    
	def __init__(self):
		super().__init__()
        
		self.initUI()
        
	def initUI(self):    
		self.serInit()
		#self.btnInit()
		grid = QGridLayout()
		self.setLayout(grid)

		send_btn = QPushButton("Send it", self)
		#send_btn.setCheckable(True)
		send_btn.clicked[bool].connect(self.switchLight)
		
		return_btn = QPushButton("Return it", self)
		#return_btn.setCheckable(True)
		return_btn.clicked[bool].connect(self.switchLight)
		
		brake_btn = QPushButton("Stop it", self)
		#return_btn.setCheckable(True)
		brake_btn.clicked[bool].connect(self.switchLight)

		on_btn = QPushButton("I", self)
		off_btn = QPushButton("O", self)
		on_btn.clicked[bool].connect(self.ioFunc)
		off_btn.clicked[bool].connect(self.ioFunc)
		ioLabelStatic = QLabel("System: ")
		ioLabelStatic.setAlignment(Qt.AlignCenter)
		ioLabelData = QLabel("OFF")
		ioLabelData.setAlignment(Qt.AlignCenter)
		ioLabel = QHBoxLayout()
		ioLabel.addWidget(ioLabelStatic)
		ioLabel.addWidget(ioLabelData)

		self.ioLabelData = ioLabelData

		self.ctrl_btns = [send_btn, return_btn, brake_btn]
		self.send_btn = send_btn
		self.return_btn = return_btn
		self.brake_btn = brake_btn

		self.pwr_btns = [on_btn, off_btn]
		self.on_btn = on_btn
		self.on_btn.setStyleSheet("background-color: grey")
		self.off_btn = off_btn
		self.off_btn.setStyleSheet("background-color: green")

		label = QLabel("A cute little hello world app")
		header = QHBoxLayout()
		header.addWidget(label)
		label.setAlignment(Qt.AlignCenter)
		
		controlBox = QVBoxLayout()
		ioBox = QVBoxLayout()

		controlBox.addWidget(send_btn)
		controlBox.addWidget(return_btn)
		controlBox.addWidget(brake_btn)

		ioBox.addWidget(on_btn)
		ioBox.addWidget(off_btn)
		ioBox.addLayout(ioLabel)

		grid.addLayout(header, 0, 0, 1, 2)
		grid.addLayout(controlBox, 1, 0)
		grid.addLayout(ioBox, 1, 1)

     
		#self.move(300, 150)
		self.setWindowTitle('TouchMeFeelMe')
		self.resize(350, 150)
		self.center()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		#print(qr)
		cp = QDesktopWidget().availableGeometry().center()
		#print(cp)
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def switchLight(self, pressed):
		source = self.sender()
		print(source)
		for btn in self.ctrl_btns:
			if (btn == source):
				btn.setStyleSheet("background-color: green")
				if (btn == self.send_btn):
					print('send ittt')
					self.ser.write(b'f')
					self.ioLabelData.setText('Sending')
				elif (btn == self.return_btn):
					print("return ittt")
					self.ser.write(b'o')
					self.ioLabelData.setText('Returning')
				elif (btn == self.brake_btn):
					print("break ittt")
					self.ser.write(b'b')
					self.ioLabelData.setText('Braking')
			else:
				btn.setStyleSheet("background-color: grey")

	def ioFunc(self, pressed):
		source = self.sender()
		for btn in self.pwr_btns:
			if (btn == source):
				btn.setStyleSheet("background-color: green")
				if (btn == self.on_btn):
					print('system live')
					self.ser.write(b'i')
					self.ioLabelData.setText('ON')
				else:
					print('system dead')
					self.ser.write(b'd')
					self.ioLabelData.setText('OFF')
			else:
				btn.setStyleSheet("background-color: grey")


		

	def serInit(self):
		self.ser = serial.Serial()
		self.ser.baudrate = 115200
		self.ser.port = 'COM4'
		self.ser.open()
		self.ser.reset_output_buffer()
		self.ser.write(b'b')
		print('brakeee')

        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())
    print('closing serial')
    ser.close();