from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=12) # add "B" or "I" before the size for bold/italic
pdf.cell(text="hello world") # 
pdf.output("hello_world.pdf")
pdf = FPDF(orientation="P", unit="mm", format="A4")
