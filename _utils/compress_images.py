"""
Comprass images using ImageMagick

Command used to compress images:
python compress_images.py --quality 30 --replace_original --pattern "../assets/images/author_images/*"
"""


import argparse
import glob
import os
import subprocess


SIZE_THRESHOLD = 25
# Version: ImageMagick 6.9.7-4 Q16 x86_64 20170114 http://www.imagemagick.org
IMAGEMAGICK_COMMAND = r'convert -sampling-factor 4:2:0 -strip -interlace JPEG -colorspace RGB'


def compress_image(image_path, quality, replace_original=False):
    # Image size in Kilobytes
    image_size = os.path.getsize(image_path) / 1000
    if image_size > SIZE_THRESHOLD:
        print(f"Compressing image '{image_path}' ({image_size}K)")
        if replace_original:
            new_path = image_path
        else:
            file_name, extension = os.path.basename(image_path).split(".")
            new_file_name = file_name + "_reduced." + extension
            new_path = os.path.join(os.path.dirname(image_path), new_file_name)
        subprocess.run(f"{IMAGEMAGICK_COMMAND} -quality {quality}% {image_path} {new_path}", shell=True)
        print(f">>> New file created: '{new_path}'")
    else:
        print(f"The image '{image_path}' ({image_size}K) does not need compression.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to compress images using ImageMagick.")
    parser.add_argument("--quality", help="compression level", type=int, default=50)
    parser.add_argument("--replace_original", help="replace original image with compressed one", action='store_true')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file_path", help="image file path", action="append", type=str)
    group.add_argument("--pattern", help="glob pattern for images", type=str)
    args = parser.parse_args()
    print(f"Compressing images with size greater than {SIZE_THRESHOLD}K.")

    if args.file_path:
        print(args.file_path)
        for p in args.file_path:
            if os.path.exists(p):
                compress_image(p, args.quality, args.replace_original)
            else:
                print(f"ERROR: The file '{p}' does not exists.")
    else:
        paths = glob.glob(args.pattern)
        for p in paths:
            compress_image(p, args.quality, args.replace_original)
