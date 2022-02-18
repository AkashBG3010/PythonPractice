# # d = 31
# # m = 12
# # y = 2020
# #
# # y0 = y - (14 - m) / 12  # Calculation using given formula
# # print(y0)
# # x = y0 + y0 / 4 - y0 / 100 + y0 / 400
# # print(x)
# # m0 = m + 12 * ((14 - m) / 12) - 2
# # print(m0)
# # d0 = (d + x + 31 * m0 / 12) % 7
# # print(round(d0))
#
#
# while True:
#     try:
#         n = input("Please enter an integer: ")
#         n = int(n)
#         break
#     except ValueError:
#         print("No valid integer! Please try again ...")
# print("Great, you successfully entered an integer!")
#
#
# def main():
#     t = 1
#     while t:
#         try:
#             userVar = int(input("Player 1, Your move. Select your move: "))
#             break
#         except ValueError:
#             print("Incorrect input type, please enter an integer: ")
#
#     # We can assume that our input is an int if we get here, so check for range
#     checkRange = isGoodRange(userVar)
#
#     # Checking to make sure our input is in range and reprompt, or print.
#     if (checkRange != False):
#         print("Player 1 chooses to make the move: %d" % (userVar))
#     else:
#         print("Your input is not in the range of 1-9, please enter a correct var.")
#         main()
#
#
# # This function will check if our number is within our range.
# def isGoodRange(whatNum):
#     if (whatNum < 10) & (whatNum > 0):
#         return True
#
#     else:
#         return False
#
#
# # Protecting the main function
# if __name__ == "__main__":
#     main()
#


# def dayofweek(day, month, year):  # Function to calculation
#     d = day
#     m = month
#     y = year
#
#     y0 = y - (14 - m) / 12  # Calculation using given formula
#     x = y0 + y0 / 4 - y0 / 100 + y0 / 400
#     m0 = m + 12 * ((14 - m) / 12) - 2
#     d0 = (d + x + 31 * m0 / 12) % 7
#
#     print("The day is: ", round(d0))  # Printing result
#
#
# def input_val():
#
#     while True:
#         try:
#             day = 1 <= int(input("Enter the day: \n")) <= 31  # Reading User input
#             print(day)
#             break
#         except ValueError:
#             print("Invalid Input! Please try again")
#             continue
#
#     while True:  # validating for date
#         try:
#             month = 1 <= int(input("Enter the month: \n")) <= 12  # Reading User input
#             print(month)
#             break
#         except ValueError:
#             print("Invalid Input! Please try again")  # Error message
#
#     while True:  # validating for date
#         try:
#             year = int(input("Enter the year: \n")) > 0  # Reading User input
#             print(year)
#             break
#         except ValueError:
#             print("Invalid Input! Please try again")  # Error message
#
#
# def isDayRange(whatNum_d):
#     if (whatNum_d < 32) & (whatNum_d > 0):
#         return True
#     else:
#         return False
#
#
# def isMonthRange(whatNum_m):
#     if (whatNum_m < 13) & (whatNum_m > 0):
#         return True
#     else:
#         return False
#
#
# def isYearRange(whatNum_y):
#     if whatNum_y > 0:
#         return True
#     else:
#         return False
#
# checkRangeDay = isDayRange(day)
#
#     if(checkRangeDay != False):
#         print("Player 1 chooses to make the move: %d" % (userVar))
#     else:
#         print("Your input is not in the range of 1-9, please enter a correct var.")
#         main(

#
#
# if __name__ == '__main__':
#     input_val()









num = int(input("type: "))
print(type(num))
