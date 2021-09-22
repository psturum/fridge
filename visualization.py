from PIL import Image
spoilage = Image.open("pics/food_spoilage1.png")

def quater_image(img):
    img0 = img.crop((400, 300, img.size[0]/2-300, img.size[1]/2-700))
    img0.save("temporary_pics/img0.png")

    img1 = img.crop((img.size[0]/2+200, 300, img.size[0]-200, img.size[1]/2-300))
    img1.save("temporary_pics/img1.png")

    img2 = img.crop((img.size[0]/2+200, img.size[1]/2+300, img.size[0]-200, img.size[1]-300))
    img2.save("temporary_pics/img2.png")

    img3 = img.crop((600, img.size[1]/2+300, img.size[0]/2-200, img.size[1]-800))
    img3.save("temporary_pics/img3.png")

def stack_images(tuple_list):
    img0 = Image.open(tuple_list[0][1]).rotate(-90).resize((490,260))
    img1 = Image.open(tuple_list[1][1]).rotate(-90).resize((490,260))
    img2 = Image.open(tuple_list[2][1]).rotate(-90).resize((490,260))
    img3 = Image.open(tuple_list[3][1]).rotate(-90).resize((490,260))

    spoilage.paste(img3, (280, 235))
    spoilage.paste(img2, (280, 525))
    spoilage.paste(img1, (280, 825))
    spoilage.paste(img0, (280, 1120))
    spoilage.show()



    
