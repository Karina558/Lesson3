try:
    x1 = int(input('Ведіть число початку діапазону: '))
    x2 = int(input('Ведіть число кінця діапазону: '))
    found = False

    print('Числа кратні 7:', end=' ')

    for i in range(x1, x2+1):
        if i % 7 ==0:
            print (i, end='; ')
            found = True
    if not found:
        print(' ! у діапазоні від', x1, 'до', x2, 'відсутні числа кратні 7')
except Exception as e:
    print (e)