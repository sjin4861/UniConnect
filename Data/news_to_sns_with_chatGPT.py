import openai
import csv
import os
from dotenv import load_dotenv

load_dotenv()

# API 키 로드
api_key = os.getenv("OPENAI_API_KEY")

# API 키가 올바르게 로드되었는지 확인
if api_key is None:
    raise ValueError("API 키가 .env 파일에서 로드되지 않았습니다.")

# 이제 api_key를 사용하여 OpenAI API에 액세스할 수 있습니다.

# CSV 파일에서 제목과 내용을 읽어와 리스트로 저장
def read_csv(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append((row['제목'], row['내용']))
    return data

# GPT 모델을 사용하여 글을 재작성
def generate_text(prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",  # GPT-3.5-turbo를 사용하려면 엔진을 변경해주세요.
        prompt=prompt,
        max_tokens=1000,  # 생성할 최대 토큰 수
        temperature=0.7,  # 낮으면 보수적, 높으면 랜덤한 결과
        n = 1  # 생성할 글의 개수
    )
    return response.choices[0].text

# CSV 파일에서 데이터 읽어오기
csv_file = '/Users/jun/Desktop/my_project/UniConnect/Data/crawled_news.csv'  # 실제 파일 경로로 바꿔주세요
data = read_csv(csv_file)

# 데이터를 기반으로 글을 생성 및 재작성
#for title, content in data:
prompt = f"제목: {data[1][0]}\n내용: {data[1][1]}\n글을 초등학생에게 흥미를 유발하는 친근한 말투로 재작성해줘."
new_text = generate_text(prompt)
    
# 생성된 글을 원하는 곳에 저장 또는 활용
# 여기서는 콘솔에 출력하겠습니다.
print(new_text)
