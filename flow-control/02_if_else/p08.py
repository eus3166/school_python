"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 8: 눈코딩 - if-else 출력 예측

아래 8개의 코드를 실행하지 않고 눈으로 읽고,
각 코드의 출력 결과를 주석으로 작성하세요.

조건식이 참인지 거짓인지 먼저 판단하고,
어떤 블록이 실행되는지 추적하세요.
"""

# --- 문제 1 ---
x = 10
if x > 5:
    print("크다")
else:
    print("작다")
# 출력 결과: 10 > 5 → True → if 블록 실행 
# 크다


# --- 문제 2 ---
name = "파이썬"
if name == "자바":
    print("자바입니다")
else:
    print("자바가 아닙니다")
# 출력 결과: "파이썬" == "자바" → False → else 블록 실행 
# 자바가 아닙니다


# --- 문제 3 ---
score = 59
if score >= 60:
    print("합격")
else:
    print("불합격")
    print("다음에 다시 도전하세요")
# 출력 결과: 59 >= 60 → False → else 블록 실행 
# 불합격 
# 다음에 다시 도전하세요


# --- 문제 4 ---
age = 20
if age >= 19:
    print("성인입니다")
    print("환영합니다")
else:
    print("미성년자입니다")
print("확인 완료")
# 출력 결과: 20 >= 19 → True → if 블록 실행 
# 성인입니다 
# 환영합니다 
# 확인 완료


# --- 문제 5 ---
money = 0
if money > 0:
    print("잔액이 있습니다")
else:
    print("잔액이 없습니다")
print("조회 완료")
# 출력 결과: 0 > 0 → False → else 블록 실행 
# 잔액이 없습니다 
# 조회 완료


# --- 문제 6 ---
a = 3
b = 3
if a == b:
    print("같다")
else:
    print("다르다")
# 출력 결과: 3 == 3 → True → if 블록 실행 
# 같다


# --- 문제 7 ---
temp = 0
if temp < 0:
    print("영하")
    print("빙판 주의")
else:
    print("영상")
print("확인")
# 출력 결과: 0 < 0 → False → elss 블록 실행 
# 영상 
# 확인


# --- 문제 8 ---
count = 1
if count == 0:
    print("비어 있음")
    print("추가 필요")
else:
    print("데이터 있음")
print("처리 완료")
# 출력 결과: 1 == 0 → False → else 블록 실행 
# 데이터 있음 
# 처리 완료
