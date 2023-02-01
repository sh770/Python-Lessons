# # Here's an example implementation of the above questions in Python:

# # Printing numbers 1 to 10 using a for loop:
# for i in range(1, 11):
#     print(i)

# # Calculating the sum of numbers 1 to 100 using a for loop:
# sum = 0
# for i in range(1, 101):
#     sum += i
# print("The sum of numbers 1 to 100 is: ", sum)

# # Printing all even numbers from 1 to 20 using a for loop:
# for i in range(2, 21, 2):
#     print(i)

# # Printing the multiplication table of a given number using a for loop:
# # num = int(input("Enter a number: "))
# # for i in range(1, 11):
# #         print(num, "", i, "=", numi)

# num = int(input("Enter a number: "))
# for i in range(1, 11):
# print(num, "", i, "=", numi)

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "", i*10, "=", num)   


# # Printing the elements of a list using a for loop:
# my_list = [1, 2, 3, 4, 5]
# for item in my_list:
#     print(item)