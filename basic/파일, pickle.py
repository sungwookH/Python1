# 파일 입출력

# 쓰기
score_file = open("score.txt", "w", encoding="utf8")          # w (기존 내용이 있으면 덮어쓰기)
print("수학 : 0", file = score_file)
score_file.write("과학 : 80")
score_file.close()

# 추가로 쓰기
score_file = open("score.txt", "a", encoding="utf8")            # a (추가로 쓰기)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")                                # write 는 줄바꿈이 안됨
score_file.close()

# 읽기
score_file = open("score.txt", "r", encoding = "utf8")         
print(score_file.read())
score_file.close()

# readline = 한 줄씩 읽기
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline(), end="")                              # 줄별로 읽고, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
score_file.close()

# readline, for == 한 줄씩 끝까지 읽기
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: break
    print(line, end="")
score_file.close()

# readlines == list로 저장해서 읽기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()                                       # 모든 라인을 list 형태로 저장
for line in lines:
    print(line, end="")   # === print(line.strip("\n"))
score_file.close()


# pickle # 리스트나 클래스같은 텍스트가 아닌 자료형은 일반적인 파일 입출력 방법으로는 데이터를 저장하거나 불러올 수 없다.
         # 파이썬에서는 이와 같은 텍스트 이외의 자료형을 파일로 저장하기 위하여 pickle이라는 모듈을 제공한다.

import pickle

# pickle 에 쓰기
profile_file = open("profile.pickle", "wb")      # pickle 은 encoding 값 필요없고 w 대신 wb로 읽는다
profile = {"이름" : "유재석", "나이" : 20, "취미" : ["축구", "배드민턴", "농구", "야구"]}
# print(profile)
pickle.dump(profile, profile_file)               # profile 의 정보를 profile_file 에 저장
profile_file.close()

# pickle 불러오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)              # file에 있는 정보를 profile 에 불러오기
print(profile)
# print(pickle.load(profile_file))
profile_file.close()



# with (close 가 필요없음)

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


# 퀴즈 8

def Work (week):
    with open("{}주차.txt".format(week), "w", encoding="utf8") as Report_file:
        print("- {} 주차 주간보고 -".format(week), file = Report_file)
        print("부서 : ", file = Report_file)
        print("이름 : ", file = Report_file)
        print("업무 요약 : ", file = Report_file)

Work (1)
Work (2)

for week in range(1, 51):
    with open("{}주차.txt".format(week), "w", encoding="utf8") as Report_file:
        print("- {} 주차 주간보고 -".format(week), file = Report_file)
        print("부서 : ", file = Report_file)
        print("이름 : ", file = Report_file)
        print("업무 요약 : ", file = Report_file)



















