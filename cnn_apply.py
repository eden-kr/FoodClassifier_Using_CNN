# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:29:49 2019

@author: kzx789
"""

from PIL import Image
import os, glob, numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import cv2
import pymysql
import MySQLdb as mysql

"""
#csv를 읽어서 영양정보 출력
def get_Nutrition(str) :
     nutrition = pd.read_csv('C:/식품영양정보/영양정보.csv')   
     print(nutrition[nutrition['음식명'] == str])
"""     
"""
#사용된 전체 이미지 출력
def drawing_plt():
    thisImg = os.listdir(caltech_dir)
    row = 4
    cols = int(math.ceil(len(thisImg)/4))    #반올림
    fig = plt.figure()
    i = 1
        
    for image in glob.glob("C:/selectripTest/*.jpg"):     #glob를 사용해서 Test로 사용된 파일 가져오기
        img = cv2.imread(image)
        subplot = fig.add_subplot(row, cols, i)
        subplot.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))    #기본컬러
        subplot.set_title(thisImg[i-1])     #타이틀 붙이기
        subplot.axis("off") 
        i += 1
    print('\t',"전체 이미지 리스트   ")
    plt.show()
"""
#조건에 맞는 개별 이미지 출력
def get_Image(str):
    imgPath = 'C:/selectripTest/'
    image = cv2.imread(imgPath+str)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])
    plt.show()
"""
#데이터베이스에서 영양소 정보 가지고 오기
def get_DB_Nutrition(str):
    db = pymysql.connect(host="localhost", user = "yeha", password="4045859a", db="nutrition")
    cur = db.cursor()        #Connection에서 Cursor생성
    sql = "SELECT * FROM NUTRITION_INFO WHERE FOODNAME LIKE '음식명' OR FOODNAME LIKE %s"
    cur.execute(sql,(str))
    data = cur.fetchall()    #정보 전부 가져오기
    df = pd.Series(data[0],data[1])
    print(df)
    db.close()
"""
caltech_dir = "C:/selectripTest"
#테스트할 데이터들을  128*128로 지정
image_w = 128
image_h = 128
pixels = image_h * image_w * 3      #픽셀 지정

X = []
files = os.listdir(caltech_dir)     #하위 디렉터리 파일 리스트 구하기
for i in range(len(files)):
    files[i]=caltech_dir+'/'+ files[i]

for f in files:
    img = Image.open(f)
    img = img.convert("RGB")
    img = img.resize((image_w, image_h))
    data = np.asarray(img)      #이미지 배열 재생성
    X.append(data)

X = np.array(X)

#모델 불러오기
from keras.models import load_model

model = load_model("C:/selectripModel/train/model/multi_img_classification.model")
model.summary()
prediction = model.predict(X)

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})


print('프로그램을 실행합니다..')
print('\n')
thisImg = os.listdir(caltech_dir)
cnt = 0

for i in prediction:
    pre_ans = i.argmax()  # 예측 레이블
    if pre_ans == 0: pre_ans_str = "스위스"
    elif pre_ans == 1: pre_ans_str = "파리"
    else: pre_ans_str = "확인할 수 없어요"

    if i[0] >= 0.6 : 
        get_Image(thisImg[cnt])
        print(thisImg[cnt]+" 이미지는 "+pre_ans_str+"(으)로 추정됩니다.")
        #get_Nutrition(pre_ans_str) 
        #get_DB_Nutrition(pre_ans_str)

    if i[1] >= 0.6: 
        get_Image(thisImg[cnt])
        print(thisImg[cnt]+" 이미지는 "+pre_ans_str+"(으)로 추정됩니다.")
        #get_Nutrition(pre_ans_str)   
        #get_DB_Nutrition(pre_ans_str)


        
        #get_Nutrition(pre_ans_str)   
        #get_DB_Nutrition(pre_ans_str)

    cnt += 1
    
drawing_plt()

            