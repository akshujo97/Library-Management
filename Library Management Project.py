class Library:

    def __init__(self,listofbooks,library_name):
        self.listofbooks = listofbooks
        self.library_name = library_name


    def Displaybook(self):
        list2.sort()
        list3.sort()
        return f"Library: {list2}\nPeople with books: {dict1}\nAvailable Books: {list3}"
    def Addbook(self):
        print(self.listofbooks)
        list2 = self.listofbooks
        print("Press 1 to add and 2 to remove")
        choice = int(input())
        if choice == 1:
            print("Please input the book you wanna add")
            addbook = input()
            list2.insert(len(self.listofbooks),addbook)
            list3.insert(len(self.listofbooks), addbook)
            return f"Successfully added {addbook}"
        elif choice == 2:
            print("Please input the book you wanna remove")
            removebook = input()
            list2.remove(removebook)
            list3.remove(removebook)
            return f"Successfully removed {removebook}"

        else:
            print("Wrong input")
        pass
    def Returnbook(self):
        print(f"Library: {list2}")
        print(f"Lended Books: {listofrentedbooks}")
        print("Please specify book name")
        retbook = input()
        print()
        if retbook in dict1:
            del dict1[retbook]
            listofrentedbooks.remove(retbook)
            list3.insert(len(list3),retbook)
            return f"Successfully returned {retbook}. Thanks for shopping :)"
        elif retbook in self.listofbooks:
            print(f"The {retbook} is already available. Do you wanna lend it instead?")
            choice  = input()
            if choice.lower() == 'y':
                return self.Lendbook()
            elif choice.lower() == 'n':
                print(f"Happy shopping")
            else:
                return f"Invalid inp"
        else:
            return "Wrong input"

    def Lendbook(self):
        list2.sort()
        list3.sort()
        print(f"Library: {list2}")
        print(f"Available Books: {list3}")
        print("Please specify book name")
        book_name = input()
        if book_name in dict1:
            return f"Sorry the book is with {dict1[book_name]}"
        elif book_name in self.listofbooks:
            print("Available")
            person_name = input("Please give your name")
            dict1[book_name] = person_name
            listofrentedbooks.insert(len(listofrentedbooks),book_name)
            list3.remove(book_name)
            return f"Congo {person_name}"
        else:
            return f"Sorry the book is not available"



if __name__ == '__main__':
    AkshayLibrary = Library(["Eragon","Eragon 2","Joey's bizzare adventures","Hajime no ippo",
                             "Fifty shades of grey"],"Akshay Library")

    dict1 = {}
    listofrentedbooks = []
    list2 = AkshayLibrary.listofbooks
    list2.sort()
    list3 = list2.copy()
    list3.sort()
    choice = 'y'

    print(f"Welcome to {AkshayLibrary.library_name}. Select from wide range of books")
    while True:
        if choice == 'y':
            dict2 = {1:"Display Book",2:"Add Book",3:"Return Book",4:"Lend Book"}
            for k,v in dict2.items():
                print(f"Press {k} for {v}")
            inp = int(input())
            if inp == 1:
                print(AkshayLibrary.Displaybook())

            elif inp == 2:
                print(AkshayLibrary.Addbook())

            elif inp == 3:
                print(AkshayLibrary.Returnbook())

            elif inp == 4:
                print(AkshayLibrary.Lendbook())

        elif choice == 'n':
            if len(listofrentedbooks) != 0:
                print("Please return all books")
            else:
                print("Thanks for visiting")
                break

        else:
            print("Invalid input. Please try again")

        choice = input("Do you wanna try again?")