
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-F9278QO7;'
                      'Database=model;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

class Sport():
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-F9278QO7;'
                          'Database=model;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    def sportBrain(self):
        z = cursor.execute("SELECT questions, answers FROM Sport_Questions")
        score = 0
        for i in z:
            print(i[0])
            answer = input("enter your answer: ")
            if answer == i[1]:
              print("correct")
              score = score + 1
            else:
              print("wrong")
        print("you have got ", score, "out of 7")
# x = Sport()
# x.sportBrain()

class Film():
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-F9278QO7;'
                          'Database=model;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    def filmBrain(self):
        y = cursor.execute("SELECT questions, answers FROM Film_Questions")
        score = 0
        for i in y:
            print(i[0])
            answer = input("enter your answer: ")
            if answer == i[1]:
              print("correct")
              score = score + 1
            else:
              print("wrong")
        print("you have got ", score, "out of 6")
# x = Film()
# x.filmBrain()


