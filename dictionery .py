#dictionery

#1. annoted by {curly brackets}
#2. dictionery is combination multiple
#3. dict are mutable.
# 4. dictionery are hetrogenous
# 5. dict are ordered
# 6. in dict keys will always be unique but value can be duplicate. 
# 7. 
""""""
# # d = {} #empty dictionery
# d = {1:10, 2:20, 3:30,4:20}#5:50
# d [5] = 50 # creating new key and assigning value. 
# print (d) 
# # agar hum direct loop run krte hai dictionery pe toh we will get keys. 
# d = {1:10,2:20,3:30,4:40}
# for i in d:
#     print(i,d[i])


# # methods in dictionary. 
# #1. .keys() 
# # To print or give only and only keys from the dict. 
# d = {"a:1.0","b:2.0","c:3.0","d:4.0"}
# print(d.key())  

# #2. .value()
# #will give all the value from the dictionary. 
# #print (d.value())


# #3. .item()
# # it will give both keys and value from the dictionary
# d = {"a":1.0,"b":2.0,"c":3.0,"d":10.89}
# print(d.item())



# d= {"a":1.0,"b":2.0,"c":3.0,"d":10.89}
# for key, value in d .items():
#     print(key,value)


# #4. .pop(key)-> remove the key and value from the dict.   
# d= {"a":1.0,"b":2.0,"c":3.0,"d":10.89}
# d. pop("e")
# print(d)



# #5. .get()
# print(d.get(2,"not found"))


# # #6. .pop()
# # d.pop(3)
# # print(d)


# # #7. update() -> to merge two dictionaries. 
# # a = {"ravi" : 80, "devraj" : 23}
# # b = {"tanishq" : 100, "akarsh bhiya" : 110}
# # a. update(b)
# # print(a)



# #7. len() -> length of dictionary (total number of keys. )
# d = {1:10, 2:20, 3:30, 4:40}



#question print each key

d = {"ravi" : 80, "rohan":33, "chirag":22, "devraj":100}
#method 1
print(d.key())
#method 2




#method 3
for key,value in d .items():


    #ques2. print sum of all the marks
    d = {"ravi" : 80,"rohan" : 33, "chirag" : 22}
    total = 0
    for i in d.value():
        total += i
        print(total)

#que. print student who scored more then 80
#  : d = {"ravi" : 80, "rohan" : 33, "chir22, "devraj" : 100}
for name, marks in d.items():
    if marks >= 80:
        print(name)


#que. find and print the student with the highest marks using for loop        
d = {"ravi" : 80, "rohan" : 33, "chirag" : 22, "devraj" : 100}

#que. create a dictioary of number and their squares (1 to 5):
square = {}
for i in range(1,6):
    square[i] = i*i
    print(square)

#que   add five bonus marks to every student. 
d = {"ravi" : 80, "rohan" : 33, "chirag" : 22, "devraj" : 100}   
for i in d:
    d[i] = d[i] + 5
    print(d)      
