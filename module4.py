# Step 1: Read N (positive integer)
N = int(input("Enter the number of elements (N): "))

# Step 2: Read N numbers one by one
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Step 3: Read the value X
X = int(input("Enter the number to search for (X): "))

# Step 4: Find and output the index or -1 if not found
if X in numbers:
    print(numbers.index(X) + 1)  # Adding 1 to make it 1-based index
else:
    print(-1)