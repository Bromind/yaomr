from PIL import Image
import os
import sys

window_width = 20
immune = 10

name_file="e3"
file_path="../assets/" + name_file + ".png"

try: 
    myImage = Image.open(file_path)
    myImage.load()
except:
    print "Cannot open image" + file_path
    sys.exit(0)

print "Output will be in: "
output=os.path.splitext(file_path)[0]
print(output)
if not os.path.exists(output):
    os.makedirs(output)

threshold = 0.25 * myImage.size[1]
myImage = myImage.convert("1")
print "the image is: "
print(myImage.format, myImage.size, myImage.mode)

cur_sum = 0
increasing=False
next_open_slot=0
for i in range(myImage.size[0]):
    prev_sum = cur_sum
    cur_sum = 0
    for j in range(myImage.size[1]):
        if myImage.getpixel((i, j)) < 64:
            cur_sum = cur_sum + 1
    print cur_sum
    if cur_sum > prev_sum:
        increasing=True
    else:
        if increasing == True and prev_sum > threshold and i >= next_open_slot:
            small = myImage.crop((i-window_width/2, 0, i + window_width/2, myImage.size[1]))
            small.save(output + "/" + name_file + "_" +str(i).zfill(3) + ".png")
            next_open_slot=i+immune

        increasing=False


