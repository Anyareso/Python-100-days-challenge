def prime_checker(number):
    # if number == 1:
    #     print(f"{number} is not a prime number")
    # elif number > 1:
    #     for i in range(2,number):
    #         if (number % i) == 0:
    #             print(f"{number} is not a prime number")
    #             break
    #     else:
    #         print(f"{number} is a prime number")
    # else:
    #     print(f"{number}is not a prime number")
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("Its a prime number")
    else:
        print("It is not a prime number")


n = input("Enter a number you want to check")
prime_checker(number=n)