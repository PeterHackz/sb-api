import requests
# key is the password that you used to encrypt the string
decrypt_me = "your string to decrypt here"
decrypted_string = requests.post("https://sb-apis.repl.co/sb9838/tools/decrypt", decrypt_me, headers={
"key": "key_here"
 }).text
print(decrypted_string)
