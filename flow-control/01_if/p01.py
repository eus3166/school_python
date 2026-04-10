"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 1: 단일 if문 이해도 확인

각 코드에서 조건식은 참인가, 거짓인가?
각 코드의 출력 결과는 무엇인가?

코드를 실행하지 말고, 먼저 직접 예측한 뒤 실행하여 확인하세요.
"""

# [1]
age = 16

if age >= 18:
    print("성인입니다.")

print("종료")

# 조건식: age >= 18 → 16 >= 18 → False
# 출력 결과:
# 종료


# [2]
score = 90

if score >= 60:
    print("합격")

print("수고하셨습니다")

# 조건식: score >= 60 → 90 >= 60 → True
# 출력 결과: 
# 합격 
# 수고하셨습니다


# [3]
money = 3000

if money >= 5000:
    print("택시를 탄다")
    print("빠르게 이동")

print("도착")

# 조건식: money >= 5000 → 3000 >= 5000 → False
# 출력 결과: 
# 도착


# [4]
temperature = 38

if temperature >= 37:
    print("발열 의심")

# 조건식: temperature >= 37 → 38 >= 37 → True
# 출력 결과: 
# 발열 의심


# [5]
x = 10

if x == 10:
    print("정답")
    print("잘했습니다")

print("끝")

# 조건식: x == 10 → 10 == 10 → True
# 출력 결과: 
# 정답 
# 잘했습니다 
# 끝


# [6]
name = "홍길동"

if name == "김철수":
    print("반갑습니다")
    print("환영합니다")

print("프로그램 종료")

# 조건식: name == "김철수" → "홍길동" == "김철수" → False
# 출력 결과: 
# 프로그램 종료


# [7]
is_raining = True

if is_raining:
    print("우산을 챙긴다")

print("외출")

# 조건식: is_raining == True → True == True → True
# 출력 결과: 
# 우산을 챙긴다 
# 외출


# [8]
count = 0

if count:
    print("값이 있습니다")

print("확인 완료")

# 조건식: count == True → 0 == True → False == True → False
# 출력 결과: 
# 확인 완료
