# c) Find the largest number in a list without using built-in functions
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

largest = arr[0]
for num in arr:
    if num > largest:
        largest = num

print("Largest number:", largest)
