class Bill:
    """
    Contain data of a bill and takes 2 attributes.
        Attribute:
            amount: int

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

    def pays(self, bill):
        return bill.amount / 2


class PdfReport:
    """
    Creates an PDF file with the names of flatmates and how much each have to pay.
    Class takes 1 attribute.
        Attribute:
            filename: str
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


my_bill = Bill(200, "June 2022")
flatmate_1 = Flatmate("Cristi", 20)
flatmate_2 = Flatmate("Razvan", 25)
print(flatmate_1.pays(my_bill))
