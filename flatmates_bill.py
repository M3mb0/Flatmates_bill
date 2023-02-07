from fpdf import FPDF


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

    def pays(self, bill, flatmate):
        """
        Method returns the amount that the flatmate has to pay and takes 2 arguments:
        Argument:
            bill: obj

            flatmate: obj
        """
        coefficient = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        return coefficient * bill.amount


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
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Insert Period label and value
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the 1st flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=1, ln=1)

        # Insert name and due amount of the 2nd flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=1, ln=1)

        pdf.output(self.filename)


my_bill = Bill(200, "June 2022")
flatmate_1 = Flatmate("Cristi", 20)
flatmate_2 = Flatmate("Razvan", 25)
print(flatmate_1.pays(my_bill, flatmate_2))
print(flatmate_2.pays(my_bill, flatmate_1))

pdf_report = PdfReport(filename="1st_report.pdf")
pdf_report.generate(flatmate_1, flatmate_2, my_bill)
