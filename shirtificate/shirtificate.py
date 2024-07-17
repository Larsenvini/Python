import requests
from io import BytesIO
from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 20)
        self.set_text_color(255, 255, 255)
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

        page_height = self.h
        y = page_height / 2 + 30  # Move the text up

        # Draw the text outline by drawing the text multiple times with a slight offset
        self.set_font("helvetica", "B", 24)
        offsets = [-0.5, 0.5, 0, 0]
        for dx in offsets:
            for dy in offsets:
                self.set_xy(x + dx, y + dy)
                self.set_text_color(0, 0, 0)  # Black outline
                self.cell(text_width, 10, text, align="C")

        # Draw the text itself
        self.set_xy(x, y)
        self.set_text_color(255, 255, 255)  # Set text color to white
        self.cell(text_width, 10, text, align="C")

    def draw_gradient_background(self):
        # Draw a vertical gradient from black to white
        self.set_fill_color(0, 0, 0)
        for i in range(256):
            self.set_fill_color(i, i, i)
            self.rect(0, i * (self.h / 256), self.w, self.h / 256, 'F')

# Function to download image
def download_image(url, save_path):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.save(save_path)

# Download the image
image_url = "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png"
image_path = "shirtificate.png"
download_image(image_url, image_path)

# Get user's name
text = input("Name: ")
final_text = f"{text} took CS50"

# Create the PDF
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.draw_gradient_background()  # Draw the gradient background
pdf.set_font("helvetica", size=12)  # add "B" or "I" before the size for bold/italic
pdf.add_centered_image(image_path)
pdf.add_centered_text(final_text)
pdf.output("shirtificate.pdf")

