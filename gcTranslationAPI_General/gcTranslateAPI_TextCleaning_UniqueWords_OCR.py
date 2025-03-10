#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:33:46 2025

@author: bmarron
"""

# %%

import os
os.getcwd()

print (os.getcwd())



# %%
'''
=========  Extraction of Vocab  ==============================
Step 1
    USE THIS to remove end of line returns from text file
    End of line returns are coded as, /n
    tr is truncate Linux command
'''
    
        # delete all newlines
    $ tr --delete '\n' < yourfile.txt
    
        # replace newlines with space
    $ tr '\n' ' ' < input_filename
    

    # USE THIS!!
$ tr '\n' ' ' < Test.txt > Test2.txt

# %%


'''
Step 2
    *Generating a unique word list from texts
    *Gives single words for student vocab lists
'''

https://stackoverflow.com/questions/43025188/regular-expression-re-findall-for-set-of-all-alphabetic-words

This will accept words like "don't" and "re-invent" and "cul-de-sac" but will 
reject numbers, underscores, whitespace, quote marks, and other punctuation.

    re.findall(r"[A-Za-z\-\']+", s)
    
The \p{L} matches all Unicode letters regardless of modifiers passed to the regex compile.
    re.findall(r"[p{L}\-\']+", s)

 

    # USE THIS!!   
import re
from contextlib import chdir

with chdir('/home/bmarron/Desktop'):
    M = []
    with open('Test2.txt') as f:
        for line in f.readlines():
            for word in line.split():
                word = re.findall('[A-Za-zñáéíóúü\,\-\.\)]+', word)    #words in español and w/ comma, dash, period
                if word:
                    M.append(word[0])

    S = list(set(M))
    S = sorted(S, key=str.lower)

    with open("output.txt", "w") as f:
        for i in S:
            f.write(i + "\n")



# %%

"""
Step 3
    Use this to find two-word vocab
    Find next word
