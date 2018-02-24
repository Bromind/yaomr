from PIL import Image

window_width = 10

try: 
    myImage = Image.open("../assets/extract.png")
    myImage.load()
except:
    print "Cannot open image"

print "the image is: "
print(myImage.format, myImage.size, myImage.mode)
scaled = myImage.copy()
scaled.thumbnail((myImage.size[0], 48))
scaled = scaled.convert("1")
scaled.show()
print "The thumbnail is:"
print(scaled.format, scaled.size, scaled.mode)

for i in range(scaled.size[0]):
    sum = 0
    for j in range(scaled.size[1]):
        if scaled.getpixel((i, j)) < 64:
            sum = sum + 1
    print sum
    if sum > 15:
        small = scaled.crop((i, 0, i + window_width, 48))
        small.save("../tmp/" + str(i) + ".png")
