try:
    x1 = int(input('Введіть початок діапазону: '))
    x2 = int(input('Введіть кінець діапазону: '))

    for i in range (x1, x2+1):
        if i % 3 == 0 and i % 5 ==0:
            print('\"Fizz Buzz\"')
        elif i % 5 ==0:
            print('\"Buzz\"')
        elif i % 3 == 0:
            print('\"Fizz\"')
        else:
            print(i)
except Exception as e:
    print (e)