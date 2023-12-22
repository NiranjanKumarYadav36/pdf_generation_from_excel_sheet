from fpdf import FPDF
import glob
from pathlib import Path

# get all the filepaths
filepaths = glob.glob("Text_file/*.txt")

# create one pdf file
pdf = FPDF(orientation='L', unit='mm', format='A4')

for filepath in filepaths:
    pdf.add_page()

    # get the filename as a filepath
    raw_filename = Path(filepath).stem
    filename = raw_filename.capitalize()

    # set the header
    pdf.set_font(family='Times', size=15, style='B')
    pdf.set_text_color(10, 23, 100)
    pdf.cell(w=50, h=8, txt=filename, ln=1)

    # read the content of the files
    with open(filepath, 'r') as file:
        content = file.read()

    # printing contents
    pdf.set_font(family='Times', size=12)
    pdf.set_text_color(10, 0, 100)
    pdf.multi_cell(w=0, h=6, txt=content)


pdf.output("PDFs/exercise_sol.pdf")
