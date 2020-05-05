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
        if lList[0][0] < rList[0][0]:
            result.append(lList.pop(0))
        elif lList[0][0] == rList[0][0]:
            if lList[0][1] < rList[0][1]:
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
points = []

for _ in range(num):
    points.append(list(map(int, sys.stdin.readline().split())))

for point in merge_sort(points):
    print("{} {}".format(point[0],point[1]))