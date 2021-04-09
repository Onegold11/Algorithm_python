def quicksort(A: list, lo: int, hi: int):
    def partition(l: int, h: int):
        left = l
        for right in range(l, h):
            if A[right] < A[h]:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[h] = A[h], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)


if __name__ == '__main__':
    A = [5, 1, 7, 10, 9]
    quicksort(A, 0, 4)
    print(A)