"""
    # How to find the next word of a specific word in a txt-file
    # https://stackoverflow.com/questions/70730240/q-how-to-find-the-next-word-of-a-specific-word-in-a-txt-file


    # USE THIS!!
from contextlib import chdir


with chdir('/home/bmarron/Desktop'):

    with open('Test2.txt','r') as f:
        data = f.read()

    search_word = "tecnologías"
    list_of_words = data.split()
    next_word = list_of_words[list_of_words.index(search_word) + 1]
    prev_word = list_of_words[list_of_words.index(search_word) - 1]

    with open("two-word_terms.txt", "a") as f:
        print(prev_word,"",search_word,"",next_word, file=f)

# %%
'''    OCR for optical pdf files
        *create text files for Extraction of Vocab
'''
    # STEP 1 ==> pdf to png
$ pdftoppm -png Webdoc.pdf Webdoc

    # STEP 2 ==> png to txt
$ tesseract Webdoc-1.png Webdoc-1 --dpi 250^C

    # STEP 3 ==> compile/concatentae text files
$ cat Webdoc* > complete.txt

# %%
'''
    Merge pdf files into one
'''


$ pdfunite in-1.pdf in-2.pdf in-n.pdf ouput.pdf

$ pdfunite W*01.pdf W*02.pdf W*03.pdf W*04.pdf W*05.pdf W*06.pdf W*07.pdf W*08.pdf W*09.pdf W*10.pdf W*11.pdf W*12.pdf ouput.pdf



# %%


# %%
'''
Optical Character Recognition (OCR)
'''

https://builtin.com/data-science/python-ocr



    # Install Tesseract in Linux and Python
    # Successfully installed pytesseract-0.3.13 in /usr/lib/python3/dist-packages
    # pytesseract in ./.local/lib/python3.10/site-packages (0.3.13)

    # for use in terminal
$ sudo aptitude install tesseract-ocr-all

    # for use in Python
$ pip3 install tesseract


# %%

'''
Tesseract   ==> image files only
            ==> unable to read PDFs. rom a PDF, you can 
            ===> use another utility first to generate a set of images
            ==> A single image will represent a single page of the PDF
            ==> pdftppm utility
'''

https://www.howtogeek.com/682389/how-to-do-ocr-from-the-linux-command-line-using-tesseract/

-r number
Specifies the X and Y resolution, in DPI.  The default is 150 DPI.


    # pdf to images is turing-01.png" "turing-02.png" etc
$  pdftoppm -png Web.pdf Web

    # JPEG option
    <opt>=<val>[,<opt>=<val>]"
-jpegopt 
$ pdftoppm -jpegopt=90[,-jpegopt=n] PDF-file PPM-root


    # general tesseract
    # creates "recital.txt" at 150 dpi
$ tesseract recital-63.png recital --dpi 150


    # loop thru turing-xx.png files
    # create a text file from each image
$ for i in turing-??.png; do tesseract "$i" "text-$i" -l eng; done;

    # concatenate text files into one file
$ cat text-turing* > complete.txt




# %%

'''
build an OCR engine in Python
'''

import pytesseract
from PIL import Image
import pytesseract
import numpy as np

    # clean image OCR
filename = "image_01.png" 
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)



    # image cleaning then OCR
import numpy as np
import cv2norm_img = np.zeros((img.shape[0], img.shape[1]))
from contextlib import chdir


with chdir('/home/bmarron/Desktop'):

    filename = 'image_02.png'
    img2 = np.array(Image.open(filename))
    img2 = cv2.normalize(img2, norm_img, 0, 255, cv2.NORM_MINMAX)
    img2 = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)[1]
    img2 = cv2.GaussianBlur(img2, (1, 1), 0)

    text = pytesseract.image_to_string(img2)
    print(text)


# %%

'''
=========  Misc Text Options =======================
    Get word frequencies
'''

import pandas as pd
#pd.options.display.max_colwidth = None
pd.options.display.max_rows = None
    
from contextlib import chdir


with chdir('/home/bmarron/Desktop'):
    
    words = open("clean_test.txt", "r").read().split()
    ordered = sorted(words)
    with open("output.txt", "a") as f:
        print(pd.Series(ordered).value_counts().sort_values(ascending=True), file=f)

# %%





'''
    TEXT CLEANING
    Use sed and 'tr' to
	+ remove all non-printable ASCII characters (garbage characters== !(octal 11-15 || 40-176)).
	+ remove all punctuation
    + NB. 'tr' uses backslash to denote an octal number.
'''

    # open terminal that has file to be counted
    # remove all punctuation
    # overwrite original
    
$ tr -cd '\11-\15\40-\176' < NAME_of_FILE.txt > clean_test.txt &&
sed 's/[[:punct:]]//g' < clean_test.txt > TMP_00 &&
mv TMP_00 clean_test.txt

# %%

from contextlib import chdir


with chdir('/home/bmarron/Desktop'):

    # opening and creating new .txt file 
    with open( 
            "CivilLaw_Terms.txt", 'r') as r, open( 
                'output.txt', 'w') as o: 
      
                    for line in r: 
                        #isspace() function 
                        if not line.isspace(): 
                            o.write(line) 
  
    f = open("output.txt", "r") 
    print("New text file:\n",f.read())


  

# %%


# %%

def count_words(line):
    words = line.split()
    return len(words)

f = open("C:/Users/John Green/Desktop/follows.txt", "r")
text = f.read()
#make a list of the file broken into lines
lines = text.split('\n')
max_words = -1
word = ''
for line in lines:
    length = count_words(line)
    if length > max_words:
        max_words = length
        words = line.split()
f.close()
print(words[0])

# %%


    #Total number of words per line in a text file


def count_words(line):
    words = line.split()
    return len(words)

f = open("/home/bmarron/Desktop/TEST.txt", "r")
text = f.read()
#make a list of the file broken into lines
lines = text.split('\n')
max_words = -1
word = ''
for line in lines:
    length = count_words(line)
    if length > max_words:
        max_words = length
        words = line.split()
f.close()
print(words[0])



# %%



# count the occurrences of number of spaces!?

txt = "Just an example here move along" 
count = 1
for i in txt:
    if i == " ":
       count += 1
print(count)





# %%

"""
USE THIS!!
Find next word
"""
    # How to find the next word of a specific word in a txt-file
    # https://stackoverflow.com/questions/70730240/q-how-to-find-the-next-word-of-a-specific-word-in-a-txt-file


with open('/home/bmarron/Desktop/TEST.txt','r') as f:
    data = f.read()

search_word = "ingeniería"
list_of_words = data.split()
next_word = list_of_words[list_of_words.index(search_word) + 1]



