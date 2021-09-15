# 함수 ===================================================

def open_account():
    print("새로운 계좌가 생성되었습니다.")                   # 정의
open_account()                                             # 함수 실행
print(open_account())  # 1

def sum(a, b):
    sum = a + b
    return sum
print(sum(10, 20))  # 2                      # 1 과 # 2 의 차이는 return(가죽)

def sum_mul(a, b):
    return a + b, a - b, a * b

print(sum_mul(100, 200)[0])
print(sum_mul(100, 200))                     # return 값이 여러개일 때


# return 값이 있는 함수와 없는 함수 ===================================================
list = [1, 2, 3]
print(list.append(4))
list = [1, 2, 3]
print(list.pop())

# 기본값 ===================================================

def introduce(name, age, gender = True):
    print("나의 이름은 : {}".format(name))
    print("나이 : {}".format(age))
    if gender == 20:
        print("남자")
    else:
        print("여자")

introduce("한", 21)
introduce("위", 22, False)
introduce("려", 23)
introduce(name = 20, age = "서율", gender = False) # 순서다를땐 맵핑


# 지역변수, 전역변수 ===================================================
a = 1                  # global a
def vart(a):
    a = a + 1          # 함수 내 a
vart(1)
print(a)    # → 1

a = 1
def vart(a):
    a = a + 1
    return a
a = vart(a)
print(a)    # → 2

a = 1
def vart():
    global a
    a = a + 1
vart()
print(a)    # → 2

b = [1, 2, 3]
def vart2(b):
    b = b.append(4)                    # global b 와 함수 내의 b는 같지 않지만, 리스트라는 것이 변할 수 있는 자료이기 때문에
    print(id(b))                       # 4 가 추가되어 출력, 즉, id값은 다르나 같은 형태를 공유!
vart2(b)
print(id(b))                           # immutable(변할 수 없는) : 정수, 실수, 문자열, 튜플
                                       # mutable(변할 수 있는) : 리스트, 딕셔너리, 집합
# *args 와 **kwargs ===================================================
def sum(*args):
    sum = 0
    for i in args:
        sum = i + sum
    return sum

print(sum(1,2, 10 ,13, 1439))

def dic(**kwargs):
    for ky, va in kwargs.items():
        print("key : {}".format(ky))
        print("value : {}".format(va))

dic(키 = "발", 코 = "입", 눈 = "귀")

# lambda (def 의 축약형)===================================================
def add(a, b):
    return a + b
print(add(10,5))

add2 = lambda a, b:a + b
print(add(1, 2))

list = [lambda a, b: a*b, lambda a, b: a/b]
print(list[0](12989,2))


# 퀴즈 6 ===================================================

def std_weight(height, gender):
    if gender == "남자" or "남성":
        return height * height * 22
    else:
        return height * height * 21


height = 177
gender = "남성"
weight = round(std_weight(height/100, gender), 2)
print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height, gender, weight))

# gender = input("성별이 어떻게 되세요")
# height = int(input("키가 어떻게 되세요?"))
# weight = round(std_weight(height/100, gender), 2)
# print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height, gender, weight))
