import json
class student_info:
    def __init__(self):
        pass
    def update_student(self):
        std_info={}
        std_id=input("Enter student id: ")
        std_name=input("Enter student name: ")
        std_age=input("Enter student age: ")
        std_class=input("Enter student class: ")
        std_rollNum=input("Enter student roll number: ")
        std_gender=input("Enter student gender: ")
        std_info.update({std_id:[std_name,std_age,std_rollNum,std_gender,std_class]})
        with open("student_info","a") as f:
            json.dump(std_info,f)
    def show_Details(self):
        id=input("Enter your id:")
        with open("student_info","r")as f:
            data=json.load(f)
            for idx in range(len(data)):
                print(type(idx))
                if((list(data.keys())[idx])==id):
                    print(f"{data.get(id)}")
    def search_Std(self):
        pass
    def delete_std(self):
        pass

s1= student_info()
is_running=True
while is_running:
    print("1. Add student")
    print("2. search student")
    print("3. show details")
    print("4. Delete student")
    print("5. Exit")
    user_Choice=(input("Enter your choice:"))
    match user_Choice:
        case "1":
            s1.update_student()
        case "2":
            s1.search_Std()
        case "3":
            s1.show_Details()
        case "4":
            s1.delete_std()
        case "5":
            is_running=False        


       