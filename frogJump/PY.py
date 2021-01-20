import math

def solution(X,Y,D):
    return math.ceil((Y-X)/D);

X = 11
Y = 150
D = 100

print(solution(X,Y,D))