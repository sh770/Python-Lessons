# x = input("enter seven words: ")
# # print(type(x))
# y = []
# # x = 
# for i in x:
#     print(i)

input_string = input("Enter words separated by spaces: ")
start = 0
for i, char in enumerate(input_string):
    if char == " ":
        print(input_string[start:i])
        start = i + 1
print(input_string[start:])
