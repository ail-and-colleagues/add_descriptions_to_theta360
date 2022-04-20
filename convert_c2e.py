from tkinter.tix import IMAGE
import numpy as np
import struct
from  PIL import Image
import argparse

# https://github.com/sunset1995/py360convert
from py360convert import e2c, c2e

# references regarding jpeg xmp segments.
# https://qiita.com/mana_544/items/3245ce87f0a0fca80c2a
# https://hp.vector.co.jp/authors/VA032610/JPEGFormat/StructureOfJPEG.htm


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog="convert.py",
        description="convert an equirectangular image to a cube image.",
        epilog="-",
        add_help=True
        )

    parser.add_argument("-e", "--eq_image", help="captured equirectangular image", action="store", type=str, required=True)
    parser.add_argument("-c", "--cb_image", help="a name of output cube image", action="store", type=str, required=True)
    parser.add_argument("-o", "--out_image", help="a name of output equirectangular image", action="store", type=str, default="")
    
    args = parser.parse_args()
    print(args.eq_image)
    print(args.cb_image)

    # name an output image when -o is not specified.
    if args.out_image == "":
        ite = args.eq_image.rfind(".")
        args.out_image = args.eq_image[:ite] + "_moded" + args.eq_image[ite:]
    print(args.out_image)

    c_img = Image.open(args.cb_image)
    e_img = Image.open(args.eq_image)
    print(np.array(c_img).shape)

    # convert the inputted cube image to an equirectangular image.
    em_img = c2e(np.array(c_img), w=e_img.size[0], h=e_img.size[1])
    print(em_img.shape, type(em_img))

    # save the converted image as _temp.JPG.
    ite = args.eq_image.rfind("\\")
    temp_image = args.eq_image[:ite] + "\\_temp.JPG"
    Image.fromarray(em_img.astype(np.uint8)).save(temp_image, quality=95)

    # fetch exif_app_seg and variable from the original equirectangular image inputted via -e.
    exif_app_seg = None
    photo_sphere_app_seg = None
    applist = e_img.applist
    for c in applist:
        print(c[0], c[1][:30])
        if c[1].find(b"Exif") >= 0:
            print("copy exif_app_seg from: ", c[0])
            exif_app_seg = c[1]
        if c[1].find(b"GPano") >= 0:
            print("copy photo_sphere_app_seg from: ", c[0])       
            photo_sphere_app_seg = c[1]
    
    if photo_sphere_app_seg is None:
        raise Exception("photo_sphere_app_seg cannot found.")
    
    with open(temp_image, mode='rb') as temp:
            with open(args.out_image, mode="wb") as out:
                while True:
                    marker =  temp.read(2)
                    t = struct.unpack("BB", marker)
                    decoded_marker = "{:02x}{:02x}".format(t[0], t[1])
                    if decoded_marker[:2] == "ff" and decoded_marker[2:] != "00":
                        if decoded_marker == "ffd8":
                            print("SOI(Start Of Image): ", temp.tell())
                            out.write(marker)
                        elif decoded_marker == "ffd9":
                            # never reach.
                            # the stream position will go EOF and break when the marker SOS(Start Of Scan) is found. 
                            print("EOI(End of Image): ", temp.tell())
                        elif decoded_marker == "ffda":
                            print("SOS(Start Of Scan): ", temp.tell())
                            out.write(marker)
                            # all data including the marker EOI will be written to the output image.
                            out.write(temp.read())
                            break
                        else:
                            # process for other markers.
                            data_length = temp.read(2)
                            decoded_data_length = struct.unpack(">H", data_length)[0]
                            print("marker: {}, pos:{}, len: {} {}".format(decoded_marker, temp.tell(), decoded_data_length, data_length))
                            data = temp.read(decoded_data_length - 2)
                            out.write(marker)
                            out.write(data_length)
                            out.write(data)
                            print(data[:20])

                            if decoded_marker == "ffe0":
                                # add exif after the ffe0 segment if exists.
                                if exif_app_seg:
                                    out.write(b"\xff\xe1")
                                    num = len(exif_app_seg) + 2
                                    out.write(num.to_bytes(2, 'big'))
                                    out.write(exif_app_seg)

                                # add photo_sphere_app_seg after the ffe0 segment.
                                out.write(b"\xff\xe1")
                                num = len(photo_sphere_app_seg) + 2
                                out.write(num.to_bytes(2, 'big'))
                                out.write(photo_sphere_app_seg)

    # chk
    o_img = Image.open(args.out_image)
    applist = o_img.applist
    for c in applist:
        print(c[0], c[1][:30])




    




