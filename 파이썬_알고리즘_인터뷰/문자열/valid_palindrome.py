import collections
import re


def isPalindrome1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


def isPalindrome2(s: str) -> bool:
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


def isPalindrome3(s: str) -> bool:
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]