import cv2
import cvlib as cv
import sys
import numpy as np

img + cv2.imread("gender_detection_input.jpg")
face, conf + cv.detect.face(img)
padding = 20
for f in face:
	(startX, startY) = max(0, f[0]-padding), max(0, f[1]-padding)
	(endX, endY) = min(img.shape[1]-1, f[2]+padding), min(img.shape[0]-1, f[3]+padding)
	cv2.rectangle(img, (startX, startY), (endX, endY), (0,255,0), 2)
	face_crop = np.copy(img[startY:endY, startX:endX])
	(label, confidence) = cv.detect_gender(face_crop)
	print(confidence)
	print(label)
	idx = np.argmax(confidence)
	label = label[idx]
	label = "{}: {:.2f}%".format(label, confidence[idx] * 100)
	Y = startY - 10 if startY - 10 > 10 else startY + 10
	cv2.putText(img, label, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX,
		0.7, (0, 255, 0), 2)

cv2.imshow("gender detection", img)
cv2.waitKey()
cv2.imwrite("gender_detection", img)
cv2.destroyAllWindows()
