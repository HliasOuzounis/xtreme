N = int(input())
magic = list(map(int, input().split()))

Q = int(input())

target_stones = [int(input()) for _ in range(Q)]

magic_graph = {n + 1: [magic[n], magic.count(n + 1)] for n in range(N)}

states = [-1] * (N + 1)
moves = 0
states[N] = 0

change = True
while change:
    change = False
    remove = []
    for node, (child, parents) in magic_graph.items():
        if parents == 0:
            magic_graph[child][1] -= 1
            change = True
            remove.append(node)
    for node in remove:
        del magic_graph[node]
    if change:
        moves += 1
        states[len(magic_graph)] = moves


for target in target_stones:
    print(states[target])


# n=gets;puts" mNrsAgcUTPvnIo".index(n[45%n.size])