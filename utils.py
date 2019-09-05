import os

def getImageList(dir_path):
    imageNames = [name for name in os.listdir(dir_path) if name.endswith('.jpg') or name.endswith('.png') or name.endswith('.bmp') ]
    return imageNames