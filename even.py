numbers = [4, 11, 90, 24, 20, 36]

sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num

print("sum of even numbers:", sum_even)