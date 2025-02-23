n = int(input())

in_count = 0
out_count = 0

for _ in range(n):
    x = int(input())
    if 10 <= x <= 20:
        in_count += 1
    else:
        out_count += 1

print(f"in: {in_count}")
print(f"out: {out_count}")