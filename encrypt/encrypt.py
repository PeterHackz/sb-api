import requests
# key is the password that you are using to encrypt the string, you need it to derypt it
encrypt_me = "your string to encrypt here"
encrypted_string = requests.post("https://sb-apis.repl.co/sb9838/tools/encrypt", encrypt_me, headers={
"key": "key_here"
 }).text
print(encrypted_string)
