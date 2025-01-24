# #To check the type of data type we use a function to see the type of data is : type() function
# # Text_Type : String
# text = "HI,I am Navid " 
# print(text)

# # 1.Numeric/Number_type : int,float,complex 

# #int type data
# num = 20
# print(num) 

# # float type data
# num_1=40.2
# print(num_1)

# # complex type data 
# num_2 = 20j # without j others words does not work or run 
# print(num_2)

# print(type(text))
# print(type(num))
# print(type(num_1))
# print(type(num_2))

# # 2.String type data 
# nm_1="Navid"
# nm_2="Iqbal"
# print(nm_1 + nm_2)
# print("My name is : "+ " " + nm_1) # Here + " " we use it take a tab or space 

# # 3.Booleans data type : 
# Bl = True 
# print(Bl)
# print(type(Bl))
# x= 5
# y=6
# print(x<y)

# # 4.Binary data types : bytes,bytearray. The bytes() function return a bytes object also immutable. immutable means that we cant't change 
# #byte
# navid_list=[1,2,3,4,5] 
# b=bytes(navid_list)
# print(type(b))

# # bytearray it is muteable 
# b_list=[10,20,30,40,50]
# b_1= bytearray(b_list)
# b_1[1]=100
# print(b_1[1])

# # 5.None data type : it is not 0 , False or True it only one None cz it return string 
# x1 = None 
# print(x1)
# print(type(x1))

# # 6. Sequence data types : list,range,tuple
# # list
# li = ["navid","ashraful","jihad","naeem"] # muteable 
# li[0] = "iqbal"
# print(li)
# print(type(li))

# # tuple 
# tup = ("Iqbal","Islam","Hasan") # immutable 
# #tup[1] = "Navid" 
# print(tup)
# print(type(tup))

# # range 
# ran = range(6)
# print(ran)
# print(type(ran))
