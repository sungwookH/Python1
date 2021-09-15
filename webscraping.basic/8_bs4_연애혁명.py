import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=570503"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class" : "title"})

for cartoon in cartoons:
    cartoon_title = cartoon.a.get_text()
    cartoon_site = "https://comic.naver.com"+cartoon.a["href"]
    print(cartoon_title, cartoon_site)