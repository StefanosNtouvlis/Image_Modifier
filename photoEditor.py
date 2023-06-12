from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"
pathOut = "/editedImgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    # img_gray = img.convert("L")
    # img_gray_smooth = img_gray.filter(ImageFilter.SMOOTH)
    # edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)

    sharpened = img.filter(ImageFilter.SHARPEN)
    detailed = sharpened.filter(ImageFilter.DETAIL)

    enhancer = ImageEnhance.Contrast(detailed)
    enhanced = enhancer.enhance(factor=1.5)

    brightener = ImageEnhance.Brightness(enhanced)
    brightened = brightener.enhance(factor=0.8)

    clean_name = os.path.splitext(filename)[0]

    brightened.save(f".{pathOut}/{clean_name}_edited.jpg", dpi=(300, 300))

# Credits to Internet Made Coder for the inspiration.
