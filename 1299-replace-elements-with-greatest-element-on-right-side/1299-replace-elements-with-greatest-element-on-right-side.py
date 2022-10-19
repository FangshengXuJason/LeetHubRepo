class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        maxNum = arr[i]
        arr[i] = -1
        i = i - 1
        while i >= 0: 
            oldMax = maxNum
            maxNum = max(maxNum, arr[i])
            arr[i] = oldMax
            i = i - 1
        return arr
        