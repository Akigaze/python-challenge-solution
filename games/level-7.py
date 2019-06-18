import re
from PIL import Image

page_url = "http://www.pythonchallenge.com/pc/def/oxygen.html"
img_url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
img_path = "..//files//oxygen.png"
LEVEL = 7
img = Image.open(img_path, "r")
width, height = img.size
grey_pixels = []
for x in range(width):
    for y in range(height):
        pixel = img.getpixel((x, y))
        if pixel[0] == pixel[1] == pixel[2]:
            grey_pixels.append((x, y))

xs = [p[0] for p in grey_pixels]
ys = [p[1] for p in grey_pixels]

x_count = sorted(set([(x, xs.count(x)) for x in xs]), key=lambda p: p[0])  # 0 - 607
y_count = sorted(set([(y, ys.count(y)) for y in ys]), key=lambda p: p[0])  # 43 - 51

chars = []
for x in range(0, 608, LEVEL):
    pixel = img.getpixel((x, 43))
    chars.append(chr(pixel[0]))

img_secret = "".join(chars)
print(img_secret)  # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
codes = re.findall(r'\d+', img_secret)
print(codes)

solution = "".join([chr(int(n)) for n in codes])
print("solution is : ", solution)

