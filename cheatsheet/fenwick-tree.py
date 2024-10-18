# ---------------- Fenwick Tree ---------------- #


# ---------------- Point Update - Query Range ---------------- #
def update(fwk, x, v):
    x += 1
    
    while x < len(fwk):
        fwk[x] += v
        x += x & -x

def query_range(fwk, q):
    # Query from 1 to q
    s = 0
    q += 1
    while q > 0:
        s += fwk[q]
        q -= q & -q

    return s

# ---------------- Range Update - Point Query ---------------- #
def update_range(fwk, l, r, v):
    update(fwk, l, v)
    update(fwk, r + 1, -v)

def query(fwk, q):
    s = 0
    q += 1
    while q > 0:
        s += fwk[q]
        q -= q & -q

    return s


if __name__ == "__main__":
    n = 10
    arr = list(range(10))
    fwk = [0] * (n + 1)
    for i in arr:
        update(fwk, i, i)
        
    # print(fwk)
    
    # print(query_range(fwk, 2))
    # print(query_range(fwk, 9))

    fwk = [0] * (n + 1)
    update_range(fwk, 1, 3, 1)
    update_range(fwk, 2, 5, 1)
    
    print(query(fwk, 2))
    print(query(fwk, 3))
    print(query(fwk, 4))
    
        