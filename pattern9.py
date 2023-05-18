rows = int(input("Enter the number of rows: "))  
k = 0  
# Reversed loop for downward inverted pattern  
for i in range(rows, 0, -1):  
    # Increment in k after each iteration  
    k += 1  
    for j in range(1, i + 1):  
        print(k, end=' ')  
    print()
