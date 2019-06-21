from PIL import Image, ImageEnhance

LEVEL = 11
page_url = "http://www.pythonchallenge.com/pc/return/5808.html"
img_path = "..//files//cave.jpg"
img_size = (640, 480)
with Image.open(img_path) as image:
    width, height = image.size
    odd_img = Image.new("RGB", (width//2, height//2), color="white")
    even_img = Image.new("RGB", (width//2, height//2), color="white")
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if (x + y) % 2 == 0:
                even_img.putpixel((x // 2, y // 2), pixel)
            else:
                odd_img.putpixel((x // 2, y // 2), pixel)

    bright_even_img = ImageEnhance.Brightness(even_img).enhance(2.5)  # 亮度
    odd_img.save("..//files//odd.png")
    bright_even_img.save("..//files//even.png")

    odd_img.close()
    even_img.close()

