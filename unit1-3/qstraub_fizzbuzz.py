start = input("Put a number to start at ")
end = input("Put a number to end at ")
end = int(end)
start = int(start)

for eh in range(start - 1, end):
    eh = eh + 1
    if eh % 3 == 0 and eh % 5 == 0:
        print ("FizzBuzz")
    elif eh % 3 == 0:
        print ("Fizz")
    elif eh % 5 == 0:
        print ("Buzz")
    else:
        print(eh)