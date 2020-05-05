import sys

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    lList = list[:mid]
    rList = list[mid:]

    lList = merge_sort(lList)
    rList = merge_sort(rList)
    return merge(lList, rList)

def merge(lList, rList):
    result = []

    while len(lList) > 0 and len(rList) > 0:
        if len(lList[0]) < len(rList[0]):
            result.append(lList.pop(0))
        elif len(lList[0]) == len(rList[0]):
            if lList[0] < rList[0]:
                result.append(lList.pop(0))
            else:
                result.append(rList.pop(0))
        else:
            result.append(rList.pop(0))

    if len(lList) > 0:
        result += lList
    else:
        result += rList

    return result


num = int(input())
words = []

for _ in range(num):
    words.append(sys.stdin.readline()[:-1])

answer = []
for word in merge_sort(words):
    if word not in answer:
        answer.append(word)
        print(word)