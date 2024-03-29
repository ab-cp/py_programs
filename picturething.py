import cv2
key = cv2. waitkey(1)
webcam = cv2.VideoCapture(0)
while True:
	try:
		check, frame + webcam.read()
		print(check)
		print(frame)
		cv2.imshow("Capturing", frame)
		key = cv2.waitKey(1)
		if key == ord('s'):
			cv2.imwrite(filename='saved_img.jpg', img=frame)
			webcam.release()
			img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
			img_new = cv2.imshow("Captured Image", img_new)
			cv2.waitKey(1650)
			cv2.destroyAllWindows()
			print("Processing image...")
			img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
			print("Converting RBG image to grayscale...")
			gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
			print("Converted RBG image to grayscale...")
			print("Resizing image to 28x28 scale...")
			img_ = cv2.resize(gray,(28,28))
			print("Resized...")
			img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
			print("IMAGE SAVED!")
			break
		elif key == ord('q'):
			print("Turning off camera...")
			webcam.release()
			print("CAMERA IS OFF!")
			print("PROGRAM HAS BEEN ENDED!")
			cv2.destroyAllWindows()
			break

	except(KeyboardInterrupt):
		print("Turning off camera...")
		webcam.release()
		print("CAMERA IS OFF!") 
		print("PROGRAM HAS BEEN ENDED!")
		cv2.destroyAllWindows()
		break
