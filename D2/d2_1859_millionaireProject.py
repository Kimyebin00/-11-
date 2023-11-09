T = int(input())

result = ''
for test_case in range(1, T + 1):
    result += '#%d ' % test_case
    benefit = 0
    n = int(input())
    prices = list(map(int, input().split(' ')))
    while len(prices) != 0:
        current_price = prices[0]
        prices_max = max(prices)
        max_index = prices.index(prices_max)

        sum_max_before = sum(prices[:max_index])
        benefit += prices_max * len(prices[:max_index]) - sum_max_before

        prices = prices[max_index + 1:]
    result += str(benefit) + '\n'

print(result)