import json
class library_info:
    def __init__(self):
        pass
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
        try:
            with open("library_data","r") as f:
                lab_info=json.load(f)
                for key in lab_info.keys():
                    print(f"Book Id={key}:{lab_info.get(key)}")
        except (FileNotFoundError, json.JSONDecodeError):
            print("file is not created!!")
    def search_book(self):
        try:
            with open("library_data","r") as f:
                lab_info=json.load(f)
                book_id=self.get_int("Enter book id:")
                for key in lab_info.keys():
                    if(book_id==int(key)):
                        print(f"Book id={key}:{lab_info.get(key)}")
        except (FileNotFoundError, json.JSONDecodeError):
            print("file is not created!!")
    def update_book(self):
        pass
    def delete_book(self):
        pass
    def is_bool_avilable(self):
        pass

l1=library_info()
is_running=True
while is_running:
    print("1.Add book")
    print("2.View book")
    print("3.Search book")
    print("4.Update book")
    print("5.Delete book")
    print("6.Is book avilable")
    print("7.Quit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:l1.add_book()
        case 2:l1.view_book()
        case 3:l1.search_book()
        case 4:l1.update_book()
        case 5:l1.delete_book()
        case 6:l1.is_bool_avilable()
        case 7:
            is_running=False

