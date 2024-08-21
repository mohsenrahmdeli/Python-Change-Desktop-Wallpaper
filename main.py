import ctypes
import os
import random

def change_wallpaper():
    # Specify the path of the images folder
    wallpaper_folder = "C:/Path/To/Your/Wallpapers"
    
    # List of image files in the folder
    wallpapers = [os.path.join(wallpaper_folder, f) for f in os.listdir(wallpaper_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # Random selection of an image
    wallpaper = random.choice(wallpapers)
    
    # Setting the desktop image
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 3)

if __name__ == "__main__":
    change_wallpaper()
