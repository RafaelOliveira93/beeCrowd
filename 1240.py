# -*- coding: utf-8 -*-

N = int(input())

for _ in range(N):
    A,B = [x for x in input().strip().split(' ')]
    dif = len(A) - len(B)
    encaixa = True
    
    if dif < 0:
        print("nao encaixa")
        continue

    for i in range(len(B)):
        if A[dif + i] != B[i]:
            encaixa = False
            break
        
    if encaixa == True:
        print("encaixa")
    else:
        print("nao encaixa")
