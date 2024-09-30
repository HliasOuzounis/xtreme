# a simple parser for python. use get_number() and get_word() to read
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


class Trie:
    def __init__(self) -> None:
        # each node used to be a class
        # class TrieNode:
        #     def __init__(self):
        #         self.children = {}
        #         self.count = 0
        # self.root = TrieNode()
        # but to stay within the memory limit, a more crude solution is needed
        self.root = [{}, 0]

    def insert(self, word, reverse=False):
        node = self.root
        if reverse:
            word = reversed(word)
        for char in word:
            if char not in node[0]:
                node[0][char] = [{}, 0]
            node = node[0][char]
            node[1] += 1


def main():
    dictionary_words = get_number()
    blended_words = get_number()

    forward_trie = Trie()
    backward_trie = Trie()

    for _ in range(dictionary_words):
        word = get_word()
        if len(word) < 3:
            continue
        forward_trie.insert(word)
        backward_trie.insert(word, reverse=True)

    for _ in range(blended_words):
        word = get_word()
        if len(word) < 5:
            print("none")
            continue

        prefix = [0] * len(word)
        prefix_pointer = forward_trie.root
        for i, char in enumerate(word):
            if char not in prefix_pointer[0]:
                break
            prefix_pointer = prefix_pointer[0][char]
            prefix[i] = prefix_pointer[1]

        suffix = [0] * len(word)
        suffix_pointer = backward_trie.root
        for i, char in enumerate(word[::-1]):
            if char not in suffix_pointer[0]:
                break
            suffix_pointer = suffix_pointer[0][char]
            suffix[len(word) - 1 - i] = suffix_pointer[1]

        prefix_index, suffix_index = get_split_index(word, prefix, suffix)

        if prefix_index != -1:
            first_word = ""
            prefix_pointer = forward_trie.root
            for i in range(prefix_index + 1):
                prefix_pointer = prefix_pointer[0][word[i]]
                first_word += word[i]
            while prefix_pointer[0]:
                char, prefix_pointer = list(prefix_pointer[0].items())[0]
                first_word += char

            second_word = ""
            suffix_pointer = backward_trie.root
            for i in range(len(word) - 1, suffix_index - 1, -1):
                suffix_pointer = suffix_pointer[0][word[i]]
                second_word += word[i]
            while suffix_pointer[0]:
                char, suffix_pointer = list(suffix_pointer[0].items())[0]
                second_word += char

            print(first_word, second_word[::-1])


# Here are all the edge cases I found. Not the best way to do it, but it works
def get_split_index(word, prefix, suffix):
    # check if there are prefixes with 3 characters and suffixes with 3 characters
    if prefix[2] == 0 or suffix[-3] == 0:
        print("none")
        return -1, -1
    
    # check if there are prefixes and suffixes up to the 4th to last character of the word
    # Don't check until the 3rd to last because suffix[i + 1] breaks it
    # for example, 
    # 2 1
    # abc xyz
    # abcyz
    # returned abc xyz instead of none
    prefix_index, suffix_index = -1, -1
    for i in range(2, len(word) - 3):
        if prefix[i] == 0:
            if prefix_index == -1:
                print("none")
            return prefix_index, suffix_index
        if suffix[i + 1] == 0:
            continue
        if prefix[i] > 1 or suffix[i + 1] > 1:
            print("ambiguous")
            return -1, -1
        prefix_index, suffix_index = i, i + 1

    # need to also check the 3rd to last character
    if suffix[-3] > 1 and prefix[-4] >= 1:
        print("ambiguous")
        return -1, -1
    
    if prefix[-3] > 1 and suffix[-3] >= 1:
        print("ambiguous")
        return -1, -1
    if prefix_index == -1:
        prefix_index, suffix_index = len(word) - 3, len(word) - 3
    return prefix_index, suffix_index


if __name__ == "__main__":
    main()
