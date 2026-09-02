"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 12: 중고차 가격 산정

신차 가격, 연식(년), 주행거리(만 km), 사고 유무를 입력받아
감가율을 적용한 중고차 예상 가격을 산정합니다.

감가 기준:
1) 연식 감가:
   - 1~3년: 연당 10% 감가
   - 4~7년: 연당 7% 감가
   - 8년 이상: 연당 5% 감가

2) 주행거리 감가 (추가 차감):
   - 5만 km 이하: 감가 없음
   - 5만 ~ 10만 km: 5% 추가 감가
   - 10만 km 초과: 10% 추가 감가

3) 사고 유무:
   - 사고 있음: 15% 추가 감가

최종 가격 = 신차 가격 × (1 - 총 감가율)
(최소 가격은 신차 가격의 10%)

힌트: 각 감가율을 따로 계산한 뒤 합산합니다.
"""

new_price = int(input("신차 가격을 입력하세요 (만원): "))
year = int(input("연식을 입력하세요 (년): "))
km = float(input("주행거리를 입력하세요 (만 km): "))
accident = input("사고 유무를 입력하세요 (Y/N): ")

# 아래에 중고차 가격을 산정하는 코드를 작성하세요

# 1) 연식 감가율 계산
# 1~3년이면 연당 10%
if year <= 3:
   year_discount = year * 10

# 4~7년이면 처음 3년은 10%, 나머지는 7%
elif year <= 7:   
   year_discount = 3 * 10 + (year - 3) * 7

# 그 외는 처음 3년 10%, 다음 4년 7%, 나머지 5%
else:
   year_discount = 3 * 10 + 4 * 7 + (year - 7) * 5

# 2) 주행거리 감가율
# 5이하이면 0%
if km <= 5:
   km_discount = 0

# 5~10이하이면 5%
elif km <= 10:
   km_discount = 5

# 그 외는 10%
else:
   km_discount = 10

# 3) 사고 감가율
# 있으면 15%
if accident == "Y" or accident == "y":
   accident_discount = 15

# 없으면 0%
else:
   accident_discount = 0

# 총 감가율
total_discount = year_discount + km_discount + accident_discount

# 감가 내역 출력
print("--- 감가 내역 ---")
print(f"연식 감가 ({year}년): {year_discount}%")
print(f"주행거리 감가: {km_discount}%")
print(f"사고 감가: {accident_discount}%")
print(f"총 감가율: {total_discount}%")

# 최종 가격 계산
final_price = int(new_price * (1 - total_discount / 100))

# 최소 신차 가격의 10%
min_price = int(new_price * 0.1)

# 최종 가격이 최소 가격 미만이면 최소 가격 적용
if final_price < min_price:
   final_price = min_price

# 예상 중고차 가격 출력
print(f"예상 중고차 가격: {final_price}만원")