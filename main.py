import sys
import numpy as np
import argparse
from PIL import Image, ImageEnhance

def pixellize(input_path, output_path, saturation = 1.25, contrast = 1.2, n_colors = 10, superpixel_size = 10):

    # load image
    #img_name = "test.jpg"
    #img_name = "./examples/original/test.jpg"

    img = Image.open(input_path)
    img_size = img.size

    # boost saturation of image 
    sat_booster = ImageEnhance.Color(img)
    img = sat_booster.enhance(float(saturation))

    # increase contrast of image
    contr_booster = ImageEnhance.Contrast(img)
    img = contr_booster.enhance(float(contrast))

    # reduce the number of colors used in picture
    img = img.convert('P', palette=Image.ADAPTIVE, colors=int(n_colors))

    # reduce image size
    reduced_size = (img_size[0] // superpixel_size, img_size[1] // superpixel_size)
    img = img.resize(reduced_size, Image.BICUBIC)

    # resize to original shape to give pixelated look
    img = img.resize(img_size, Image.BICUBIC)

    # plot result
    img.save(output_path)
