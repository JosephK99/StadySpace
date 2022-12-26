def test_1(value, correct_value) -> str:
    """
    This function is for testing
    """
    result = 'Failed'
    if value == correct_value:
        result = 'Passed'
    print(f'Testing expected value {correct_value}, calculated {value}')
    return result
