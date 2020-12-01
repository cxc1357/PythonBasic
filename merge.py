def merge(left,right):
    i = 0
    j = 0
    temp = []
    while i <= len(left) - 1 and j <= len(right) - 1:
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    temp += left[i:] + right[j:]
    return temp
print(merge([1,3,10],[2,4,6]))
