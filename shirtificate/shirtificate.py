from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(80)
        self.cell(30,10, "CS50 Shirtificate", border =1, align="C")
        self.ln(20)

    def add_centered_img(self, image_path):
        image_width, image_height = self.get_image_dimensions(image_path)

        page_width =self.w -2 * self.l_margin
        page_height =self.h -2 * self.t_margin
        x = (page_width - image_width) / 2
        y = (page_height - image_height) / 2

        self.image(image_path, x, y, image_width, image_height)

    def get_image_dimensions(self, image_path):
        from PIL import Image
        image = Image.open(image_path)
        width, height = image.size
        aspect_ratio = height / width
        return 100, 100 * aspect_ratio

    def add_centered_text(self, text):
        page_width = self.w - 2 * self.l_margin
        text_width = self.get_string_width(text)
        x = (page_width - text_width) / 2

        page_height = self.h - 2 * self.t_margin
        y = page_height / 2

        self.set_xy(x,y)
        self.set_font("helvetica", "B", 24)
        self.cell(text_width,  10, text, align="C")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=12) # add "B" or "I" before the size for bold/italic
pdf.add_centered_image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png")
pdf.output("hello_world.pdf")
pdf = FPDF(orientation="P", unit="mm", format="A4")
