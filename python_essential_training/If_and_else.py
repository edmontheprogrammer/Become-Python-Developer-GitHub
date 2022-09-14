def FizzBuzzChallenge(number):
    if (number % 5 == 0) and (number % 3 == 0):
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Fizz')
    elif number % 3 == 0:
        print('Buzz')
    else:
        print(number)


FizzBuzzChallenge(15)
FizzBuzzChallenge(10)
FizzBuzzChallenge(9)
FizzBuzzChallenge(7)
