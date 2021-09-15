# immutable(변할 수 없는) : 정수, 실수, 문자열, 튜플
# mutable(변할 수 있는) : 리스트, 딕셔너리, 집합

# ' " \ ==============================================================
a = '''가나다라
ㅇ아라주
어하마ㅓ어'''
print(a)

b = "가나다라\'마바사아"
print(b)

c = "가나\n다라"
print(c)

# 변수, 자료형의 값을 저장하는 공간

a = [1, 2, 3]
b = a
a[0] = 4
print(a)
print(b)
print(id(a))
print(id(b))

a = [1, 2, 3]
b = a[:]
a[0] = 4
print(a)
print(b)
print(id(a))
print(id(b))


a, b = ['python', 'java']
a, b = ('python', 'java')

print(a)
print(b)

a = 3
b = 5
a, b = b, a

print(a)
print(b)


# 슬라이스
d = "Life is too short."
print(d[2])
print(d[:4])
print(d[:4:2])                #[이상:미만:간격]
print(d[::-1])
print(d[:-1])

# % 와 소수점
a = "Dafsf"
print("%s 가나라"%(a))     #  %s 는 모든 문자가능
print("%-10s 가나라"%(a))   # 공백과 정렬

num = "%0.4f" %284.28946
print(num)
num1 = "{0:.4f}".format(274.349257)
print(num1)

# index, find, replace, split

aa = "Alphabeta"
print(aa.index("a",5,9))
print(aa.find("a"))

print(aa.replace("A", "B"))

abc = "Life is short"
print(abc.split("i"))           # split 특정 문자 기준으로 짤라서 리스트로 만듬


# 리스트 (서랍장) ==============================================================

usa_stock = ["starbucks", "Nvidia", "intel", "Apple", ["etf", "dollar", "spxl"]]
print(usa_stock[2])
print(usa_stock[-1])

usa_stock[0] = "Alphabet"
print(usa_stock[0])

# del usa_stock[0]
# print(usa_stock[0])

usa_stock[0:] = ""
print(usa_stock)

# 리스트 더하기
korean_stock = ["samsung", "hyundai", "lg", "sk"]
print(usa_stock + korean_stock)

korean_stock.extend(usa_stock)
print(korean_stock)

# append(맨 뒤에 요소 추가), sort(정렬), reverse(), index, insert, remove, pop(마지막 요소 삭제), count(요소 카운팅), extend
num12 = [2,431,5,4,2,57,8]
num12.reverse()
print(num12)



# 튜플 (고정, 잠긴 서랍장) ==============================================================

t1 = (1, 2, 'a', 'b')
# del t1[0]       # 'tuple' object doesn't support item deletion
print(t1[0] + 1)      # 꺼내 볼 순 있지만, 튜플 안의 값을 지우거나 수정해서 고정시킬 순 없음


# 딕셔너리 ===============================================================
# key 와 value

dic = {'name' : 'Eric', 2 : "ui"}          # value 는 같아도 되지만 key 가 같으면 안됨
print(dic['name'])
print(dic.get(3, "없음"))
print(2 in dic)

dic['name1'] = 'susan'    # key 와 value 추가
print(dic)

del dic['name']              # key 와 value 삭제
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

dic.clear()
print(dic)

# 집합(set) 중복 안됨, 순서 없음===============================================================

s1 = {1, 2, 3, 1}      # s1 = set([1, 2, 3, 1]) 로도 가능
print(set(s1))           # 중복 불가

s2 = {"Hello", 2, 3}
print(set(s2))

print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

s1.add(7)
print(s1)
s1.remove(1)
print(s1)

# 자료구조의 변경 ================================================

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(type(menu))

menu = tuple(menu)
print(type(menu))

menu = set(menu)
print(type(menu))

# boolean (True, False) ==========================================
a = True
if a:
    print(a)

a = "안녕"
if a:
    print(a)

a = ""
if a:
    print(a)

a = [1, 2, 3, 4]                     # "py"  /  [1,2,3]  /  1  → 참,  ""  /  []  /  {}  /  0  → 거짓
while a:
    a.pop()
    print(a)

# 랜덤함수 ================================
from random import *

print(random()) # 0.0 ~ 1.0 미만
print(random() * 10) # 0.0 ~ 10.0 미만
print(random() * 10 + 1) # 1 ~ 10 이하
print(int(random() * 45) + 1) # 1 ~ 45 이하
print(randrange(1,46)) # 1 ~ 46 미만
print(randint(1,45)) # 1 ~ 45 이하

print(list(range(1,21))) # 1 ~ 20까지의 숫자
print(round(3.39301, 2)) # 소수점 2번째 자리까지 표현

from random import *

users = list(range(1, 21))
shuffle(users)
chicken_winner = sample(users, 1)


# 표준 입출력 ================================================================

print("Python", "Java")
print("Python" + "Java")
print("Python", "Java", sep = ",")
print("Python", "Java", "Javascript", sep = " vs ")           # sep

print("Python", "Java", sep = ",", end = "?")                 # 문장 끝에 줄바꿈 대신 물음표가 입력됨

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)


scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":")    # 좌, 우 정렬


for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))                    # zfill


answer = input("아무 값이나 입력하세요 : ")                      # input 은 항상 str로 입력받음
print(type(answer))
print("입력하신 값은 {} 입니다.".format(answer))


# 빈 자리는 빈공간, 오른쪽 정렬하되, 10자리 공간 확보
print("{0: >10}".format(500))
# 양수, 음수 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬, 빈칸 _
print("{0:_<10}".format(500))
# 3자리 마다 ,찍어주기
print("{0:,}".format(10000000000000))
# 3자리 마다 ,찍어주기, +- 부호도 붙이기
print("{0:+,}".format(10000000000000))
print("{0:+,}".format(-10000000000000))
# 3자리 마다 ,찍고, 부호 붙이고, 자릿수 확보, 빈 자리 ^
print("{0:^<+30,}".format(1520500000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수까지만 표시 (3째자리 반올림)
print("{0:.2f}".format(5/3))

# map
x = input().split()    # input().split()의 결과는 문자열 리스트
m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = m               # 맵 객체는 변수 여러 개에 저장할 수 있음

print(-1 % 24) # 23

# reverse 와 reversed / reverse 는 해당 리스트를 변환 reversed 는 해당 리스트는 유지, 변수로 변환된 것을 받아야함


############################ for o in str(a):  # str에서 for #######################
for o in str(a): 
    pass

# zip *zip

kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng)))
mix = list(zip(kor, eng))
print(list(zip(*mix)))
kor2, eng2 = zip(*mix)
print(kor2)
print(eng2)


# list 캐스팅과 for문으로 문자열 자르기