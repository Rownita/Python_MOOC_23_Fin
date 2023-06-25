### Please write a program that asks the user to choose between addition and removal. Depending on the choice, the program adds an item to or removes an item from the end of a list. The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.

### The list is printed out at the beginning and after each operation. Have a look at the example execution below:

###Sample output
###The list is now []
###a(d)d, (r)emove or e(x)it: d
###The list is now [1]
###a(d)d, (r)emove or e(x)it: d
###The list is now [1, 2]
###a(d)d, (r)emove or e(x)it: d
###The list is now [1, 2, 3]
###a(d)d, (r)emove or e(x)it: r
####The list is now [1, 2]
###a(d)d, (r)emove or e(x)it: d
###The list is now [1, 2, 3]
###a(d)d, (r)emove or e(x)it: x
###Bye!



list = []
print(f"The list is now {list}")
i = 1
while True:

    a = input(f"a(d)d, (r)emove or e(x)it:")
    if a == 'd':  ### Conditions for adding
        if len(list) != 0:
            list.append(i)
            i = i + 1
            print(f"The list is now {list}")
        if len(list) == 0:
            i = 1
            list.append(i)
            i = i + 1
            print(f"The list is now {list}")

    if a == 'r':  ### conditions for removing
        list.pop()
        i = i-1
        print(f"The list is now {list}")

    if a == 'x':  ### condition for exit
        print("Bye!")
        break
