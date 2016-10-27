end = input("Put in a number to stop at ")
end = int(end)

for eh in range(1, end):
    eh = eh + 1
    if eh % 3 == 0 and eh % 5 == 0:
        print ("FizzBuzz")
    elif eh % 3 == 0:
        print ("Fizz")
    elif eh % 5 == 0:
        print ("Buzz")
    else:
        print(eh)