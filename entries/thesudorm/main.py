import requests
import click

from PIL import Image
from PIL import ImageColor

def get_hexbot_colors(number):
    response = requests.get('https://api.noopschallenge.com/hexbot?count=' + str(number))

    hexbot_colors = []
    for color in response.json()['colors']:
        hexbot_colors.append(ImageColor.getrgb(color['value']))

    return hexbot_colors
    
@click.command()
def random():
    im = Image.open("war.png")
    im = im.convert('RGB')
    width, height = im.size
    original_colors = im.getcolors()

    hexbot_colors = get_hexbot_colors(len(original_colors))
    color_converter = {}

    x = 0
    for color in original_colors:
        color_converter[color[1]] = hexbot_colors[x]
        x += 1

    new_image = im

    for x in range(width):
        for y in range(height):
            new_image.putpixel((x,y), color_converter[im.getpixel((x,y))])
    new_image.save("test.png", "PNG")

if __name__ == '__main__':
    random()
