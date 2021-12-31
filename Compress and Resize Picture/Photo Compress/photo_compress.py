from PIL import Image
import os

def get_size(file):
    # get the size of file:KB
    size = os.path.getsize(file)
    return size / 1024

def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, suffix)
    return outfile

def compress_image(infile, outfile='', mb=3000, step=10, quality=80):
    """Compress the image to the specified size without changing the size
    :param infile: Source files that need to be compressed
    :param outfile: Saving address of the compressed file
    :param mb: Required image size，KB
    :param step: The compression ratio of each adjustment
    :param quality: Initial compression ratio
    :return: Compressed file address, compressed file size
    """
    o_size = get_size(infile)
    if o_size <= mb:
        return infile
    outfile = get_outfile(infile, outfile)
    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)
    return outfile, get_size(outfile)

def resize_image(infile, outfile='', x_s=1376):
    """Resize the picture
    :param infile: Source files that need to be resized
    :param outfile: Saving address of the resized photo
    :param x_s: Width
    :param y_s: Height
    :return:
    """
    im = Image.open(infile)
    x, y = im.size
    y_s = int(y * x_s / x)
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    outfile = get_outfile(infile, outfile)
    out.save(outfile)


if __name__ == '__main__':
    Address = input("Please enter the address of your picture:")
    Quality = input("Please ENTER the quality of photo you need(enter the number in KB):")
    compress_image(Address,mb=int(Quality))