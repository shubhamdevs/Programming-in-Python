# Find the factorial of the given number:
    
num = int(input("Enter a number: "))

fact = 1
answer = 1

while fact <= num:
    answer = answer * fact
    fact = fact + 1
print(answer)