import array
import array as arr

arr.array = []
while True:  # validating for date

    try:
        month = input("Enter the month: \n")
        array.append(int(month))
        month = (1 <= month <= 12)  # Reading User input
        print(arr)
        break

    except ValueError:
        print("Invalid Input! Please try again")    # Error message
