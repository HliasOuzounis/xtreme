# a simple parser for python. use get_number() and get_word() to read
from collections import defaultdict


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


def main():
    n = get_number()
    in_degree = defaultdict(int)
    double_connections = defaultdict(set)
    for relations in range(n):
        person1, relation_type, person2 = get_word(), get_word(), get_word()
        if not person1 in in_degree:
            in_degree[person1] = 0
        if not person2 in in_degree:
            in_degree[person2] = 0
            
        if relation_type == "??":
            double_connections[person1].add(person2)
            double_connections[person2].add(person1)
        else:
            in_degree[person2] += 1

        
    candidates = {person for person in double_connections if in_degree[person] == 0}
    for person in candidates:
        if in_degree[person] != 0:
            continue
        if not all(in_degree[neighbours] == 0 for neighbours in double_connections[person]):
            change_doubly_connected(person, double_connections, in_degree)
            
    roots = list(filter(lambda x: in_degree[x] == 0, in_degree))

    print(*sorted(roots), sep="\n")


def change_doubly_connected(person, double_connections, in_degree):
    in_degree[person] += 1
    for neighbours in double_connections[person]:
        if in_degree[neighbours] != 0:
            continue
        double_connections[neighbours].remove(person)
        change_doubly_connected(neighbours, double_connections, in_degree)


if __name__ == "__main__":
    main()