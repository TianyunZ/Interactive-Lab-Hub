import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

def process_img(path, width, height):
    image = Image.open("imgs/" + path + ".jpg")
    image_ratio = image.width / image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)
    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    image = image.crop((x, y, x + width, y + height))
    return image

mode = 1 # 0 for day mode and 1 for night mode
sky_color = ["#29dfff", "#003d91"]
sun_color = ["#fa5902", "#ffee2e"]
diameter = 40
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    cur_time = time.strftime("%m/%d/%Y %H:%M:%S")
    cur_month = int(time.strftime('%m'))
    cur_hour = int(time.strftime('%H'))
    # cur_month = int(time.strftime("%S")) % 12
    # cur_hour = int(time.strftime("%S")) % 24
    season = "autumn"
    if cur_month in [12, 1, 2]:
        season = "winter"
    elif cur_month in [3, 4, 5]:
        season = "spring"
    elif cur_month in [6, 7, 8]:
        season = "summer"

    period = "night"
    if cur_hour in range(6, 10):
        period = "morning"
        mode = 0
    elif cur_hour in range(10, 14):
        period = "day"
        mode = 0
    elif cur_hour in range(14, 19):
        period = "afternoon"
        mode = 0
    elif cur_hour in range(19, 22):
        period = "evening"
        mode = 1
    else:
        mode = 1

    image = process_img(period, width, height)
    hour = cur_hour
    if mode:
        hour = (cur_hour - 12) if cur_hour > 18 else (cur_hour + 12)
    sun_x = (hour - 6) * (width-diameter) // 12
    sun_y = abs(height-diameter//2-(hour - 6)*((height-diameter//2) // 6))
    if buttonA.value and buttonB.value:
        draw = ImageDraw.Draw(image)
        draw.ellipse((sun_x, sun_y, sun_x + diameter,  sun_y + diameter), fill=sun_color[mode])
    if not buttonA.value and buttonB.value:  # just button A pressed
        # show detailed time
        draw = ImageDraw.Draw(image)
        y = height // 2.5
        x = 10
        draw.ellipse((sun_x, sun_y, sun_x + diameter,  sun_y + diameter), fill=sun_color[mode])
        draw.text((x, y), cur_time, font=font, fill="#000000")
    if not buttonB.value and buttonA.value:  # just button B pressed
        image = process_img(season, width, height)
    if not buttonB.value and not buttonA.value:
        weekday = time.strftime("%A")
        w = int(time.strftime("%w"))
        image = process_img("map", width, height)
        draw = ImageDraw.Draw(image)

        routes = [(170, 18), (100, 18), (44, 46), (115, 59), (173, 67), (120, 100), (44, 110)]
        for x, y in routes[:w]:
            draw.ellipse((x, y, x + 15,  y + 15), fill="#910b09")
        x, y = routes[w]
        draw.ellipse((x, y, x + 15,  y + 15), fill="#fc0400")
        for x, y in routes[w+1:]:
            draw.ellipse((x, y, x + 15,  y + 15), fill="#f7a2a1")
        x, y = routes[w][0]-20, routes[w][1]-15
        font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
        for i in range(5):
            draw.text((x, y), weekday, font=font2, fill="#fc0400")
    disp.image(image, rotation)

    # time.sleep(0.3)
