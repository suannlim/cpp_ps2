#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:18:56 2020

@author: suannlim
"""

#Q1: Write a program that explicitly multiplies 2 matrices C= AB 

def multiply(A,B):
    # checks to see if matrices can be multiplied
    if len(A[0])!= len(B):
        print("These matrices cannot be multiplied!")
        return None
    else:
        # creates empty matrix
        C=[[0 for x in range(len(A[0]))] for y in range(len(B))]
        # nested for loop that will iterate through input matrices
        for i in range(len(A)):
            for j in range(len(B[0])):
                # Get ready to store C value
                answer = 0
                # Loop through A's row and B's column, multiplying their 
                # respective values and outputting the sum
                for k in range(len(B)):
                    answer = answer + A[i][k]*B[k][j]
                C[i][j] = answer
        print(C)
        return C
    
    


    

