import requests
from bs4 import BeautifulSoup
import csv

# 크롤링할 웹 페이지 URL 설정

url = 'https://cse.pusan.ac.kr/cse/14636/subview.do'  # 크롤링할 웹 사이트의 URL로 변경해주세요.

# HTTP GET 요청 보내고 응답 받기
response = requests.get(url)

# 응답 내용을 BeautifulSoup을 이용해 파싱
soup = BeautifulSoup(response.content, 'html.parser')

# 웹 페이지에서 제목과 링크 정보 추출
titles = soup.find_all('strong')  # 예제로 h2 태그를 제목으로 가정
articles = soup.find_all('div', class_='artclContent')

filtered_titles = []
filtered_articles = []


for title in titles:
    title = title.text.strip()
    title_length = len(title)
    # 길이가 10자 이상 80자 미만인 제목만 추출
    if 10 <= title_length < 80:
        filtered_titles.append(title)

for article in articles:
    filtered_articles.append(article.text.strip())



# 크롤링한 데이터를 리스트로 저장
data = [
    {"제목" : filtered_titles[i], "내용" : filtered_articles[i]} for i in range(len(articles))
]

# CSV 파일로 데이터 저장
csv_file = "Data/crawled_news.csv"

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["제목", "내용"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # 헤더 쓰기
    writer.writeheader()

    # 데이터 쓰기
    for row in data:
        writer.writerow(row)

print(f"데이터가 {csv_file}에 저장되었습니다.")



