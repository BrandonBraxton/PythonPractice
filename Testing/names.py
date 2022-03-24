from name_function import get_formatted_name

print("Enter 'q' to quit at any time.")

while True:
    first = input("\nPlease enter a first name: ")
    if first == 'q':
        break;
    last = input("Please enter a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    
    print("\tNeatly formatted named: " + formatted_name)
    