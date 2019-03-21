# inside a function all variables are local
def square(x) :
    y = x * x
    return y

# Global frame
y = 5
print(y)
to_square = int(input("Give the number you wish to compute its square: "))
result = square(to_square)
print("Square of ", to_square, " is ", result)
