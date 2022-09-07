import sys


# A, B = map(int,input().split()) #2가지 수 입력
#
# print(A-B)


A = int(input())


if 90 <= A <= 100:
    print("A")
elif 80 <= A <= 89:
    print("B")
elif 70 <= A <= 79:
    print("C")
elif 60 <= A <= 69:
    print("D")
else:
    print("F")

    from sys import stdin, stdout #(입출력 가속)

    input = stdin.readline
    print = stdout.write