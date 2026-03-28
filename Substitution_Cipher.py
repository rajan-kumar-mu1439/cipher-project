import string   # Used to get predefined alphabets (A-Z)


# Function to encrypt text using substitution cipher
def substitution_encrypt(text, key_map):
    result = ""   # Stores encrypted output
    
    # Loop through each character in the input text
    for char in text:
        
        # Check if character is alphabet
        if char.isalpha():
            
            # If character is uppercase
            if char.isupper():
                # Directly replace using key_map
                result += key_map[char]
            
            else:
                # Convert to uppercase → map → convert back to lowercase
                result += key_map[char.upper()].lower()
        
        else:
            # Non-alphabet characters remain unchanged
            result += char

    # Return encrypted string
    return result


# Function to decrypt text
def substitution_decrypt(text, key_map):
    
    # Reverse the key_map:
    # Example: {'A':'Q'} becomes {'Q':'A'}
    reverse_map = {v: k for k, v in key_map.items()}
    
    result = ""   # Stores decrypted output

    # Loop through each character
    for char in text:
        
        # Check if alphabet
        if char.isalpha():
            
            # If uppercase
            if char.isupper():
                # Use reverse_map to get original character
                result += reverse_map[char]
            
            else:
                # If lowercase:
                # Convert → decrypt → convert back
                result += reverse_map[char.upper()].lower()
        
        else:
            # Keep symbols, spaces unchanged
            result += char

    # Return decrypted string
    return result


# Create standard alphabet A-Z
alphabet = string.ascii_uppercase  

# - All 26 letters must be present
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Create mapping dictionary:
# Example: {'A':'Q', 'B':'W', 'C':'E', ...}
key_map = dict(zip(alphabet, key))


# Input text
text = input("Enter your password :")


# Encrypt text
encrypted = substitution_encrypt(text, key_map)


# Decrypt text
decrypted = substitution_decrypt(encrypted, key_map)


# Output results
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)