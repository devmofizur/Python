# Exception is used for handling errors and keep executing code

class Accident(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg
    def print_exception(self):
        print("User defined exception: ", self.msg)

try:
    raise Accident('Car crash')
except Accident as e:
    e.print_exception()

# Example

def process_file():
    try: 
        f = open("data.txt")
        x = 10/0
        
    except FileNotFoundError as e:
        print("File missing")
    except ZeroDivisionError as z:
        print ("Dividing by zero is not possible")
    finally:
        f.close()
        print("You forgot to close file but I closed it.")
        

process_file()