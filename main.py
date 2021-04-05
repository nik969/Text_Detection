import cv2
import pytesseract

img = cv2.imread("Res/image1.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #one liner code


print(pytesseract.image_to_string(img))
cv2.imshow("sample",img)

himg= img.shape[0]
wimg = img.shape[1]
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,himg-y), (w,himg-h), (0,200,105), 2)

cv2.imshow("out", img)
cv2.waitKey(0)
