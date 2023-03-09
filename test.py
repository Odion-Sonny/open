 def dup(ls):
     n = len(ls)
     ls.sort()
     dup=[]
     for i in range(n-1):
         if ls[i] == ls[i+1]:
             if i not in dup:
                 dup.append(ls[i])
     return dup
print(dup([3,2,1,2,2,3]))
