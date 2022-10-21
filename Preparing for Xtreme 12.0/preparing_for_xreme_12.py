import functools
from sys import maxsize

inp = []
for _ in range(101):
    try:
        inp.append(input())
    except Exception:
        break


class Book:
    def __init__(self, index, time, topics):
        self.index = index
        self.time = time
        self.topics = {_topic: True for _topic in topics}


books = [Book(ind, int(book.split()[0]), book.split()[1:]) for ind, book in enumerate(inp)]

topics_dict = {}
for ind, book in enumerate(books):
    for topic in book.topics:
        if topic in topics_dict:
            topics_dict[topic].append(ind)
        else:
            topics_dict[topic] = [ind]

topics_queue = list(topics_dict.keys())


@functools.lru_cache(maxsize=None)
def next_topics(queue):
    if len(queue) == 0:
        return 0
    min_time = maxsize
    for next_book in topics_dict[queue[-1]]:
        new_queue = tuple(x for x in queue if not books[next_book].topics.get(x))
        if len(queue) == len(new_queue):
            continue
        new_time = books[next_book].time + next_topics(new_queue)
        if new_time < min_time:
            min_time = new_time
    return min_time


print(next_topics(tuple(topics_queue)))