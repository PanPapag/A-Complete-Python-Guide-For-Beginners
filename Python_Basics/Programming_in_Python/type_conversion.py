print("INT CONVERSION")

print(3.14, int(3.14))
print(3.99999, int(3.99999))      # this does not round to closest int!
print(-3.99999, int(-3.99999))    # Note that the result is closer to zero

print("2345", int("2345"))        # parse a string to produce int
# wrong:  print(int("sth123"))
print("FLOAT CONVERSION")

print(float("2345.12"), type(float("2345.12")))

print("STRING CONVERSION")

print(str(14))
print(str(123.4))
print(type(str(12)))

val = 50 + 5
print("The val is: " + str(val))    # cannot be done withoud str() conversion
