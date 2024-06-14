import sqlite3, datetime, pytz


class Attendance:
    def __init__(self):
        self.conn = sqlite3.connect('/storage/emulated/0/My_Python_Files/SQL_Files/Databases/attendance.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
        
        
    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students_table (
                                student_id TEXT,
                                first_name TEXT,
                                last_name TEXT,
                                sex TEXT,
                                age  TEXT
                                
                                
                             )''')
                        
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS attendance_table (
                                student_id TEXT PRIMARY KEY,
                                name TEXT,
                                attendance TEXT,
                                date TEXT,
                                FOREIGN KEY(student_id) REFERENCES students_table(student_id)
                            )''')
                            
        self.conn.commit()


    def create_account(self, firstName,lastName, age):
        # Insert account into the accounts table
        id = input("Enter your Id: ")
        self.cursor.execute('''INSERT INTO students_table (student_id, first_name, last_name, sex, age)
                               VALUES (?, ?, ?, ?, ?)''', (id, firstName, lastName, sex, age))
        self.conn.commit()
        return account_number
  
    def check_in(self, id):
        date_time = datetime.datetime.now(tz=pytz.UTC)
        time_zone = d_t.astimezone(pytz.timezone('Asia/Manila'))
        current_time = datetime.time(dt.hour, dt.minute)
        start_time = datetime.time(6,30)
        if current_time >= start_time:
            print(f"Today: {ph_tz}")
            print("Present ")     
       else:
            print(f"Today: {ph_tz}")
            print("Absent ")
        
        

