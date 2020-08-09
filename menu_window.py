from PyQt5.Qt import *
# p
import sys
from PyQt5.QtWidgets import QFileDialog
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('QLineEdit-使用')
		self.resize(1000,800)
		self.setup_ui()
	
	def setup_ui(self):
		# ql_a = QLineEdit(self)
		# ql_a.setPlaceholderText('测试。。。')
		# action = QAction(self)
		# action.setIcon(QIcon('xxx.png'))
		# ql_a.addAction(action, QLineEdit.TrailingPosition)
		# # ql_a.setEchoMode(QLineEdit.text)
		# ql_a.move(100, 100)
		
		# ql_b = QLineEdit(self)
		# ql_b.move(100, 150)

		btn_open = QPushButton(self)
		btn_open.setText('打开图片')
		btn_open.move(100, 50)
		
		btn = QPushButton(self)
		btn.setText('阈值分割')
		btn.move(100, 700)
		
		btn1 = QPushButton(self)
		btn1.setText('取消')
		btn1.move(200, 700)

		btn2 = QPushButton(self)
		btn2.setText('灰度变换')
		btn2.move(300, 700)

		self.label = QLabel(self)
		self.label.setText("   显示图片")
		self.label.setFixedSize(300, 200)
		self.label.move(160, 160)

		self.label.setStyleSheet("QLabel{background:white;}"
								 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
								 )


		def cancel():
			# 取消选中
			# ql_a.deselect()
			exit(0)

		btn1.clicked.connect(cancel)
		

		def yuzhifenge():
			# text = ql_a.text()

			# imgPath = input("请输入待处理图片的路径")
			img = cv2.imread(self.imgpath, 0)

			# 阈值分割 固定阈值
			ret, th = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO_INV)
			# 自适应阈值
			th2 = cv2.adaptiveThreshold(
				img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
			cv2.imshow('thresh', th2)
			cv2.waitKey(0)
		btn.clicked.connect(yuzhifenge)


		def huidubianhuan():


			img = cv2.imread(self.imgpath, 0)
			gau = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯滤波
			blur = cv2.bilateralFilter(img, 5, 75, 75)  # 双边滤波

			res = np.hstack((img, gau, blur))
			cv2.imshow('res', res)
			cv2.waitKey(0)
			# cv2.imwrite(filepath, img)




		btn2.clicked.connect(huidubianhuan)

		def dakaitupian():
			# imgPath = ql_a.text()
			directory = QFileDialog.getOpenFileName(self,
			  "getOpenFileName","./",
			  "All Files (*);;Text Files (*.txt)") 
			self.imgpath = directory[0]
			jpg = QtGui.QPixmap(self.imgpath).scaled(self.label.width(), self.label.height())
			self.label.setPixmap(jpg)
		
		btn_open.clicked.connect(dakaitupian)



		btn_bianyuan = QPushButton(self)
		btn_bianyuan.setText('边缘检测')
		btn_bianyuan.move(400, 700)
		def bianyuanjiance():
			capture = cv2.VideoCapture(0)
			
			ret, frame = capture.read()
			edges = cv2.Canny(frame, 100, 100)
			# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 灰度图
			cv2.namedWindow('shen', cv2.WINDOW_NORMAL)
			cv2.imshow('shen', edges)
			# if cv2.waitKey(1) == ord('q'):
			# 	break
		btn_bianyuan.clicked.connect(bianyuanjiance)

	
		btn_pingyi = QPushButton(self)
		btn_pingyi.setText('平移图片')
		btn_pingyi.move(500, 700)
		def pingyitupian():
			print("here")


			img = cv2.imread(self.imgpath, 0) #打开图片


			# 4、平移图片
			rows, cols = img.shape[:2]
			# 定义平移矩阵，需要是numpy的float32类型
			# x轴平移100，y轴平移50
			M = np.float32([[1, 0, 100], [0, 1, 50]])
			res4 = cv2.warpAffine(img, M, (cols, rows)) # 用仿射变换实现平移


			cv2.imshow('shen', res4) #显示图片
			cv2.waitKey(0) 

		btn_pingyi.clicked.connect(pingyitupian)	







		
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
