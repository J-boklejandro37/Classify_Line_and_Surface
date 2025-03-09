def print_unique_chair_numbers():
    # Set to keep track of unique chair numbers
    unique_chair_nums = set()
    
    # Open and read the file
    with open('labels.csv', 'r') as file:
        for line in file:
            # Skip empty lines
            if line.strip() == '':
                continue
                
            # Extract chair number from filename
            if 'chair_' in line:
                # Split by underscore and get the middle number
                parts = line.split('_')
                if len(parts) >= 2:
                    chair_num = parts[1]
                    unique_chair_nums.add(chair_num)
    
    # Print each unique chair number
    for chair_num in sorted(unique_chair_nums, key=int):
        print(chair_num)

    print(f'Total number of chairs: {len(unique_chair_nums)}')

# Run the function
print_unique_chair_numbers()