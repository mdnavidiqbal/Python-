# # Check Tuple 
# NewTuple = (1,2,3,"Navid","Turzo")
# print(NewTupple)
# print(type(NewTupple))
# # To check tuple immuteable 
# NewTupple[1]=20
# print(NewTupple)

# # Negative Indexing :Data count start from the end 
# num = (1,2,"True","False")
# print(f"The (-1) index is : {num[-1]}") # Here 'f' means string formatting


# # range of indexing : 
# fruitsTuples = ("apple","banana","cherry","orange","kiwi","melon","mango")
# fruits = fruitsTupples[2:5]
# print(fruits)


# # Update Tuple : (i) Convert tuple from list 
# ThisTuple =("apple","banana","cherry","orange","kiwi","melon","mango")
# # convert tuple 
# y = list(ThisTuple)
# y.append("Navid")
# ThisTuple = tuple(y)
# print(f"Update Tuple is : {ThisTuple}")

# Unpack Tuples:
# fruitsTuples = ("apple","banana","cherry")
# (a,b,c) = fruitsTuples
# print(a)

# # Aeshtaric (*) : 
# (*a,) = fruitsTuples
# print(a)

# # Tuples Loops : 
# fruitsTuples = ("apple","banana","cherry")
# for i in fruitsTuples:
#     print(i)

# # range()
# for x in range(len(fruitsTuples)):
#     print(fruitsTuples[x])

# # While Loop : 
# fruitsTuples = ("apple","banana","cherry")

# i = 0
# while i<len(fruitsTuples):
#     print(fruitsTuples[i])

#     i += 1

# Join Touple : 

# tuple1 = ("Navid","Iqbal","Turzo")
# tuple2 = (7,8,9)

# Tuple Method : count(),index()

# fruitsTuples = ("apple","banana","cherry")
# y = fruitsTuples.count("apple")
# print(y) 

# x = fruitsTuples.index("apple")
# print(x)
