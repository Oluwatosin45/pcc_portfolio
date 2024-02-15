
 #how to find a prime number 

number = int(input('Please enter a number: '))

# function to determine a prime number

def findPrime(number):
    isPrime = True
    for num in range(2, number):
        if number % num == 0:
            isPrime = False
            break
    if isPrime:
        print('This is a prime number')
    else:
        print('This is not a prime number')


findPrime(number)