import os, sys
from PIL import Image, ImageColor
import numpy as np
from rich.progress import Progress

color_hexes = {
  "alice_blue": "F0F8FF",
  "antique_white": "FAEBD7",
  "aqua": "00FFFF",
  "aquamarine": "7FFFD4",
  "azure": "F0FFFF",
  "beige": "F5F5DC",
  "bisque": "FFE4C4",
  "black": "000000",
  "blanched_almond": "FFEBCD",
  "blue": "0000FF",
  "blue_violet": "8A2BE2",
  "brown": "A52A2A",
  "burly_wood": "DEB887",
  "cadet_blue": "5F9EA0",
  "chartreuse": "7FFF00",
  "chocolate": "D2691E",
  "coral": "FF7F50",
  "cornflower_blue": "6495ED",
  "cornsilk": "FFF8DC",
  "crimson": "DC143C",
  "cyan": "00FFFF",
  "dark_blue": "00008B",
  "dark_cyan": "008B8B",
  "dark_goldenrod": "B8860B",
  "dark_gray": "A9A9A9",
  "dark_green": "006400",
  "dark_khaki": "BDB76B",
  "dark_magenta": "8B008B",
  "dark_olive_green": "556B2F",
  "dark_orange": "FF8C00",
  "dark_orchid": "9932CC",
  "dark_red": "8B0000",
  "dark_salmon": "E9967A",
  "dark_sea_green": "8FBC8F",
  "dark_slate_gray": "2F4F4F",
  "dark_turquoise": "00CED1",
  "dark_violet": "9400D3",
  "deep_pink": "FF1493",
  "deep_sky_blue": "00BFFF",
  "dim_gray": "696969",
  "dodger_blue": "1E90FF",
  "fire_brick": "B22222",
  "floral_white": "FFFAF0",
  "forest_green": "228B22",
  "fuchsia": "FF00FF",
  "gainsboro": "DCDCDC",
  "ghost_white": "F8F8FF",
  "gold": "FFD700",
  "goldenrod": "DAA520",
  "gray": "808080",
  "green": "008000",
  "green_yellow": "ADFF2F",
  "honeydew": "F0FFF0",
  "hot_pink": "FF69B4",
  "indian_red": "CD5C5C",
  "indigo": "4B0082",
  "ivory": "FFFFF0",
  "khaki": "F0E68C",
  "lavender": "E6E6FA",
  "lavender_blush": "FFF0F5",
  "lawn_green": "7CFC00",
  "lemon_chiffon": "FFFACD",
  "light_blue": "ADD8E6",
  "light_coral": "F08080",
  "light_cyan": "E0FFFF",
  "light_goldenrod_yellow": "FAFAD2",
  "light_green": "90EE90",
  "light_gray": "D3D3D3",
  "light_pink": "FFB6C1",
  "light_salmon": "FFA07A",
  "light_sea_green": "20B2AA",
  "light_sky_blue": "87CEFA",
  "light_slate_gray": "778899",
  "light_steel_blue": "B0C4DE",
  "light_yellow": "FFFFE0",
  "lime": "00FF00",
  "lime_green": "32CD32",
  "linen": "FAF0E6",
  "magenta": "FF00FF",
  "maroon": "800000",
  "medium_aquamarine": "66CDAA",
  "medium_blue": "0000CD",
  "medium_orchid": "BA55D3",
  "medium_purple": "9370DB",
  "medium_sea_green": "3CB371",
  "medium_slate_blue": "7B68EE",
  "medium_spring_green": "00FA9A",
  "medium_turquoise": "48D1CC",
  "medium_violet_red": "C71585",
  "midnight_blue": "191970",
  "mint_cream": "F5FFFA",
  "misty_rose": "FFE4E1",
  "moccasin": "FFE4B5",
  "navajo_white": "FFDEAD",
  "navy": "000080",
  "old_lace": "FDF5E6",
  "olive": "808000",
  "olive_drab": "6B8E23",
  "orange": "FFA500",
  "orange_red": "FF4500",
  "orchid": "DA70D6",
  "pale_goldenrod": "EEE8AA",
  "pale_green": "98FB98",
  "pale_turquoise": "AFEEEE",
  "pale_violet_red": "DB7093",
  "papay_whip": "FFEFD5",
  "peach_puff": "FFDAB9",
  "peru": "CD853F",
  "pink": "FFC0CB",
  "plum": "DDA0DD",
  "powder_blue": "B0E0E6",
  "purple": "800080",
  "red": "FF0000",
  "rosy_brown": "BC8F8F",
  "royal_blue": "4169E1",
  "saddle_brown": "8B4513",
  "salmon": "FA8072",
  "sandy_brown": "F4A460",
  "sea_green": "2E8B57",
  "seashell": "FFF5EE",
  "sienna": "A0522D",
  "silver": "C0C0C0",
  "sky_blue": "87CEEB",
  "slate_blue": "6A5ACD",
  "slate_gray": "708090",
  "snow": "FFFAFA",
  "spring_green": "00FF7F",
  "steel_blue": "4682B4",
  "tan": "D2B48C",
  "teal": "008080",
  "thistle": "D8BFD8",
  "tomato": "FF6347",
  "turquoise": "40E0D0",
  "violet": "EE82EE",
  "wheat": "F5DEB3",
  "white": "FFFFFF",
  "white_smoke": "F5F5F5",
  "yellow": "FFFF00",
  "yellow_green": "9ACD32",
}

