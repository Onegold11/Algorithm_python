from typing import List
import collections


def aroupAnagrams(strs: List[str]) -> List[List[str]]:
    # 없는 키는 자동으로 디폴트
    anagrams = collections.defaultdict(list)

    # 글자마다 정렬한 후 정렬한 글자를 키로 입력
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(aroupAnagrams(strs))
