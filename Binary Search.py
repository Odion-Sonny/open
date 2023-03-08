# def binary_search(arr, key):
#     first = 0
#     last = int(len(arr)-1)

#     while first <= last:
#         midpoint = (first + last) //2
#         if arr[midpoint] == key:
#             return midpoint
#         elif arr[midpoint] < key:
#             first = midpoint + 1
#         elif arr[midpoint] > key:
#             last = midpoint - 1
#     return None

# x= binary_search([1,2,3,4,5,6,7,8], 8)
# print(f'index[{x}]')



def binarySearch(arr, key):
    first = 0
    last = int(len(arr)-1)

    while first <= last:
        midpoint = first+ (last - first)//2
        if arr[midpoint] == key:
            return midpoint
        elif midpoint < key:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None



x= binarySearch([1,2,3,4,5,6,7,8], 8)
print(f'index[{x}]')









