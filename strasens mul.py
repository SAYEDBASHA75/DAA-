def strassen_matrix_multiplication(A, B):
    # Unpacking the matrices
    a11, a12 = A[0][0], A[0][1]
    a21, a22 = A[1][0], A[1][1]
    
    b11, b12 = B[0][0], B[0][1]
    b21, b22 = B[1][0], B[1][1]

    # Strassen's products
    P1 = a11 * (b12 - b22)
    P2 = (a11 + a12) * b22
    P3 = (a21 + a22) * b11
    P4 = a22 * (b21 - b11)
    P5 = (a11 + a22) * (b11 + b22)
    P6 = (a12 - a22) * (b21 + b22)
    P7 = (a11 - a21) * (b11 + b12)

    # Calculating the elements of the result matrix C
    c11 = P5 + P4 - P2 + P6
    c12 = P1 + P2
    c21 = P3 + P4
    c22 = P5 + P1 - P3 - P7

    # Result matrix C
    C = [[c11, c12], [c21, c22]] 
    return C

# Test case
A = [[1, 7], [3, 5]]
B = [[6, 8], [4, 2]]
C = strassen_matrix_multiplication(A, B)
print("Resultant Matrix C:")
for row in C:
    print(row)

Output:
Resultant Matrix C:
[34, 22]
[38, 34]
