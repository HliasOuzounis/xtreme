n, m = list(map(int, input().split()))

rhymes={}


capitals = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
double_capitals = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"
triple_capitals = "AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOOOPPPQQQRRRSSSTTTUUUVVVWWWXXXYYYZZZ"
quadruple_capitals = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ"
capitals=capitals+double_capitals+triple_capitals+quadruple_capitals
# print(capitals)
for i in range(n):
    for word in input().split():
        rhymes[word.lower()]=i
input()
out=[]
for i in range(m):
    # print(i)
    line = input()
    word = line.split()[-1]
    # print(word)
    if word.lower() in rhymes:
        
        out.append(rhymes[word.lower()])
    else:
        out.append("X")

for i in range(0, len(out)):
    if out.count(out[i])==1 and out[i]!="X":
        out[i] = "X"


# print(out)
out2=[]
counter=0
found_pairs = {}
for i in range(0, len(out)):
    if out[i]=="X":
        out2.append("X")
        
    else:
        if found_pairs.get(out[i], -1)==-1:
            # print("if", out[i])
            out2.append(capitals[counter])
            counter+=1
            found_pairs[out[i]]=i
        else:
            # print("else", out[i])
            out2.append(out2[found_pairs[out[i]]])
# print(out)
print("".join(out2))


