"""Script pour redimensionner un image avant de la publier sur le web. Les
enregistre dans un sous-dossier nommé LQ
 
Usage:
  resize.py <nom_image_1> ... [--max_w <width>] [--max_h <height>] [-q <quality>]
 
Options:
  -h --help          C'est généré automatiquement.
  --max_h=<valeur>  hauteur maximale
  --max_w=<valeur>   largeur maximmale
  -q qualite de sortie en jpg
 
Copyright Maxime Bellec
"""

from docopt import docopt
from PIL import Image
import sys
import os

max_width, max_height = 1500, 1500

# actual squaring function
def resize(im_path, save_path):
    im = Image.open(im_path)
    ratio = im.size[0]/im.size[1]
    if (ratio >=1):
        # cas largeur plus grande
        if im.size[0] > int(max_width):
            im = im.resize((max_width, int(max_width/ratio)))
    else:
        if im.size[1] > max_height:
            im = im.resize((int(max_width*ratio), max_height))
    im.save(save_path, quality=quality, progressive=True)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    
    save_dir = os.path.join(os.getcwd(), 'LQ')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir) 

    # getting the arguments
    max_width = int(arguments['--max_w'] or 1500)
    max_height = int(arguments['--max_h'] or 1500)
    quality = arguments['-q'] or 60

    # apply the resize function to every image
    for image in arguments['<nom_image_1>']:
        source_path = os.path.join(os.getcwd(), image)
        if not(os.path.isdir(source_path)):
            resize(source_path, os.path.join(os.getcwd(), 'LQ', image))
