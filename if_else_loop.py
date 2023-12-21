try:
    n = int(input('Введіть довжину рядка: '))
    m = str(input('Введіть символ для рядка: '))
    number = 1
    while number < n+1:
        print (m, end ='')
        number += 1

except Exception as e:
    print (e)
