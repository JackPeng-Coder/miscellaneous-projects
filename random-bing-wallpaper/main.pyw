import requests
import warnings
import time
import sys
import os
import ctypes
import hashlib
import random
import shutil
from pathlib import Path

# 忽略警告
warnings.filterwarnings("ignore")

# 设置壁纸的Windows API常量
SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDWININICHANGE = 0x02

def set_wallpaper(path):
    """设置Windows桌面壁纸"""
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(path), SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)

def calculate_sha256(file_path):
    """计算文件的SHA256哈希值"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def download_wallpaper(url, save_path):
    """从指定URL下载壁纸并保存到本地"""
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            file.write(response.content)
        return True
    except Exception as e:
        print(f"下载失败: {e}")
        return False

def get_random_wallpaper(pictures_folder):
    """从Pictures文件夹中随机选取一张图片"""
    images = list(pictures_folder.glob("*.jpg")) + list(pictures_folder.glob("*.jpeg")) + list(pictures_folder.glob("*.png"))
    return random.choice(images) if images else None

def main():
    sleep_time = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    url = "https://bing.img.run/rand.php"
    wallpaper_path = Path(os.getcwd()) / "wallpaper.jpg"
    pictures_folder = Path(os.getcwd()) / "Pictures"
    pictures_folder.mkdir(exist_ok=True)

    print(f"Pictures文件夹路径: {pictures_folder}")

    while True:
        if download_wallpaper(url, wallpaper_path):
            sha256_hash = calculate_sha256(wallpaper_path)
            new_wallpaper_path = pictures_folder / f"{sha256_hash}.jpg"
            if new_wallpaper_path.exists():
                new_wallpaper_path.unlink()
            shutil.move(wallpaper_path, new_wallpaper_path)
            set_wallpaper(new_wallpaper_path)
        else:
            random_wallpaper = get_random_wallpaper(pictures_folder)
            if random_wallpaper:
                set_wallpaper(random_wallpaper)
            else:
                print("Pictures文件夹中没有可用的图片。")

        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
