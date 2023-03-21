from cryptography.fernet import Fernet
'''
# key generation
key = Fernet.generate_key()

# string the key in a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

# opening the key
with open('filekey.key', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open("C:\\Users\\10710516\\OneDrive - LTI\\Desktop\\JBL\\Python_Files\\ConsoleApp\\console.txt", 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open("C:\\Users\\10710516\\OneDrive - LTI\\Desktop\\JBL\\Python_Files\\ConsoleApp\\console.txt", 'wb') as encrypted_file:
	encrypted_file.write(encrypted)
'''

'''
# Decrytion Part
# using the key
with open('filekey.key', 'rb') as filekey:
	key = filekey.read()
fernet = Fernet(key)

# opening the encrypted file
with open("C:\\Users\\10710516\\OneDrive - LTI\\Desktop\\JBL\\Python_Files\\ConsoleApp\\console.txt", 'rb') as enc_file:
	encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open("C:\\Users\\10710516\\OneDrive - LTI\\Desktop\\JBL\\Python_Files\\ConsoleApp\\console.txt", 'wb') as dec_file:
	dec_file.write(decrypted)
'''
