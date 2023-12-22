try:
    x1 = int(input('Введіть початок діапазону: '))
    x2 = int(input('Введіть кінець діапазону: '))
    count = 0

    print('Числа у даному діапазоні:')
    for i in range (x1, x2+1):
        print (i, end='; ' if i < x2 else '.')

    print("\nЧисла у діапазоні в зворотньому порядку:")
    for i in range (x1, x2+1) [::-1]:
        print (i, end='.' if i < x1+1 else '; ')

    print("\nЧисла кратні 7:")
    for i in range(x1, x2 + 1):
        if i % 7 == 0:
            print(i, end='; ' if i < x2-6 else '.')

    print("\nКількість чискл кратних 5:")
    for i in range(x1, x2 + 1):
        if i % 5 == 0:
            count += 1
    print(count, end='.')

except Exception as e:
    print (e)