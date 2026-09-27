'''

-----Membership Operators-----

---> Membership operators are also return two conditions either true or false
---> If the condition is true returns TRUE
---> If the condition is false returns FALSE

Types:

1. in
2. not in

'''

word=str(input("Enter the word:"))
charecter=str(input("Enter the charecter"))

print(charecter in word)

a="apple"
print("z" in a)
print("z" not in a)

b="Welcome to the class"
print("class" in b)

c="Welcome to the class"
print(" " in c)
print(" "not in c)