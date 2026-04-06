"""
실습 5: BMI 계산기

키(cm)와 몸무게(kg)를 입력받아 BMI를 계산하세요.

BMI 공식: 몸무게(kg) / 키(m)의 제곱
주의: 키는 cm로 입력받지만, 공식에서는 m 단위를 사용합니다.

힌트: cm → m 변환은 / 100, 제곱은 ** 2를 사용합니다.
"""

height = int(input("키(cm)를 입력하세요: "))
weight = int(input("몸무게(kg)를 입력하세요: "))

# 아래에 BMI를 계산하여 출력한다.

# 키(m) = (키(cm)/100)을 계산한다.
height_m = height/100

# 그 후 (몸무게/ 키의 제곱)을 계산하여 출력한다.
print("BMI: ", weight/height_m**2)
