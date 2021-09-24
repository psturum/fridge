from visualization import quater_image, resize_pics, input_output, stack_images
from numpy.core.numeric import False_
from predict import predict_class, predict_shelf_life
from tensorflow.keras.models import load_model
from PIL import Image
from user_interaction import prepare_input
import cv2

#initiating
model_best_ = load_model('best_model_14class.hdf5', compile = False)
img_plates_ = Image.open("pics/4_plate.png")
game_start_ = resize_pics("game_start.png")
insert_ = resize_pics("insert.png")
# resize_pics("input_output.png")


def listOfTuples(l1, l2):
    return list(map(lambda x, y:(x,y), l1, l2))


def main():
    # Starting Game

    #Prepare input
    input_photo = Image.open(prepare_input())
    quater_image(input_photo)
    img_input = ["temporary_pics/img0.png", "temporary_pics/img1.png", 
    "temporary_pics/img2.png", "temporary_pics/img3.png"]

    #Predict in prepare list to visuals
    food = predict_class(model_best_, img_input)
    shelf_life = predict_shelf_life(food)
    merged_list = list(zip(shelf_life, img_input, food))
    merged_list.sort()
    stack_images(merged_list)


    input_output(food)
    input_output_pic = cv2.imread("temporary_pics/input_output.png")
    resized = cv2.resize(input_output_pic, (2000, 1500))
    cv2.imshow('image', resized)
    cv2.waitKey(1)
    
    #Exit program is char q is given
    key = input("Tryk enter for at se resultat")
    if key=="q":
        exit()



    result = cv2.imread("temporary_pics/Result.png")
    resized = cv2.resize(result, (2000, 1500))
    cv2.imshow('image', resized)
    cv2.waitKey(1)
    
    #Exit program is char q is given
    key = input("Tryk enter for at spille igen")
    if key=="q":
        exit()

while (True):
    # Starting Game
    start = cv2.imread("temporary_pics/game_start.png")
    cv2.imshow('image', start)
    cv2.waitKey(1)
    
    #Exit program is char q is given
    key = input("Tryk enter for at starte spillet")
    if key == "q":
        break
    main()


