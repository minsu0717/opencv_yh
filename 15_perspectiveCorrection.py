import cv2
import numpy as np

from utils import get_four_points

image = cv2.imread('data/images/test.jpg')

# cv2.imshow('original',image)

point_src = get_four_points(image)

print(point_src)



# 이제, 아까했던 14번 파일처럼!
# 이미지는 2개가 다 준비됬다.
# 14번 파일을 참고하여, 실습 1번 문제를 해결하세요.

# 힌트, image 의 4개의 점은, 마우스클릭으로 해결완료!
# 1. image_dst 의 4개의 점은 여러분들이 구해서
point_dst = np.array([0, 0, 400, 0, 400, 400, 0, 400])
point_dst = point_dst.reshape(4,2)

# 2. 행렬 구하고
matrix, status = cv2.findHomography(point_src,point_dst)

# 3. 변환함수를 통해, 이미지를 가져오세요. 
#    새로운 이미지의 사이즈는 x=300, y=400 으로 되도록
#    파라미터 셋팅해서 이미지 가져오세요.
image_dst = cv2.warpPerspective(image,matrix,(400,400))

cv2.imshow('dst',image_dst)


cv2.waitKey(0)
cv2.destroyAllWindows()