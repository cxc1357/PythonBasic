def binary_search(arr,left,right,hkey):
    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == hkey:
            return mid
        elif arr[mid] > hkey:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def binary_search_recursive(arr,left,right,hkey):
    if len(arr) == 0:
        return -1
    if left > right:
        return -1
    mid = left + (right-left)//2
    if arr[mid] == hkey:
        return mid
    elif arr[mid] < hkey:
        return binary_search_recursive(arr,mid+1,right,hkey)
    else:
        return binary_search_recursive(arr,left,mid-1,hkey)

if __name__ == "__main__":
    sorted_list = [1,2,3,4,5,6,7,8]
    result = binary_search_recursive(sorted_list,0,7,5)
    print(result)