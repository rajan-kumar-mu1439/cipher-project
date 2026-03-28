# Function to encrypt text using Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""   # Empty string to store encrypted result
    
    # Loop through each character in the input text
    for char in text:
        
        # Check if the character is an alphabet (A-Z or a-z)
        if char.isalpha():
            
            # 65 for uppercase letters (A-Z)
            # 97 for lowercase letters (a-z)
            shift_base = 65 if char.isupper() else 97
            
            # chr() converts number back to character
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        
        else:
            # If not a letter (space, number, symbol), keep it unchanged
            result += char

    # Return the final encrypted string
    return result


# Function to decrypt text
def caesar_decrypt(text, shift):
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)


# Take input from user
text = input("Enter your Passwoed :")

# Fixed shift value (can be changed)
shift = 3

# Encrypt the input text
encrypted = caesar_encrypt(text, shift)

# Decrypt the encrypted text
decrypted = caesar_decrypt(encrypted, shift)

# Print results
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)