# add_descriptions_to_theta360
RICHO Thetaなどで撮影した全天球映像に説明を追加する、という目的で作成しました。
## convert_e2c.py
: 全天球映像（equirectangular image）をサイコロ状に展開した映像（cubed image）に展開します。

"""
usage: convert.py [-h] -e EQ_IMAGE [-d DIM_CUBE] [-c CB_IMAGE]

convert an equirectangular image to a cube image.

optional arguments:
  -h, --help            show this help message and exit
  -e EQ_IMAGE, --eq_image EQ_IMAGE
                        captured equirectangular image
  -d DIM_CUBE, --dim_cube DIM_CUBE
                        a dimension of a cube
  -c CB_IMAGE, --cb_image CB_IMAGE
                        a name of output cube image
"""

-eで全天球映像、-dでサイコロ状にした際の一辺のサイズ（ピクセル）、-cで出力するサイコロ映像の名称を指定します。

具体の変換についてはhttps://github.com/sunset1995/py360convertをお借りしています。

## convet_c2e.py
: サイコロ状に展開した映像（cubed image）を全天球映像（equirectangular image）に変換します。

"""
usage: convert.py [-h] -e EQ_IMAGE -c CB_IMAGE [-o OUT_IMAGE]

convert an equirectangular image to a cube image.

optional arguments:
  -h, --help            show this help message and exit      
  -e EQ_IMAGE, --eq_image EQ_IMAGE
                        captured equirectangular image
  -c CB_IMAGE, --cb_image CB_IMAGE
                        a name of output cube image
  -o OUT_IMAGE, --out_image OUT_IMAGE
                        a name of output equirectangular image
"""

-eで全天球映像、-cでサイコロ映像、-oで出力する全天球映像の名称を指定します。Google Photoなどに全天球映像をアップロードすると自動的に球状にマップされGoogle Street　Viewのように操作可能な状態になりますが、これはxmpと

