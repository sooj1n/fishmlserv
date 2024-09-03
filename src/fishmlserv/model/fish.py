import os
import pickle

def prediction(length, weight):
    ### 모델 불러오기
    with open("/home/sujin/code/fishmlserv/src/fishmlserv/model", "rb") as f:
        fish_model = pickle.load(f)

    prediction = fish_model.predict([[length, weight]])

    fish_class = "몰라"
    return {
                "prediction": fish_class,
                "length": length, 
                "weight": weight
            }