import streamlit as st
import numpy as np
from PIL import Image




st.set_page_config(page_title="Dice game", page_icon="🎲🎲🎲🎲", layout="wide")
st.sidebar.image("dice_animation.gif",width=1000)


def dice_game():
    a, b = np.random.randint(1,7,2)
    st.write(f"Your numbers are {a} and {b}")
    if a==6 and b ==6:
        st.balloons()
        return('Congratulations!!!!!!! You don chop 👏')
    else:
        return("Try again, maybe you go chop next time🤣😂🤣😂")


if st.button("Play"):
    st.write(dice_game())
