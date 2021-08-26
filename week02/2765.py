# 입력은 여러 줄의 데이터로 구성된다. 각 데이터는 지름, 회전수, 시간이 공백으로 구분되어 주어진다.
# 지름은 inch단위의 실수이며, 회전수는 정수이다.
# 시간은 초단위의 실수로 주어진다. 입력은 회전수가 0이면 끝난다.
# 실수는 소수점 셋째자리이하까지 주어진다.

# π의 값은 3.1415927을 사용하면 된다.
# 1마일은 5280피트이다.
# 1피트는 12인치이다.
# 1시간은 60분이다.
# 1분은 60초이다.
# 1펄롱은 201.168미터이다.

# 바퀴의 지름을 안다면 회전수를 통해 이동 거리를 측정할 수 있다.
# 또한 바퀴가 회전하는 동안 걸린 시간을 안다면 평균 속도 역시 알 수 있다.

# 출력
# 각각의 데이터에 대해 다음을 출력한다

# Trip #N: distance MPH

# N은 각각의 데이터 번호를 출력해야 하며, distance는 총 거리(Miles)를 소수 둘째 자리까지 반올림하여 나타내며,
# MPH는 평균 속도(miles per hour)를 소수 둘째 자리까지 반올림하여 나타낸다.
# 회전수가 0인 데이터에 대해서는 출력하지 않는다.

import sys
input = sys.stdin.readline

test_num = 0
PI = 3.1415927
HOUR = 3600
MILE = 63360

while True:
    r, rotate, time = map(float, input().split())
    if rotate == 0:
        break
    test_num += 1

    distance = r / MILE * PI * rotate
    MPH = distance / time * HOUR

    print("Trip #%d: %.2f %.2f" % (test_num, distance, MPH))
