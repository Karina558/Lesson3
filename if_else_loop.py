try:
    n = int(input('Введіть довжину рядка: '))
    number = 1
    while number < n+1:
        print ('*', end ='')
        number += 1

except Exception as e:
    print (e)
