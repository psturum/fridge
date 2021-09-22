from visualization import quater_image, stack_images
from numpy.core.numeric import False_
from predict import predict_class, predict_shelf_life
from tensorflow.keras.models import load_model
from PIL import Image

model_best = load_model('best_model_14class.hdf5', compile = False)
img_plates = Image.open("pics/4_plate.png")


def listOfTuples(l1, l2):
    return list(map(lambda x, y:(x,y), l1, l2))


def main():
    quater_image(img_plates)
    img_input = ["temporary_pics/img0.png", "temporary_pics/img1.png", 
    "temporary_pics/img2.png", "temporary_pics/img3.png"]
    food = predict_class(model_best, img_input)
    shelf_life = predict_shelf_life(food)
    merged_list = listOfTuples(shelf_life, img_input)
    merged_list.sort()
    stack_images(merged_list)



main()
