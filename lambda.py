# Lambda Function

def square(x):
    return x*x

lambda_square = lambda x : x*x

print(square(5))
print(lambda_square(5))


# Using lambda() function with filter()
# that returns even numbers
lis = [1, 2, 3 ,4 ,5 , 6, 7, 9, 32, 67, 7234, 723, 12, 671, 122, 52, 314, 122, 79, 580]
final_list = list(filter(lambda x: (x % 2 == 0), lis))
print(final_list)

ages = [12, 123, 32, 21, 34, 13, 54, 64, 77, 11, 17]
adults = list(filter(lambda age: age>18, ages))
print(adults)


# Using lambda() function with map()
# that'll transform all the items
# together in the list

ages = [12, 123, 412, 521, 1245, 125, 12, 12, 123]
after = list(map(lambda age: (age * 2) + 1, ages))
print(after)

animals = ["cat", "dog", "cow", "eagle", "shark", "cRoCodiLE"]
upper = list(map(lambda animals: str.upper(animals), animals))
print(upper)



# Using lambda() function with reduce()
import functools

lis = [ 1 , 3, 5, 8, 6, 9, 2 ]

# using reduce to compute maximum element from list
print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis))

names = ["zed", "akali", "braum", "malphite", "cho"]
print("The maximum element of the list : ", end="")
print(functools.reduce(lambda a,b: a if len(a) > len(b) else b, names))
