import json
class member_info:
    def get_read_file(self):
        try:
            with open("member_data","r") as f:
                member_info=json.load(f)
                return member_info
        except (FileNotFoundError, json.JSONDecodeError):
             print("file is not created!!")
    def get_int(self,message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Error! Enter numbers only!!")
    def add_member(self):
        try:
            with open("member_data","r") as f:
                member_info=json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            member_info={}
        while True:
            found=False
            member_id=self.get_int("Enter member id:")
            for id in member_info.keys():
                if(int(id)==member_id):
                    found=True
                    print(f"{member_id} id is already exsit please make new one!!")
            if found==False:
                break
        member_name=input("Enter name of member:")
        member_info[member_id]={"name":member_name}
        with open("member_data","w") as f:
            json.dump(member_info,f,indent=2)
            print("Data is successfully added!!") 
    def view_member(self):
                member_info=self.get_read_file()
                if str(member_info)=="{}":
                    print("file is empty!!")
                for key in member_info.keys():
                    print(f"member Id={key}:{member_info.get(key)}")
    def search_member(self):             
                member_info=self.get_read_file()
                if str(member_info)=="{}":
                    print("file is empty!!")
                member_id=self.get_int("Enter member id:")
                for key in member_info.keys():
                    if(member_id==int(key)):
                        print(f"member id={key}:{member_info.get(key)}")
    def delete_member(self):
        print("1.Delete all member record")
        print("2.Delete specific member record")
        choice=input("Enter your choice:")
        if(choice=="1"):
            with open("member_data","w")as f:
                f.write("{}")
                print("All member record was deleted!!")
        elif(choice=="2"):
                with open("member_data","r+")as f:
                    data=json.load(f)
                    if str(data)=="{}":
                        print("file is empty!!")
                    else:
                        id=self.get_int("Enter member id:")
                        for key in list(data.keys()):
                            if int(key)==id:
                                data.pop(id,None)
                                f.seek(0)
                                f.truncate() 
                                json.dump(data,f,indent=2)
                                print(f"id={id} has been delete successfully")
                                return
                        else:
                            print(f"Id={id} didn't exist!!")
                                
        else:
            print("Invalid choice!")
l1=member_info()
is_running=True
while is_running:
    print("1.Add member")
    print("2.View member")
    print("3.Search member")
    print("4.Delete member")
    print("5.Quit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:l1.add_member()
        case 2:l1.view_member()
        case 3:l1.search_member()
        case 4:l1.delete_member()
        case 5:
            is_running=False