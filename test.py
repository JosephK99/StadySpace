def test_1(value, correct_value):
    result = ''
    if value == correct_value:
        result = 'Passed'
    else:
        result = 'Failed'

    return result