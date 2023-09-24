import requests
from bs4 import BeautifulSoup

# 부산대 기하학 기초 연구실 세미나 탭 url
url = "https://sites.google.com/view/geometrybrl/seminars?authuser=0"

# HTTP GET 요청 보내고 응답 받기
response = requests.get(url)
# 응답 내용을 BeautifulSoup을 이용해 파싱
soup = BeautifulSoup(response.content, 'html.parser')

target_texts = ["Pusan", "PNU", "pusan", "pnu"]


#부산대 구성원의 세미나
PNU_tags = soup.find_all('span', string=lambda text: text and any(target in text for target in target_texts))

#Title로 시작하는 태그들
title_tags = soup.find_all('span', string=lambda text: text and text.startswith("Title:"))

#Abstract로 시작하는 태그들
abstract_tags = soup.find_all('span', string=lambda text: text and text.startswith("Abstract:"))


PNU = [pnu.text for pnu in PNU_tags]
titles = [tag.text.split("Title:", 1)[1] for tag in title_tags]
abstracts = [abs.text.split("Abstract:", 1)[1] for abs in abstract_tags]

print(PNU)

for title in titles:
    print(title)

for abstract in abstracts:
    print(abstract)
