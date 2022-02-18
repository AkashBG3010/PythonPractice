# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#
# print(x)
#
#
# while True:
#     try:
#         while True:
#             try:
#                 day = int(input("Enter the day(1-31): \n"))
#                 break
#             except ValueError:
#                 print("Invalid Input!")
#
#         while True:
#             try:
#                 if 0 < day < 32:
#                     month = int(input("Enter the month(1-12): \n"))
#                 break
#             except ValueError:
#                 print("Invalid Input!")
#
#     except NameError:
#         print("Invalid Input!")
#         pass


num = 5
while True:
    try:
        if num == 1:
            day = int(input("Enter the day(1-31): \n"))
            break
    except (ValueError, NameError):
        print("Invalid Input!")

    else:
        if num != 1:
            print("Invalid Input!")
            break
        pass
