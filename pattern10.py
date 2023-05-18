rows = int(input("Enter the number of rows: "))  
# rows value assign to n variable  
n = rows  
# Download reversed loop  
for i in range(rows, 0, -1):  
    for j in range(0, i):  
        # this will print the same number  
        print(n, end=' ')  
    print()  
