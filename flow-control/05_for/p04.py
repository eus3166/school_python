"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 4: 1부터 N까지의 합 구하기

숫자 N을 입력받아 1부터 N까지의 합을 구하여 출력하세요.
for + range()를 사용합니다.
"""

n = int(input("숫자를 입력하세요: "))

# 누적 변수 선언
total = 0

# n + 1만큼 반복하기
for num in range(n + 1):
    # num 누적하기
    total += num

# 결과 출력하기
print(f"1부터 {n}까지의 합: {total}")