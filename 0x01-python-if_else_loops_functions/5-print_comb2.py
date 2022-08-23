for i in range(100):
    if i < 99:
        print('{}'.format('0' * (2 - len(str(i))) + str(i)), end=', ')
    elif i == 99:
        print('{}'.format('0' * (2 - len(str(i))) + str(i)))
