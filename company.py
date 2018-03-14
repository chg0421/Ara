from employee import Employee


class Company:
    employee_register = []
    employee_count = 0

    def add_employee(self, empid, gender, age, sales, bmi, salary, birthday):
        emp = Employee(empid, gender, age, sales, bmi, salary, birthday)
        self.employee_register.append(emp)

    def get_all_employee(self):
        return self.employee_register

    # renee
    def get_ave_sales(self, employee_register):
        sum_sales = sum(employee_register[3])
        ave_sales = sum_sales / len(employee_register)
        return ave_sales

    def get_ave_salary(self, employee_register):
        sum_salary = sum(employee_register[5])
        ave_salary = sum_salary / len(employee_register)
        return ave_salary

    def get_ave_age(self, employee_register):
        sum_age = sum(employee_register[2])
        ave_age = sum_age / len(employee_register)
        return ave_age

    list = [("EMP001", "M", 23, 201, "Normal", 200, "01/08/1991"),
            ("EMP002", "M", 23, 201, "Normal", 200, "01/08/1991")]
    db = EmployeeDatabase()
    db.create_connection("test2.db")
    for item in list:
        db.insert_employee(item)
    db.get_all_employee()
    db.get_ave_sales()

#v = Validator()
#for item in content:
#    v.validate_all(item)
#f.save_excel(content)




def get_employees():
    the_list = company.get_all_employee()
    for x in the_list:
        info = x.get_all_data()
        for i in info:
            View.display(i)


def add_employee():
    id = View.input("Enter Employee ID ")
    gender = View.input("Enter Employee gender ")
    age = int(View.input("Enter Employee age "))
    sales = int(View.input("Enter Employee sales "))
    bmi = View.input("Enter Employee bmi ")
    salary = int(View.input("Enter Employee salary "))
    birthday = View.input("Enter Employee Bday ")
    company.add_employee(id, gender, age, sales, bmi, salary, birthday)

#db = EmployeeDatabase()
#db.create_connection("test2.db")
#v = Validator()
#f = Filer()
#list_check = f.read_csv()
#for item in list_check:
#    v.validate_all(item)
#    db.insert_employee(item)
c = Controller()

