"""
글로벌시스템융합과 프로그래밍(1) 실습 문제
실습 11: 환전 프로그램

통화를 선택하고 원화 금액을 입력하면 환전 결과를 출력합니다.

환율 (원화 → 외화):
- 1. 달러(USD): 1달러 = 1350원
- 2. 엔(JPY): 100엔 = 900원
- 3. 유로(EUR): 1유로 = 1450원

수수료: 환전 금액의 1.5%

힌트: 통화를 선택한 뒤 환율에 맞게 계산합니다.
"""

print("=== 환전 프로그램 ===")
print("1. 달러 (USD)")
print("2. 엔 (JPY)")
print("3. 유로 (EUR)")
currency = int(input("통화를 선택하세요 (1/2/3): "))
krw = int(input("환전할 원화 금액을 입력하세요: "))

# 아래에 환전 결과를 계산하는 코드를 작성하세요

# 환전 금액 초기화
exchange_amount = 0

# 1이면 달러로 계산 후 출력
if currency == 1:
    exchange_amount = (krw / 1350) * 1
    print(f"환전 금액: {exchange_amount:.2f}달러")

# 2이면 엔으로 계산
elif currency == 2:
    exchange_amount = (krw / 900) * 100
    print(f"환전 금액: {exchange_amount:.2f}엔")

# 3이면 유로로 계산
elif currency == 3:
    exchange_amount = (krw / 1450) * 1
    print(f"환전 금액: {exchange_amount:.2f}유로")

# 그 외는 "잘못된 통화 선택입니다."
else:
    print("잘못된 통화 선택입니다.")

# 환전 금액이 있으면 수수료와 실 지불 금액을 구하고 출력
if exchange_amount > 0:
    fee = krw * 0.015
    final_amount = krw + fee

    print(f"수수료 (1.5%): {int(fee)}원")
    print(f"실 지불 금액: {int(final_amount)}원")