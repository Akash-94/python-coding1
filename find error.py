a = int(input("Enter number 'a': "))
b = int(input("Enter number 'b': "))
c = int(input("Enter number 'c': "))

if a == b == c:
    print("The values are equal")

elif (a > b) and (a > c):
    print("The largest number is {} ".format(a))

elif (b > a) and (b > c):
    print("The largest number is {} ".format(b))

else:
    print("The largest number is {} ".format(c))

print()

