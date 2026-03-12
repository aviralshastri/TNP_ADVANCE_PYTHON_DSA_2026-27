N = int(input("Enter number of dishes: "))

A = []
for i in range(N):
    x = int(input("Enter dish type: "))
    A.append(x)

unique_types = set(A)

max_count = 0
ans = float('inf')

for dish in unique_types:
    last = -2
    count = 0

    for i in range(N):
        if A[i] == dish:
            if i != last + 1:
                count += 1
                last = i

    if count > max_count or (count == max_count and dish < ans):
        max_count = count
        ans = dish

print("Dish type with maximum picks:", ans)
