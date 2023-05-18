# A basic code for matrix input from user

R1 = int(input("Enter the number of rows:"))
C1  = int(input("Enter the number of columns:"))

# Initialize matrix
print("Enter Matrix Elements of A:")
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R1):		 # A for loop for row entries
	a =[]
	for j in range(C1):	 # A for loop for column entries
		a.append(int(input()))
	matrix.append(a)

# For printing the matrix
for i in range(R1):
	for j in range(C1):
		print(matrix[i][j]=x, end = " ")
	print()
R2 = int(input("Enter the number of rows:"))
C2  = int(input("Enter the number of columns:"))

# Initialize matrix
print("Enter Matrix Elements of B:")
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R2):		 # A for loop for row entries
	a =[]
	for j in range(C2):	 # A for loop for column entries
		a.append(int(input()))
	matrix.append(a)

# For printing the matrix
for i in range(R2):
	for j in range(C2):
		print(matrix[i][j]=x, end = " ")
	print()
if(C1==R2): #if no. of columns of matrix A is equal to no. of rows of matrix B
    P=[[0 for i in range(C2)] for j in range(R1)] #initialize product matrix
    for i in range(len(A)):
        for j in range(C2):
            for k in range(len(B)):
                P[i][j]=P[i][j]+(A[i][k]*B[k][j]) #multiplication
    #print the product matrix
    print("Product of Matrices A and B: ")
    for i in range(R1):
        for j in range(C2):
            print(P[i][j],end=" ")
        print()
else: #if no. of columns of matrix A isn't equal to no. of rows of matrix B
    print("Matrix Multiplication is not possible.")


