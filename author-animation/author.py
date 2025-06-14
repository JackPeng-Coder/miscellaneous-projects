from pygame import *
import pygame
import time
from math import *
from random import shuffle
import sys

def displayAuthor(surface : Surface, fontPath, actionListener=None):
    author = [2, 14, 18, 21, 23, 24, 25, 26, 30, 31, 34, 37, 39, 42, 44, 46, 50, 53, 55, 58, 61, 62, 64, 65, 66, 67, 68, 69, 71, 74, 78, 82, 85, 87, 90, 93, 98, 101, 103, 106, 108, 109, 114, 117, 119, 120, 121, 122, 125, 130, 141, 159, 165, 170, 175, 180, 185, 190, 195, 200, 205, 209, 210, 215, 220, 229, 230, 234, 235, 264, 279, 293, 294, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 351, 356, 360, 363, 367, 371, 372, 375, 378, 382, 386, 388, 390, 393, 394, 398, 400, 401, 404, 407, 408, 409, 411, 413, 420, 425, 428, 436, 441, 443, 445, 450, 452, 454, 457, 458, 462, 467, 468, 471, 479, 484, 485, 488, 495, 521, 527, 531, 537, 542, 547, 552, 556, 557, 563, 567, 579, 582, 595, 597, 604, 611, 612, 621, 622, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 643, 644, 652, 659, 661, 669, 670, 675, 678, 691, 695, 707, 712, 716, 723, 729, 733, 734, 735, 745]
    make = [6, 20, 22, 33, 34, 35, 38, 41, 42, 43, 44, 45, 51, 54, 57, 67, 70, 73, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 99, 102, 105, 108, 115, 118, 121, 125, 131, 134, 137, 138, 139, 140, 150, 163, 164, 165, 166, 167, 168, 169, 170, 171, 190, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 264, 279, 293, 294, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 342, 356, 357, 368, 369, 370, 371, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 403, 407, 411, 419, 423, 427, 435, 439, 443, 451, 455, 459, 467, 475, 483]
    shuffle(author)
    texts = ["《健康游戏忠告》", "抵制不良游戏，拒绝盗版游戏。", "注意自我保护，谨防受骗上当。", "适度游戏益脑，沉迷游戏伤身。", "合理安排时间，享受健康生活。"]
    width, height = surface.get_rect().size
    font = pygame.font.Font(fontPath, floor(.05 * height))
    if actionListener == None:
        def actionListener():
            for e in event.get():
                if e.type == QUIT:
                    sys.exit()

    start = time.time()
    step = 0
    long = 24

    while len(author) > step - long:
        actionListener()
        surface.fill("black")
        step = (time.time() - start) * len(author) / 2.5

        for i in range(len(author))[::-1]:
            if i > step:continue
            elif i > step - long:
                x, y = (author[i] // 16 + .5) * width / 144 + width / \
                    3, (author[i] % 16 + .5) * width / \
                    144 + height / 2 - width / 18
                draw.rect(surface, Color(255 - floor((i - step + long)*255/long), 255 - floor((i - step + long)*255/long), 255 - floor((i - step + long)*255/long)), (
                    x - width / 288 * (i - step + long),
                    y - width / 288 * (i - step + long),
                    width / 144 * (i - step + long),
                    width / 144 * (i - step + long)
                ), width // 288)
            else:
                x, y = (author[i] // 16 + .5) * width / 144 + width / \
                    3, (author[i] % 16 + .5) * width / \
                    144 + height / 2 - width / 18
                draw.rect(surface, "white", (
                    x - width / 288,
                    y - width / 288,
                    width / 144,
                    width / 144
                ))
        display.update()

    start = time.time()
    step = 0
    long = 10
    while step - long / 48 < 1:
        actionListener()
        surface.fill("black")
        step = time.time() - start

        for i in author:
            if step < 1:
                x, y = (i // 16 + .5) * width / 144 + width / \
                    3 - width * (cos(pi*(step+1))+1) / 2 / 18, (i % 16 + .5) * width / \
                    144 + height / 2 - width / 18
            else:
                x, y = (i // 16 + .5) * width / 144 + width / \
                    3 - width / 18, (i % 16 + .5) * width / \
                    144 + height / 2 - width / 18
            draw.rect(surface, "white", (
                x - width / 288,
                y - width / 288,
                width / 144,
                width / 144
            ))
        
        for i in make:
            if i // 16 + i % 16 > step * 48:continue
            elif i // 16 + i % 16 > step * 48 - long:
                x, y = (i // 16 + 192.5) * width / \
                    288 - width * (cos(pi*(step+1))+1) / 36, \
                    (i % 16 + .5) * width / 288 + 144 * height / 288
                draw.rect(surface, "white", (
                    x - width / 576 * ((step * 48 - i // 16 - i % 16) / long),
                    y - width / 576 * (step * 48 - i // 16 - i % 16) / long,
                    width / 288 * (step * 48 - i // 16 - i % 16) / long,
                    width / 288 * (step * 48 - i // 16 - i % 16) / long
                ))
            elif step < 1:
                x, y = (i // 16 + 192.5) * width / \
                    288 - width * (cos(pi*(step+1))+1) / 36, \
                    (i % 16 + .5) * width / 288 + 144 * height / 288
                draw.rect(surface, "white", (
                    x - width / 576,
                    y - width / 576,
                    width / 288,
                    width / 288
                ))
            else:
                x, y = (i // 16 + 192.5) * width / \
                    288 - width / 18, \
                    (i % 16 + .5) * width / 288 + 144 * height / 288
                draw.rect(surface, "white", (
                    x - width / 576,
                    y - width / 576,
                    width / 288,
                    width / 288
                ))


        display.update()

    start = time.time()
    step = 0
    while step < 2.5:
        actionListener()
        surface.fill("black")
        step = time.time() - start
        if step < 1.5:
            color = "white"
        elif step < 2.5:
            color = Color(floor((2.5-step)*255), floor((2.5-step)*255), floor((2.5-step)*255))
        else:break

        for i in author:
            x, y = (i // 16 + .5) * width / 144 + width / \
                3 - width / 18, (i % 16 + .5) * width / \
                144 + height / 2 - width / 18
            draw.rect(surface, color, (
                x - width / 288,
                y - width / 288,
                width / 144,
                width / 144
            ))
    
        for i in make:
            x, y = (i // 16 + 192.5) * width / \
                288 - width / 18, \
                (i % 16 + .5) * width / 288 + 144 * height / 288
            draw.rect(surface, color, (
                x - width / 576,
                y - width / 576,
                width / 288,
                width / 288
            ))

        display.update()

    start = time.time()
    step = 0
    while step < 4:
        actionListener()
        surface.fill("black")
        step = time.time() - start
        if step < 1:
            color = Color(floor(step*255), floor(step*255), floor(step*255))
        elif step < 2.5:
            color = "white"
        elif step < 3.5:
            color = Color(floor((-step+3.5)*255), floor((-step+3.5)*255), floor((-step+3.5)*255))
        else:break

        for i in range(len(texts)):
            text = font.render(texts[i], True, color)
            surface.blit(text, text.get_rect(center=(.5*width, (.3 + i * .1)*height)))
        
        display.update()

if __name__ == "__main__":
    init()
    window = display.set_mode(flags=FULLSCREEN)
    print(window.get_size())
    while True:
        start = time.time()
        displayAuthor(window, "HarmonyOS_Sans_SC_Regular.ttf")
        print(time.time() - start)
    text = font.Font("HarmonyOS_Sans_SC_Regular.ttf", 72).render("[游戏主菜单(懒得做)]", True, "white")
    window.blit(text, text.get_rect(center=window.get_rect().center))
    display.update()
    while True:
        for e in event.get():
            if e.type == QUIT:sys.exit()

        
