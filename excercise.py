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
    pdf.cell(w=0, h=8, txt=filename)


pdf.output("PDFs/exerc_sol.pdf")
