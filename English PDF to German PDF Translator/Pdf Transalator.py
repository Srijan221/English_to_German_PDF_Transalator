# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:17:47 2021

@author: Srijan
"""
import os
from PyPDF2 import PdfFileReader
from googletrans import Translator
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

#First we will convert our pdf to Image for better extraction of text
images = convert_from_path("SOP_Srijan_PDF_English.pdf",poppler_path=r'D:\Anaconda Files and Projects\English pdf to German\poppler-0.68.0_x86\poppler-0.68.0\bin')
for i,image in enumerate(images,start=1):
    image.save("translate.jpg")
    
#Then We will import the image and extract it's text using pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Dell\AppData\Local\Tesseract-OCR\tesseract.exe"
img = Image.open("hello.jpg")
text = pytesseract.image_to_string(img)

#Now We will translate the extracted text from english to German using googletrans
from googletrans import Translator
URL_COM = 'translate.googleapis.com'
URL_LV = 'translate.google.de'
LANG = "de"
translator = Translator(service_urls=[URL_COM, URL_LV])
translation = translator.translate(text, dest=LANG)
translated_text = str(translation)

#Now we will use reportlab to convert this text into pdf again
from reportlab.pdfgen import canvas

report = canvas.Canvas('GermanPdf.pdf')#new pdf report i am creating
report.setFont("Times-Roman", 20)
report.drawString(10, 800, "Statement of Purpose in German")
size = 10
y = 760
for translated_text in translated_text.split('\n'):
    report.setFont("Helvetica", size)
    report.drawString(10, y, translated_text)
    y = y - 10
report.save() 

#Now we have our translated pdf from english to german