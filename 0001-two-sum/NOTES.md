We could also do this:
def twosum(arr, target):
    left = 0
    right = len(arr) - 1
    curr = arr[left] + arr[right]
    while left < right:
        if curr < target:
            return [left, right]
        elif curr < target:
            arr[left] += 1
        elif curr > target:
            arr[right] -= 1
        else:
            return -1
            
            
answer = twosum([1, 2, 3, 4, 5], 7) 
print(answer)​
