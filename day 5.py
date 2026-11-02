#comparision operator
#(==,>,<,>=,<= , !=)
a = 10
b = 20

print(a == b) #left side and right side must be equal
print(12.5 > 12) # it can compare between 2 datatypes
print("ABC" < "WBC")# string 










#when you must want to get a single result out of multiple 
# comperision you have to use logical operators 
# ( and, or, not)

print(c > a,c > b)#-> multiple result -> true , true 
print (c > a and c > b)

#and logical operator says all the comperision must be 
#true 
print(12 == 12 and 45 != 23 and 60 > 50 and 34 != 34)#false

#or logical operator says out of all the comparisions
#any one must be true 
print(12 == 45 or 45 == 67 or 23 == 23)#true
#not logical operator conerts true -> false and 
# false -> true

print(not 12 == 12) #false 


