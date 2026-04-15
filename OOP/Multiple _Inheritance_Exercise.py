class Teacher:
    def __init__(self) -> None:
        print("I am teacher")
        super().__init__()


class Youtuber:
    def __init__(self) -> None:
        print("I am YouTuber")

class Student(Teacher,Youtuber):
    def __init__(self) -> None:
        super().__init__()

s = Student()