# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:59:03 2019

@author: 1605458
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:31:00 2019

@author: 1605458
"""
import base64
import json
import urllib.parse
from PIL import Image
import PIL.Image
import tempfile
import numpy as np
import imutils
from flask import Flask, request
import pytesseract
import cv2
import re
import io
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def getdate():
    if request.method == 'POST':
        #data = request.data
        #data = str(request.data)
        #data = urllib.parse.unquote(data)
        #data = urllib.parse(data)
        #data=request.data
        #data = json.loads(data)
        '''data= request.data
        image_encode=data["base_64_image_content"]
        print(image_encode)'''
        data=request.get_json()
        #print(s)
        image_encode=data["base_64_image_content"]
        image_decode=base64.decodebytes(image_encode)
        print(image_decode)
        img = Image.open(io.BytesIO(image_decode))
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
        #TESSDATA_PREFIX = 'C:/Users/KIIT/tessdata-master'
        output = pytesseract.image_to_string(img, lang='eng')
        #s=output.replace(" ", "")
        #print (s)
        pattern1='((\d{1,2})[-|/|\.]((\d{1,2})|([A-Z]*([a-z]+|[a-z]*)))[-|/|\.](\d{2,4}))'
        pattern2='(([A-Z]*([a-z]+|[a-z]*))(\d{1,2}| |\.)(\'|\d{1,2})(\'|\,)\d{2,4})'
        pattern3='(\d{1,2}([A-Z]*([a-z]+|[a-z]*))[\'|\,]\d{2,4})'      
    
        match = re.findall(pattern1, output)
        if len(match)==0:
            match = re.findall(pattern2, output)
        if len(match)==0:
            match = re.findall(pattern3, output)
        print(match[0][0])
        s=str(match[0][0])
        return s
        

if __name__ == '__main__':
    app.run(threaded=True)        


