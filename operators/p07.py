"""
실습 7: 할인 가격 계산

아래 3개 상품의 원래 가격과 할인율이 주어져 있습니다.
각 상품의 할인 가격을 계산하고, 총 결제 금액을 구하세요.

힌트: 할인 가격 = 원래 가격 * (1 - 할인율)
      총액은 += 연산자로 누적합니다.
"""

total = 0

# 상품 1: 노트북 1200000원, 10% 할인
price1 = 1200000
discount1 = 0.1

# 상품 2: 마우스 35000원, 20% 할인
price2 = 35000
discount2 = 0.2

# 상품 3: 키보드 55000원, 15% 할인
price3 = 55000
discount3 = 0.15

# 아래에 각 상품의 할인 가격을 계산하고 총액을 구하세요

# 노트북의 할인 가격을 계산한다. 계산 식: price1 * (1-discount1)
sale1 = int(price1 * (1-discount1))

# 마우스의 할인 가격을 계산한다. 계산 식: price2 * (1-discount2)
sale2 = int(price2 * (1-discount2))

# 키보드의 할인 가격을 계산한다. 계산 식: price3 * (1-discount3)
sale3 = int(price3 * (1-discount3))

# 그 후 가격을 total에 누적한다.

total+=sale1
total+=sale2
total+=sale3

# 노트북 마우스 키보드의 할인 금액을 출력하고 총 결제 금액을 출력한다.
print("노트북: ", sale1)
print("마우스: ", sale2)
print("키보드: ", sale3)
print("총 결제 금액: ",total)

