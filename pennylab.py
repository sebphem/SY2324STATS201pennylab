import sys
from PIL import Image
import os
import numpy

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("usage: %s <filename>" % sys.argv[0])
        sys.exit()


#1400, 500
#1600, 750
file1 = open('pennyyears.txt', 'r')
Lines = file1.readlines()
years = []
for line in Lines:
    years.append(int(line))

red_final_vals = []
green_final_vals = []
blue_final_vals = []
for filename in os.listdir('pennylabphotos'):
    filePath = os.path.join('pennylabphotos', filename)
    # checking if it is a file
    if not os.path.isfile(filePath):
        print("filename %s didnt work" % filePath)
    with Image.open(filePath) as im:
        red_temp_array = []
        blue_temp_array = []
        green_temp_array = []
        for y in range(500,750,1):
            for x in range(1400,1600,1):
                if im.mode == "RGBA":
                    r, g, b, a = im.getpixel((x, y))
                elif im.mode == "RGB":
                    r, g, b = im.getpixel((x, y))
                else:
                    print("Unsupported image mode:", im.mode)
                red_temp_array.append(r)
                green_temp_array.append(g)
                blue_temp_array.append(b)
    red_final_vals.append(numpy.mean(red_temp_array))
    green_final_vals.append(numpy.mean(green_temp_array))
    blue_final_vals.append(numpy.mean(blue_temp_array))

output = "Penny Year, Ave RGB, Ave R, Ave G, Ave B\n"
for count, val in enumerate(red_final_vals):
    output +=f"{years[count]},{(red_final_vals[count]+green_final_vals[count]+blue_final_vals[count])/3},{red_final_vals[count]}, {green_final_vals[count]}, {blue_final_vals[count]}\n"

with open("./pennylab_out.csv", "w") as f:
    f.write(output)