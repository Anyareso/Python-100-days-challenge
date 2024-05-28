def prime_checker(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("Its a prime number")
    else:
        print("It is not a prime number")


n = int(input("Enter a number you want to check"))
prime_checker(number=n)