import sqlite3
from sqlite3 import Error


class EmployeeDatabase:

    #  jonno
    def create_connection(self, db_file):
        """Create a database connection to SQLite Database """
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            print("Database created")
            self.drop_employee_table(conn)
            self.create_employee_table(conn)
        except Error as e:
            print(e)
        except NameError:
            print("Incorrect file format for db name")
        finally:
            conn.close()

    #  jonno
    def drop_employee_table(self, conn):
        conn.execute('''DROP TABLE IF EXISTS EMPLOYEES''')
        print("Table Dropped")

    def create_employee_table(self, conn):
        try:
            conn.execute('''CREATE TABLE EMPLOYEES
            (EMPID TEXT PRIMARY KEY,
            GENDER CHAR(1),
            AGE INT,
            SALES INT,
            BMI TEXT,
            SALARY INT,
            DOB TEXT);''')
            print("Employee Table created successfully")
        except Error as e:
            print(e)
        finally:
            conn.close()

    #  jonno
    def insert_employee(self, item):
        """insert an employee into employee table"""
        try:
            conn = sqlite3.connect('test2.db')
            conn.execute("INSERT INTO EMPLOYEES "
                         "(EMPID, GENDER, AGE, SALES, BMI, SALARY, DOB)"
                         "VALUES (?, ?, ?, ?, ?, ?, ?)",
                         (item[0], item[1], item[2], item[3],
                          item[4], item[5], item[6]))
            print("item added successfully")
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

    # renee
    @staticmethod
    def get_all_employee():
        """
        Query all rows in the employee table
        :param conn: the Connection object
        :return:
        """
        conn = sqlite3.connect('test2.db')
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM EMPLOYEES")
            rows = cur.fetchall()
            employee_list = []
            for row in rows:
                employee_list.append(row)
            return employee_list
        except (sqlite3.ProgrammingError, sqlite3.Error) as e:
            print("TABLE EMPLOYEES not found")
        except sqlite3.Error as er:
            print("Database error: ", er.message)
        except Exception as e:
            print(e)

    # Renee
    @staticmethod
    def get_ave_salary():

        conn = sqlite3.connect('test2.db')
        cur = conn.cursor()
        try:
            cur.execute("SELECT AVG(SALARY) FROM EMPLOYEES")
            ave_salary = cur.fetchone()[0]
            if ave_salary < 0:
                raise ValueError("wrong value")
            else:
                return ave_salary
        except (sqlite3.ProgrammingError, sqlite3.Error) as e:
            print("TABLE EMPLOYEES not found")
        except sqlite3.Error as er:
            print("Database error: ", er.message)
        except Exception as e:
            print(e)
        finally:
            if conn:
                conn.close()

    # Chami
    def get_ave_sales(self):

        conn = sqlite3.connect('test2.db')
        cur = conn.cursor()
        cur.execute("SELECT avg(sales) FROM EMPLOYEES")
        ave_sales = round(cur.fetchone()[0], 2)
        return ave_sales


db = EmployeeDatabase()
db.create_connection("test2.db")
