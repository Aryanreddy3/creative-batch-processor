# filters.py
from PIL import ImageOps, Image, ImageFilter # type: ignore
import numpy as np # type: ignore

# Grayscale filter
def apply_grayscale(image):
    return ImageOps.grayscale(image)

# Sepia filter
def apply_sepia(image):
    img = np.array(image)
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    tr = 0.393 * r + 0.769 * g + 0.189 * b
    tg = 0.349 * r + 0.686 * g + 0.168 * b
    tb = 0.272 * r + 0.534 * g + 0.131 * b
    tr, tg, tb = np.clip([tr, tg, tb], 0, 255)
    img[:,:,0], img[:,:,1], img[:,:,2] = tr, tg, tb
    return Image.fromarray(img)

# Blur filter
def apply_blur(image):
    return image.filter(ImageFilter.BLUR)

# Brightness adjustment
from PIL import ImageEnhance # type: ignore
def adjust_brightness(image, factor=1.2):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

# Contrast adjustment
def adjust_contrast(image, factor=1.5):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)
