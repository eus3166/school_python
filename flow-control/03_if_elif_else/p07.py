"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 7: 동전 변환

금액(원)을 입력받아 최소 동전 수로 변환하세요.
사용 가능한 동전: 500원, 100원, 50원, 10원
(10원 미만은 버림)

힌트: 나누기(//)와 나머지(%) 연산자를 사용하세요.
if/elif는 필요 없을 수도 있지만, 각 동전이 0개가 아닐 때만 출력하세요.

[처리 순서]
1. 큰 동전부터 몇 개 필요한지 계산
2. 나머지 금액을 다음 동전으로 계산
3. 0개가 아닌 동전만 출력
"""

amount = int(input("금액을 입력하세요 (원): "))

# 아래에 동전 수를 계산하여 출력하세요

# (f"{amount}원 → 동전 변환:")을 출력한다.
print(f"{amount}원 → 동전 변환:")

# coin_500 = amount // 500를 먼저 구한 후 amount = amount % 500를 구한다.
# (먼저 500원 동전이 몇 개인지를 구한 후 500을 나눈 후 나머지를 다시 amount에 대입한다.
coin_500 = amount // 500
amount = amount % 500

# coin_100 = amount // 100를 먼저 구한 후 amount = amount % 100를 구한다.
coin_100 = amount // 100
amount = amount % 100

# coin_50 = amount // 50를 먼저 구한 후 amount = amount % 50를 구한다.
coin_50 = amount // 50
amount = amount % 50

# amount = amount //  10를 구한다.
amount = amount // 10

total = coin_500 + coin_100 + coin_50 + amount

# 각각의 동전이 몇 개 나왔고 총 동전 수를 출력한다.
print(f"500원: {coin_500}개")
print(f"100원: {coin_100}개")
print(f"50원: {coin_50}개")
print(f"10원: {amount}개" )
print(f"총 동전 수: {total}개")
