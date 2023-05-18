import streamlit as st
from PIL import Image
import os

st.title("민채영")

#주제별로 묶어서 화면에 출력하는 방법
#1. 사이드바를 만든다
#2. 컬럼(열) 단위로 나눈다 - st.columns()

#selectbox를 사용해서 제목을 선택하면 이미지가 각각 화면에 출력되도록
col1, col2 = st.columns(2, gap="small")
with col1:
    img_list = ['sleeping sando', 'cute sando','sleeping crown']
    cat_select = st.selectbox('우리집 고양이', img_list)
    st.write(cat_select)

    img_idx = img_list.index(cat_select)
    folder = './data/'
    image_files = ['cat(1).jpg','cat(2).jpg','cat(3).jpg']

    image_path = folder + image_files[img_idx]
    image = Image.open(image_path)
    st.image(image)

with col2:
    food_list = ['Burger', 'Susi','Taco']
    food_select = st.selectbox('좋아하는 음식', food_list)
    st.write(food_select)

    food_idx = food_list.index(food_select)
    folder = './data/'
    food_files = ['burger.jpg','susi.jpg','taco.jpg']

    image_path1 = folder + food_files[food_idx]
    image1 = Image.open(image_path1)
    st.image(image1)

#streamlit run 02_streamlit_example.py
