
total = 0
count = 0
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    value = float(num)
    total += value
    count += 1

print("Average: ", total/count)
print("Total: ", total)
print("Count: ", count)
