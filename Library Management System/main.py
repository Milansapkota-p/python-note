import json
class library_info:
    def get_read_file(self):
        try:
            with open("library_data","r") as f:
                lab_info=json.load(f)
                return lab_info
        except (FileNotFoundError, json.JSONDecodeError):
             print("file is not created!!")
    def get_int(self,message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Error! Enter numbers only!!")
    def add_book(self):
        try:
            with open("library_data","r") as f:
                lab_info=json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            lab_info={}
        while True:
            found=False
            book_id=self.get_int("Enter book id:")
            for id in lab_info.keys():
                if(int(id)==book_id):
                    found=True
                    print(f"{book_id} id is already exsit please make new one!!")
            if found==False:
                break
        book_name=input("Enter title of book:")
        author=input(f"Enter author name of {book_name} book:")
        catogory=input(f"Enter catogory of {book_name} book:")
        t_copies=self.get_int(f"Enter total copies of {book_name}:")
        avil_copies=self.get_int(f"Enter total avilable copies:")
        lab_info[book_id]={"book name":book_name,"author":author,"catogory":catogory,
                           "total copies":t_copies,"avilable copies":avil_copies}
        with open("library_data","w") as f:
            json.dump(lab_info,f,indent=2)
            print("Data is successfully added!!") 
    def view_book(self):
                lab_info=self.get_read_file()
                if str(lab_info)=="{}":
                    print("file is empty!!")
                for key in lab_info.keys():
                    print(f"Book Id={key}:{lab_info.get(key)}")
    def search_book(self):             
                lab_info=self.get_read_file()
                if str(lab_info)=="{}":
                    print("file is empty!!")
                book_id=self.get_int("Enter book id:")
                for key in lab_info.keys():
                    if(book_id==int(key)):
                        print(f"Book id={key}:{lab_info.get(key)}")
    def delete_book(self):
        print("1.Delete all labrary record")
        print("2.Delete specific labrary record")
        choice=input("Enter your choice:")
        if(choice=="1"):
            with open("library_data","w")as f:
                f.write("{}")
                print("All library record was deleted!!")
        elif(choice=="2"):
                with open("library_data","r+")as f:
                    data=json.load(f)
                    if str(data)=="{}":
                        print("file is empty!!")
                    else:
                        id=self.get_int("Enter book id:")
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
    def is_book_avilable(self):
        id=self.get_int("Enter book Id :")
        lab_info=self.get_read_file()
        for key in lab_info.keys():
            if(id==int(key)):
                 print("Book is avilable!!")



l1=library_info()
is_running=True
while is_running:
    print("1.Add book")
    print("2.View book")
    print("3.Search book")
    print("4.Delete book")
    print("5.Is book avilable")
    print("6.Quit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:l1.add_book()
        case 2:l1.view_book()
        case 3:l1.search_book()
        case 4:l1.delete_book()
        case 5:l1.is_book_avilable()
        case 6:
            is_running=False