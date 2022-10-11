# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

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

def compare_dice(dice_1, dice_2):
    return 1 if dice_1.count(6) > dice_2.count(6) else 2


def main():
    T = get_number()
    for _game in range(T):
        N = get_number()
        dice = [[], []]
        score = [0, 0]
        swapped = False
        for _round in range(N):
            if swapped:
                roll_2 = get_number()
                roll_1 = get_number()
                score[0] += roll_2
                score[1] += roll_1
            else:
                roll_1 = get_number()
                roll_2 = get_number()
                score[0] += roll_1
                score[1] += roll_2

            dice[0].append(roll_1)
            dice[1].append(roll_2)
            if score[0] != score[1]:
                swapped = not swapped

        print(compare_dice(dice[0], dice[1]))        

if __name__ == "__main__":
    main()