from pprint import pprint
# #from the pprint module, import the pprint function
# #dictionaries!

# #dictionaries contain key-value pairs
# d = {
# #   key   :  value
#     "name":"Quinn",
#     "birthmonth":"November",
#     "grade":16
# }
schedule = {
    "A":"SE11",
    "F":"SE12",
    "G":"SE10",
    "D":"SE12"
}

# print(d['name'])
# print (schedule)
schedule['E'] = "holla"
# #add a key-value pair where the key is "E" and
# #   the value is "holla"
# print(schedule)
# #change a value
# schedule["F"] = "SE9"
# print(schedule["F"])
# print(schedule)

if "E" in schedule:
    print("E is in schedule")
else:
    print("E is not in schedule")

# if "SE12" in schedule:
#     print("SE12 is in schedule")
# else:
#     print("SE12 is not in schedule")
#     #how to check if a value exists?

# for key in schedule:
#     print(key)
    
# for key in schedule:
#     print(schedule[key])
    
# for key in schedule:
#     if schedule[key] == "SE12":
#         print("exists as value!")
#     else:
#         print("does not exist as value!")
        
# for key in schedule:
#     if schedule[key] == "SE12":
#         print("exists as value!_")
#         break
# else: #this only happens if for loop doesnt break
#     print("does not exist as value!_")
    
# long = {
#     "name":"Mr. Chen",
#     "school":"Urban Assembly Gateway",
#     "money":0,
#     "status":"tired"
# }
# pprint(long)
# del long['name']
# pprint(long)