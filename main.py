import test


def print_massage(massage):
    print(f'The massage is {massage}')


def calculate_average(data: list) -> (str, float):
    status = 'Calculation fail'
    average = 0
    if data:
        status = 'Calculation successes'
        for i in data:
            average += i

    return status, round(average/len(data), 2)


print_massage(test.test_1(1, 1))

data = [1, 2, 3, 4, 5]
status, average = calculate_average(data)
print(status, average)
print_massage(test.test_1(average, 3))
