
# from pdf2image import convert_from_path
image_columns = '/Users/neerajvyas/job/charu/image_0_3.png'
image_data = '/Users/neerajvyas/job/charu/image_data.png'
# output_path = '/Users/neerajvyas/job/charu/5808025495.jpg'

print("USING OCR COLUMN NAMES")

import pytesseract
from PIL import Image

import pytesseract
from PIL import Image

def read_text_from_image(image_path):
    # Open the image using PIL (Python Imaging Library)
    with Image.open(image_path) as img:
        # Use pytesseract to perform OCR on the image
        text = pytesseract.image_to_string(img)
    
    return text

# Example usage
print("= = = = image_columns = = = =")

text = read_text_from_image(image_columns)
print(text)


# Example usage
print("= = = = image_data = = = =")

text = read_text_from_image(image_data)
print(text)


# Import pandas library
import pandas as pd
 
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
import pytesseract
from PIL import Image

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

# Example usage
image_path = "image_data.png"
clockwise = True  # Set to False for counterclockwise rotation
text = read_text_from_rotated_image(image_path, clockwise)
print(text)




from PIL import Image

def tilt_image(image_path, angle):
    # Open the image using PIL (Python Imaging Library)
    with Image.open(image_path) as img:
        # Tilt the image by the specified angle
        tilted_img = img.rotate(angle, resample=Image.BICUBIC, expand=True)
    
    return tilted_img

# Example usage
image_path = "image_data.png"
tilted_image = tilt_image(image_path, 0.5)  # Tilt the image by 5 degrees
tilted_image.save("image_data.png")



print("==== ANOTHER OCR API ==== ")
import requests

def ocr_space_file(filename, api_key, language='eng'):
    payload = {'apikey': api_key,
               'language': language,
               'isOverlayRequired': False}
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload)
    return r.json()

def extract_text_from_ocr_space(image_path, api_key):
    # Perform OCR using OCR.space API
    result = ocr_space_file(image_path, api_key)
    
    # Extract text from the OCR result and store in a dictionary
    extracted_text = {}
    parsed_results = result.get('ParsedResults', [])
    for idx, parsed_result in enumerate(parsed_results, start=1):
        text = parsed_result.get('ParsedText', '').strip()
        extracted_text[f"Result{idx}"] = {'Text': text}
    
    return extracted_text

# Example usage
api_key = 'K82538231088957'
image_path = 'image_data.png'
extracted_text = extract_text_from_ocr_space(image_path, api_key)
print(extracted_text)

# Example usage
api_key = 'K82538231088957'


# {'Result1': {'Text': 'MASTER BEDROOM & CORRIDOR\r\nAREA\r\nCUPBOARD EXTENSION WORK\r\nFOR ANDALUS GARDEN - VILLA 2\r\nWR YKP 23/6860\r\nQTN IFM/Q/CVWYKP/2752/23\r\nLPO 1195176255\r\n1\r\n250.000\r\n250.000\r\n10\r\n25.000\r\nTotal excl. VAT BHD\r\nVAT BHD\r\nTotal BHD\r\nBalance due BHD\r\n275.000\r\n250.000\r\n25.000\r\n275.000\r\n275.000'}}
import pytesseract
from PIL import Image

def extract_text_with_coordinates(image_path):
    # Open the image using PIL (Python Imaging Library)
    with Image.open(image_path) as img:
        # Use pytesseract to perform OCR on the image and extract text with coordinates
        text_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    
    # Extract relevant information and organize it into a list of dictionaries
    extracted_text_list = []
    for i in range(len(text_data['text'])):
        word_dict = {
            'text': text_data['text'][i],
            'left': text_data['left'][i],
            'top': text_data['top'][i],
            'width': text_data['width'][i],
            'height': text_data['height'][i],
            'conf': text_data['conf'][i]
        }
        extracted_text_list.append(word_dict)
    
    return extracted_text_list

# Example usage
image_path = 'image_data.png'
extracted_text_list = extract_text_with_coordinates(image_path)
print(extracted_text_list)



