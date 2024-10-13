number = int(input("Enter a number \n"))
def prime_number_checker(number):
    if number >1:
        for i in range(2, (number//2)+1):
            if(number % i) == 0:
                print("Given number is not prime:", number)
                break
            else:
                print("Given number is prime:", number)
                break
        else:
            print("It is not a prime number")
prime_number_checker(number)
    
