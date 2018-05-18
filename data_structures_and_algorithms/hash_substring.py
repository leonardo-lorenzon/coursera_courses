# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    d = 8933
    q = 988
    positions = []
    m = len(pattern)
    n = len(text)
    h = pow(d,m-1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p+ord(pattern[i])) % q
        t = (d * t+ord(text[i])) % q
    for s in range(n - m + 1):
        if p == t:
            match = True
            for i in range(m):
                if pattern[i] != text[s + i]:
                    match = False
                    break
            if match:
                positions.append(s)
        if s < n-m:
            t = (t - h * ord(text[s])) % q
            t = (t * d + ord(text[s + m])) % q
            t = (t + q) % q

    return positions


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
