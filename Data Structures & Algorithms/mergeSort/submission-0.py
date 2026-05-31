# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        i = 0
        j = len(pairs) - 1
        def sort(arr, i, j):
            print([(i.key, i.value)for i in arr])

            def merge(arr, s, m, e):
                L = arr[s: m+1]
                R = arr[m+1: e+1]

                i = 0
                j = 0
                k = s

                while i < len(L) and j < len(R):
                    if L[i].key <= R[j].key:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1

                # One of the halfs will have elements remaining
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1

            if (j - i + 1 <= 1):
                return arr

            n = (j + i) // 2
            sort(arr, i, n)
            sort(arr, n + 1, j)

            merge(arr, i, n, j)

            return arr
        return sort(pairs, i, j)