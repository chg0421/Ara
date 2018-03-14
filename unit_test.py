import unittest
from validator import Validator
from filer import Filer
from controller import Controller
from employee_database import EmployeeDatabase
from employee import Employee
import os


class UnitTestValidate(unittest.TestCase):
    # Renees
    def test_validate_empid_is_true(self):
        v = Validator()
        result = v.validate_empid("A002")
        self.assertTrue(result, 'valid employee id')

    def test_validate_empid_too_long_is_false(self):
        v = Validator()
        result = v.validate_empid("A0001")
        self.assertFalse(result, 'invalid employee id')

    def test_validate_empid_num_only_is_false(self):
        v = Validator()
        result = v.validate_empid("0001")
        self.assertFalse(result, 'valid employee id')

    def test_validate_empid_no_num_is_false(self):
        v = Validator()
        result = v.validate_empid("AAAA")
        self.assertFalse(result, 'invalid employee id')

    def test_validate_empid_low_case_is_false(self):
        v = Validator()
        result = v.validate_empid("a001")
        self.assertFalse(result, 'invalid employee id')

    def test_validate_empid_is_false(self):
        result = Validator.validate_empid("A02")
        self.assertFalse(result, 'invalid employee id')

    def test_validate_gender_is_true(self):
        """
        Test the validate gender function
        """
        result = Validator.validate_gender("F")
        self.assertTrue(result, 'valid GENDER')

    def test_validate_gender_with_lowcase_is_true(self):
        """
        Test the validate gender function
        """
        result = Validator.validate_gender("f")
        self.assertTrue(result, 'valid GENDER')

    def test_validate_gender_with_long_input_is_true(self):
        """
        Test the validate gender function
        """
        result = Validator.validate_gender("Female")
        self.assertFalse(result, 'invalid GENDER')

    def test_validate_gender_with_upper_only_is_true(self):
        """
        Test the validate gender function
        """
        result = Validator.validate_gender("F")
        self.assertTrue(result, 'valid GENDER')

    def test_validate_gender_is_false(self):
        """
        Test the validate gender function
        """
        result = Validator.validate_gender("E")
        self.assertFalse(result, 'invalid GENDER')

    def test_read_file_from_csv(self):
        f = Filer()
        result = f.read_csv("test_renee.csv")
        expected = [['EMPID', 'GENDER', 'AGE', 'SALES', 'BMI',
                     'SALARY', 'BIRTHDAY'],
                    ['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991'],
                    ['A002', 'F', '26', '300', 'Normal', '30', '09-10-1991']]
        self.assertEqual(expected, result, "didnt read file correctly")

    def test_read_not_found_csv_exception(self):
        f = Filer()
        with self.assertRaises(FileNotFoundError) as context:
            f.read_csv('unfound.csv')
            self.assertTrue('No such file or directory')
        # self.assertRaises(FileNotFoundError, f.read_csv('unfound.csv'))

    def test_os_error_read_csv_exception(self):
        f = Filer()
        self.assertRaises(TypeError, f.read_csv('test2.db'))

    def test_read_unfound_csv_exception(self):
        f = Filer()
        self.assertRaises(FileNotFoundError, f.read_csv('#####.csv'))

    def test_can_not_open_csv_general_exception(self):
        f = Filer()
        self.assertRaises(Exception, f.read_csv('test'))

    def test_name_error_save_cvs_exception(self):
        f = Filer()
        self.assertRaises(NameError, f.save_csv('#####.csv', [1, 2, 3]))

    def test_can_not_save_csv_file_exist_error_exception(self):
        f = Filer()
        ans = f.save_csv('test_renee.csv', [1, 2, 3])
        self.assertRaises(FileExistsError, ans)

    def test_can_not_save_csv_general_exception(self):
        f = Filer()
        self.assertRaises(Exception, f.save_csv('test', [1, 2, 3]))

    def test_employee_id(self):
        e = Employee('A001', 'M', '26', '200', 'Normal', '20', '08-10-1991')
        expected = 'A001'
        self.assertEqual(expected, e._empid)

    def test_employee_gender(self):
        e = Employee('A001', 'M', '26', '200', 'Normal', '20', '08-10-1991')
        expected = 'M'
        self.assertEqual(expected, e._gender)

    def test_employee_age(self):
        e = Employee('A001', 'M', '26', '200', 'Normal', '20', '08-10-1991')
        expected = '26'
        self.assertEqual(expected, e._age)

    # Jono's
    # Validator Tests
    def test_validate_salary_is_true(self):
        """
        Test the validate salary function
        :return: True
        """
        v = Validator()
        result = v.validate_salary("20")
        self.assertTrue(result, 'valid Salary')

        def test_validate_salary_is_true_3_digit(self):
            """
            Test the validate salary function
            :return: True
            """
            v = Validator()
            result = v.validate_salary("200")
            self.assertTrue(result, 'valid Salary')

    def test_validate_salary_is_false_words(self):
        """
        Test the validate salary function
        :return: True
        """
        v = Validator()
        result = v.validate_salary("seventy thousand")
        self.assertFalse(result, 'valid Salary')

    def test_validate_salary_is_false_negative_value(self):
        """
        Test the validate salary function
        :return: True
        """
        v = Validator()
        result = v.validate_salary("-20")
        self.assertFalse(result, 'invalid Salary')

    def test_validate_salary_is_false_too_big(self):
        """
        Test the validate salary function
        :return:
        """
        v = Validator()
        result = v.validate_salary('8000')
        self.assertFalse(result, 'invalid SALARY')

    def test_validate_salary_is_false_too_small(self):
        """
        Test the validate salary function
        :return:
        """
        v = Validator()
        result = v.validate_salary('8')
        self.assertFalse(result, 'invalid SALARY')

    def test_validate_salary_is_true_small_but_includes_zero(self):
        """
        Test the validate salary function
        :return:
        """
        v = Validator()
        result = v.validate_salary('008')
        self.assertTrue(result, 'valid SALARY')

    def test_validate_date_is_true(self):
        """
        Test the validate date function
        :return: True
        """
        v = Validator()
        result = v.validate_date("02-03-1990")
        self.assertTrue(result, 'valid Date')

    def test_validate_date_is_false_words(self):
        """
        Test the validate date function
        :return: True
        """
        v = Validator()
        result = v.validate_date("02-March-1991")
        self.assertFalse(result, 'invalid Date format')

    def test_validate_date_is_false_invalid_format(self):
        """
        Test the validate date function
        :return:
        """
        v = Validator()
        result = v.validate_date('01/08/1991')
        self.assertFalse(result, 'invalid date, wrong format')

    def test_validate_date_is_false_invalid_date(self):
        """
        Test the validate date function
        :return:
        """
        v = Validator()
        result = v.validate_date('89/13/1991')
        self.assertFalse(result, 'invalid date, date doesnt exist')

    def test_validate_age_is_true(self):
        """
        Test the validate age function
        :return: True
        """
        v = Validator()
        result = v.validate_age("20")
        self.assertTrue(result, 'valid AGE')

    def test_validate_age_is_false(self):
        """
        Test the validate age function
        :return:
        """
        v = Validator()
        result = v.validate_age('8000')
        self.assertFalse(result, 'invalid AGE')

    def test_validate_age_is_false_negative_num(self):
        """
        Test the validate age function
        :return:
        """
        v = Validator()
        result = v.validate_age('-20')
        self.assertFalse(result, 'invalid AGE')

    def test_validate_all_all_true(self):
        """
        Test valid data being passed into validate_all
        :return:
        """
        v = Validator()
        list1 = ['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991']
        result = v.validate_all(list1)
        expected = [True, True, True, True, True, True, True]
        self.assertEqual(expected, result, "Not valid input")

    def test_validate_all_with_false(self):
        """
        Test invalid date being passed through and if list recognises it
        :return:
        """
        v = Validator()
        list1 = ['A001', 'M', '26', '200', 'Normal', '20', '08/10/1991']
        result = v.validate_all(list1)
        expected = [True, True, True, True, True, True, False]
        self.assertEqual(expected, result, "invalid input")

    # Filer test code
    def test_filer_read_excel(self):
        """
        Test if it can read an xlsx document
        :return: list
        """
        f = Filer()
        result = f.read_excel("test.xlsx")
        expected = [['A001', 'M', 26, 200, 'Normal', 20, '08-10-1991'],
                    ['A002', 'F', 26, 300, 'Normal', 30, '09-10-1991']]
        self.assertEqual(result, expected, "file does not match")

    def test_filer_save_excel_and_read_saved(self):
        """
        Test if it can save to excel
        :return:
        """
        f = Filer()
        li1 = [['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991'],
               ['A002', 'F', '26', '300', 'Normal', '30', '09-10-1991']]
        f.save_excel('doc_test22.xlsx', li1)
        result = f.read_excel("doc_test22.xlsx")
        expected = [['A002', 'F', 26, 300, 'Normal', 30, '09-10-1991']]
        self.assertEqual(result, expected, "saved file couldn't be read")

    # Controller
    def test_load_file_name_error(self):
        """
        test is extension file name wrong
        """
        c = Controller()
        fun = c.load_file("test.xx")
        self.assertRaises(NameError, fun)

    def test_load_file_no_found_error(self):
        """
        test if file not found
        """
        c = Controller()
        fun = c.load_file("test999999999999.csv")
        self.assertRaises(FileNotFoundError, fun)

    def test_load_file_exception(self):
        """
        test file name no extension
        """
        c = Controller()
        fun = c.load_file("test999999999999")
        self.assertRaises(Exception, fun)

    def test_validate_items_returns_valid(self):
        """
        test if items return validated
        """
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991")]
        validated = c.validate_items(content)
        valid = len(validated['Valid'])
        expected = 2
        self.assertEqual(valid, expected, "incorrect validator")

    def test_validate_items_returns_invalid(self):
        """
        test if invalid items also return
        """
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991"),
                   ("A003", "Female", 44, "", "Fat", 90, "")]
        validated = c.validate_items(content)
        valid = len(validated['Invalid'])
        expected = 1
        self.assertEqual(valid, expected, "incorrect validator")

    def test_validate_items_returns_both_valid_and_invalid(self):
        """
        test is both valid and invalid return in dict
        """
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991"),
                   ("A003", "Female", 44, "", "Fat", 90, "")]
        validated = c.validate_items(content)
        valid = len(validated['Invalid'])
        expected = 1
        self.assertEqual(valid, expected, "incorrect validator")

    def test_add_to_database_adds_employees(self):
        """
        test if employees can be added to db
        """
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991")]
        c.add_to_database(content)
        database = c.get_all_employees()
        self.assertEqual(database, content)

    def test_get_all_employees_returns_employees(self):
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991")]
        c.add_to_database(content)
        database = c.get_all_employees()
        self.assertEqual(database, content)

    def test_get_all_employees_returns_none_when_database_created(self):
        c = Controller()
        c.db.create_connection("test2.db")
        database = c.get_all_employees()
        self.assertEqual(database, None)

    # Database
    def test_database_created(self):
        c = Controller()
        c.db.create_connection("test_case.db")
        result = os.path.isfile("test_case.db")
        self.assertTrue(result)

    def test_database_employee_table_created(self):
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991")]
        c.add_to_database(content)
        database = c.get_all_employees()
        self.assertEqual(database, content)

    # Chami
    def test_validate_bmi_is_true(self):
        v = Validator()
        result = v.validate_bmi("Normal")
        self.assertTrue(result, "Valid BMI")

    def test_validate_bmi_is_false(self):
        v = Validator()
        result = v.validate_bmi("normal")
        self.assertFalse(result, "Invalid BMI")

    def test_validate_sales_is_true(self):
        v = Validator()
        result = v.validate_sales("999")
        self.assertTrue(result, 'Valid Sales value')

    def test__validate_sales_is_false(self):
        v = Validator()
        result = v.validate_sales("1234")
        self.assertFalse(result, 'Invalid Sales Amount')

    def test_15_validate_bmi_is_false_notequal_under(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("U")
        self.assertNotEqual(result, 'Underweight', "Invaid BMI")

    def test_14_validate_bmi_is_false_notequal_over(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("OVERWEIGHT")
        self.assertNotEqual(result, 'Overweight', "Invaid BMI")

    def test_13_validate_bmi_is_false_notequal_normal(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("NORMAL")
        self.assertNotEqual(result, 'Normal', "Invaid BMI")

    def test_12_validate_bmi_is_false_notEqualO(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("OBESITY")
        self.assertNotEqual(result, 'Obesity', "Invaid BMI")

    def test_11_validate_bmi_is_false_notEqualN(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("N")
        self.assertNotEqual(result, 'Normal', "Invaid BMI")

    def test_10_validate_bmi_is_false_space(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("  ")
        self.assertFalse(result, "Invalid BMI")

    def test_09_validate_bmi_is_true(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("Normal")
        self.assertTrue(result, "Valide BMI")

    def test_08_validate_bmi_is_false(self):
        """
        Test the validate bmi false function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("normal")
        self.assertFalse(result, "Invalide BMI")

    def test_07_validate_bmi_is_false_N(self):
        """
        Test the validate bmi false function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("N")
        self.assertFalse(result, "Invalide BMI")

    def test_06_validate_sales_is_true(self):
        """
        Test the validate sales true function
        :return:
        """
        v = Validator()
        result = v.validate_sales("999")
        self.assertTrue(result, 'Valide Sales value')

    def test_05_validate_sales_is_false(self):
        """
        Test the validate sales false function
        :return:
        """
        v = Validator()
        result = v.validate_sales("1234")
        self.assertFalse(result, 'Invalide Sales Amount')

    def test_04_validate_sales_is_false_space(self):
        """
        Test the validate sales false function
        :return:
        """
        v = Validator()
        result = v.validate_sales(" ")
        self.assertFalse(result, 'Invalide Sales Amount')

    def test_03_validate_sales_is_false_characters(self):
        """
        Test the validate sales false function
        :return:
        """
        v = Validator()
        result = v.validate_sales(",")
        self.assertFalse(result, 'Invalide Sales character')

    def test_02_validate_sales_is_false_letters(self):
        """
        Test the validate sales false function
        :return:
        """
        v = Validator()
        result = v.validate_sales("qwer")
        self.assertFalse(result, 'Invalide Sales you can not enter letters')

    def test_01_validate_sales_is_false_minus(self):
        """
        Test the validate sales false function
        :return:
        """
        v = Validator()
        result = v.validate_sales("-3")
        self.assertFalse(result, 'Invalid Sales you cant enter minus values')


if __name__ == '__main__':
    unittest.main()
    # with more details
