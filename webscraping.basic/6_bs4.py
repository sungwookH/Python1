import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # lxml을 통해서 가져옴
print(soup.title)
print(soup.title.get_text()) # title안에 있는 글자만 가져옴
print(soup.a) # soup에서 맨 처음 a를 가져옴
print(soup.a.attrs) # a element 의 모든 속성 정보를 dict 형태로 가져옴
print(soup.a["href"]) # a element 의 href 속성 정보를 출력

print(soup.find("a", attrs={"class":"Nbtn_upload"})) # a에 해당 하는 첫 element 에서 class="Nbtn_upload" 을 가져옴
print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 을 가져옴

rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
print(rank1.a.get_text())
print(rank1.next_sibling) # rank1 의 다음 element로 넘어감 but 개행정보가 담겨져 있어 안나옴
print(rank1.next_sibling.next_sibling) # rank1 개행정보 rank2 순으로 구성되어 나옴
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling # rank3 의 이전 element
print(rank1.parent) # rank1 의 부모 ol 태그가 출력됨

rank1.find_next_sibling("li") # rank1의 다음 태그 중 li태그 1개 찾기
rank1.find_next_siblings("li") # rank1의 다음 태그 중 모든 li태그 찾기

webtoon = soup.find("a", text="연애혁명") # text가 연애혁명인 a태그를 가져옴
print(webtoon)