'''
Complexity = O(N^2) # 2 for loops
'''
def selectionSort(ls):

    for i in range(len(ls)):
        min_indx = i
        for j in range(i+1, len(ls)):
            if ls[min_indx] > ls[j]:
                min_indx = j
        ls[i], ls[min_indx] = ls[min_indx], ls[i]
    return ls


print(selectionSort([64, 25, 12, 22, 11]))