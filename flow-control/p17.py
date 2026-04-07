"""
실습 17: 점수 처리 프로그램

국어, 영어, 수학 점수를 입력받아 아래 작업을 수행하세요.

[지시사항]
1. 각 점수를 변수에 저장
2. 다중 대입으로 과목명을 한 줄에 저장
3. total = 0으로 초기화
4. +=를 사용하여 총점 계산
5. 평균 계산 후 출력
"""

# 아래에 코드를 작성하세요

# total를 0으로 초기화한다.
total = 0

# korean english math에 각각 점수를 저장한다.
korean = int(input("국어 점수 입력: "))
english = int(input("영어 점수 입력: "))
math = int(input("수학 점수 입력: "))

# 다중 대입을 사용하여 과목명을 저장한다.
sud1, sud2, sud3 = "국어", "영어", "수학"

# 입력 받은 점수를 total에 더한다.
total += korean
total += english
total += math

# 평균 계산 후 출력한다.
print(f"과목: {sud1, sud2, sud3}")
print(f"국어: {korean}")
print(f"영어: {english}")
print(f"수학: {math}")
print(f"총점: {total}")
print(f"평균: {total/3}")
