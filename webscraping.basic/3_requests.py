import requests
a = requests.get("http://google.com")
a.raise_for_status()  # 올바로 가져올 수 있는지
# print("응답코드:", a.status_code)     # res.status_code 가 200이면 정상

b = requests.get("http://youtu.com")
# b.raise_for_status()
# print("응답코드:", b.status_code)

print(len(a.text)) # a 에서 가져오는 텍스트 길이
print(a.text) # a 에서 가져온 텍스트

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(a.text)