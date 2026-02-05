"""Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""
start = 2000
end = 3201
numbers =  []
for i in range(start, end):
    if i%7== 0 and i%5 != 0:
      numbers.append(i)

print(list(numbers))

""""Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("Input a number: "))
    print(f"The factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input! Please enter an integer.")

"""Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

n = int(input("Input a number: "))
my_dict = {}
for i in range(1, n+1):
    my_dict.update({i : i*i})

print(my_dict)


