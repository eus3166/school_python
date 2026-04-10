"""
실습 18: 조건식 작성 연습

아래 변수들을 사용하여 각 주석에 해당하는 조건식을 작성하고,
결과(True/False)를 출력하세요.

작성 예시:
  # 점수가 80 이상인 식
  print(score >= 80)
"""

# ========================================
# [1단계] 성적 관련
# ========================================
score = 85
attendance = 92

# 점수가 80 이상인 식
print(score >= 80)

# 점수가 90 초과인 식
print(score > 90)

# 출석률이 95 이하인 식
print(attendance <= 95)

# 출석률이 80 미만인 식
print(attendance < 80)

# 점수가 100인 식
print(score == 100)

# 점수가 80 이상이고 출석률이 90 이상인 식
print(score >= 80 and attendance >= 90)

# 점수가 90 이상이거나 출석률이 95 이상인 식
print(score >= 90 or attendance >= 95)

# 점수가 70 이상이고 출석률이 80 이상인 식
print(score >= 70 and attendance >= 80)

# ========================================
# [2단계] 입장 관련
# ========================================
age = 17
guardian = True
height = 168
weight = 60

# 나이가 20 이상인 식
print(age > 20)

# 나이가 19 미만인 식
print(age < 19)

# 키가 170 이상인 식
print(height >= 170)

# 몸무게가 65 이하인 식
print(weight <= 65)

# 나이가 17인 식
print(age == 17)

# 키가 168인 식
print(height == 168)

# 보호자가 있는 식
print(guardian)

# 보호자가 없는 식
print(not guardian)

# 나이가 20 이상이거나 보호자가 있는 식
print(age >= 20 or guardian)

# 키가 170 이상이고 몸무게가 65 이하인 식
print(height >= 170 and weight <= 65)

# 보호자가 있고 나이가 19 미만인 식
print(guardian and age < 19)

# 키가 165 이상이거나 몸무게가 55 이하인 식
print(height >= 165 or weight <= 55)

# ========================================
# [3단계] 회원 관련
# ========================================
is_vip = False
is_member = True
money = 12000

# VIP인 식
print(is_vip)

# 회원인 식
print(is_member)

# VIP가 아닌 식
print(not is_vip)

# 회원이 아닌 식
print(not is_member)

# 돈이 10000 이상인 식
print(money >= 10000)

# 돈이 5000 미만인 식
print(money < 5000)

# 돈이 12000인 식
print(money == 12000)

# VIP이거나 회원인 식
print(is_vip or is_member)

# 돈이 10000 이상이고 회원인 식
print(money >= 10000 and is_member)

# VIP가 아니고 회원인 식
print(not is_vip and is_member)

# 회원이 아니고 보호자가 있는 식
print(not is_member and guardian)

# ========================================
# [4단계] 종합
# ========================================
temperature = 28

# 온도가 30 초과인 식
print(temperature > 30)

# 온도가 25 이상인 식
print(temperature >= 25)

# 온도가 28인 식
print(temperature == 28)

# 몸무게가 60이 아닌 식
print(weight != 60)

# 점수가 60 미만이거나 출석률이 70 미만인 식
print(score < 60 or attendance < 70)

# 출석률이 90 이상이고 회원이 아닌 식
print(attendance >= 90 and not attendance)

# 돈이 10000 이상이고 보호자가 없는 식
print(money >= 10000 and not guardian)

# 보호자가 없고 나이가 20 이상인 식
print(not guardian and age >= 20)

# 점수가 80 이상이고 VIP가 아닌 식
print(score >= 80 and not is_vip)

# 점수가 70 이상이거나 VIP가 아닌 식
print(score >= 70 or not is_vip)

# 회원이 아니거나 나이가 20 이상인 식
print(not is_member or age >= 20)

# 돈이 5000 미만이거나 온도가 30 초과인 식
print(money < 5000 or temperature > 30)

# 점수가 80 이상이고 (출석률이 90 이상이거나 VIP인) 식
print(score >= 80 and (attendance >= 95 or is_vip))

# 나이가 19 미만이거나 (보호자가 있고 회원인) 식
print(age < 19 or (guardian and is_member))

# 점수가 90 이상이거나 (출석률이 95 이상이고 회원인) 식
print(score >= 90 or (attendance >= 95 and is_member))

# VIP가 아니고 회원이면서 돈이 10000 이상인 식
print(not is_vip and (is_member and money >= 10000))

# 점수가 70 이상이고 (출석률이 80 이상이거나 나이가 20 이상인) 식
print(score >= 70 and (attendance >= 80 or age >= 20))

# 보호자가 있거나 (회원이 아니고 VIP가 아닌) 식
print(guardian or (not is_member and not is_vip))
