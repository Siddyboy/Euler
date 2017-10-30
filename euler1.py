#!/usr/bin/env python3
from asyncio.streams import LimitOverrunError



def main():
    result3 = 0
    result5 = 0
    result15 = 0
    
    i = 1
    limit = 1000
    total = 0
    
    while result3 <= limit:
        result3 = i * 3
        total = total + result3
        i = i + 1
    
    i = 1    
    while result5 <= limit:
        result5 = i * 5
        total = total + result5
        i = i + 1
        
    i = 1
    while result15 <= limit:
        result15 = i * 15
        total = total - result15
        i = i + 1
        
    print(total)


if __name__ == "__main__":
    main()

