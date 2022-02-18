import re

# while True:
#     try:
#         number = int(input("Please enter a number: "))
#         while number = re.match("^\-?[1-31]*$", number):
#             print("Invalid Input! Please try again..")
#             break
#         pass
#     except ValueError:
#         print("Error! Make sure you only use numbers..")
#     continue
############################################################################


# def input_date_val():
#     while True:
#         try:
#             day = int(input("Enter the day: \n"))  # Reading User input
#             break
#         except ValueError:
#             print("Invalid Input! Please try again")
#             continue
#
#     def isDayRange(whatNum_d):
#         if (whatNum_d < 32) & (whatNum_d > 0):
#             return True
#         else:
#             return False
#
#     checkRangeDay = isDayRange(day)
#
#     if (checkRangeDay == False):
#         print("Entered date is not valid! try Date range(1-31)")
#         input_date_val()
#     else:
#         print("hd", day)
#         result = day
#         return result
#
#     return day
#
#


# while True:  # validating for date
#     try:
#         month = 1 <= int(input("Enter the month: \n")) <= 12  # Reading User input
#         print(month)
#         break
#     except ValueError:
#         print("Invalid Input! Please try again")  # Error message
#
# while True:  # validating for date
#     try:
#         year = int(input("Enter the year: \n")) > 0  # Reading User input
#         print(year)
#         break
#     except ValueError:
#         print("Invalid Input! Please try again")  # Error message

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


# if __name__ == '__main__':
#     input_val()
