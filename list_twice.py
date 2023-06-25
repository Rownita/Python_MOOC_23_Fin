"""
Programming exercise:
List twice
Points:
1

/

1

Please write a program that asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:

in the order the items were added
ordered from smallest to greatest
The program exits when the user types in 0.

An example of expected behavior:

Sample output
New item: 3
The list now: [3]
The list in order: [3]
New item: 1
The list now: [3, 1]
The list in order: [1, 3]
New item: 9
The list now: [3, 1, 9]
The list in order: [1, 3, 9]
New item: 5
The list now: [3, 1, 9, 5]
The list in order: [1, 3, 5, 9]
New item: 0
Bye!
"""
list_1 = []

while True:
    element = int(input("New  Item: "))
    if element!=0: # run the loop if the element is not 0
        list_1.append(element)
        print(f"The list  now: {list_1}")

        list_2 = sorted(list_1)  # sorting the list
        print(f"The list in order: {list_2}")

    if element == 0:  #break the loop if 0 element is entered
        print("Bye!")
        break
