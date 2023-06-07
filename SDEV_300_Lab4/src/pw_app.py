'''Command menu-driven app to generate passwords
and see if they can be cracked'''

import hashlib
# input a message to encode
print("Enter a message to encode: ")
message = input()
# encode it to bytes using UTF-8 encoding
message = message.encode()
# hash with MD5 (very weak)
print("MD5: " + hashlib.md5(message).hexdigest())
print()
# stronger SHA-2 family
print("SHA-256: " + hashlib.sha256(message).hexdigest())
print()
print("SHA-512: " + hashlib.sha512(message).hexdigest())
