num = input("Enter any number")
sum = 0
total = 0

for digits in num():
    sum = sum + digits
    total = total + int(digits)
print("sum of numbers", sum)
print("total number of digits", total)