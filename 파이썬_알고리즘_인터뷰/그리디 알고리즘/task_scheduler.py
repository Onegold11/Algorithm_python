from typing import List
import collections

def leastInterval(tasks: List[str], n: int) -> int:
    counter = collections.Counter(tasks)
    result = 0

    while True:
        sub_count = 0

        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1

            counter.subtract(task)
            # 빈 counter를 더하면 0이하인 아이템이 사라진다
            counter += collections.Counter()

        if not counter:
            break

        result += n - sub_count + 1

    return result