import requests
from io import BytesIO
from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 25)
        self.cell(80)
        self.cell(30,10, "CS50 Shirtificate", align="C")
        self.ln(20)

    def add_centered_image(self, image_path):
        image_width, image_height = self.get_image_dimensions(image_path)

        page_width =self.w -2 * self.l_margin
        page_height =self.h -2 * self.t_margin
        x = (page_width - image_width) / 2
        y = (page_height - image_height) / 2

        self.cell(80)

        self.image(image_path, x, y, image_width, image_height)

    def get_image_dimensions(self, image_path):
        from PIL import Image
        image = Image.open(image_path)
        width, height = image.size
        aspect_ratio = height / width
        return 150, 150 * aspect_ratio

    def add_centered_text(self, text):
        page_width = self.w - 2 * self.l_margin
        text_width = self.get_string_width(text)
        x = (page_width - text_width) / 2

        page_height = self.h - 2 * self.t_margin
        y = page_height / 2 - 30

        self.set_xy(x,y)
        self.set_font("helvetica", "B", 24)
        self.set_text_color(255, 255, 255)
        self.cell(text_width,  10, text, align="C")

def download_image(url, save_path):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.save(save_path)

image_url = "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png"
image_path = "shirtificate.png"
download_image(image_url, image_path)

text = input("Name: ")
final_text = (f"{text} took CS50")

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=12) # add "B" or "I" before the size for bold/italic
pdf.add_centered_image(image_path)
pdf.add_centered_text(final_text)
pdf.output("shirtificated.pdf")
