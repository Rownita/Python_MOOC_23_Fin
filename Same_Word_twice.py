###Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.

Sample output
Word: once
Word: upon
Word: a
Word: time
Word: upon
You typed in 4 different words
###


list = []

while True:
    word = input("Word:")
### if same word is typed then count words and break 
    if word in list:
        length = len(list)
        print(f"You typed in {length} different words ")
        break
### if different words are typed then append the word to the lsit and continue     
    if word not in list:
        list.append(word)
