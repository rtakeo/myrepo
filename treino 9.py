fruit = "orange"
for x in range(len(fruit)):
    print("{:<2}".format(fruit[(x+1) * -1]), end="")
print()
for number in range(len(fruit)):
    print("{:<2}".format(number), end="")
print()
print()
name = "Are you Danny?"
realName = input("Please enter your name: ",  )
name = name.replace("Danny", realName)
print(name)
answer = input("Am I right?: ", )
if answer == "y".upper or "yes".upper:
    print("I knew it!! haha")