# asciimage

A library designed in python to convert images into ascii paintings.
To install: pip install asciimage

### Table of Contents

1. [Installation](#installation)
2. [Motivation](#motivation)
3. [Example](#example)


## Installation <a name="installation"></a>
The repository contains a zipped file of my Python package asciimage and should be installed via pip.<br/>
Instalation procedure: pip install asciimage


## Motivation <a name="Motivation"></a>
The package is intended as a simple drawing tool that produces ASCII art.<br/>
The user will upload an image. The image has to be a jpg or png image. The image should have a nice contrast for proper output.<br/>
The package contains the function make_ascii_image() which produces ascii art <br/>


## Example <a name="Example"></a>
This is the way to run the module:


		from asciimage import *
		from PIL import Image #import the module
		image_path = "input_image.jpg"
		file_path = "output.txt" #'output.txt' is the destination where the ASCII art will be stored
		ascii_char = list(",.")
		height = 400 #intended height of output file
		width = 400 #intended width of output file
		art = asciimage(image_path,file_path,ascii_char,height,width) #optional: ascii_char,height,width
		art.make_ascii_image()



If you like the library, please consider giving it a star on Github :)                                  
