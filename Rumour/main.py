
def power_of_two(num):
    power = 0
    # print(num)
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


def find_dist(querrie):
    a = querie[0]
    b = querie[1]
    dist_a_root = power_of_two(a)
    dist_b_root = power_of_two(b)
    lca = find_lca(a,b)
    dist_lca_root = power_of_two(lca)
    if( b == 1 ):
        return power_of_two(a)
    if( a == 1 ):
        return power_of_two(b)

    # print(f"{dist_a_root} + {dist_b_root} -2 * {dist_lca_root}  =")
    return dist_a_root + dist_b_root - 2 * dist_lca_root
    

f = open("in.txt", "r")
n = int(f.readline())
###
# print(n)
rectangles = []
for i in range(n):
    querie = f.readline().split()
    querie = sorted([int(querie[0]), int(querie[1])])
    # print(querie)
    print(find_dist(querie))
    