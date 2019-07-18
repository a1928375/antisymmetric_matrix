def antisymmetric(A):
    
    i=0
    while i<len(A):
        j=0
        L=[]
        while j<len(A):
            L.append(A[j][i]*(-1))
            j=j+1
        
        if L==A[i]:
                i=i+1
        else:
                return False
    return True 


print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
