import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

def query(codeword):
    print(f"Q {format_codeword(codeword)}", flush=True)
    ans = get_number()
    sys.stdout.flush()
    return ans

def format_codeword(codeword):
    string = ""
    for num in codeword[:-1]:
        string += str(num) + " "
    string += str(codeword[-1])
    return string

def solve_case():
    n = get_number()
    
    code = [0 for _ in range(n)]
    prev_correct = query(code)
    for i in range(n - 1):
        code[i] = 1
        new_correct = query(code)
        if new_correct < prev_correct:
            code[i] = 0
        prev_correct = new_correct
    
    if code[-2] == 0:
        prev_correct += 1
        
    if prev_correct != n:
        code[n - 1] = 1
    
    print(f"A {format_codeword(code)}", flush=True)


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
