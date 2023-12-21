try:
    n = int(input('Введіть число, факторіал якого треба знайти: '))
    def factorial_iterative(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    result = factorial_iterative(n)
    print(result)  # Виведе: 120

except Exception as e:
    print (e)
