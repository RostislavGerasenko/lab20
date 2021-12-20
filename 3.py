n = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(n)]
k = int(input("The number of a series to swap with the last: "))
last_element = arr[-1]
for index, element in reversed(list(enumerate(arr[:-1]))):
    if element != last_element:
        last_series_start = index + 1
        break
current_series = 1
series_start = 0
series_element = arr[0]
for i, element in enumerate(arr[1:], 1):
    if element == series_element:
        continue
    else:
        if current_series == k:
            series_end = i
            break
        current_series += 1
        series_start = i
        series_element = element
arr = arr[:series_start] + arr[last_series_start:] +\
arr[series_end:last_series_start]+arr[series_start:series_end]
print(f"The altered array: {arr}")
