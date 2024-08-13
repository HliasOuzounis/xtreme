from math import log2, ceil

def xor_range(l, r):
    nof_bits = int(log2(r)) + 1

    ans = 0
    for bit in range(nof_bits):
        l_bit = get_xor_for_bit(bit, l - 1)
        r_bit = get_xor_for_bit(bit, r)
        ans |= r_bit ^ l_bit
        
    return ans
    
def get_xor_for_bit(bit, x):
    if bit == 0:
        return 1 if (x & 2) >> 1 != x % 2 else 0
    div = 1 << bit
    mod = x % (div * 2)
    if mod < div:
        return 0
    return 0 if mod % 2 else div

def xor_range_control(l, r):
    ans = 0
    for x in range(l, r + 1):
        ans ^= x
    return ans

# for l in range(1, 10):
#     for r in range(l, 10):
#         assert xor_range(l, r) == xor_range_control(l, r), "Error: l = {}, r = {}, xor_range = {}, xor_range_control = {}".format(l, r, xor_range(l, r), xor_range_control(l, r))

for i in range(66, 71):
    print(i, xor_range(1, i))