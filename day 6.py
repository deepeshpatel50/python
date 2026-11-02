
#accept two number nad print the gretest between them 

a = int(input("tell your first number :-"))
b = int(input("tell your second number :-"))


if a > b:
    print(f"{a} is greater then {b}")

elif b > a:
    print(f"{b} is greater than {a}")


else:
    print("both number are equal")


#accept an integers and check wheather it is an even number or odd



a = int(input("tell your number :-"))

if a % 2 == 0:
    print("the number is even")

else:
    print("the number is odd")    