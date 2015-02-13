"""
Script pour recadrer une image en image carre en gardant le ratio en en positionnant
l'image au milieu de l'axe "en exces"
"""

from PIL import Image
import sys
import os

# missing input arguments
if not len(sys.argv) >= 2:
    print("Usage: to_square.py name_of_file_1 name_of_file_2 ...")
    sys.exit()

# actual squaring function
def to_square(im_path, save_path):
    im = Image.open(im_path)
    largeur, hauteur = im.size
    if largeur >=hauteur:
        delta = (largeur-hauteur)//2
        im = im.crop((delta,0,delta+hauteur,hauteur))
    else:
        delta = -(largeur-hauteur)//2
        im = im.crop((0,delta,largeur,delta+largeur))
    im.save(save_path)

# apply the squaring function to every image
for image in sys.argv[1:]:
    to_square(os.path.join(os.getcwd(), image),
              os.path.join(os.getcwd(), image[:image.rfind('.')] + "_square" + image[image.rfind('.'):]))
