"""
실습 6: 시간 변환

초(seconds)를 입력받아 시, 분, 초로 변환하여 출력하세요.

힌트: //(몫)과 %(나머지)를 사용합니다.
      1시간 = 3600초, 1분 = 60초
"""

seconds = int(input("초를 입력하세요: "))

# 아래에 시, 분, 초로 변환하여 출력하세요

# 먼저 초를 3600로 나누어 시간(몫)을 구한 후 나머지를 구한다.

hour = seconds//3600
seconds = seconds % 3600

# 나머지에 60를 나누어 분(몫)을 구한 후 나머지를 구한다.
minute = seconds//60
seconds = seconds % 60

# 그 후 "= 몇시간 몇분 몇초" 행태로 출력한다.
print(f"{hour}시간 {minute}분 {seconds}초")
