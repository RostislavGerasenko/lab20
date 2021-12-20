n = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(n)]
l = int(input("The maximum length of a series: "))
arr.append(None)
new_arr = []
series_start = 0
series_element = arr[0]
for i, element in enumerate(arr[1:], 1):
    if element == series_element:
        continue
    else:
        length = i - series_start
        if length > l:
            new_arr.append(0)
        else:
            new_arr.extend([series_element] * length)
        series_start = i
        series_element = element
print(f"The altered array: {new_arr}")
