import base64
from PIL import Image
import io
import glob
import numpy as np
from natsort import natsorted

path = "Frames/*"


def CreateGIF(frame_folder, file_name):
    files = glob.glob(path)
    images = []
    files = natsorted(files)
    for i in files:
        im = Image.open(i)
        images.append(im)

    frame_one = images[0]
    save_path = "GIFs/" + file_name + ".gif"
    frame_one.save(save_path, format="GIF", append_images=images,
                   save_all=True, duration=125, loop=0)


CreateGIF(path, "All-Data-NoFilter")
