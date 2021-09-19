import cv2
from pathlib import Path
import pytesseract 
import collections
from pytesseract import * 
import re

class CascadeClassifier:
    def __init__(self) -> None:
        
        self.image=None
        self.type_=None

    def preprocessing(self):
        grayed_image=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        threshold_img = cv2.threshold(grayed_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        config= r'--oem 3 --psm 6'
        details=pytesseract.image_to_data(threshold_img,output_type=pytesseract.Output.DICT,config=config,lang='eng')

        actual_words = []

        locator = []

        lw = ''

        for word in details['text']:

            if word!='':

                locator.append(word)

                lw = word

            if (lw!='' and word == '') or (word==details['text'][-1]):

                actual_words.append(locator)

                locator = []

        search_id=re.findall('')
        search_passport=re.findall('')

        #Initiate the classifiers to their respective classes
        # self.id_xml=cv2.CascadeClassifier(CascadeClassifier.id_xml_path)
        # self.passport_xml=cv2.CascadeClassifier(CascadeClassifier.passport_xml_path)

        # #Detect the   type of image
        # value1=self.id_xml.detectMultiScale(grayed_image,minSize=(20,20))
        # value2=self.passport_xml.detectMultiScale(grayed_image,minSize=(20,20))

        # if value1>value2:
        #     self.type='id'
        # if value2>value1:
        #     self.type='passport'
        # else:
        #     self.type=None

        


            
        


