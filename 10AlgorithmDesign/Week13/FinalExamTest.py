

# COMPLETE
arr = [1, 4, 9, 10, 5, 3, 7, 2, 8, 6, 14, 13, 11, 12]

# COMPLETE
n = len(arr) + 1

# COMPLETE
sum = (n * (n + 1)) / 2

# COMPLETE
sumArr = 0

# COMPLETE
for i in range(0, n - 1):
    print("i = " + str(i))
    print("arr[i] = " + str(arr[i]))
    sumArr = sumArr + arr[i]
    print("sumArr = " + str(sumArr))
    print()
missingStudent = sum - sumArr
print(int(missingStudent))