# class (반복되는 메소드와 변수를 미리 정해놓은 틀, 설계도)

class Book:                                # author, title, publisher, date 는 클래스 속성
    author = ""
    title = ""
    publisher = ""
    date = ""

book = Book()                         # book 은 인스턴스
book.author = "Susan"
book.title = "Python"
print(book.author)
print(book.title)

# ----------------------------------------------------

class Book:                                   
    author = ""
    title = ""
    publisher = ""
    date = ""

    def print_info(self):                          # self 는 class Book 으로 만들어진 인스턴스 그 자체를 의미
        print("Author : ", self.author)            # print_info는 메소드
        print("Title : ", self.title)
        print("Publisher : ", self.publisher)
        print("Date : ", self.date)

book = Book()                         
book.author = "Susan1"                # book.any - 인스턴스 속성
book.title = "Python1"
book.print_info()

Book.author = "Susan"                # Book.any - 클래스 속성
Book.title = "Python"
book.print_info()

# ----------------------------------------------------

class Book():
    count = 0

    def __init__(self, author, title, publisher, date):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date
        Book.count += 1

    def print_info(self):                         
        print("Author : ", self.author)            
        print("Title : ", self.title)
        print("Publisher : ", self.publisher)
        print("Date : ", self.date)

b2 = Book("Suan", "Python", "colab", "2020")
b2.print_info()
print("책 수량 : ", Book.count)

# ----------------------------------------------------
# 매직 메소드 __str__
class Book():

    def __init__(self, author, title, publisher, date):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date

    def __str__(self):                         
        return ("Author : "+ self.author+ "\nTitle : "+ self.title+ "\nPublisher : "+ self.publisher+ "\nDate : "+ self.date)

b2 = Book("Suan", "Python", "colab", "2020")
print(b2)

# ----------------------------------------------------
class SuperClass():
    def method(self):
        pass

class SubClass1(SuperClass):
    def method(self):
        print("Method Overriding")

class SubClass2(SuperClass):
        pass

sub1 = SubClass1()
sub1.method()
sub2 = SubClass2()
sub2.method()