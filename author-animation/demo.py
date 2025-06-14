from PIL import Image

image = Image.open("unifont-15.0.01.bmp")
text = "天道酬勤"
result = []


for i in range(len(text)):
    code = ord(text[i])
    for x in range(16):
        for y in range(16):
            if image.getpixel((code % 256 * 16 + x + 32, code // 256 * 16 + y + 64)) == 0:
                result.append((x+i*16) * 16 + y)

import pyperclip
pyperclip.copy(str(result))

