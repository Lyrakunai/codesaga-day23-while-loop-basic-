#  ---Mini Challenges---
# 1. Sum of digits
num = 1234
total = 0
while num > 0:
    last_digit = num % 10
    total += last_digit
    num = num // 10
print(total)


# 2. Reverse number
num = 123
rev = 0
while num > 0:
    last_digit = num % 10
    rev = rev * 10 + last_digit
    num = num// 10
print(rev)


# 3. Count digits
num = 4567
count = 0
while num > 0:
    num = num // 10
    count += 1
print(count)


# 4. Even digits count
num = 24680
even_count = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_count += 1
    num = num // 10
print(even_count)



