import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x)) # numpy.ndarray

#산술연산

y = np.array([2.0,4.0,6.0])
print(x+y)
print(x-y)
print(x*y)
print(x/y)

# N차원 배열
A = np.array([[1,2],[3,4]])
print(A)
print(A.shape) # 행렬의 형상
print(A.dtype) # 원소의 자료형

# 브로드캐스트
B = np.array([10,20])
print(A*B)

# 원소 접근

print(A[0])
for row in A:
    print(row)