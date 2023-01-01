
# Problem: Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.


num = input()
num1 = int(num[0])
num2 = int(num[2])
num3 = int(num[4])
num4 = int(num[6])
num5 = int(num[8])

print(num1 * num2 * num3 * num4 * num5)
