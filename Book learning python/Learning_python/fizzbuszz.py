for a in range(1, 21):
    if a % 3 == 0:
        print('fizz')
    if a % 5 == 0:
        print('buzz')
    if a % 3 != 0 and a % 5 != 0:
        print('fizzbuzz')
