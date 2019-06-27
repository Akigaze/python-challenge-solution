from PIL import Image, ImageEnhance

LEVEL = 12
page_url = "http://www.pythonchallenge.com/pc/return/evil.html"
evil1_img_path = "..//files//12//evil1.jpg"
evil2_img_path = "..//files//12//evil2.jpg"
evil3_img_path = "..//files//12//evil3.jpg"
evil2_gfx_path = "..//files//12//evil2.gfx"

gfx_data = None
GAP = 5

with open(evil2_gfx_path, "rb") as gfx:
    gfx_data = gfx.read()
    print(gfx_data)
    print(len(gfx_data))

if gfx_data:
    for i in range(GAP):
        with open("..//files//12//%d.jpg" % i, "wb") as output:
            output.write(gfx_data[i::GAP])
