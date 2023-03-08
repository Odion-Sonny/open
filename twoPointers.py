def twoPointers(ls,n):
    l,r=0,len(ls)-1
    while l<=r:
        if ls[l]+ls[r] == n:
            return [l,r]
        elif ls[l]+ls[r]>n:
            r-=1
        else:
            l+=1
    return False 
print(twoPointers([2,5,8,12,30], 17))