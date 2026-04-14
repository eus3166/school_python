"""
글로벌시스템융합과 프로그래밍(1) 실습 문제

실습 3: 교통수단 추천

거리(km)를 입력받아 적절한 교통수단을 추천하세요.
if/elif/else를 사용합니다.

[추천 기준]
2km 미만: 도보
2km 이상 5km 미만: 자전거
5km 이상 20km 미만: 버스
20km 이상: 지하철
"""

distance = float(input("거리를 입력하세요 (km): "))

# 아래에 교통수단을 추천하여 출력하세요

# 만약 거리가 2km 미만이면 "거리: {distance}km"와 "추천 교통수단: 도보"을 출력한다.
if distance < 2 :
    print(f"거리: {distance}km")
    print("추천 교통수단: 도보")

# 그게 아니고 거리가 2km 이상 5km 미만이면 "거리: {distance}km"와 "추천 교통수단: 자전거"을 출력한다.
elif 2 <= distance < 5:
    print(f"거리: {distance}km")
    print("추천 교통수단: 자전거")

# 그게 아니고 거리가 5km 이상 20km 미만이면 "거리: {distance}km"와 "추천 교통수단: 버스"을 출력한다.
elif 5 <= distance < 20:
    print(f"거리: {distance}km")
    print("추천 교통수단: 버스")

# 이외의 나머지는 "거리: {distance}km"와 "추천 교통수단: 지하철"을 출력한다.
else :
    print(f"거리: {distance}km")
    print("추천 교통수단: 지하철")
