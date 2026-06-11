data = (5, 10, 15, 20, 25, 30, 35)

count = 0
total = 0

for i in data:
    if i % 5 == 0:
        count += 1

    total += i

average = total / len(data)

print("Count divisible by 5:", count)
print("Sum of all elements:", total)
print("Average:", average)
