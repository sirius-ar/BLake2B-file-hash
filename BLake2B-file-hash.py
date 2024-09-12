import hashlib
import os

def generate_blake2b_hash(file_path):
    try:
        blake2b = hashlib.blake2b()
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                blake2b.update(chunk)
        return blake2b.hexdigest()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    print("=== BLAKE2b File Hashing Tool ===")
    file_path = input("Enter the file path: ")
    
    # Check if the file exists before proceeding
    if os.path.isfile(file_path):
        print("Generating BLAKE2b hash, please wait...")
        file_hash = generate_blake2b_hash(file_path)
        if file_hash:
            print(f"Success! The BLAKE2b hash for the file '{file_path}' is:\n{file_hash}")
    else:
        print(f"Error: The file '{file_path}' does not exist. Please check the path and try again.")

if __name__ == "__main__":
    main()
