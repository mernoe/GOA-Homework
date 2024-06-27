total_sum = 0

for number in range(1, 1000):
    if number >= 500 and number < 600:
        continue
    total_sum += number
print(f"{total_sum}")
