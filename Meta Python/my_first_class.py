# Define class MyFirstClass
class MyfirstClass():
    print("Who wrote this?")
    # Define string variable called index
    index = "Author-book"
    # Define function hand_list()
    def hand_list(self, philosofer, book):
        print(MyfirstClass.index)
        # variable + “ wrote the book: ” + variable
        print(philosofer + " wrote the book: " + book)

# Call function handlist()
whodunnit = MyfirstClass()
whodunnit.hand_list("Patrick Roothfus", "Road between desires")
