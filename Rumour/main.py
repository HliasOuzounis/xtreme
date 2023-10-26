def power_of_two(num):
    power = 0
    while(num > 0):
        num = num >> 1
        power +=1
    return power-1


def find_lca(a,b):
    while(a != b):
        if(a > b ):
            a = a//2
        if(a < b):
            b = b//2
    return b


def find_dist(query):
    a = query[0]
    b = query[1]
    dist_a_root = power_of_two(a)
    dist_b_root = power_of_two(b)
    lca = find_lca(a,b)
    dist_lca_root = power_of_two(lca)
    if( b == 1 ):
        return power_of_two(a)
    if( a == 1 ):
        return power_of_two(b)

    return dist_a_root + dist_b_root - 2 * dist_lca_root
    

q = int(input())
for i in range(q):
    query = tuple(map(int, input().split(" ")))
    query = sorted([int(query[0]), int(query[1])])
    print(find_dist(query))