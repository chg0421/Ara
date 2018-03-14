import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt


class ChartMaker:

    #  Renee
    @staticmethod
    def make_bar_average(ave_sales, ave_salary):

        objects = ('Average Sales', 'Average Salary')
        y_pos = len(objects)
        performance = [ave_sales, ave_salary]
        if ave_sales < 0 or ave_salary < 0:
            raise ValueError("wrong value of the input")
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Number')
        plt.title('Average Sales and Average Salary')
        plt.show()

    #  Chamila
    def make_pie(self, employee_list):
        labels = [emp[0] for emp in employee_list]
        sales = [emp[5] for emp in employee_list]

        plt.pie(sales, labels=labels, shadow=True)
        plt.axis('equal')
        plt.show()

        #emp_data = {
        #    'data': [{'labels': [emp[0] for emp in employee_list],
        #              'values': [emp[5] for emp in employee_list],
        #              'type': 'pie'}],
        #    'layout': {
        #        'title': '---Employees salary details---'}
        #}
        #pf.plot(emp_data)

    #Chami
    def make_line(self, employee_list):
        # our X values:
        emp_id = [emp[0] for emp in employee_list]
        # our Y values:
        sales_values = [emp[3] for emp in employee_list]
        plt.plot(emp_id, sales_values, '-b', label="A simple line")
        plt.legend(loc='upper left')
        plt.title("Sales Value for Employees")
        plt.xlabel('Employee ID')
        plt.ylabel('Sales')
        plt.show()

        plt.plot(emp_id, sales_values, 'bo')
        plt.show()

    #  Jonno
    def make_bar_sales(self, list):
        objects = [item[0] for item in list]
        sales = [item[3] for item in list]
        y_pos = len(objects)

        plt.bar(y_pos, sales, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel("Sales")
        plt.xlabel("Salesperson by ID")
        plt.title("Sales By Salesperson")

        plt.show()




