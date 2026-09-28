# This file checkes input number whether it is prime or not

# Taking number using input function as integer
number = int(input("Enter a number: "))

# Validating input number 
if number <= 1:
    print(f"{number} is not a prime number")
else:

    # Assuming it is a prime number to process further
    is_prime = True

    # Dividing number using 0.5 square root
    for n in range(2, int(number ** 0.5)+ 1):

        # If the number is divible by range n, it is not a prime number and we will break the loop
        if number % n == 0:
            is_prime = False
            break
    
    # If the number is not divided by its 0.5 square root from the range 2, it is prime
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

