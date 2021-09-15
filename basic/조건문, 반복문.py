# if ============================================
 
weather = input("오늘 날씨는 어때요? ")                             # input

if weather == "비" or weather == "눈" :          # or = |     and = &
    print("우산을 챙기세요")
elif weather == "미세먼지" or weather == "corona" :
    print("마스크를 챙기세요")
else :
    print("준비물 필요 없어요.")

# 조건부 표현식(한 줄, 더 간단하게) ============================================
score = 70
if score >= 60:
    msg = "success"
else :                                            #  →→→→→ msg = "success" if score >= 60 else "failure"
    msg = "failure"
print(msg)

for i in range(2, 10):
    for j in range(1, 10):
        x = i * j
        print(x, end=" ")
    print("")

result = [x * y for x in range(2, 10) for y  in range(1, 10)]
print(result)


print('>') if A > B else print('<') if A < B else print('==')
print(['><'[a<b],'=='][a==b])


# for ============================================

# for waiting_no in [0, 1, 2, 3, 4, 5]:
for waiting_no in range(6):
    print("대기번호 : {0}".format(waiting_no))

starbucks = {"아이언맨", "캡틴 아메리카", "헐크"}
for customer in starbucks:
    print("{}님, 커피 준비되었습니다.".format(customer))


# while ============================================   # while True = 무한루프
customer = "토르"
count = 5
while count >= 1:
    # print("{}님, 커피 준비되었습니다. {}분 남았습니다.".format(customer, count))
    print(f"{customer}님, 커피 준비되었습니다. {count}분 남았습니다.")
    count -= 1
    if count == 0:
        print(f"{customer}님, 대기시간이 초과되어 주문하신 상품 폐기되었습니다. 카운터로 와주세요. ")


customer = "헐크"                                                  # while !=
unknown = input("이름이 어떻게 되세요?")
while unknown != customer:
    say = input("")
    if say == "hi":
            unknown = input("이름이 어떻게 되세요?")
            if unknown == customer:
                print("here you are. 감사합니다. 안녕히 가세요!")
            else:
                print("죄송합니다. 아직 준비되지 않았습니다.")
                print("{}님, 주문하신 상품 준비되었습니다.".format(customer))
                continue
    else:
        print("{}님, 주문하신 상품 준비되었습니다.".format(customer))
        continue


# countinue, break ============================================

from random import *

absent = 2, 7, 17, 21, 30
no_book = 13, 20
group = list(range(1, 33))
shuffle(group)
for student in group:
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 끝. {}는 교무실로 와요.".format(student))
        break
    print("{}친구, 다음 글 읽어봐요.".format(student))

a = 0
while a < 10:
    a = a + 10
    if a % 2 ==0:
        continue
    print(a)


# 퀴즈 5

from random import *

passenger = 0

for person in range(1,51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {}번째 손님 (소요시간 : {}분)".format(person, time), end = " ")
        passenger += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(person, time))
print(f" 총 탑승 승객 : {passenger} 분")