for i in range(201):
    if i % 45 == 0:
        print('mega fizzbuzz *bzz* *bzz*')
    elif i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
