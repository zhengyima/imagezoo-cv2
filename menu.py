import cv2
import numpy as np

print("----------请输入要执行的功能")


while True:
	function_id = input("功能ID(0-9):\n1.阈值分割\n2.平滑图像\n3.缩放\n4.裁剪\n5.灰度变换\n6.高低通滤波\n7.翻转功能")

	if int(function_id) == 1:
		# 灰度图读入
		imgPath = input("请输入待处理图片的路径")
		img = cv2.imread(imgPath, 0)

		# 阈值分割 固定阈值
		ret, th = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO_INV)
		# 自适应阈值
		th2 = cv2.adaptiveThreshold(
			img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
		cv2.imshow('thresh', th2)
		cv2.waitKey(0)

	elif int(function_id) == 2:

		imgPath = input("请输入待处理图片的路径")

		img = cv2.imread(imgPath, 0)
		gau = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯滤波
		blur = cv2.bilateralFilter(img, 5, 75, 75)  # 双边滤波

		res = np.hstack((img, gau, blur))
		cv2.imshow('res', res)
		cv2.waitKey(0)
	elif int(function_id) == 3:

		imgPath = input("请输入待处理图片的路径")

		img = cv2.imread(imgPath)

		# 1、按照指定的宽度、高度缩放图片
		x = input("请输入x:")
		y = input("请输入y:")
		res1 = cv2.resize(img, (int(x), int(y)))

		cv2.imshow('res', res1)
		cv2.waitKey(0)	

	elif int(function_id) == 4: #裁剪

		imgPath = input("请输入待处理图片的路径")

		img = cv2.imread(imgPath, 0)
		x1 = input("请输入起始x:")
		x2 = input("请输入终止x:")

		y1 = input("请输入起始y:")

		y2 = input("请输入终止y:")
		newimg = img[int(x1):int(x2), int(y1):int(y2)]
		cv2.imshow('res', newimg)
		cv2.waitKey(0)	

		# y = input("请输入y:")


	elif int(function_id) == 5:
		
		imgPath = input("请输入待处理图片的路径")

		img = cv2.imread(imgPath, 0)


		# 阈值分割 固定阈值
		ret, th = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO_INV)
		# 自适应阈值
		th2 = cv2.adaptiveThreshold(
			img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
		cv2.imshow('thresh', th2)
		cv2.waitKey(0)

	elif int(function_id) == 6:

		imgPath = input("请输入待处理图片的路径")


		img = cv2.imread(imgPath, 0)
		gau = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯滤波
		blur = cv2.bilateralFilter(img, 5, 75, 75)  # 双边滤波

		res = np.hstack((img, gau, blur))
		cv2.imshow('res', res)
		cv2.waitKey(0)

	elif int(function_id) == 7:

		imgPath = input("请输入待处理图片的路径")

		img = cv2.imread(imgPath)


		# 1、按照指定的宽度、高度缩放图片
		# res1 = cv2.resize(img, (132, 150))

		# 2、按照比例缩放，如x,y轴均放大一倍
		# res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

		# 3、翻转图片
		res3 = cv2.flip(img, 0)
		cv2.imshow('zoom', res3)
		cv2.waitKey(0)

	elif int(function_id) == 8:#按照比例缩放

		imgPath = input("请输入待处理图片的路径")

		img = cv2.imread(imgPath)
		res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
		cv2.imshow('zoom', res2)
		cv2.waitKey(0)
	

	elif int(function_id) == 9:
	# 4、平移图片

		imgPath = input("请输入待处理图片的路径")

		img = cv2.imread(imgPath)
		rows, cols = img.shape[:2]
		# 定义平移矩阵，需要是numpy的float32类型
		# x轴平移100，y轴平移50
		M = np.float32([[1, 0, 100], [0, 1, 50]])
		res4 = cv2.warpAffine(img, M, (cols, rows)) # 用仿射变换实现平移
		
		cv2.imshow('zoom', res4)
		cv2.waitKey(0)