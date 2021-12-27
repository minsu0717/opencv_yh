import cv2
import numpy as np

# cv2.IMREAD_COLOR 랑 1 은 같은 의미 입니다.
source = cv2.imread('data/images/sample.jpg',1)

print(cv2.IMREAD_COLOR)

# 가로는 80%
# 세로는 60%
# 이미지 확대 / 축소

scaleX = 0.8
scaleY = 0.6

scaleDown = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)

print(scaleDown)

cv2.imshow('Original',source)
cv2.imshow('Scaled Down',scaleDown)

# CROP 이미지 자르기

crop_img = source[10:200,150:250]

cv2.imshow('crop image',crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

