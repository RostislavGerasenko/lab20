n = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(n)]
series = []
items = []
current = arr[0]
current_len = 1
for element in arr[1:]:
    if element == current:
        current_len += 1
    else:
        series.append(current_len)
        items.append(current)
        current = element
        current_len = 1
series.append(current_len)
items.append(current)
print(f"Lengths of series: {series}. Series elements: {items}")
