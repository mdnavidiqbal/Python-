# # List data type 
# food_list = ["Apple","Orange","Bannana","Jackfruit","Lichi"]
# print(f"Name of food is : {food_list}") # Here use String formatting 
# name_list = ["Tusher","Sisir","Turzo","Tarik"]
# print(f"Name lis is : {name_list}")
# # To see the specific value from the list 
# print(name_list[3])
# # To assigne or input the new value to the list 
# food_list[4] = "Lemon"
# print(food_list)

# # Add item 
# # এখানে আমরা দুটি মেথড এর মাধ্যম্যে আইটেম এড করতে পারিন এক হচ্ছে append() এর মাধ্যম্যে একটি আইটে আমরা লিস্ট এর সর্বশেষে এ এড করতে পারি 
# # আরেকটি মেথড হচ্ছে insert() এর মাধ্যম্যে আমরা আমাদের ইচ্ছেমতো ইনডেক্সে ভেলু এড করতে পারবো 

# # append()
# navid_list = ["Navid","Iqbal","Turzo"]
# navid_list.append("Sabina")
# print(navid_list)

# # insert()
# navid_list.insert(1, "Rahman")
# print(navid_li)


# Remove item from list 
# এখানে চারটি মেথড আছে ডেটা রিমুভ করার জন্য যেমন ঃ remove(এটি হচ্ছে এমন একটি মেথড যা ব্যবহার করে একদম স্পেসিফিক ডেটা রিমুভ করা হয় এবং হুবুহুবু আইটেম টি লিখে দিতে হয় যা আমি ডিলিট করতে চাচ্ছি )
# pop(এই মেথড ব্যবহার করে আমরা স্পেসিফিক ইনডেক্স ডিলিট করতে পারি)
# del(এই মেথড ব্যাবহার করে স্পেসিফিক ইনডেক্স এর ভেলু ডিলিট করতে পারি)
# clear(এই মেথড ব্যাবহার করে আমরা আমদের লিস্ট সব ডেটা রিমুভ করতে পারি )

# # remove()
# Navid = ["Website","Google","Microsoft","Facebook","GitHub"]
# print(Navid)
# Navid.remove("Facebook")
# print(Navid)

# # pop() method remove the specified index
# Navid = ["Website","Google","Microsoft","Facebook","GitHub",40]
# Navid.pop(2)
# #Navid.pop(5)
# print(Navid)

# # del() method remove the specific index 
# del Navid[0]
# print(Navid)

# # clear() method to remove the all list 
# Navid.clear()
# print(Navid)

# List Comprehension এই ক্ষেত্রে সর্বপ্রথম আমাদের ইউজ করতে হয় স্কোয়ার ব্র্যাকেট এর পর এর ভেতরে প্রথমে কন্ডিশন মানে কি করতে হবে 
# Comprehension হচ্ছে আমাদের যে ফর লুপ ইউজ করে লিস্ট টা দেয়া থাকবে তাকে শুধু দ্বিগুন করবে 
# name_list = [1,2,3,4,5]
# [i * 2 for i in name_list]
# Double = [i * 2 for i in name_list]
# print(Double)

# List comprehesion(এর কাজ হচ্ছে যেই লিস্ট টা দেয়া থাকবে সেই লিস্ট টা কে মডিফাই করে একলাইনে প্রিন্ট করতে পারবো ইচ্ছে মতো লোপ ইউজ করে )
# num = [1,2,3,4,5]
# for i in num : 
#     x = i * 2
#     print(i)
# double = [i*2 for i in num ]
# print(double)




# Sort List : 

# num = [3,9,5,2,7,1]
# eng = ['d','a','c','b']
# eng.sort()
# num.sort()
# print(num)
# print(eng)


# Reverse List : 

# Num = [1,2,3,4,5,6,7]
# Num.sort(reverse=True)
# print(Num)

# Copy List : 
# number = [1,2,3,4,5,6,7]
# num1 = number.copy()
# print(number)
# print(num1)

# Join List : 

# # normal rules : 
# num1=[1,2,3]
# num2=[4,5,6]
# # num3=num1+num2
# # print(num3)
# print(num1)
# # use extend() method 
# num1.extend(num2)
# print(num1)


# All method use in one : 

# # Access the list Item 
# navid = [1,2,3,"Navid","Iqbal","Turzo"]
# print(navid)

# # Add item on the list:append(),insert() 
# fruits = ["apple","banana"]
# print(fruits)
# # append() method
# fruits.append("orange")
# print(fruits)
# # insert() method
# fruits.insert(1,"kiwi")
# print(fruits)

# # Remove item on the list:remove(),pop(),del(),clear()
# fruits = ["apple","banana","orange","kiwi"]
# print(fruits)
# # remove() method
# fruits.remove("kiwi")
# print(fruits)
# # pop method()
# fruits.pop(2)
# print(fruits)
# # del() method 
# del fruits[1]
# print(fruits)
# # clear() method 
# fruits.clear()
# print(fruits)

# # Loop List 
# fruits = ["apple","banana","orange","kiwi"]
# # loop 
# for i in fruits : 
# print(i)

# # Sort and reverse:sort(),sort(reverse=True)
# num = [1,4,7,9,6,2,5,3,8]
# num.sort()
# print(num)
# # reverse() method
# num.sort(reverse=True)
# print(num)

# # copy() method
# num1 = num.copy 
# print(num1)

# # join the two list : extend() method
# num2 = ['a','b','c','d']
# num = [1,4,7,9,6,2,5,3,8]
# num2.extend(num)
# print(num2)

## ""List Exercise"" ##
# # Use the insert method to add "lemon" as the second item in the fruits list.
# fruits = ["apple","banana","cherry"]
# fruits.insert(2,"lemon")
# print(fruits)





