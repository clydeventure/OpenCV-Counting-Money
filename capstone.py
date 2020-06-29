import numpy as np
import cv2 as cv

def av_pix(img,circles,size):
    av_value = []
    for coords in circles[0,:]:
        col = np.mean(img[coords[1]-size:coords[1]+size,coords[0]-size:coords[0]+size])
        av_value.append(col)
    return av_value   


def get_radius(circles):
    radius = []
    for coords in circles[0,:]:
        radius.append(coords[2])
    return radius

img = cv.imread('capstone_coins.png',cv.IMREAD_GRAYSCALE)
original_image = cv.imread('capstone_coins.png',1)
img = cv.GaussianBlur(img, (5,5), 0)

circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,0.9,120,param1=50,param2=27,minRadius=60,maxRadius=120)

print(circles)

circles = np.uint16(np.around(circles))
count = 1
for i in circles[0,:]:
    
    # draw the outer circle
    cv.circle(original_image,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(original_image,(i[0],i[1]),2,(0,0,255),3)
    cv.putText(original_image, str(count),(i[0],i[1]), cv.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2)
    count += 1

radii = get_radius(circles)
print(radii)

bright_values = av_pix(img,circles,20)

values = []
for a,b in zip(bright_values,radii):
    if a > 150 and b > 110:
        values.append(10)
    elif a > 150 and b <= 110:
        values.append(5)
    elif a < 150 and b > 110:
        values.append(2)
    elif a < 150 and b < 110:
        values.append(1)        
           
count_2 = 0
for i in circles[0,:]:
    cv.putText(original_image, str(values[count_2]) + 'p',(i[0],i[1]), cv.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2)
    count_2 += 1
cv.putText(original_image, 'ESTIMATED TOTAL VALUE: ' + str(sum(values)) + 'p', (200,100), cv.FONT_HERSHEY_SIMPLEX, 1.3, 255)

cv.imshow('Detected Coins',original_image)
cv.waitKey(0)
cv.destroyAllWindows()