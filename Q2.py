# -*- coding: utf-8 -*-

#Q2: Implement a way to solve for x in Ax=B by using Gaussian elimination
# or Gauss Jordan Elimnation


def gaus_elim(A,B):
    #for loop to form the Gaussian Matrix
    for i in range(len(B)):
        A[i].append(B[i])
   # print(A)
    new_matrix=[[0 for x in range(len(A[0]))] for y in range(len(A))]
    new_matrix[0] = A[0]
    #print(new_matrix)
    #first we focus on eliminating x in the first collumn except for first row
    
    
    for smat in range(len(A)):
        for j in range(smat, len(A)):
            if j<(len(A)-1):
                for k in range(smat, len(A[0])):
                    ratio=A[j+1][smat]/A[smat][smat]
                    print(ratio)
                    new_row=A[j+1][k] - (ratio*A[smat][k])
                    #print(new_row)
                    new_matrix[j+1][k]=new_row
                    A[j+1][k]=new_row
                    print(new_matrix)
                    
    
    print(new_matrix)
    return(new_matrix)
    
                
                
        
  
        
        
        
        
        
        
      
    
A=[[1,2],[3,1],[7,1],[8,1]]
B=[3,4,5,6]

gaus_elim(A,B)
    