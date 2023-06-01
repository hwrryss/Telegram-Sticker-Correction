import os, sys
import cv2
from cv2 import dnn_superres
import math
from cprint import *
from PIL import Image

def jpg2png(path, stickers):
    for i, sticker in enumerate(stickers):
        if str(sticker).endswith(".jpg"):
            print(path + sticker)
            im = Image.open(path + sticker)
            im.save(path + f"sticker{i}.png")
            os.remove(path+sticker)


def crop_to_size(img):
    img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)

    return img

def upscale_image(img, upscaling_value):
    sr = dnn_superres.DnnSuperResImpl_create()

    path = f"./models/EDSR_x{upscaling_value}.pb"
    sr.readModel(path)

    sr.setModel("edsr", upscaling_value)

    upscaled_image = sr.upsample(img)

    return upscaled_image


def main(path):
    cprint("Initialized main")

    stickers = os.listdir(path)

    jpg2png(path, stickers)

    for i, sticker in enumerate(stickers):

        img = cv2.imread(path + sticker)
        w, h = img.shape[1], img.shape[0]

        cprint.ok(f"Working on {sticker}")

        if w < 512 and h < 512: 
            upscaling_value = math.ceil(512/min(w,h))
            if upscaling_value > 4: 
                upscaling_value = 4

            cprint.ok(f"Upscaling {sticker} {w, h} with factor {upscaling_value}")
            img = upscale_image(img, upscaling_value)
        
        cprint.ok(f"Resizing {sticker}")
        img = crop_to_size(img)

        if "result" not in os.listdir():
            os.mkdir("result")
        cv2.imwrite(f"./result/sticker_{i}.png", img)
        

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    else:
        cprint.err("No arguments specified")
        exit()

    if "-h" in sys.argv or "--help" in sys.argv:
        cprint.ok("Usage: python3 correction.py $path_to_directory\nOutput will be in the /result directory.")
    else:
        if path:
            main(path)