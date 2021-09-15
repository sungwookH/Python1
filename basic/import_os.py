# 특정 디렉터리부터 시작해서 그 하위 모든 파일 중 파이썬 파일만 출력해 주는 프로그램

import os

print(os.getcwd())
def search(pat):
    files = os.listdir(pat)          # os.listdir(경로) : 특정 경로에 위치한 파일들을 리스트로 확인
    for file in files:
        file_fullname = os.path.join(pat, file)     # os.path.join 파일명과 경로 합치기
        if os.path.isdir(file_fullname):
            search(pat)
        else:    
            ext = os.path.splitext(file_fullname)          # os.path.splitext : 확장자 분리
            if ext[-1] == ".py":
                print(file_fullname)

search("C:/Users/sunguk/Desktop/python workspace")
