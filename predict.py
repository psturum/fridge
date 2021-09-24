from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd

#List of classes trained in model
food_list = ['apple_pie','pizza','omelette','caesar_salad','ceviche', 'grilled_cheese_sandwich', 'hamburger','macaroni_and_cheese',
             'pulled_pork_sandwich','risotto','seaweed_salad','spaghetti_carbonara','tiramisu','waffles']

food_list1 = ['Taerte','Pizza','Omelette','Caesar salat','Ceviche', 'Toast', 'Hamburger','Macaroni',
             'Pulled pork','Risotto','Tang salat','Carbonara','Tiramisu','Vafler']

def listOfTuples(l1, l2):
    return list(map(lambda x, y:(x,y), l1, l2))


#Method for predicting food in images
def predict_class(model, images):
    list = []  
    for img in images:
        img = image.load_img(img, target_size=(299, 299))
        img = image.img_to_array(img)                    
        img = np.expand_dims(img, axis=0)         
        img /= 255.                                    
        pred = model.predict(img)
        index = np.argmax(pred)
        merged_list = listOfTuples(food_list, food_list1)
        merged_list.sort()
        list += [merged_list[index][1]]
    return list

def predict_shelf_life(predicted_food):
    df = pd.read_csv (r'conversion_table1.csv',header=0)
    ret = [0,0,0,0]
    i = 0
    print(predicted_food)
    for food in predicted_food:
        df1 = (df.loc[df['food'] == food])
        if(i<2):
            value = df1['shelf_life_back'].values[0]
            ret[i] = value
        else:
            value = df1['shelf_life_front'].values[0]
            ret[i] = value
        i += 1
    return ret

    