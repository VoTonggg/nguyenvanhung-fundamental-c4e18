n = int(input("Enter a number n "))

factorial_result = 1

for i in range(n):
    factorial_result *= (i+1)

print("Factorial of n is: ", factorial_result)