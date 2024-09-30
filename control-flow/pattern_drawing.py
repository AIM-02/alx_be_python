# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))
    
# Validate that the input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after finishing the row
        row += 1