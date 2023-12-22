from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("Text_file/*.txt")

# create one pdf file
pdf = FPDF(orientation='L', unit='mm', format='A4')

for filepath in filepaths:
    pdf.add_page()

    raw_filename = Path(filepath).stem
    filename = raw_filename.capitalize()

    pdf.set_font(family='Times', size=15, style='B')
    pdf.cell(w=50, h=8, txt=filename, ln=1)

    with open(f"Text_file/{raw_filename}.txt", 'r') as file:
        content = file.read()

    pdf.set_font(family='Times', size=12)
    pdf.multi_cell(w=0, h=6, txt=content)


pdf.output("PDFs/exercise_sol.pdf")
