import requests
from PIL import Image
from PIL import ImageColor

im = Image.open("war.png")
im = im.convert('RGB')
width, height = im.size
original_colors = im.getcolors()
print("original")
print(original_colors)

response = requests.get('https://api.noopschallenge.com/hexbot?count=' + str(len(original_colors)))

hexbot_colors = []
for color in response.json()['colors']:
    hexbot_colors.append(ImageColor.getrgb(color['value']))

color_converter = {}

x = 0
for color in original_colors:
    print(color)
    color_converter[color[1]] = hexbot_colors[x]
    x += 1

new_image = im

print("Before making new image.")
for x in range(width):
    for y in range(height):
        new_image.putpixel((x,y), color_converter[im.getpixel((x,y))])

new_image.save("test.png", "PNG")
