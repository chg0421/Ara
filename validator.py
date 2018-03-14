import datetime
import re


class Validator:

    #  Renee code
    @staticmethod
    def validate_empid(empid):
        """
        >>> Validator.validate_empid("A001")
        True

        >>> Validator.validate_empid("A0001")
        False

        >>> Validator.validate_empid("0001")
        False

        >>> Validator.validate_empid("AAAA")
        False

        >>> Validator.validate_empid("A01")
        False

        >>> Validator.validate_empid("a001")
        False
        """
        validate = re.compile('[A-Z][0-9]{3}')

        if re.fullmatch(validate, empid):
            return True
        else:
            return False

    @staticmethod
    def validate_gender(gender):
        """
        >>> Validator.validate_gender("F")
        True

        >>> Validator.validate_gender("f")
        False

        >>> Validator.validate_gender("Female")
        False

        >>> Validator.validate_gender("FEMALE")
        False

        >>> Validator.validate_gender("E")
        False

        :param gender:
        :return:
        """
        gender_values = ['F', 'M']
        tempt = gender.upper()
        if tempt in gender_values:
            return True
        else:
            return False

    # Chamilas
    @staticmethod
    def validate_bmi(bmi):
        bmi_values = ['Normal', 'Overweight', 'Underweight', 'Obesity']
        if bmi in bmi_values:
            return True
        else:
            return False

    @staticmethod
    def validate_sales(sales):
        check = re.compile('[0-9]{2,3}')
        if re.fullmatch(check, sales):
            return True
        else:
            return False

    # Jono's
    @staticmethod
    def validate_salary(salary):
        """
        To test 2 digit input
        >>> Validator.validate_salary("23")
        True

        To test 3 digit input
        >>> Validator.validate_salary("244")
        True

        To test invalid input
        >>> Validator.validate_salary("4000")
        False
        """

        check = re.compile('[0-9]{2,3}')
        if re.fullmatch(check, salary):
            return True
        else:
            return False

    @staticmethod
    def validate_date(date_string):
        """
        To test valid date:
        >>> Validator.validate_date("10-09-1991")
        True

        To test invalid date format:
        >>> Validator.validate_date("10/1/1991")
        False

        To test invalid date
        >>> Validator.validate_date("33/22/1991")
        False

        :param date_string:
        :return:
        """
        try:
            datetime.datetime.strptime(date_string, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_age(age):
        """
        To test valid input
        >>> Validator.validate_age("10")
        True

        To test invalid input
        >>> Validator.validate_age("five")
        False

        To test invalid input, over range
        >>> Validator.validate_age("500")
        False

        :param age:
        :return:
        """
        check = re.compile('[0-9]{2}')
        if re.fullmatch(check, age):
            return True
        else:
            return False

    def validate_all(self, employee):
        items_valid = [self.validate_empid(str(employee[0])),
                       self.validate_gender(str(employee[1])),
                       self.validate_age(str(employee[2])),
                       self.validate_sales(str(employee[3])),
                       self.validate_bmi(str(employee[4])),
                       self.validate_salary(str(employee[5])),
                       self.validate_date(str(employee[6]))]

        return items_valid


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
