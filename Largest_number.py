def largest_number(A):
    A = [str(num) for num in A]
    A.sort(key=lambda x: x * 3, reverse=True)
    if A[0] == '0':
        return '0'

    return ''.join(A)

A = list(map(int,input().split()))
print(largest_number(A))

"""
Input 1:
A = [3, 30, 34, 5, 9]

Input 2:
A = [2, 3, 9, 0]


Output 1:
"9534330"

Output 2:
"9320"

"""
