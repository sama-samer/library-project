
class book:
    def __init__(self,filename):
        self.filename=filename
        
    def add(self,ID,name,author,num_copies):
        # Check if ID is a number
        if not ID.isdigit()or not num_copies.isdigit():
            print(" ID and number of copies should be a number")
            return
        #checking for repeated ids 
        with open(self.filename,'r')as file:
            for line in file:
                # removing white space,sperate the info in the line,choosing the id
                 ext_ID= line.strip().split(',')[0] 
                 if ext_ID==str(ID):
                    print("error the id is repeated")
                    return
        try:
            with open(self.filename, 'a') as file:
            # Append data to the file
                file.write(f"{ID},{name},{author},{num_copies}\n")
        except FileNotFoundError:
            # If the file doesn't exist, create it and append data
            with open(self.filename, 'w') as file:
                file.write(f"{ID},{name},{author},{num_copies}\n")
        print('the book is added successfully')
        
    def display(self):
        #display all books found
        print("Book ID\t\tBook\t\tAuthor\t\tCopies")
        print("-" * 50) #for the format
        with open(self.filename, 'r') as file:
            for line in file:
                book_data = line.strip().split(',')
                print(f"{book_data[0]}\t\t{book_data[1]}\t\t{book_data[2]}\t\t{book_data[3]}")
                
    def delete(self,ID):
        with open(self.filename,'r')as file:
            lines=file.readlines()
        id_found=False
        with open(self.filename,'w')as file: 
            for line in lines:
                 ext_ID= line.strip().split(',')[0]
                 if ext_ID!=str(ID):
                     #returning the line back to the file
                    file.write(line)
                #in this else if the id matches the line doesn't return back to the file
                 else:
                    id_found=True
            if not id_found:
                print("error the id is not found")
                
    def check(self,iden):
            #check by the id
        ids=False
        with open(self.filename,'r')as file:
            for line in file:
                 data= line.strip().split(',')
                 if data[0]==str(iden):
                     ids=True
                     print('the book is found')
                     print(f"{data[0]}\t\t{data[1]}\t\t{data[2]}\t\t{data[3]}")
                     break
            #check by name if the id is not found 
        if not ids:
            name=False
            with open(self.filename,'r')as file:
                for line in file:
                    data=line.strip().split(',')
                    if data[1].lower()==iden.lower():
                        name=True
                        print('the book is found')
                        print(f"{data[0]}\t\t{data[1]}\t\t{data[2]}\t\t{data[3]}")
                        break
            if not name:
                print("Error: Book not found!")
                
    def update(self,ids):
        #takes the new inputs from the user 
        new_bookname=input('please enter the new book name : ')
        new_author=input('please enter the new author name : ')
        new_num_copies=input('please enter the new number of copies : ')
        found=False
        with open(self.filename,'r')as file:
            lines=file.readlines() #reads all lines in the file and returns them as a list of strings
        with open(self.filename,'w')as file:
            for line in lines:
                ext_ID,name,author,num_copies=line.strip().split(',')
                if ext_ID==str(ids):
                    found=True
                    updatedline=f"{ext_ID},{new_bookname},{new_author},{new_num_copies}\n"
                    file.write(updatedline)
                else:
                    file.write(line)
        if not found:
            print('the book you are searching for is not found')
        print('the book is updated successfully')
        
    # allows you to define code that should only run when the file is executed directly.
if __name__ == "__main__":
     # Provide the same filename every time
    filename = 'books.txt'
    # Create the book object using the same filename
    book = book(filename)
    while True:
# Get input from the user
        user_input = input("1.add book \n 2.display book \n 3.check a particular book \n 4.update book \n 5.delete book \n 6.exit \n")
        if user_input=='1':
            book_id=input('please enter the book id : ')
            book_name=input('please enter the book name : ')
            author=input('please enter the author name : ')
            num_copies=input('please enter the number of copies : ')
            book.add(book_id,book_name,author,num_copies)
            
        elif user_input=='2':
            book.display()
            
        elif user_input=='3':
            identifier=input('please enter the book id or the name to be checked : ')
            book.check(identifier)
            
        elif user_input=='4':
            idy=input('please enter the id of the book you want to update : ')
            book.update(idy)
            
        elif user_input=='5':
            book_id=input('please enter the book id you want to delete : ')
            book.delete(book_id)
            
        elif user_input=='6':
            print('the program will exit')
            break
        
        else:
             print("Invalid input Please enter a valid option")
