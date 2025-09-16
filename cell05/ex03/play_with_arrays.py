arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = [x + 2 for x in arr if x > 5]

unique_arr = list(set(new_arr))

print(arr)
print(unique_arr)