print("What size should the image be? (Screen size is 480x240)")
size_x = 240
size_y = 240
try:
    size_x = int(input("(240) > "))
    size_y = int(input("(240) > "))
except ValueError:
    print("Using 240 x 240")
    size_x = 240
    size_y = 240
size = size_x, size_y

img_pth = sys.argv[1]
print(img_pth)

tmpfile = os.path.splitext(img_pth)[0] + "-resized.jpeg"
try: 
    img = Image.open(img_pth)
    img.thumbnail(size, Image.Resampling.LANCZOS)
    img.save(tmpfile, "JPEG")
except IOError:
    print("nuh uh")

for name in color_hexes:
    color_hexes[name] = ImageColor.getcolor("#" + color_hexes[name], "RGB")

possible_values = []
for color in color_hexes:
    possible_values.append(color_hexes[color])

print("Compressed Image")

im2: Image

with Progress() as progress:
    task1 = progress.add_task("[green]Filter Image...", total=(size_x * size_y))
    task2 = progress.add_task("[red]Find Colors...", total=(size_x * size_y))
    try:
        im = Image.open(tmpfile);
        pixels = list(im.getdata())
        width, height = im.size
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        
        list_pixels = []

        for row in pixels:
            row_pixels = []
            for pixel in row:
                colors = np.array(possible_values)
                color = np.array(pixel)
                distances = np.sqrt(np.sum((colors-color)**2,axis=1))
                index_of_smallest = np.where(distances==np.amin(distances))
                smallest_distance = colors[index_of_smallest]
                pixel = [smallest_distance[0][0], smallest_distance[0][1], smallest_distance[0][2]]
                row_pixels.append(pixel)
                progress.advance(task1)
            list_pixels.append(row_pixels)

        im2 = Image.fromarray(np.uint8(list_pixels))
        im2.save(os.path.splitext(img_pth)[0] + "-filtered.jpeg", "JPEG")
    except IOError:
        print("nuh uh")

    print("Filtered image to colorspace")

    #TODO:
    # Put image into massive array of names and pixel locations
    # Detect horizontal lines
    # Put list of lines and colors into arrays
    # Sort arrays by color used
    # Write code to output file

    idata = list(im2.getdata())
    namedata = []
    row_names = []
    i = 0
    for pixel in idata:
        name = list(color_hexes.keys())[
                list(color_hexes.values()).index(pixel)
            ]
        row_names.append(name)
        i += 1
        if (i == size_x):
            namedata.append(row_names)
            row_names = []
            i = 0
        progress.advance(task2)
    with open("color_name_data.txt", "+w") as f:
        f.write(str(namedata))

    task3 = progress.add_task("[yellow]Convert to JSON...", total=(size_x * size_y))

    finaldata = []
    current_string = None
    current_count = 0
    for row in namedata:
        for item in row:
            progress.advance(task3)
            if item == current_string: current_count += 1
            else:
                if current_string is not None:
                    finaldata.append({"color": current_string, "count": current_count})
                current_string = item
                current_count = 1
    if current_string is not None:
        finaldata.append({"color": current_string, "count": current_count})
    print(len(finaldata))
    with open("final_color_data.json", "+w") as f:
            f.write(str(finaldata))


print("Got color names")