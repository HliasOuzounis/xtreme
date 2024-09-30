# use pypy3

testcases = int(input())
for i in range(testcases):
    cache = {}
    result = 0
    state = -1
    v0, v1, loop_size = list(map(int, input().split()))
    # print(v0, v1, v2)
    v13 = v0
    result = 1
    v9 = v0+v1
    i = 1
    loop_times = (2 * (v13 - v1) + v1)//(v1 * 2) + 1
    v13 -= v1 * loop_times

    v13 = abs(v13)

    v17 = v13 * result - v9 * i
    if v13 * result - v9 * i < 0:
        result = i
        v9 = v13

    loop_times = loop_size
    for i in range(1, loop_size + 1):
        v13 = v0 * i

        loop_times = (2 * v13 - v1)//(v1 * 2) + 1
        v13 = abs(v0 * i - v1 * loop_times)

        v17 = v13 * result - v9 * i
        if v13 * result - v9 * i < 0:
            result = i
            v9 = v13
    result = result
    print(result)