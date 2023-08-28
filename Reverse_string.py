
### reversing a string

def reverse_string(x):
    return x[::-1] 

### counting characters of a string 

def count_characters(txt,ch):
    count_ch = txt.count(ch)
    return count_ch 
    
    
if __name__ == "__main__":
    x = input("Enter a string:")
    
    y = reverse_string(x)
    print(y)
    
    z = "Rownita is a beautiful girl"
    
    r = count_characters(z,"i")
    
    print(r)
    
    Z = "Akbar loves Rownita"
    

    m=Z.replace("Rownita","Akbar")
    print(m)
