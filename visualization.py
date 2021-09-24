from PIL import Image, ImageFont, ImageDraw
from math import floor
import cv2

font1_ = ImageFont.truetype("font/Bunny Lover.ttf", 50)
font_ = ImageFont.truetype("font/micro_se.ttf", 100)
font2_ = ImageFont.truetype("font/micro_se.ttf", 90)


def quater_image_crop(img):
    img0 = img.crop((400, 300, img.size[0]/2-300, img.size[1]/2-700))
    img0.save("temporary_pics/img0.png")

    img1 = img.crop((img.size[0]/2+200, 300, img.size[0]-200, img.size[1]/2-300))
    img1.save("temporary_pics/img1.png")

    img2 = img.crop((img.size[0]/2+200, img.size[1]/2+300, img.size[0]-200, img.size[1]-300))
    img2.save("temporary_pics/img2.png")

    img3 = img.crop((600, img.size[1]/2+300, img.size[0]/2-200, img.size[1]-800))
    img3.save("temporary_pics/img3.png")

def quater_image(img):
    img0 = img.crop((0, 0, img.size[0]/2, img.size[1]/2))
    img0.save("temporary_pics/img0.png")

    img1 = img.crop((img.size[0]/2, 0, img.size[0], img.size[1]/2))
    img1.save("temporary_pics/img1.png")

    img2 = img.crop((img.size[0]/2, img.size[1]/2, img.size[0], img.size[1]))
    img2.save("temporary_pics/img2.png")

    img3 = img.crop((0, img.size[1]/2, img.size[0]/2, img.size[1]))
    img3.save("temporary_pics/img3.png")

def stack_images(tuple_list):
    spoilage_ = Image.open("pics/food_spoilage.png")
    img0 = Image.open(tuple_list[0][1]).resize((350,200))
    img1 = Image.open(tuple_list[1][1]).resize((350,200))
    img2 = Image.open(tuple_list[2][1]).resize((350,200))
    img3 = Image.open(tuple_list[3][1]).resize((350,200))

    #Inserting food pictures
    spoilage_.paste(img3, (1400, 110))
    spoilage_.paste(img2, (1400, 340))
    spoilage_.paste(img1, (1400, 575))
    spoilage_.paste(img0, (1400, 810))

    #Inserting shelf_life in picture
    drawing = ImageDraw.Draw(spoilage_)
    drawing.text((720, 200), str(floor(tuple_list[3][0])) + " dag(e)", fill=(0, 0, 0), font = font_)
    drawing.text((720, 430), str(floor(tuple_list[2][0])) + " dag(e)", fill=(0, 0, 0), font = font_)
    drawing.text((720, 670), str(floor(tuple_list[1][0])) + " dag(e)", fill=(0, 0, 0), font = font_)
    drawing.text((720, 910), str(floor(tuple_list[0][0])) + " dag(e)", fill=(255, 0, 0), font = font_)

    #Inserting food predictions
    drawing.text((100, 200), tuple_list[3][2], fill=(0, 0, 0), font = font2_)
    drawing.text((100, 430), tuple_list[2][2], fill=(0, 0, 0), font = font2_)
    drawing.text((100, 670), tuple_list[1][2], fill=(0, 0, 0), font = font2_)
    drawing.text((100, 910), tuple_list[0][2], fill=(255, 0, 0), font = font2_)
    
    spoilage_.save("temporary_pics/Result.png")

def load_result():
    result = Image.open("temporary_pics/Result.png")
    result.show()

def resize_pics(picname):
    # print(picname)
    picture = cv2.imread("pics/" + picname)
    resized = cv2.resize(picture, (2000, 1500))
    cv2.imwrite("temporary_pics/" + picname, resized)
    path = "temporary_pics/" + picname
    return path

def input_output(food_list):
    input_pic = Image.open("pics/input_output.png")

    img0 = Image.open("temporary_pics/img0.png").resize((290,200))
    img1 = Image.open("temporary_pics/img1.png").resize((290,200))
    img2 = Image.open("temporary_pics/img2.png").resize((290,200))
    img3 = Image.open("temporary_pics/img3.png").resize((290,200))
    img4 = Image.open("camera_pic.png").resize((420,248))

    input_pic.paste(img4, (675, 65))
    input_pic.paste(img3, (1353, 514))
    input_pic.paste(img2, (928, 514))
    input_pic.paste(img1, (515, 514))
    input_pic.paste(img0, (140, 514))

    drawing = ImageDraw.Draw(input_pic)
    drawing.text((70, 910), food_list[0], fill=(255, 0, 0), font = font1_)
    drawing.text((500, 910), food_list[1], fill=(255, 0, 0), font = font1_)
    drawing.text((900, 910), food_list[2], fill=(255, 0, 0), font = font1_)
    drawing.text((1300, 910), food_list[3], fill=(255, 0, 0), font = font1_)

    input_pic.save("temporary_pics/input_output.png")


# input_output(["Caesar salat", "Caesar salat", "Caesar salat", "Caesar salat"])
# input_ = [(3, 'temporary_pics/img1.png'), (3.0, 'temporary_pics/img2.png'), (4.0, 'temporary_pics/img3.png'), (5, 'temporary_pics/img0.png')]

# stack_images(input_)
    
