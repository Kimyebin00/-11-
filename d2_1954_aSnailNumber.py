T = int(input())

def myFunction(n):
    arr = [[0]*n for _ in range(n)]

    right = n-1
    left = 0
    up = 1
    down = n-1

    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    direction = 0

    num = 1
    i = 0
    j = 0

    while num <= n * n:
        arr[i][j] = str(num)
        num += 1

        if direction % 4 == 0 and j == right:
            direction += 1
            right -= 1
        elif direction % 4 == 1 and i == down:
            direction += 1
            down -= 1
        elif direction % 4 == 2 and j == left:
            direction += 1
            left += 1
        elif direction % 4 == 3 and i == up:
            direction += 1
            up += 1

        i += di[direction % 4]
        j += dj[direction % 4]

    return arr

result = ''
for test_case in range(1, T+1):
    result += '#%d\n' % test_case

    n = int(input())
    result_arr = myFunction(n)

    for nums in result_arr:
        result += ' '.join(nums) + '\n'

print(result)
