num = input("Put in a number : ")
word = input("Put in a word to pluralizer : ")

if (word[-2:]) == "fe":
    print(num + " " + word[:-2] + "ves")
elif (word[-2:]) == "sh":
    print(num + " " + word + "es")
elif (word[-2:]) == "ch":
    print(num + "  " + word + "es")
elif (word[-2:]) == "us":
    print(num + " " + word[:-2] + "i")
elif (word[-2:]) == "ay":
    print(num + " " + word + "s")
elif (word[-2:]) == "oy":
    print(num + " " + word + "s")
elif (word[-2:]) == "ey":
    print(num + " " + word + "s")
elif (word[-2:]) == "uy":
    print(num + " " + word + "s")
elif (word[-1:]) == "y":
    print(num + " " + word[:-1] + "ies")
else:
    print(num + " " + word + "s")