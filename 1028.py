# -*- coding: utf-8 -*-
N = int(input())
for _ in range(N):
    F1, F2 = [int(x) for x in input().strip().split(' ')]
    if F1 % F2 == 0 or F2 % F1 == 0:
        print(min(F1,F2))
    else:
        MDC = max(F1,F2) % min(F1,F2)
        while F1 % MDC != 0 or F2 % MDC != 0:
            if F1 % MDC != 0:
                MDC = F1 % MDC
            elif F2 % MDC != 0:
                MDC = F2 % MDC
        print(MDC)
