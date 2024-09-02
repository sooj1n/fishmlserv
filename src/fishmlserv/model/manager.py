import os

def get_model_path():
    # 이 함수 파일의 절대 경로를 받아온다.
    my_path = __file__
    #/home/sujin/code/fishmlserv/src/fishmlserv/model/manager.py
    dir_name = os.path.dirname(my_path)
    #/home/sujin/code/fishmlserv/src/fishmlserv/model

    # 절대 경로를 이용해 model.pkl의 경로를 조합
    #model_path = dir_name + "/" + "model.pkl"
    model_path = os.path.join(dir_name, "model.pkl")

    # 조합된 경로를 리턴 - 끝
    return model_path

    # 사용 fastapi mian.py에서 아래와 같이 사용
    # from fishmlserv.model.manager import get_model_path

