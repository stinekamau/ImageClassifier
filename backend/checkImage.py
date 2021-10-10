import cv2
from pathlib import Path
import pytesseract 
import collections
from pytesseract import * 
import re

class CascadeClassifier:
    def __init__(self,image) -> None:
        
        self.image=cv2.imread(image)
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

        found=self.traverse(actual_words)
       

        if found=='id':
            self.type_=found
        elif found=='passport':
            self.type_=found

        return {'type_':self.type_}




    def  traverse(self,arr):
        for element in arr:
            for var in element:
                if re.match(r'passp.*?|passport|pas.*?',var,re.I|re.DOTALL):
                    return 'passport'
                if re.match(r'identification|id|ide.*?',var,re.I|re.DOTALL):
                    return 'id'
        return None

    def process(self):
        return self.preprocessing()


if __name__=='__main__':
    c=CascadeClassifier(r'C:/Users/user/Desktop/passport.jpg')
    print(f'Value of the photo is {c.process()}')

        


            
        


