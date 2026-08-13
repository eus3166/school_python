"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 5: 특정 문자 찾기

문자열에서 특정 문자의 위치를 찾아 출력합니다.
찾으면 즉시 종료합니다.

[조건]
- 문자열: "hello python"
- 찾을 문자: "p"
- for 반복문으로 문자열을 한 글자씩 확인
- 찾으면 위치(인덱스)를 출력하고 break
- 못 찾으면 "찾지 못했습니다" 출력

힌트: 위치를 추적하는 변수를 사용하세요.
"""

text = "hello python"
target = "p"

# 아래에 특정 문자를 찾는 코드를 작성하세요

# text만큼 반복
for num, char in enumerate(text):
    # target을 찾으면 위치를 출력
    if char == target:
        print(f"'{target}'을(를) {num}번째 위치에서 찾았습니다!")
        # 즉시 반복 종료
        break

# 못 찾으면 "찾지 못했습니다" 출력
else:
    print("찾지 못했습니다")