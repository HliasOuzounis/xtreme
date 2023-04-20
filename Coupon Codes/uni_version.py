import random


def generate_codes(num):
    letters = "ABCDEFGHIJK"
    digits = "012345"
    set_codes, codes = set(), []
    while len(codes) < num:
        code = (
            "".join(random.sample(letters, 4))
            + "-"
            + "".join(random.sample(digits, 4))
            + "-"
            + "".join(random.sample(letters, 4))
        )
        if code in set_codes:
            continue

        codes.append(code)
        set_codes.add(code)

    return codes


def hamming_distance(string1, string2):
    return sum([xi != yi for xi, yi in zip(string1, string2)])


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_prime(n):
    # find prime number greater than n
    while not is_prime(n):
        n += 1
    return n


class Hashtable:
    def __init__(self, size) -> None:
        self.size = find_prime(size)
        self.table = [None] * self.size
        self.dulicates_found = [[] for _ in range(self.size)]

    def hash_function(self, value):
        hash_value = 0

        for c in value:
            hash_value += ord(c)
            hash_value = hash_value * 17

        # Return the hash value
        return hash_value % self.size

    def insert(self, value, code):
        key = self.hash_function(value)

        if self.table[key] is None:
            self.table[key] = value
            self.dulicates_found[key].append(code)
            return

        while self.table[key] != value:
            key = (key + 1) % self.size
            if self.table[key] is None:
                self.table[key] = value
                self.dulicates_found[key].append(code)
                return

        self.dulicates_found[key].append(code)

        return

    def search(self, value):
        key = self.hash_function(value)
        if self.table[key] == value:
            return True
        else:
            return False

    def find_duplicates_pairs(self):
        s = 0
        print("Duplicates found: ")
        for duplicates in self.dulicates_found:
            for i, code1 in enumerate(duplicates):
                for code2 in duplicates[i + 1 :]:
                    for index, (char1, char2) in enumerate(zip(code1, code2)):
                        if char1 != char2:
                            break
                    print(
                        code1[:index]
                        + "\033[44;33m" + code1[index] + "\033[0m"
                        + code1[index + 1:],
                        code2[:index]
                        + "\033[44;33m" + code2[index] + "\033[0m"
                        + code2[index + 1:],
                    )
                    s += 1
        return s


def main():
    nof_codes = 100_000

    codes = generate_codes(nof_codes)
    print(f"{nof_codes} codes generated\nStarting Calculating")

    hashtable = Hashtable(nof_codes * 12 * 2)
    
    for i, code in enumerate(codes):
        # code = get_word()
        for index, char in enumerate(code):
            if char == "-":
                continue
            hashtable.insert(code[:index] + "?" + code[index + 1 :], code)
        if i % 1000 == 0:
            print(i)

    print(f"total duplicate pairs: {hashtable.find_duplicates_pairs()}")


if __name__ == "__main__":
    main()