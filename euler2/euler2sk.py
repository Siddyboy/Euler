#!/usr/bin/env python3

def main():
    limit = 4000000
    
    fib = set()
    a = 1
    b = 1
    
    while a <= limit:
        fib.add(a)
        a, b = a+b, a
    
    print(fib)        
              
    a = sum(x for x in range(limit) if x % 2 == 0 and x in fib)
    print(a)

if __name__ == "__main__":
    main()
