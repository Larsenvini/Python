from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(80)
        self.cell(30,10, "CS50 Shirtificate", border =1, align="C")
        self.ln(20)
        
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=12) # add "B" or "I" before the size for bold/italic
pdf.cell(text="hello world") # specify dimensions before tex with 40, 10 example
pdf.output("hello_world.pdf")
pdf = FPDF(orientation="P", unit="mm", format="A4")
