"""
This module contains, 2 classes Bill and Flatmates
"""


class Bill:
    """
    Contain data of a bill and takes 2 attributes.
        Attribute:
            amount: int, float

            period: str
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Contain data of a flat mate and take 2 attributes.
        Attribute:
            name: str

            days_in_house: int
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, flatmate):
        """
        Method returns the amount that the flatmate has to pay and takes 2 arguments:
        Argument:
            bill: obj

            flatmate: obj
        """
        coefficient = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        return coefficient * bill.amount
