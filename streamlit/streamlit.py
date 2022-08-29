import streamlit as st
from PIL import Image
import numpy as np
from mlchain.client import Client

model = Client(api_address='http://localhost:8045').model()

st.header("Model classify people below:")
st.image(Image.open('./streamlit/labels.png'))

img = st.file_uploader('Upload a image: ')

if img is not None:
    img = Image.open(img).convert("RGB")
    img = np.array(img)
    out = model.predict_single_image(img)
    st.write(out)