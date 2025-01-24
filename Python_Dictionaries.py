# studentInfo={
#     "Navid":{
#         "Name":"Md.Navid Iqbal",
#         "Roll": 40,
#         "Department": "CSE",
#         "Batch": "D-88",
#         "E-mail": "navidiqbal2000@gmai.com",
#         "Adress": "Gulshan,Vatara,Dhaka-1212"
#     },
#     "Sabina":{
#         "Name":"Sabina Rahman",
#         "Roll": 35,
#         "Department": "Physics",
#         "Batch": "Infinity",
#         "E-mail": "sabinarahman@gamil.com",
#         "Adress": "Azimpur,Dhaka"
#     }
# }
# print(studentInfo)
# # To show the specific keys 
# print(studentInfo["Sabina"])
# # To show the specific keys specific values 
# print(studentInfo["Sabina"]["Adress"])

# Using get(),keys(),values() method to show the specific data 

# # get() method to see the dictionary 
# x = studentInfo.get("Navid")
# print(x)

# # keys() method to see the keys 

# y = studentInfo.keys()
# print(y)

# # values() method to see the values 

# z = studentInfo.values()
# print(z)

# #Add item on the dictionary 

# studentInfo={
#     "Navid":{
#         "Name":"Md.Navid Iqbal",
#         "Roll": 40,
#         "Department": "CSE",
#         "Batch": "D-88",
#         "E-mail": "navidiqbal2000@gmai.com",
#         "Adress": "Gulshan,Vatara,Dhaka-1212"
#     }
# }

# # Normal Rules : 
# studentInfo["Roll"] = 43
# print(studentInfo["Roll"])

# # Using update() method
# studentInfo.update({"Name":"Sabina Rahman"})
# print(studentInfo["Name"])

# Remove item on the dictionary : pop(),popitem(),del(),clear()


# # pop() method 
# studentInfo={
#     "Navid":{
#         "Name":"Md.Navid Iqbal",
#         "Roll": 40,
#         "Department": "CSE",
#         "Batch": "D-88",
#         "E-mail": "navidiqbal2000@gmai.com",
#         "Adress": "Gulshan,Vatara,Dhaka-1212"
#     },
#     "Sabina":{
#         "Name":"Sabina Rahman",
#         "Roll": 35,
#         "Department": "Physics",
#         "Batch": "Infinity",
#         "E-mail": "sabinarahman@gamil.com",
#         "Adress": "Azimpur,Dhaka"
#     }
#    "Year": 2024
# }
# studentInfo.pop("Sabina")
# print(studentInfo)

# Loop Dictoniary : 

# studentInfo={
#     "Navid":{
#         "Name":"Md.Navid Iqbal",
#         "Roll": 40,
#         "Department": "CSE",
#         "Batch": "D-88",
#         "E-mail": "navidiqbal2000@gmai.com",
#         "Adress": "Gulshan,Vatara,Dhaka-1212"
#     },
#     "Sabina":{
#         "Name":"Sabina Rahman",
#         "Roll": 35,
#         "Department": "Physics",
#         "Batch": "Infinity",
#         "E-mail": "sabinarahman@gamil.com",
#         "Adress": "Azimpur,Dhaka"
#     }
# }

# # to see the main key
# for x in studentInfo:
#     print(x)
# # to see the values 
# for a in studentInfo.values():
#     print(a)
# to see the keys 
# for b in studentInfo.keys():
#     print(b)

# Dictionary copy : 

