from decorators import cache_decorator

operators = {"+": lambda a, b: a + b,
             "-": lambda a, b: a-b,
             "/": lambda a, b: a/b,
             "*": lambda a, b: a*b,
             "**": lambda a, b: a**b}

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation not in operators:
        return "Операция неизвестна"
    return operators[operation](a, b)


if __name__ == '__main__':
    # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))
        
        operation = input('Введите операцию: ')
        
        print('Результат: ', calculator(a, b, operation))
    except Exception as e:
        print("Введено не число")

