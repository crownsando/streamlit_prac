import streamlit as st
from PIL import Image
import os

st.title("민채영")

img_list = ['sleeping sando', 'cute sando','sleeping crown']
cat_select = st.sidebar.selectbox('우리집 고양이',img_list)

