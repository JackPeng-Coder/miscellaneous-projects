from PIL import Image
import pickle
from tqdm.rich import trange

image = Image.open("unifont-15.1.05.bmp")
data = []
for num in trange(65536):
    char = []
    for y in range(num//256*16+64, num//256*16+64+16):
        for x in range(num%256*16+32, num%256*16+32+16):
            if image.getpixel((x,y)) == 0:
                char.append((x%16, y%16))
    data.append(char)

pickle.dump(data, open("data.dat", "wb"))

# Test
data = pickle.load(open('data.dat', 'rb'))
print(data[ord(input("Enter a character: "))])