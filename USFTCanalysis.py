# Function that produces measurements from US image
from PIL import Image, ImageDraw

red_color = (255, 0, 0)
white_color = (255, 255, 255)
trim_color = teal_color = (100, 120, 140)


def usftc_analysis(image_path: str):

    img = Image.open(image_path).convert("RGB")
    
    # Image needs to be rotated for consistent analyisis
    width, height = img.size
    top_pixel_coords = []
    for x in range(width):
        for y in range(height):
            

    