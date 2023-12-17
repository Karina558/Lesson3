try:
    x1 = (int(input('Enter the first number: ')))
    x2 = (int(input('Enter the second number: ')))
    x = x1 - 1 + 1
    sum = 0
    while x < x2 + 1:
        sum += x
        x += 1
    print('Sum of all integers between', x1, 'and', x2, 'including them is', sum)

except Exception as e:
    print (e)



