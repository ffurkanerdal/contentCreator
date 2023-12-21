from findImg import image
from textToSpeech import TextToSpeech
from writeText import create

title   =   input("Write a blog Title: ")
images  =   input("Write a images subject: ") # Write English
def create_content(title,images):
    text    =   create(title)
    TextToSpeech(text).textToSpeech()
    image(images).downPhoto() # optional

create_content(title,images)