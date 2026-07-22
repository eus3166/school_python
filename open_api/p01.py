"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 1: REST API로 "2026년 한국 공휴일" 받아와 출력하기

예제(ex11_open_api_weather)에서는 날씨 서버에서 JSON을 받아 파이썬 dict로 다루었습니다.
이번에는 다른 API에서 공휴일 JSON을 받아와 화면에 출력해 봅니다.

[받아올 데이터]
  공휴일 정보 서버(Nager.Date)에서 2026년 대한민국 공휴일 목록을 받아옵니다.
  주소: https://date.nager.at/api/v3/PublicHolidays/2026/KR
  - API 키 불필요, 무료

[받아온 JSON의 모양]
  이번 데이터는 "list 안에 dict가 여러 개" 들어 있는 형태입니다.
  [
    {"date": "2026-01-01", "localName": "새해",   "name": "New Year's Day", ...},
    {"date": "2026-02-16", "localName": "설날",   "name": "Lunar New Year", ...},
    ...
  ]
  → 각 dict에서 "date"(날짜)와 "localName"(한국어 이름)을 꺼내면 됩니다.

[해야 할 일]
  1. requests로 위 주소에 요청하고 response.json()으로 JSON을 받는다.
  2. 반복문으로 공휴일을 하나씩 꺼낸다.
  3. 각 공휴일의 날짜와 한국어 이름에 번호를 붙여 출력한다.

힌트:
  - 받아온 데이터는 list이므로 for 반복문으로 하나씩 꺼낼 수 있다.
  - 공휴일 하나는 dict이므로 holiday["date"], holiday["localName"]으로 값을 꺼낸다.
  - 번호를 붙일 때는 enumerate(holidays, 1)을 활용한다.
"""

import requests

URL = "https://date.nager.at/api/v3/PublicHolidays/2026/KR"

# 아래에 코드를 작성하세요.
# URL에 요청해 JSON(list) 받기
try:
  response = requests.get(URL, timeout=10)
  holidays = response.json()

# 인터넷이 막혀 서버에 접속하지 못하면 프로그램 끝내기
except requests.RequestException:
  print(" 인터넷 연결을 확인하세요. 날씨 서버에 접속하지 못했습니다.")
  raise SystemExit

# 문구 출력
print("=== 2026년 대한민국 공휴일 ===")

# 공휴일을 하나씩 꺼내 날짜와 한국어 이름 출력하기
for number, holiday in enumerate(holidays, 1):
  # 공휴일 한국어 이름 꺼내기
  name = holiday["localName"]
  # 공휴일 날짜 꺼내기
  day = holiday["date"]
  # 결과 출력
  print(f"{number}. {day} {name}")

# 총 공휴일 수 출력
print(f"총 공휴일 수: {len(holidays)}")