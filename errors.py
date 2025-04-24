rows = int(input("Enter the number of rows: "))

# Initialize row counter
i = 0

# Outer while loop for rows
while i < rows:
    # Initialize column counter
    j = 0
    # Inner while loop for columns
    while j < rows:
        # Use if condition to decide whether to print the alphabet or not
        if j <= i:
            print(chr(65 + j), end=" ")
        j += 1  # Increment column counter
    print()  # Move to the next line after each row
    i += 1  # Increment row counter