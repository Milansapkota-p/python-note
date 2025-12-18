import random
import string
StrValue=string.ascii_letters
NumValue=string.digits
punc=string.punctuation
p_len=int(input("Enter password length :"))
CharValue=StrValue+NumValue+punc
password=""
for el in range(p_len):
    password+=(random.choice(CharValue))
print("Your random password is :",password)
