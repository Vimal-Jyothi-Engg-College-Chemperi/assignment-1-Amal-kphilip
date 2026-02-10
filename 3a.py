# a) Display the given integer in reverse manner
n = int(input("Enter an integer: "))
rev = 0
temp = n

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

print("Reversed number:", rev)