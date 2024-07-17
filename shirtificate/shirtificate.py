import requests
from io import BytesIO
from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 24)  # Increase font size
        self.set_text_color(255, 255, 255)  # Set text color to white
        self.cell(0, 10, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    def add_centered_image(self, image_path):
        image_width, image_height = self.get_image_dimensions(image_path)

        page_width = self.w
        page_height = self.h
        x = (page_width - image_width) / 2
        y = (page_height - image_height) / 2 + 20  # Adjust the y position if needed

        self.image(image_path, x, y, image_width, image_height)

    def get_image_dimensions(self, image_path):
        image = Image.open(image_path)
        width, height = image.size
        aspect_ratio = height / width
        return 150, 150 * aspect_ratio  # Increase size of the image

    def add_centered_text(self, text):
        page_width = self.w
        text_width = self.get_string_width(text)
        x = (page_width - text_width) / 2


