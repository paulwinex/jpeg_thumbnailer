from PIL import Image
import os


def compress(src, size_h=1000, size_w=1000, quality=50):
    im = Image.open(src)
    im.thumbnail([size_h, size_w], Image.ANTIALIAS)
    trg_folder = os.path.join(os.path.dirname(src), 'resize')
    if not os.path.exists(trg_folder):
        os.makedirs(trg_folder)
    trg = os.path.join(trg_folder, os.path.basename(src))
    im.save(trg, optimize=True, quality=quality)
    return trg