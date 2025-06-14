import pygame
import sys
import pickle
import random
import time
import math

class Text:
    def __init__(self, text):
        self.text = text
        self.pixel_size = height//20 if len(text) <= 1 else width//len(text)//20
        self.pixel_start = ((width-self.pixel_size*16*len(text))//2, (height-self.pixel_size*16)//2)
        self.chars = []
        for num in range(len(self.text)):
            for x, y in data[ord(self.text[num])]:
                self.chars.append((x+num*16, y))
                
    def draw(self):
        random.shuffle(self.chars)

        for x, y in self.chars:
            pygame.draw.rect(window, "WHITE", (
                self.pixel_start[0]+x*self.pixel_size,
                self.pixel_start[1]+y*self.pixel_size,
                self.pixel_size,
                self.pixel_size
            ))
        pygame.display.update()

    def replace(self, to_text, run_time=1):
        to_pixel_size = height//20 if len(to_text) <= 1 else width//len(to_text)//20
        to_pixel_start = ((width-to_pixel_size*16*len(to_text))//2, (height-to_pixel_size*16)//2)
        to_chars = []
        for num in range(len(to_text)):
            for x, y in data[ord(to_text[num])]:
                to_chars.append((x+num*16, y))
        random.shuffle(self.chars)
        random.shuffle(to_chars)

        start = time.time()
        last = 0
        blank = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            window.fill("BLACK")
            if last == 1:break
            last = (time.time() - start) / run_time
            if last > 1:last = 1
            
            if len(self.chars) == 0 or len(to_chars) == 0 or blank:
                self.__init__(to_text)
                self.draw()
                pygame.display.update()
                blank = True
                continue
            if len(self.chars) >= len(to_chars):
                for i in range(max(len(self.chars), len(to_chars))):
                    pygame.draw.rect(window, "WHITE", (
                        transform(self.pixel_start[0]+self.chars[i][0]*self.pixel_size, to_pixel_start[0]+to_chars[i%len(to_chars)][0]*to_pixel_size, last),
                        transform(self.pixel_start[1]+self.chars[i][1]*self.pixel_size, to_pixel_start[1]+to_chars[i%len(to_chars)][1]*to_pixel_size, last),
                        transform(self.pixel_size, to_pixel_size, last),
                        transform(self.pixel_size, to_pixel_size, last)
                    ))
            else:
                for i in range(max(len(self.chars), len(to_chars))):
                    pygame.draw.rect(window, "WHITE", (
                        transform(self.pixel_start[0]+self.chars[i%len(self.chars)][0]*self.pixel_size, to_pixel_start[0]+to_chars[i][0]*to_pixel_size, last),
                        transform(self.pixel_start[1]+self.chars[i%len(self.chars)][1]*self.pixel_size, to_pixel_start[1]+to_chars[i][1]*to_pixel_size, last),
                        transform(self.pixel_size, to_pixel_size, last),
                        transform(self.pixel_size, to_pixel_size, last)
                    ))

            pygame.display.update()
        self.__init__(to_text)

    
def transform(from_, to_, t):
    return from_ + (to_ - from_) * change(t)

def change(num):
    return (-math.cos(num * math.pi) + 1) / 2

pygame.init()
window = pygame.display.set_mode()
width, height = window.get_size()
pygame.display.set_caption("Animation")
data = pickle.load(open("data.dat", "rb"))

text = Text("")
while True:
    text.replace(chr(random.randint(0x4e00, 0x9fff)), 2)
    time.sleep(1)
