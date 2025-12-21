#Building the logic of data encryption using list
import random
import string

charValue=string.whitespace+string.ascii_letters+string.digits+string.punctuation
str=list(charValue)
char_copy=str.copy()
shuffledChar=random.shuffle(char_copy)
#encryption
encrypt_input=input("Enter any message to encryption: ")
unreadable_text=[]
for el in encrypt_input:
    ind=str.index(el)
    unreadable_text.append(char_copy[ind])
'''implementing .join function which help to
    concatenate element of iterable into single string'''
unreadable="".join(unreadable_text)
'''implementing the f string in code 
    which help to add placeholder of variable'''
print(f"original message: {encrypt_input}")
print(f"your encrypted messange: {unreadable}")

#decryption
decrypt_input=input("Enter any message to decryption: ")
plain_text=[]
for el in unreadable_text:
    ind=char_copy.index(el)
    plain_text.append(str[ind])
readable="".join(plain_text)
print(f"original message: {decrypt_input}")
print(f"your decrypted messange: {readable}")