sum = 0
total = 0
num = input("Enter any number")
for digits in num():
    sum = sum + digits
    total = total + int(digits)
print("sum of numbers", sum)
print("total number of digits", total)