import numpy as np
from  PIL import Image
import argparse

# https://github.com/sunset1995/py360convert
from py360convert import e2c, c2e

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog="convert.py",
        description="convert an equirectangular image to a cube image.",
        epilog="-",
        add_help=True
        )
    parser.add_argument("-e", "--eq_image", help="captured equirectangular image", action="store", type=str, required=True)
    parser.add_argument("-d", "--dim_cube", help="a dimension of a cube", action="store", type=int, default=2048)
    parser.add_argument("-c", "--cb_image", help="a name of output cube image", action="store", type=str, default="")

    args = parser.parse_args()
    print(args.eq_image)
    print(args.dim_cube)
    if args.cb_image == "":
        ite = args.eq_image.rfind(".")
        args.cb_image = args.eq_image[:ite] + "_cubed" + args.eq_image[ite:]
    print(args.cb_image)

    e_img = Image.open(args.eq_image)
    
    e_img.show()
    c_img = e2c(np.array(e_img), args.dim_cube)
    c_img = Image.fromarray(c_img.astype(np.uint8))
    c_img.show()
    c_img.save(args.cb_image, quality=95)

    





    




