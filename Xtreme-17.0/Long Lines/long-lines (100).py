# Use pypy3

n, h0, a, c, q = list(map(int, input().split()))

stack=[h0]
counter=0

for i in range(1, n):
    h = (a*stack[-1]+c)%q
        
    counter+=len(stack)
    while len(stack) and stack[-1]<=h:
        stack.pop()
    
    stack.append(h)
    # print(stack, counter)
print(counter)
