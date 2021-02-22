def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0

    for index, char in enumerate(s):
        # 이미 등장
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)

        used[char] = index
    return max_length


if __name__ == '__main__':
    s1, s2, s3 = "abcabcbb", "bbbbb", "pwwkew"
    print(lengthOfLongestSubstring(s1))
    print(lengthOfLongestSubstring(s2))
    print(lengthOfLongestSubstring(s3))