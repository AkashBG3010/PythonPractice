for value in range(51):
    if value % 3 == 0 and value % 5 == 0:
        print("fizzbuzz")
        continue
    elif value % 3 == 0:
        print("fizz")
        continue
    elif value % 5 == 0:
        print("buzz")
        continue
    print(value)