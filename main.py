import test
from collections import Counter

def print_massage(massage):
    print(f'The massage is {massage}')


def calculate_mean_values(data: list) -> (str, float, float, float):
    status = 'Calculation fail'
    size = len(data)
    average = 0
    mediane = 0
    mode = None
    if data:
        status = 'Calculation successes'
        # average
        for i in data:
            average += i
        average = round(average / size, 2)
        # mediane
        data.sort()
        print(data)
        if size % 2 == 0:
            mediane = (data[size//2-1] + data[size//2]) / 2
        else:
            mediane = data[size//2]

        # mode
        count_dict = Counter(data)
        mode = max(count_dict, key=count_dict.get)
    return status, average, round(mediane, 2), mode


print_massage(test.test_1(1, 1))

data = [1, 2, 3, 4, 5, 7, 8, 6, 6, 6, 9, 2]
status, average, mediane, mode = calculate_mean_values(data)
print(status, average, mediane, mode)
print_massage(test.test_1(average, 4.92))
print_massage(test.test_1(mediane, 5.5))
print_massage(test.test_1(mode, 6))