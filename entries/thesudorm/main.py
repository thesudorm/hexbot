import requests
from PIL import Image
from PIL import ImageColor

im = Image.open("strawhat.png")
width, height = im.size
original_colors = im.getcolors()

response = requests.get('https://api.noopschallenge.com/hexbot?count=' + str(len(original_colors)))

hexbot_colors = []
for color in response.json()['colors']:
    hexbot_colors.append(ImageColor.getrgb(color['value']))


color_converter = {}

x = 0
for color in original_colors:
    color_converter[color[1]] = hexbot_colors[x]
    x += 1

print(color_converter)
new_image = im

for x in range(width):
    for y in range(height):
        color = new_image.getpixel((x, y))
