# add_descriptions_to_theta360
RICHO Thetaなどで撮影した全天球画像に説明を追加する、という目的で作成したスクリプトです。
## convert_e2c.py
: 全天球画像（equirectangular image）をサイコロ状に展開した画像（cubed image）に展開します。

```
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
```

-eで全天球画像、-dでサイコロ状にした際の一辺のサイズ（ピクセル）、-cで出力するサイコロ画像の名称を指定します。

具体の変換についてはhttps://github.com/sunset1995/py360convert をお借りしています。

![image](https://user-images.githubusercontent.com/39890894/163902291-0a322639-a124-435f-8149-b20363a3cdc4.png)

## convet_c2e.py
: サイコロ状に展開した画像（cubed image）を全天球画像（equirectangular image）に変換します。

```
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
```

-eで全天球画像、-cでサイコロ画像、-oで出力する全天球画像の名称を指定します。変換については上と同じくhttps://github.com/sunset1995/py360convert をお借りしています。

Google Photoなどに全天球画像をアップロードすると自動的に球状にマップされGoogle Street Viewのように操作可能な状態になりますが、これは画像（jpeg）内に埋め込まれる[Photo Sphere XMP](https://developers.google.com/streetview/spherical-metadata?hl=ja&fbclid=IwAR37LZ9-3NHf0gHG1B78e0tBJECoz7qUS2_fdZh1ZHt_wRJ7NT7vX8kXwUg)というセグメントの働きのようです。カメラ情報や撮影位置を記録するExifと似たような感じでしょうか。xmpセグメントは画像処理ソフトウェアで編集すると失われるようですので、このスクリプトでは元の全天球画像からこのセグメントを複製し、出力ファイルに埋め込んでいます。

出力された画像を[Google Photoにアップロードする](https://photos.app.goo.gl/gSbU9LbGbh1EAi8v8)と若干歪みがあるものの、それらしく説明が追加できているのが確認できると思います。全天球画像のままこの手の説明を加えてもよいのですが、キューブ化したほうが直線がちゃんと直線になる（ただしキューブのエッジでは折れる）ので便利でした。

\#Google Photoにアップロードしながら試行していたのですが、失敗画像（セグメントの埋め込みに失敗したもの）もしばらくしたら「パノラマを作成した」とのことで全天球画像として認識されていました笑。確認していませんがもしかしたらそれらしい画像には自動的にセグメントを埋め込んでくれるのかもしれません。

![image](https://user-images.githubusercontent.com/39890894/163903687-b88b3986-18f8-4f2f-8427-0e8cbc7f74e6.png)


## links

https://github.com/sunset1995/py360convert

下記のサイトですともう少し凝った全天球のセグメントを埋め込む方法が紹介されています。
https://qiita.com/mana_544/items/3245ce87f0a0fca80c2a

https://hp.vector.co.jp/authors/VA032610/JPEGFormat/StructureOfJPEG.htm


