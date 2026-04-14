"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 1: 성적 등급

점수를 입력받아 등급을 출력하세요.
if/elif/else를 사용합니다.

[등급 기준]
90 이상: A
80 이상: B
70 이상: C
60 이상: D
60 미만: F
"""

score = int(input("점수를 입력하세요: "))

# 아래에 등급을 판정하여 출력하세요
# 만약 점수가 90점 이상이면 "점수: {score}"와 "등급: A"를 출력한다.
if score >= 90:
    print(f"점수: {score}")
    print("등급: A")

# 그게 아니고 80점 이상이면 "점수: {score}"와 "등급: B"를 출력한다.
elif score >= 80:
    print(f"점수: {score}")
    print("등급: B")

# 그게 아니고 70점 이상이면 "점수: {score}"와 "등급: C"를 출력한다.
elif score >= 70:
    print(f"점수: {score}")
    print("등급: C")

# 그게 아니고 60점 이상이면 "점수: {score}"와 "등급: D"를 출력한다.
elif score >= 60:
    print(f"점수: {score}")
    print("등급: D")

# 이외의 나머지는 "점수: {score}"와 "등급: F"를 출력한다.
else :
    print(f"점수: {score}")
    print("등급: F")
