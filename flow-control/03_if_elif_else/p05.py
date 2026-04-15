"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 5: BMI 판정

키(cm)와 몸무게(kg)를 입력받아 BMI를 계산하고 판정 결과를 출력하세요.
if/elif/else를 사용합니다.

BMI = 몸무게(kg) / (키(m))^2
(키는 cm로 입력받으므로 m로 변환 필요: cm / 100)

[판정 기준]
BMI 18.5 미만: 저체중
BMI 18.5 이상 23 미만: 정상
BMI 23 이상 25 미만: 과체중
BMI 25 이상: 비만
"""

height = float(input("키를 입력하세요 (cm): "))
weight = float(input("몸무게를 입력하세요 (kg): "))

# 아래에 BMI를 계산하고 판정 결과를 출력하세요

# height_m = height / 100
height_m = height / 100

# BMI = weight / (height_m ** 2)       나누기하는 순간 결과값의 자료형은 실수형
BMI = weight / (height_m ** 2)

# 만약 BMI 18.5미만이면 저제중
if BMI < 18.5:
    result = "저체중"

# 그게 아니라면 BMI 18.5이상 23미만이면 정상
elif 18.5 <= BMI < 23:
    result = "정상"

# 그게 아니라면 BMI 23이상 25미만이면 과체중
elif 23 <= BMI < 25:
    result = "과체중"

# 이외의 나머지는 비만
else:
    result = "비만"

# f"키: {height}cm, 몸무게: {weight}"을 출력한다.
print(f"키: {height}cm, 몸무게: {weight}")

# f"BMI: {BMI}"을 출력한다.       소수점 2개만 보여주고 싶을 때 쓰는 함수 print(f"{BMI:.2f}")
print(f"BMI: {BMI:.2f}")

# f"판정: {result}"을 출력한다.
print(f"판정: {result}")
