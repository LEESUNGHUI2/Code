def gcd(a,b):
    larger = 0
    smaller = 10000
    
    if(a>b):
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
        
    while smaller > 0:
        rem = larger % smaller
        larger = smaller
        smaller = larger 
        smaller = rem
    return larger

if __name__ == "__main__":
    res = gcd(16,24)
    print(res)
