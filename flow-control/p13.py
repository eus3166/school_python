"""
실습 13: 미니 성적 관리

5명의 점수를 입력받아 평균과 최고점을 출력하세요.

[조건]
- 리스트를 사용하지 않고 변수만으로 해결합니다.
- 합계와 최고점을 누적하며 계산합니다.

힌트: for + if + 누적 변수를 사용합니다.
"""

total = 0
best = 0
max_score=0
# 아래에 5명의 점수를 입력받아 평균과 최고점을 출력하세요

# 1,2,3,4,5번 학생의 점수를 입력받는다.
for i in range(5):
    score = int(input(f"{i+1}번 학생 점수: "))
    total+=score

    # 만약에 입력된 값이 max_score보다 크면 덮어쓰기
    if score>max_score:
        max_score=score

vudrbs = total/5


print(f"평균: {vudrbs}")
print(f"최고점: {max_score}")
