rows = int(input("Enter the number of rows: "))  
# Outer loop will print number of rows  
for i in range(rows+1):  
    # Inner loop will print the value of i after each iteration  
    for j in range(i):  
        print(i, end=" ")  # print number  
    # line after each row to display pattern correctly  
    print(" ")
  
