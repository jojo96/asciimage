# asciimage

A library designed in python to convert images into ascii paintings.
To install: <br><br>
<b>pip install asciimage</b><br>
<b>pip install docx</b><br>
<b>pip install python-docx </b><br>
For more exmamples or if you are still struggling with installation check out the <a href="https://github.com/jojo96/asciimage/blob/main/asciimage/asciimageExample.ipynb">Jupyter notebook</a>


### Table of Contents

1. [Installation](#installation)
2. [Motivation](#motivation)
3. [Example](#example)
4. [Sample](#sample)
5. [Troubleshooting](#sample)


## Installation <a name="installation"></a>
The repository contains a zipped file of my Python package asciimage and should be installed via pip.<br/>
Instalation procedure: <br>
<b>pip install asciimage</b><br>
<b>pip install docx</b><br>
<b>pip install python-docx </b><br>
#The docx and python-docx libraries must be installed

## Motivation <a name="Motivation"></a>
The package is intended as a simple drawing tool that produces ASCII art.<br/>
The user will upload an image. The image has to be a jpg or png image. The image should have a nice contrast for proper output.<br/>
The package contains the function make_ascii_image() which produces ascii art <br/>
For the colored ASCII image function, the input images should not be very richly colored and the function works well for images of small size, up to dimensions 256X256. 


## Example <a name="Example"></a>
This is the way to run the module:


		from asciimage import *
		from PIL import Image #import the module
		image_path = r"input_image.jpg"
		file_path = r"output.txt" #'output.txt' is the destination where the ASCII art will be stored
		ascii_char = list(",.")
		height = 400 #intended height of output file
		width = 400 #intended width of output file
		art = asciimage(image_path,file_path,ascii_char,height,width) #optional: ascii_char,height,width
		art.make_ascii_image()
		
		#for colored ascii image
		from PIL import Image
		from docx import *
		from docx.shared import *
		image_path = r"input_image.jpg"
		file_path = r"output.doc" #'output.doc' is the destination where the ASCII art will be stored
		art = asciimage(image_path,file_path) #compulsory: image_path,file_path
		#this function outputs a doc file only
		art.make_colored_ascii(64)#produces 64X64 image; 



## Sample <a name="Sample"></a>

Input Image: <br>
![input](https://raw.githubusercontent.com/jojo96/asciimage/main/pok.jpg)

Output text file: <br>
![output](https://raw.githubusercontent.com/jojo96/asciimage/main/pok_txt.png)


Colored ASCII Input Image: <br>
![input](https://raw.githubusercontent.com/jojo96/asciimage/main/blastoise.jpg)

Output doc file: <br>
![output](https://raw.githubusercontent.com/jojo96/asciimage/main/blastoiseASCII.png)

If you like the library, please consider giving it a star on Github :)       


## Troubleshooting <a name="Troubleshooting"></a>

This is a common error: <br>
![input](https://raw.githubusercontent.com/jojo96/asciimage/main/error.png)
If this happens, it is because of python-docx not being installed. In that case, please proceed with:<br> 
<b>pip install python-docx</b><br>
<b>pip install docx</b><br>

