import requests
url = 'http://nadocoding.tistory.com'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"}
a = requests.get(url, headers=headers) # user agent 확인 - What is my user agent? 사이트에서 확인
a.raise_for_status()                   # 올바른 정보를 가져올 수 없을 때, user agent 사용

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(a.text)