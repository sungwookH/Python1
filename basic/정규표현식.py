# 정규 표현식 (긴 글에서 원하는 패턴을 가진 것을 찾고 싶을때 / 특정한 패턴에 부합하는지 유효성 검사)
import re

p = re.compile('[a-z]+')   
m = p.match('python')    # match
print(m)                 # <re.Match object; span=(0, 6), match='python'>
print(m.group())  # python   /  매치된 문자열 리턴
print(m.start())  # 0
print(m.end())    # 6
print(m.span())   # (0, 6)

m1 = p.match('3 python')
print(m1)                # None


p = re.compile('[a-z]+')
m2 = p.search('3 python') # search
print(m2)                 # <re.Match object; span=(2, 8), match='python'>


p = re.compile('[a-z]+')
m3 = p.findall('life is too short') # findall
print(m3)                           # ['life', 'is', 'too', 'short']

p = re.compile('[a-z]+')
m3 = p.finditer('life is too short') # finditer
print(m3)                            # <callable_iterator object at 0x000001C874BCFAC0>
p = re.compile('[a-z]+')
m3 = p.finditer('life is too short')
for i in m3:
    print(i)                         # <re.Match object; span=(0, 4), match='life'> <re.Match object; span=(5, 7), match='is'>
                                     # <re.Match object; span=(8, 11), match='too'> <re.Match object; span=(12, 17), match='short' 


# ======================================= # 컴파일 옵션

 # DOTALL, S     / 줄바꿈 문자도 포함하도록
p = re.compile('a.b')
m = p.match('a\nb')
print(m)            # NONE

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)            # <re.Match object; span=(0, 3), match='a\nb'>

 # IGNORECASE, I    / 대소문자 무시
p = re.compile('[a-z]')
print(p.match('python')) # <re.Match object; span=(0, 1), match='p'>
print(p.match('Python')) # NONE
print(p.match('PYTHON')) # NONE

p = re.compile('[a-z]', re.I)
print(p.match('python')) # <re.Match object; span=(0, 1), match='p'>
print(p.match('Python')) # <re.Match object; span=(0, 1), match='p'>
print(p.match('PYTHON')) # <re.Match object; span=(0, 1), match='p'>

 # MULTILINE, M   / ^ 를 맨 처음만이 아닌 각 라인의 처음으로 인식시킴
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))  # ['python one']

p = re.compile("^python\s\w+", re.M)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))  # ['python one', 'python two', 'python three']

# VERBOSE, X   /  정규식은 줄바꿈으로 나누면 compile이 안됨 VERBOS는 되게 만들어줌
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
 &[#]
 |(
     0[0-7]+
    | [0-9]+
    | x[0-9a-fA-F]+
 )
 ;
 """, re.VERBOSE)


# 백슬래시 문제

#  \section        \s 는 공백을 표현
p = re.compile('\\section')  # \\ 는 \ 로 치환, \s 는 공백으로 치환
p = re.compile('\\\\section')
p = re.compile(r'\\section')


# 메타문자
# |  ^  $  \b

 # 메타문자 |      /   or의 의미
p = re.compile('Crow|havana')
m = p.match('CrowHello')       # <re.Match object; span=(0, 4), match='Crow'> 
m1 = p.match('havanahei')      # <re.Match object; span=(0, 6), match='havana'>
print(m, m1)


 # 메타문자 ^        /   ^ 는 맨 처음을 의미함   / 추가로 compile 없이 한 줄에도 표현가능
print(re.search('^Life', 'Life is too short')) # <re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life')) # None

 # 메타문자  $       /   ^ 는 맨 끝을 의미함
print(re.search('short$', 'Life is too short')) # <re.Match object; span=(12, 17), match='short'>
print(re.search('short$', 'Life is too short, you need python')) # None

 # 메타문자 \b       / 공백을 의미
p = re.compile(r'\bclass\b')
print(p.search('no class at all')) # <re.Match object; span=(3, 8), match='class'>
print(p.search('the declassified algorithm')) # None
print(p.search('one subclass is')) # None

 # 그루핑 ()
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)                           # <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group())                   # ABCABCABC

p = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')
m = p.search("park 010-1234-1234")
print(m.group())   # park 010-1234-1234
print(m.group(1))  # park

p = re.compile(r'(\b\w+)\s+\1')    # \1  그루핑 되어 있을 때, 앞에 걸린게 한 번더 반복
print(p.search('Paris in the the spring').group())  # the the

 # 그루핑된 문자열에 이름 붙이기 ?P<name>
p = re.compile(r'(?P<name>\w+)\s+\d+[-]\d+[-]\d+')
m = p.search("park 010-1234-1234")
print(m.group("name"))

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')   
print(p.search('Paris in the the spring').group())

 # 전방탐색: 긍정형 (?=) / 검색조건엔 포함시키고 싶으나 결과엔 포함시키지 않음
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

 # 전방탐색: 부정형 (?!)
p = re.compile(".*[.](?!bat$).*$", re.M)
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)

 # 문자열 바꾸기 sub
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))

 # Greedy vs Non-Greedy
s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group())
print(re.match('<.*?>', s).group())