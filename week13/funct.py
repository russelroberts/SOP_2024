# def greet():
#     return "Hello, World!"

# def area_circle(r):
#     return 3.14 * ( r ** 2)

# print(greet())
# print(area_circle(5))

#positional argument - parameters must follow the sequence.. 
# def area_trap(a,b,h): #values have to be placed in this order
#     return((a+b) /2) *h

# x = area_trap(2,3,5) #positional
# y = area_trap(a=2,h=5,b=3) #order not important

# print(x)
# print(y)

#declaring types and return types
def area_trapezoid(a:float,b:float,h:float)->float:
    return ((a+b)/2 *h)

#perimeter of parallelogram = 2(a+b)
def sum_num(a:float,b:float)->float:
    return a +b

#high order function
def area_trap_high(func,h) ->float:
    return (func /2) * h

print(area_trap_high(sum_num(a=2,b=3),5))


#collect user input

user_input = input("enter family name :")
print(user_input)