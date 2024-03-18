
# from pdf2image import convert_from_path
pdf_path_pdf = '/Users/neerajvyas/job/charu/5808025495.pdf'
# output_path = '/Users/neerajvyas/job/charu/5808025495.jpg'

import pdfplumber

def calculate_distance_to_horizontal_line(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        lines = first_page.lines
        
        # Iterate through all lines
        for line in lines:
            # Check if the line is horizontal
            if line['y0'] == line['y1']:
                # Calculate the distance of the horizontal line from a reference point
                distance = line['y0']  # Assuming the reference point is the top of the page
                return distance


def calculate_distance_to_vertical_line(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        lines = first_page.lines
        
        # Iterate through all lines
        for line in lines:
            # Check if the line is vertical
            if line['x0'] == line['x1']:
                # Calculate the distance of the vertical line from a reference point
                distance = line['x0']  # Assuming the reference point is the left side of the page
                return distance

# Example usage
distance_to_vertical_line = calculate_distance_to_vertical_line(pdf_path_pdf)
print("Distance to the first vertical line:", distance_to_vertical_line)

# Example usage
distance_to_horizontal_line = calculate_distance_to_horizontal_line(pdf_path_pdf)
print("Distance to the first horizontal line:", distance_to_horizontal_line)




import tabula
import pandas as pd

def extract_first_table_from_pdf(pdf_path):
    # Extract tables from the PDF file
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    
    # Check if any tables were extracted
    if tables:
        # Extract the first encountered table
        first_table = tables[0]
        
        # Convert the table into a DataFrame
        df = pd.DataFrame(first_table)
        
        return df
    else:
        print("No tables found in the PDF.")




from collections import Counter
from PIL import Image
import io
import pdfplumber

def count_unique_rgb_combinations(pdf_path):
    unique_rgb_combinations = Counter()
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            images = page.images
            for image in images:
                # Extract image data
                img_data = image["stream"].get_data()
                
                try:
                    # Attempt to open the image with PIL
                    img = Image.open(io.BytesIO(img_data))

                    # Convert image to RGB mode if not already
                    if img.mode != "RGB":
                        img = img.convert("RGB")

                    # Analyze pixels and count unique RGB combinations
                    pixels = img.getdata()
                    unique_rgb_combinations.update(pixels)
                except Exception as e:
                    print("Error processing image:", e)

    return unique_rgb_combinations

# Example usage
# unique_combinations = count_unique_rgb_combinations(pdf_path_pdf)

# print("Total unique RGB combinations:", len(unique_combinations))
# Example usage

first_table_df = extract_first_table_from_pdf(pdf_path_pdf)
print("First encountered table:")
print(first_table_df)


# import fitz

# def rotate_images(pdf_path, output_path):
#     # Open the PDF file
#     pdf_document = fitz.open(pdf_path)
    
#     # Iterate through each page of the PDF
#     for page_number in range(len(pdf_document)):
#         # Get the current page
#         page = pdf_document.load_page(page_number)
        
#         # Extract images from the page
#         image_list = page.get_images(full=True)
        
#         # Iterate through each image on the page
#         for img_info in image_list:
#             # Get the image data
#             xref = img_info[0]
#             base_image = pdf_document.extract_image(xref)
#             image_bytes = base_image["image"]
            
#             # Get image width and height
#             width = base_image["width"]
#             height = base_image["height"]
            
#             # Check if rotation is needed
#             if width > height:
#                 page.insert_image((0, 0), stream=image_bytes, rotate=90)
            
#     # Save the modified PDF to a new file
#     pdf_document.save(output_path)
#     pdf_document.close()

# # Example usage
# pdf_path = "example.pdf"
# output_path = "output.pdf"
# rotate_images(pdf_path_pdf, output_path)


from PyPDF2 import PdfReader, PdfWriter
from PIL import Image

def straighten_images(pdf_path, output_path):
    # Open the input PDF file
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        writer = PdfWriter()
        
        # Iterate through each page of the PDF
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            writer.add_page(page)
            
            # Check if the page contains images
            if "/XObject" in page:
                images = page["/XObject"].keys()
                
                # Iterate through each image on the page
                for image_name in images:
                    # Check if the image is rotated
                    if "/Rotate" in page["/XObject"][image_name]:
                        rotation = int(page["/XObject"][image_name]["/Rotate"])
                        
                        # Rotate the image back to correct orientation
                        if rotation in [90, 270]:
                            image = Image.open(page["/XObject"][image_name]._data)
                            image = image.transpose(Image.ROTATE_270)
                            
                            # Update the image on the page
                            page["/XObject"][image_name]._data = image.tobytes()
                            page["/XObject"][image_name]["/Rotate"] = 0

        # Write the modified PDF to a new file
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

# Example usage
# pdf_path = "example.pdf"
output_path = "output.pdf"
straighten_images(pdf_path_pdf, output_path)




print("USING OCR")

import fitz
import pytesseract
from PIL import Image

def ocr_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Initialize empty string to store extracted text
    text = ""
    
    # Iterate through each page of the PDF
    for page_number in range(len(pdf_document)):
        # Get the current page
        page = pdf_document.load_page(page_number)
        
        # Extract images from the page
        image_list = page.get_images(full=True)
        
        # Extract text from the page
        text += page.get_text()
        
        # Iterate through each image on the page
        for img_info in image_list:
            # Get the image data
            xref = img_info[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            
            # Open the image using PIL
            image = Image.open(io.BytesIO(image_bytes))
            
            # Perform OCR on the image using pytesseract
            image_text = pytesseract.image_to_string(image)
            
            # Append the extracted text to the result
            text += image_text
            
    # Close the PDF document
    pdf_document.close()
    
    return text

# Example usage
extracted_text = ocr_pdf(pdf_path_pdf)
print(extracted_text)


print("======fitz=====")
import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page of the PDF
    for page_number in range(len(pdf_document)):
        # Get the current page
        page = pdf_document.load_page(page_number)

        # Get the images on the page
        images = page.get_images(full=True)

        # Iterate through each image on the page
        for img_index, img in enumerate(images):
            # Get the image's XREF (cross-reference) number
            xref = img[0]

            # Extract the image data
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]

            # Save the image to a file (or process it as needed)
            with open(f"image_{page_number}_{img_index}.png", "wb") as image_file:
                image_file.write(image_bytes)

    # Close the PDF document
    pdf_document.close()

# Example usage
pdf_path = "example.pdf"
extract_images_from_pdf(pdf_path_pdf)