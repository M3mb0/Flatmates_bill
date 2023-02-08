"""
This module contain one class PdfReport which creates and display a PDF file with the amount that
every flatmate has to pay.

Modules:
    pathlib module - creating paths and keep code organised
    webbroser module - displays the PDF file
    fpdf module - import only the FPDF class to create the PDF file
"""


import pathlib
import webbrowser
from fpdf import FPDF

OUT_DIR_NAME = "bills"
OUT_DIR = pathlib.Path(__file__).parent.joinpath(OUT_DIR_NAME)

FILES_DIR = pathlib.Path(__file__).parent.joinpath("files")


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
        """
        Generates and display the PDF file.
        Method take 3 arguments.
            Argument:
                flatmate1: obj

                flatmate2: obj

                bill: obj
        """
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=30, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Add image
        pdf.image(str(FILES_DIR.joinpath("Untitled.png")), w=540, h=350)

        # Insert Period label and value
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the 1st flatmate
        pdf.set_font(family='Arial', size=24)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=0, ln=1)

        # Insert name and due amount of the 2nd flatmate
        pdf.set_font(family='Arial', size=24)
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=0, ln=1)

        # Creates and display the PDF file
        OUT_DIR.mkdir(exist_ok=True)
        pdf.output(str(OUT_DIR.joinpath(f"{self.filename}")))
        webbrowser.open(str(OUT_DIR.joinpath(f"{self.filename}")))
