# This is the example of print simple pyramid pattern  
n = int(input("Enter the number of rows"))  
# outer loop to handle number of rows  
for i in range(0, n):  
    # inner loop to handle number of columns  
    # values is changing according to outer loop  
        for j in range(0, i + 1):  
            # printing stars  
            print("* ", end="")       
  
        # ending line after each row  
        print()





rows = int(input("Enter the number of rows: "))  
# Downward loop for inverse loop  
for i in range(rows, 0, -1):  
    n = i   # assign value to n of i after each iteration  
    for j in range(0, i):  
        # print reduced value in each new line  
        print(n, end=' ')  
    print("\r")
current_Number = 1  
stop = 2  
rows = 3  # Number of rows to print numbers  
  
for i in range(rows):  
    for j in range(1, stop):  
        print(current_Number, end=' ')  
        current_Number += 1  
    print("")  
    stop += 2
rows = int(input("Enter the number of rows: "))  
for i in range(0, rows + 1):  
    # inner loop for decrement in i values  
    for j in range(rows - i, 0, -1):  
        print(j, end=' ')  
    print()
rows = int(input("Enter the number of rows: "))  
i = 1  
# outer file loop to print number of rows  
while i <= rows:  
    j = 1  
    # Check the column after each iteration  
    while j <= i:  
        # print odd values  
        print((i * 2 - 1), end=" ")  
        j = j + 1  
    i = i + 1  
    print()
rows = int(input("Enter the number of rows: "))  
for i in range(1, rows + 1):  
    for j in range(1, rows + 1):  
        # Check condition if value of j is smaller or equal than  
        # the j then print i otherwise print j  
        if j <= i:  
            print(i, end=' ')  
        else:  
            print(j, end=' ')  
    print()
rows = int(input("Enter the number of rows: "))  
for i in range(1, rows):  
    for j in range(1, i + 1):  
        # It prints multiplication or row and column  
        print(i * j, end='  ')  
    print()  
