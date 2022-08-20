def sum(*args):
    result = 0
    for arg in args:
        print('sum>', arg)
        result += arg
        print('result teraz:', result)
    print('przed return...')
    return result


def minus(*args):
    # return -sum(*args)
    result = 0
    for arg in args:
        print('sum>', arg)
        result -= arg
    return result


def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


def one_divide_by(*args):
    return 1 / multiply(*args)


def main():
    func = {
        '+': sum,
        '-': minus,
        '*': multiply,
        '/': one_divide_by
    }

    while 1:

        try:
            nums = input('\n\nWrite exit for exit.\nWrite numbers, separate with spaces. After last, write enter: ')
            if 'exit' in nums.lower():
                exit()
            nums = [int(_) for _ in nums.split(' ')]
            print('nums = ', nums)
        except ValueError:
            print('# ERROR: write numbers only!')
            continue

        while 1:
            op = input('Write one operator of: + - * /:\t')
            if op in ['+', '-', '*', '/']:
                break

        print('Result: ', func[op](*nums), '\n', '-' * 20 + '\n')


if __name__ == '__main__':
    main()
