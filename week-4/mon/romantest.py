def test(expected, actual, message):
    if expected == actual:
        print('check')
    else:
        print('Error: ' + message)
        print(expected, actual)

TOKENS = {
'5': 'V',
'4': 'IV',
'1': 'I'
}

def arabic2roman(arabic):
    if arabic == 5 or arabic == 4:
        return TOKENS[str(arabic)]
    return 'i' * arabic

test(arabic2roman(0), '', 'It should handle 0')
test(arabic2roman(1), 'i', 'It should handle 1')
test(arabic2roman(2), 'ii', 'It should handle 2')
test(arabic2roman(4), 'iv', 'It should handle 4')
test(arabic2roman(5), 'v', 'It should handle 5')
