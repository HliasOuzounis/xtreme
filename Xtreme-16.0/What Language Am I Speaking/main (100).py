def parser():
    while 1:
        data = list(input().split(" "))
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


from functools import cache


@cache
def get_possible_languages(node):
    global tree
    node = tree[node]
    if isinstance(node, str):
        return {node}
    return get_possible_languages(node[1][0]) | get_possible_languages(node[1][1])


def main():
    nodes, phrases = get_number(), get_number()
    global tree
    tree = {}
    special_chars = set()
    languages = set()

    for _ in range(nodes):
        node_type = get_word()
        if node_type == "I":
            node_id = get_number()
            char = get_word()
            yes_node = get_number()
            no_node = get_number()
            tree[node_id] = (char, (yes_node, no_node))
            special_chars.add(char)

        elif node_type == "L":
            node_id = get_number()
            language = get_word()
            tree[node_id] = language
            languages.add(language)

    languages_per_node = {n: get_possible_languages(n) for n in tree}

    root = find_root(tree)

    for _ in range(phrases):
        possible_languages = []
        # possible_languages = langauges.copy()
        phrase = input()
        special_found = {char for char in special_chars if char in phrase}

        queue = [tree[root]]
        while queue:
            node = queue.pop(0)
            if isinstance(node, str):
                possible_languages.append(node)
                continue
            if node[0] in phrase:
                queue.append(tree[node[1][0]])
            else:
                queue.extend((tree[node[1][0]], tree[node[1][1]]))

        for language in sorted(possible_languages):
            print(language, end=" ")


def find_root(tree):
    for node_id in tree:
        if all(node_id not in node[1] for node in tree.values() if not isinstance(node, str)):
            return node_id


if __name__ == "__main__":
    main()
