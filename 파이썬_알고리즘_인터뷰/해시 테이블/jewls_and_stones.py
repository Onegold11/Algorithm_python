import collections


def numJewelsInStones1(J: str, S: str) -> int:
    freqs = {}
    count = 0

    # 개별 개수
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    # 합계
    for char in J:
        if char in freqs:
            count += freqs[char]

    return count


def numJewelsInStones2(J: str, S: str) -> int:
    freqs = collections.defaultdict(int)
    count = 0

    for char in S:
        freqs[char] += 1

    for char in J:
        count += freqs[char]

    return count


def numJewelsInStones3(J: str, S: str) -> int:
    freqs = collections.Counter(S)
    count = 0
    
    for char in J:
        count += freqs[char]

    return count


def numJewelsInStones4(J: str, S: str) -> int:
    return sum(s in J for s in S)


if __name__ == '__main__':
    J, S = "aA", "aAAbbbb"

    print(numJewelsInStones1(J, S))
    print(numJewelsInStones2(J, S))
    print(numJewelsInStones3(J, S))
    print(numJewelsInStones4(J, S))