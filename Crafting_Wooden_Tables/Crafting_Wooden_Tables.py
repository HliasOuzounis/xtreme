from math import floor, ceil


def main():  
    c, n, p, w = tuple(map(int, input().split()))

    max_tables = floor(w/c)
    if max_tables <= n:
        return max_tables 
    return n - ceil((w - n * c)/(p - c))


if __name__ == "__main__":
    print(main())
