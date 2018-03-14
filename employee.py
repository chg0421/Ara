class Employee:
    """Base class for all Employees"""

    def __init__(self, empid, gender, age, sales, bmi, salary, birthday):
        self._empid = empid
        self._gender = gender
        self._age = age
        self._sales = sales
        self._bmi = bmi
        self._salary = salary
        self._birthday = birthday

    def get_all_data(self):
        employee_info = [self._empid, self._gender, self._age, self._sales, self._bmi, self._salary, self._birthday]
        return employee_info