[{'text': '', 'left': 0, 'top': 0, 'width': 2436, 'height': 1742, 'conf': -1}, {'text': '', 'left': 244, 'top': 579, 'width': 515, 'height': 55, 'conf': -1}, {'text': '', 'left': 244, 'top': 579, 'width': 515, 'height': 55, 'conf': -1}, {'text': '', 'left': 244, 'top': 579, 'width': 515, 'height': 55, 'conf': -1}, {'text': 'MASTER', 'left': 244, 'top': 602, 'width': 132, 'height': 32, 'conf': 96}, {'text': 'BEDROOM', 'left': 386, 'top': 592, 'width': 162, 'height': 33, 'conf': 95}, {'text': '&', 'left': 559, 'top': 590, 'width': 20, 'height': 24, 'conf': 93}, {'text': 'CORRIDOR', 'left': 589, 'top': 579, 'width': 170, 'height': 34, 'conf': 96}, {'text': '', 'left': 236, 'top': 641, 'width': 526, 'height': 269, 'conf': -1}, {'text': '', 'left': 236, 'top': 641, 'width': 526, 'height': 269, 'conf': -1}, {'text': '', 'left': 236, 'top': 641, 'width': 88, 'height': 30, 'conf': -1}, {'text': 'AREA', 'left': 236, 'top': 641, 'width': 88, 'height': 30, 'conf': 96}, {'text': '', 'left': 248, 'top': 655, 'width': 481, 'height': 52, 'conf': -1}, {'text': 'CUPBOARD', 'left': 248, 'top': 673, 'width': 178, 'height': 34, 'conf': 96}, {'text': 'EXTENSION', 'left': 439, 'top': 661, 'width': 181, 'height': 33, 'conf': 96}, {'text': 'WORK', 'left': 629, 'top': 655, 'width': 100, 'height': 28, 'conf': 96}, {'text': '', 'left': 251, 'top': 703, 'width': 511, 'height': 55, 'conf': -1}, {'text': 'FOR', 'left': 251, 'top': 730, 'width': 67, 'height': 28, 'conf': 93}, {'text': 'ANDALUS', 'left': 326, 'top': 720, 'width': 151, 'height': 33, 'conf': 91}, {'text': 'GARDEN', 'left': 487, 'top': 712, 'width': 133, 'height': 31, 'conf': 93}, {'text': '-', 'left': 632, 'top': 724, 'width': 10, 'height': 4, 'conf': 92}, {'text': 'VILLA', 'left': 649, 'top': 705, 'width': 88, 'height': 28, 'conf': 96}, {'text': '2', 'left': 746, 'top': 703, 'width': 16, 'height': 24, 'conf': 96}, {'text': '', 'left': 252, 'top': 770, 'width': 250, 'height': 38, 'conf': -1}, {'text': 'WR', 'left': 252, 'top': 782, 'width': 55, 'height': 26, 'conf': 93}, {'text': 'YKP', 'left': 315, 'top': 778, 'width': 63, 'height': 26, 'conf': 92}, {'text': '23/6860', 'left': 389, 'top': 770, 'width': 113, 'height': 30, 'conf': 96}, {'text': '', 'left': 257, 'top': 805, 'width': 431, 'height': 54, 'conf': -1}, {'text': 'QTN', 'left': 257, 'top': 831, 'width': 66, 'height': 28, 'conf': 90}, {'text': 'IFM/QICVLIVKP/2752/23', 'left': 335, 'top': 805, 'width': 353, 'height': 54, 'conf': 81}, {'text': '', 'left': 260, 'top': 872, 'width': 249, 'height': 38, 'conf': -1}, {'text': 'LPO', 'left': 260, 'top': 882, 'width': 63, 'height': 28, 'conf': 95}, {'text': '1195176255', 'left': 335, 'top': 872, 'width': 174, 'height': 33, 'conf': 96}, {'text': '', 'left': 1130, 'top': 826, 'width': 114, 'height': 30, 'conf': -1}, {'text': '', 'left': 1130, 'top': 826, 'width': 114, 'height': 30, 'conf': -1}, {'text': '', 'left': 1130, 'top': 826, 'width': 114, 'height': 30, 'conf': -1}, {'text': '250.000', 'left': 1130, 'top': 826, 'width': 114, 'height': 30, 'conf': 96}, {'text': '', 'left': 1435, 'top': 808, 'width': 113, 'height': 30, 'conf': -1}, {'text': '', 'left': 1435, 'top': 808, 'width': 113, 'height': 30, 'conf': -1}, {'text': '', 'left': 1435, 'top': 808, 'width': 113, 'height': 30, 'conf': -1}, {'text': '250.000', 'left': 1435, 'top': 808, 'width': 113, 'height': 30, 'conf': 96}, {'text': '', 'left': 1626, 'top': 787, 'width': 264, 'height': 40, 'conf': -1}, {'text': '', 'left': 1626, 'top': 787, 'width': 264, 'height': 40, 'conf': -1}, {'text': '', 'left': 1626, 'top': 787, 'width': 264, 'height': 40, 'conf': -1}, {'text': '10', 'left': 1626, 'top': 802, 'width': 31, 'height': 25, 'conf': 95}, {'text': '25.000', 'left': 1794, 'top': 787, 'width': 96, 'height': 29, 'conf': 96}, {'text': '', 'left': 1595, 'top': 987, 'width': 305, 'height': 41, 'conf': -1}, {'text': '', 'left': 1595, 'top': 987, 'width': 305, 'height': 41, 'conf': -1}, {'text': '', 'left': 1595, 'top': 987, 'width': 305, 'height': 41, 'conf': -1}, {'text': 'Total', 'left': 1595, 'top': 1001, 'width': 75, 'height': 27, 'conf': 96}, {'text': 'excl.', 'left': 1680, 'top': 996, 'width': 69, 'height': 27, 'conf': 93}, {'text': 'VAT', 'left': 1758, 'top': 991, 'width': 64, 'height': 28, 'conf': 96}, {'text': 'BHD', 'left': 1833, 'top': 987, 'width': 67, 'height': 26, 'conf': 95}, {'text': '', 'left': 1742, 'top': 1038, 'width': 164, 'height': 72, 'conf': -1}, {'text': '', 'left': 1742, 'top': 1038, 'width': 164, 'height': 72, 'conf': -1}, {'text': '', 'left': 1760, 'top': 1038, 'width': 143, 'height': 31, 'conf': -1}, {'text': 'VAT', 'left': 1760, 'top': 1042, 'width': 64, 'height': 27, 'conf': 96}, {'text': 'BHD', 'left': 1835, 'top': 1038, 'width': 68, 'height': 26, 'conf': 95}, {'text': '', 'left': 1742, 'top': 1077, 'width': 164, 'height': 33, 'conf': -1}, {'text': 'Total', 'left': 1742, 'top': 1081, 'width': 76, 'height': 29, 'conf': 96}, {'text': 'BHD', 'left': 1838, 'top': 1077, 'width': 68, 'height': 27, 'conf': 96}, {'text': '', 'left': 1637, 'top': 1128, 'width': 272, 'height': 39, 'conf': -1}, {'text': '', 'left': 1637, 'top': 1128, 'width': 272, 'height': 39, 'conf': -1}, 
 {'text': '', 'left': 1637, 'top': 1128, 'width': 272, 'height': 39, 'conf': -1}, 
 {'text': 'Balance', 'left': 1637, 'top': 1141, 'width': 118, 'height': 26, 'conf': 96}, 
 {'text': 'due', 'left': 1766, 'top': 1134, 'width': 55, 'height': 26, 'conf': 96}, 
 {'text': 'BHD', 'left': 1841, 'top': 1128, 'width': 68, 'height': 27, 'conf': 96}, 
 {'text': '', 'left': 2063, 'top': 769, 'width': 114, 'height': 31, 'conf': -1},
{'text': '', 'left': 2063, 'top': 769, 'width': 114, 'height': 31, 'conf': -1}, 
 {'text': '', 'left': 2063, 'top': 769, 'width': 114, 'height': 31, 'conf': -1}, 
 {'text': '275.000', 'left': 2063, 'top': 769, 'width': 114, 'height': 31, 'conf': 95}, 
 {'text': '', 'left': 2073, 'top': 970, 'width': 114, 'height': 30, 'conf': -1}, 
 {'text': '', 'left': 2073, 'top': 970, 'width': 114, 'height': 30, 'conf': -1}, 
 {'text': '', 'left': 2073, 'top': 970, 'width': 114, 'height': 30, 'conf': -1}, 
 {'text': '250.000', 'left': 2073, 'top': 970, 'width': 114, 'height': 30, 'conf': 96}, 
 {'text': '', 'left': 2078, 'top': 1020, 'width': 114, 'height': 71, 'conf': -1}, 
 {'text': '', 'left': 2078, 'top': 1020, 'width': 114, 'height': 71, 'conf': -1}, 
 {'text': '', 'left': 2093, 'top': 1020, 'width': 96, 'height': 30, 'conf': -1}, 
 {'text': '25.000', 'left': 2093, 'top': 1020, 'width': 96, 'height': 30, 'conf': 94}, 
 {'text': '', 'left': 2078, 'top': 1060, 'width': 114, 'height': 31, 'conf': -1}, 
 {'text': '275.000', 'left': 2078, 'top': 1060, 'width': 114, 'height': 31, 'conf': 95}, 
 {'text': '', 'left': 2081, 'top': 1110, 'width': 113, 'height': 31, 'conf': -1},
  {'text': '', 'left': 2081, 'top': 1110, 'width': 113, 'height': 31, 'conf': -1},
{'text': '', 'left': 2081, 'top': 1110, 'width': 113, 'height': 31, 'conf': -1}, 
 {'text': '275.000', 'left': 2081, 'top': 1110, 'width': 113, 'height': 31, 'conf': 96}]