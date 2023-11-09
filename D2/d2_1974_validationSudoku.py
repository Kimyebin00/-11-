T = int(input())

result = ''
for test_case in range(1, T + 1):
    result += '#%d ' % test_case

    sudoku_arr = []
    for i in range(9):
        input_nums = input().split(' ')
        sudoku_arr.append(input_nums[:9])

    isSudoku = True

    while isSudoku:
        # 가로 확인
        for i in range(9):
            if len(set(sudoku_arr[i])) != 9:
                isSudoku = False
                break

        if isSudoku:
            for i in range(9):
                if isSudoku is False:
                    break
                sudoku = []
                for k in range(9):
                    sudoku.append(sudoku_arr[k][i])
                if len(set(sudoku)) != 9:
                    isSudoku = False
                    break

        if isSudoku:
            for i in range(3):
                if isSudoku is False:
                    break
                for k in range(3):
                    sudoku = []
                    for j in range(3 * k, 3 * k + 3):
                        for z in range(3 * i, 3 * i + 3):
                            sudoku.append(sudoku_arr[z][j])
                    if len(set(sudoku)) != 9:
                        isSudoku = False
                        break

        if isSudoku:
            result += '1\n'
            break

    if isSudoku is False:
        result += '0\n'

print(result)