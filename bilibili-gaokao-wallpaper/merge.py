from PIL import Image

def is_grayscale(r, g, b, threshold=30):
    """判断像素是否接近黑白灰色"""
    return abs(r - g) < threshold and abs(g - b) < threshold and abs(r - b) < threshold

def invert_grayscale_pixels(image):
    """将接近黑白灰色的像素反色"""
    pixels = image.load()
    width, height = image.size
    
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]  # 获取RGBA值
            
            if is_grayscale(r, g, b):
                # 反色处理，保留透明度
                pixels[x, y] = (255 - r, 255 - g, 255 - b, a)
    
    return image

# 打开大图片和小图片
big_img = Image.open('c5cf74353f91ec4b69c81855f00f69e0.png').convert('RGBA')
small_img = Image.open('e93cac58c6c806ed1f7afb68117e1dd8.png').convert('RGBA')

# 处理小图片（反色接近黑白灰的像素）
small_img = invert_grayscale_pixels(small_img)

# 计算小图片放置在大图片中心的位置
bx, by = big_img.size
sx, sy = small_img.size
paste_x = (bx - sx) // 2
paste_y = (by - sy) // 2

# 创建一个透明图层用于合成
result = Image.new('RGBA', big_img.size, (0, 0, 0, 0))
result.paste(big_img, (0, 0))
result.paste(small_img, (paste_x, paste_y), small_img)  # 第三个参数用于保留透明度

# 保存结果
result.save('result.png')