#!/usr/bin/env python3

def main():
    limit = 1000
              
    a = sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)
    print(a)
    print(a)

if __name__ == "__main__":
    main()
