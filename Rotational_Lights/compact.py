len_n, T = tuple(map(int, input().split()))
n = list(map(int, input().split()))

def get_common_divisors(n1, n2):
    if n2 % n1 == 0:
        yield n1
    n1, n2 = min(n1, n2), max(n1, n2)
    for i in range(int(n1//2) + 1, 1, -1):
        if n1 % i == 0 and n2 % i == 0:
            yield i

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

symmetries = 1
for div in get_common_divisors(len_n, T):
    split_arrays = chunks(n, len_n//div)
    base_chunk = next(split_arrays)
    if all(list(map(lambda x: x % (T//div), chunk)) == base_chunk for chunk in split_arrays):
        symmetries = div
        break

print(T//symmetries - 1)