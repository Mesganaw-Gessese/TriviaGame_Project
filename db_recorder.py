import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-F9278QO7;'
                      'Database=model;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
def scoreRecorder():
    id = int(input('Please enter your Id: '))
    name = input("Please enter your full name: ")
    score = int(input("Please enter your score: "))
    date = input("please enter the date you have played: ")
    cursor.execute("INSERT INTO Triva_Game (id, name, score, date) VALUES (?, ?, ?, ?) ", (id, name, score, date))
    conn.commit()

