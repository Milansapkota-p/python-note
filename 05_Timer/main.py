#Bulding the simple logic of timer using time module
import time
user_input=int(input("Enter time in second: "))
for s in range(user_input,0,-1):
    time.sleep(1)
    second=s%60
    minutes=(int(s/60))%60
    hours=int(s/3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
print("Time's up!")