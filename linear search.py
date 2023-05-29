arr = []
j = int(input("Enter array Numbers:"))
for i in range(j):
  arr.insert(i, int(input()))
print("Enter the Number to Search: ")
num = int(input())
for i in range(j):
  if num==arr[i]:
    index = i
    break
print("\nNumber Found at Index Number: ")
print(index)
