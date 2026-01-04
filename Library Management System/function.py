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
            if(book_id==int(key)):
                if(lab_info[str(book_id)] ["total copies"])>0:
                    lab_info[str(book_id)] ["total copies"]-=1
                    with open("library_data","w") as f:
                        json.dump(lab_info,f,indent=2)
                        print(f"{lab_info[str(book_id)]["book name"]} book is issue to {m_info[str(m_id)]["name"]}")
                else:
                    print("all book is already issued")

f1= function()
f1.issue_book()