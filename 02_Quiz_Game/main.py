#Bulding the logic of quiz game.
questions={"1.which keyword is used to define a function in python":"def",
          "2.which of the following is an immutable datatype":"tuple",
          "3.what does len'python' return?" :"6"}
options={"1.which keyword is used to define a function in python":"A.func B.define C.def D.funtion",
         "2.which of the following is an immutable datatype":"A.list B.dictionary C.set D.tuple",
         "3.what does len'python' return?":"A.6 B.5 C.7 D.error"}
score=0
while True:
    for idx in range(len(questions)):
        print(list(questions.keys())[idx])
        print(list(options.values())[idx])
        guess=input("Enter your answer:").lower().strip()
        if(guess==list(questions.values())[idx]):
            print("correct answer!!")
            score+=1
        else:
            print("wrong answer")
            print("correct is :",list(questions.values())[idx])
    print("your score is",score,"/",len(questions))
    break