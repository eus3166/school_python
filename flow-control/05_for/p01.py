"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 1: 구구단 출력

단 수를 입력받아 해당 구구단을 출력하세요.
for + range()를 사용합니다.
"""

dan = int(input("몇 단을 출력할까요? "))

# 아래에 구구단을 출력하세요

# 1에서 9까지 반복
for i in range(1, 10):
    result = dan * i
    print(f"{dan} x {i} = {result}")
