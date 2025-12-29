class library_info:
    def __init__(self):
        pass
    def add_book(self):
        pass
    def view_book(self):
        pass
    def search_book(self):
        pass
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

