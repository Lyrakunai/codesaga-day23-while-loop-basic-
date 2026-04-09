# Day 23 - while loop practice

# 1. basic while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# 2. reverse counting
i = 5 
while i >= 1:
    print(i)
    i -= 1

# 3. print Hello 5 times
count = 1 
while count <= 5:
    print("Hello")
    count += 1

# 4. sum of first 4 numbers
i = 1
total = 0
while i <= 4:
    total += i
    i += i
print("sum:", total)

# 5. even numbers till 10
i = 1 
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1