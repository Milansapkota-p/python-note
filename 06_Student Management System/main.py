import json
class student_info:
    def __init__(self):
        pass
    def update_student(self):
        #learn about Exception handling previously program give error when there is 
        # file didn’t exist
        try:
            with open("student_info","r")as f:
                std_info=json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            std_info = {}
        std_id=input("Enter student id: ")
        for key in std_info.keys():
            if key==std_id:
                print(f"Id {key} is already exist!! please make different one")
                return
        std_name=input("Enter student name: ")
        std_age=input("Enter student age: ")
        std_class=input("Enter student class: ")
        std_rollNum=input("Enter student roll number: ")
        std_gender=input("Enter student gender: ")
        std_info[std_id]=["name:"+std_name,"age:"+std_age,"Roll no:"+std_rollNum,
                          "Gender:"+std_gender,"class:"+std_class]
        with open("student_info","w") as f:
            json.dump(std_info,f,indent=2)
        print("Data added successfully")
    def show_Details(self):
        try:
            with open("student_info","r")as f:
                data=json.load(f)
                for key in data.keys():
                    print(f"Id={key}:{data.get(key)}")
                # print(data)
        except (FileNotFoundError, json.JSONDecodeError):
            print("File is not created ")
    def search_Std(self):
        id=input("Enter your id:")
        with open("student_info","r")as f:
            data=json.load(f)
            for i in range(len(data)):
                if(list(data.keys())[i]==id):
                    print(list(data.values())[i])
    def delete_std(self):
        print("1.Delete all student record")
        print("2.Delete specific student record")
        choice=input("Enter your choice:")
        if(choice=="1"):
            with open("student_info","w")as f:
                return
        elif(choice=="2"):
            id=input("Enter student id:")
            with open("student_info","r+")as f:
                data=json.load(f)
                for key in data.keys():
                    if key==id:
                        data.pop(id,None)
                        f.seek(0)    # move the file pointer to the beginning
                        f.truncate() # cuts from current pointer position
                        json.dump(data,f,indent=2)
                        print(f"id={id} has been delete successfully")
                    else:
                        print(f"Id={id} didn't exist!!")
                        return
        else:
            print("Invalid choice!")

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