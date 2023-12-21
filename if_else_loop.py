try:
    x1 = (int(input('Enter the first number: ')))
    x2 = (int(input('Enter the second number: ')))

    if x1 > x2:
        x1, x2 = x2, x1
    sum = 0
    for x in range(x1, x2 + 1):
        sum += x
        x += 1

    print('Sum of all integers between', x1, 'and', x2, 'including them is: ', sum)

    numbers = list(range(x1, x2+1))
    count = len (numbers)
    avg = (sum / count)
    print ('Average of all integers between', x1, 'and', x2, 'including them is: ', avg)

except Exception as e:
    print (e)