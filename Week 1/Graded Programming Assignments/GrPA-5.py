# Problem: Accept two positive integers x and y as input. Print the number of digits in xy. You should be able to solve this problem using the concepts covered in week-1.

num1 = int(input())
num2 = int(input())
num3 = str(num1 ** num2)
print(len(num3))
