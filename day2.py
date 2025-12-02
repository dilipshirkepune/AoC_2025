inputs = []
with open("day2_input.txt") as f:
    for line in f:
        parts = [s.strip() for s in line.split(',') if s.strip()]
        inputs.extend(parts)

total = 0
for input_range in inputs:
    start, end = int(input_range.split('-')[0]), int(input_range.split('-')[1])

    for num in range (start, end + 1):
        num1, num2 = str(num)[:len(str(num))//2 + len(str(num))%2], str(num)[len(str(num))//2 + len(str(num))%2:]
        if(num1 == num2):
            print("Invalid: ", num)
            total += int(num)

print("Total: ", total)