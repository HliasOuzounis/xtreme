len_n, T = tuple(map(int, input().split()))
n = list(map(int, input().split()))

# The solution is based around finding the number of symmetries for the lights
# If they have s symmetries, then after T/s rotations we'll have the starting configuration
# The symmetries divide the whole circle to similar groups of on/off lights 
# reducing the amount of rotations until we land on the starting configuration
# because there is no need to make a full rotation since the group to the left will fill
# the gaps the first group left 

# In order to have *a* symmetry T and N must have common divisors =! 1
# since s must divide T and N to make sub-groups of the same size

def get_common_divisors(n1, n2):
    if n2 % n1 == 0:
        yield n1
    n1, n2 = min(n1, n2), max(n1, n2)
    for i in range(int(n1//2) + 1, 1, -1):
        if n1 % i == 0 and n2 % i == 0:
            yield i

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

symmetries = 1

for div in get_common_divisors(len_n, T):
    split_arrays = chunks(n, len_n//div) # create the sub-groups
    base_chunk = next(split_arrays) # sub-group 1 which is used for comparisons
    # every sub group must have the "on" lights at the same relative position => mod
    if all(
        list(map(lambda x: x % (T//div), chunk)) == base_chunk for chunk in split_arrays
    ):
        symmetries = div
        # we only need the biggest order of symmetry
        break

print(T//symmetries - 1) # -1 for the base config