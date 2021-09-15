import time
from PIL import ImageGrab # pip install Pillow

time.sleep(5) # 5초간 대기 : 사용자 준비 시간
for i in range(1, 11): # 2초 간격 이미지 10개 저장
    image = ImageGrab.grab() # 현재 스크린 이미지 가져옴
    image.save(f"image{i}.png") # 파일로 저장
    time.sleep(2) # 2초 단위