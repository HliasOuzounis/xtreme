import sys
sys.setrecursionlimit(10**6)


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

prime_products = [1, 2]
def calculate_prime_products():
    k = 10**18
    i = 3
    while prime_products[-1] <= k:
        if is_prime(i):
            prime_products.append(prime_products[-1] * i)
        i += 2
        

def solve_case():
    n, m = get_numbers()
    village_ids = [get_number() for _ in range(n)]
    
    from collections import defaultdict
    graph = defaultdict(list)
    for _ in range(m):
        u, v, w = get_numbers()
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    min_node = min(village_ids)
    max_node = max(village_ids)
    
    distances = dijkstra(graph, max_node)
    
    print(get_max_gold(distances, min_node, max_node, 0))
    
def get_max_gold(distances, node, end, gold):
    if node == end:
        return gold + gold_from_city(node)

    max_gold = 0
    for parent in distances[node][1]:
        max_gold = max(max_gold, get_max_gold(distances, parent, end, gold + gold_from_city(node)))
    
    return max_gold
    
    
def dijkstra(graph, start):
    from heapq import heappush, heappop
    distances = {node: (float('inf'), []) for node in graph}
    distances[start] = (0, [])
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heappop(queue)
        if current_distance > distances[current_node][0]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor][0]:
                distances[neighbor] = (distance, [current_node])
                heappush(queue, (distance, neighbor))
                
            elif distance == distances[neighbor][0]:
                distances[neighbor][1].append(current_node)
                
    return distances

def gold_from_city(city_id):
    l, r = 0, len(prime_products) - 1
    while l < r:
        m = (l + r) // 2
        if prime_products[m] <= city_id:
            l = m + 1
        else:
            r = m
    return l - 1

def main():
    calculate_prime_products()
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
