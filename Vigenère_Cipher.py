# Function to encrypt text using Vigenère Cipher
def vigenere_encrypt(text, key):
    result = ""   # Stores the encrypted output
    
    key = key.lower()   # Convert key to lowercase to simplify shift calculation
    key_index = 0       # Tracks position in the key

    # Loop through each character in the input text
    for char in text:
        
        # Process only alphabet characters
        if char.isalpha():
            
            # Get shift value from key:
            # ord('a') = 97 → so 'a' → 0, 'b' → 1, ..., 'z' → 25
            shift = ord(key[key_index % len(key)]) - 97
            
            # Decide ASCII base depending on uppercase/lowercase
            base = 65 if char.isupper() else 97
           
            # Convert back to character
            result += chr((ord(char) - base + shift) % 26 + base)
            
            # Move to next key character
            key_index += 1
        
        else:
            # Keep non-alphabet characters unchanged (space, symbols, etc.)
            result += char

    # Return encrypted text
    return result


# Function to decrypt text
def vigenere_decrypt(text, key):
    result = ""   # Stores decrypted output
    
    key = key.lower()   # Normalize key
    key_index = 0       # Reset key position

    # Loop through each character
    for char in text:
        
        # Only decrypt alphabet characters
        if char.isalpha():
            
            # Same shift calculation from key
            shift = ord(key[key_index % len(key)]) - 97
            
            # Decide ASCII base
            base = 65 if char.isupper() else 97
            
            # Decryption logic:
            # Same as encryption BUT subtract shift
            result += chr((ord(char) - base - shift) % 26 + base)
            
            # Move key forward
            key_index += 1
        
        else:
            # Keep non-alphabet characters unchanged
            result += char

    # Return decrypted text
    return result


# Example input
text = input("Enter your password :")
key = "abc"

# Encrypt the text using key
encrypted = vigenere_encrypt(text, key)

# Decrypt back using same key
decrypted = vigenere_decrypt(encrypted, key)

# Output results
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)