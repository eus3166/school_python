"""
실습 12: 숫자 피라미드

줄 수를 입력받아 아래와 같은 숫자 피라미드를 출력하세요.

힌트: 중첩 for문과 print(값, end="")를 사용합니다.
      print()는 줄바꿈만 합니다.
"""

n = int(input("줄 수를 입력하세요: "))

# 아래에 숫자 피라미드를 출력하세요

# 출력할 때마다 n+1씩 증가하며 출력한다.

for i in range(1, n+1):
    for j in range(1, i+1):
      print(j,end="")

    print()
