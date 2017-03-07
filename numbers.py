symbols = '0123456789ABCDEFGHIJ'

def recurs(number, base):
    string = symbols[number%base]
    if number < base:
        return string
    else:
        string = recurs(number/base, base) + string
        return string

def test(number, base, expected):
    result = 'PASS' if expected == recurs(number, base) else 'FAIL'
    print("({0} - {1}, {2}): expected {3}, actual {4}".format(result, number, base, expected, recurs(number, base)))

test(10, 16, 'A')
test(20, 16, '14')
