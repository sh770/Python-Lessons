def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

x = int(input("Enter a number: "))
if is_palindrome(x):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
print()