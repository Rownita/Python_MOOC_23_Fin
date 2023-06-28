"""
Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False
Hint: the function sorted can be used on strings as well.

"""


# Write your solution here
def anagrams(word1,word2):
    
    list_1 = list(sorted(word1))
    list_2 = list(sorted(word2))
    flag = True     
  
    len_1 = len(list_1)
    len_2 = len(list_2)
    a = 0
### if two words are not of same legth,they are not anagrams
    if len_1<len_2:
        flag = False
      
    if len_1>len_2:
        flag = False
    ### if they are of same length, then check whether they are anagrams
    if len_1 == len_2:
       a= len_1
       for i in range(0,a,1):
            if list_1[i]!=list_2[i]:   ### if two characters are not same, then they are not anagrams
                flag = False
                break
           
        
    if flag == True:
        return True
    if flag == False:
        return False
        
if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False
