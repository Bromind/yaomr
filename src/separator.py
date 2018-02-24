from PIL import Image
import os
import sys

window_width = 10
threshold = 10
immune = 10

file_path="../assets/e3.png"

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

print "the image is: "
print(myImage.format, myImage.size, myImage.mode)
scaled = myImage.copy()
#scaled.thumbnail((myImage.size[0], 48))
scaled = scaled.convert("1")
scaled.show()
print "The thumbnail is:"
print(scaled.format, scaled.size, scaled.mode)

cur_sum = 0
increasing=False
next_open_slot=0
for i in range(scaled.size[0]):
    prev_sum = cur_sum
    cur_sum = 0
    for j in range(scaled.size[1]):
        if scaled.getpixel((i, j)) < 64:
            cur_sum = cur_sum + 1
    print cur_sum
    if cur_sum > prev_sum:
        increasing=True
    else:
        if increasing == True and prev_sum > threshold and i >= next_open_slot:
            small = scaled.crop((i-window_width/2, 0, i + window_width/2, scaled.size[0]))
            small.save(output + "/" + str(i).zfill(3) + ".png")
            next_open_slot=i+immune

        increasing=False


