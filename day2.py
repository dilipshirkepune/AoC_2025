def is_valid(num):
    # for part 1 and 2: check for adjacent digits
    num1, num2 = str(num)[:len(str(num))//2 + len(str(num))%2], str(num)[len(str(num))//2 + len(str(num))%2:]
    if(num1 == num2):
        return False
    
    # For part 2: check for non-repeated patterns
    s = str(num)
    n = len(s)
    # check for repeated patterns of size 1..n//2 (e.g. all chars same, pairs repeating, etc.)
    for chunk_size in range(1, n // 2 + 1):
        if n % chunk_size != 0:
            continue
        parts = [s[i:i+chunk_size] for i in range(0, n, chunk_size)]
        if all(p == parts[0] for p in parts):
            return False

    return True

inputs = []
with open("day2_input.txt") as f:
    for line in f:
        parts = [s.strip() for s in line.split(',') if s.strip()]
        inputs.extend(parts)

total = 0
for input_range in inputs:
    start, end = int(input_range.split('-')[0]), int(input_range.split('-')[1])

    for num in range (start, end + 1):
        if not is_valid(num):
            #print("Invalid: ", num)
            total += int(num)

print("Total: ", total)