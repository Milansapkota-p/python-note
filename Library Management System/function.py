import json
from memberManage import member_info as m
from main import library_info
class function(library_info,m):
    def issue_book(self):
        lab_info=self.get_read_file()
        m_info=m.get_read_file(self)
        if str(lab_info)=="{}":
            print("file is empty!!")
        m_id=self.get_int("Enter your library id:")
        book_id=self.get_int("Enter book id:")
        for key in lab_info.keys():
            id=False
            if(book_id==int(key)):
                id=True
                if(lab_info[str(book_id)] ["avilable copies"])>0:
                    lab_info[str(book_id)] ["avilable copies"]-=1
                    with open("library_data","w") as f:
                        json.dump(lab_info,f,indent=2)
                    try:
                        with open("issued_book","r") as f:
                            issued=json.load(f)
                    except (FileNotFoundError, json.JSONDecodeError):
                        issued={}
                    with open("issued_book","w") as f:
                        issued[str(book_id)]=lab_info[str(book_id)]
                        json.dump(issued,f,indent=2)
                        print(f"{lab_info[str(book_id)]["book name"]} book is issue to {m_info[str(m_id)]["name"]}")
                        break
                else:
                    print(f"{lab_info[str(book_id)]["book name"]} book is already issued")
        if id==False:
                print(f"{book_id} id book  not found!!")
    def return_book(self):
        lab_info=self.get_read_file()
        with open("issued_book","r+")as f:
                    data=json.load(f)
                    if not data:
                        print("There is no issued book!!")
                    else:
                        id=self.get_int("Enter book id:")
                        for key in list(data.keys()):
                            if int(key)==id:
                                if(lab_info[str(id)] ["avilable copies"])>0:
                                    lab_info[str(id)] ["avilable copies"]+=1
                                    with open("library_data","w") as f:
                                        json.dump(lab_info,f,indent=2)
                            with open("issued_book","r+")as f:
                                data.pop(str(id))
                                f.seek(0)
                                f.truncate() 
                                json.dump(data,f,indent=2)
                                print(f"id={id} has been delete successfully")
                                return
                        else:
                            print(f"Id={id} didn't exist!!")                           

f1= function()
is_running=True
while is_running:
        print("1.Issued book")
        print("2.Return book")
        choice=int(input("Enter your choice:"))
        match choice:
            case 1:f1.issue_book()
            case 2:f1.return_book()
            case 3:is_running=False