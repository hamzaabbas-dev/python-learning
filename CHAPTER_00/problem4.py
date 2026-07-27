import os

def print_directory():
    # Get the current working directory
    current_dir = os.getcwd()
    print(f"/ New folder: {current_dir}")

    # List the contents of the directory
    print("\nDirectory Contents:")
    try:
        contents = os.listdir(current_dir)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Directory not found!")

# Call the function
print_directory()