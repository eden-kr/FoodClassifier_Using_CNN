# FoodClassifier_Using_CNN
CNN을 통해 음식을 분류하고 영양 정보를 출력
![20200501_220420](https://user-images.githubusercontent.com/64695947/80898635-b73ef000-8d40-11ea-91b9-7b2a40d3da41.png)
![cnn4](https://user-images.githubusercontent.com/64695947/80898637-ba39e080-8d40-11ea-8ae6-3857cf6ea5e6.png)


입력된 이미지와 영양 정보를 함께 출력

영양 정보는 csv를 읽어와서 DataFrame으로 출력하는 방법 대신 영양소 정보 데이터베이스에 접속해 Series형식으로 출력

분류 및 출력이 끝날 때 사용된 전체 이미지와 이미지명을 matplot에 추가해 파일 확인이 가능하도록 수정
