def split(str):
    a = str.find('a')
    
    b = str[:a+1] 
    c = str[a+1:]  

    print(b)
    print(c)

user = input("Your word: ")

split(user)
