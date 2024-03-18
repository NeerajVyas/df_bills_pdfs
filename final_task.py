
# from pdf2image import convert_from_path
image_columns = '/Users/neerajvyas/job/charu/other_images/image_0_3.png'
image_data = '/Users/neerajvyas/job/charu/image_data.png'
# output_path = '/Users/neerajvyas/job/charu/5808025495.jpg'

import pytesseract
from PIL import Image
import pandas as pd

def read_text_from_image(image_path):
    # Open the image using PIL (Python Imaging Library)
    with Image.open(image_path) as img:
        # Use pytesseract to perform OCR on the image
        text = pytesseract.image_to_string(img)
    
    return text


print("= = = = image_columns = = = =")

text = read_text_from_image(image_columns)
print(text)

print("= = = = image_data = = = =")

text = read_text_from_image(image_data)
print(text)

 
# initialize list of lists
data = []
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=[
    'Particulars',
    'Qty',
    'Unit Price',
    'Gross Amount(BHD)'
    'Vat %',
    'Vat BHD',
    'Total Amount ({BHD)'
    ])
 
# print dataframe.
print(df)


print("= = = = Horizintally image_data = = = =")


def read_text_from_rotated_image(image_path, clockwise=True):
    # Open the image using PIL (Python Imaging Library)
    with Image.open(image_path) as img:
        # Rotate the image 90 degrees clockwise or counterclockwise
        if clockwise:
            rotated_img = img.transpose(Image.ROTATE_270)
        else:
            rotated_img = img.transpose(Image.ROTATE_90)
        
        # Use pytesseract to perform OCR on the rotated image and extract the text
        text = pytesseract.image_to_string(rotated_img)
    
    return text

def tilt_image(image_path, angle):
    # Open the image using PIL (Python Imaging Library)
    with Image.open(image_path) as img:
        # Tilt the image by the specified angle
        tilted_img = img.rotate(angle, resample=Image.BICUBIC, expand=True)

    return tilted_img

# Example usage
image_path = "image_data.png"
tilted_image = tilt_image(image_path, -3)  # Tilt the image by 5 degrees
tilted_image.save(image_path)



from PIL import Image

def increase_quality(input_image_path, output_image_path, quality=95):
    image = Image.open(input_image_path)
    image.save(output_image_path, quality=quality)

# Example usage
input_image_path = image_path
output_image_path = "output_image.png"
increase_quality(input_image_path, output_image_path, quality=95)




# Example usage
clockwise = True  # Set to False for counterclockwise rotation
text = read_text_from_rotated_image(output_image_path, clockwise)
print(text)

