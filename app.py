import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/boobs.png")
#img_lottie_animation = Image.open("images/)

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, Tuvshin hier :wave:")
    st.title("Ein Anime Fan!")
    st.write(
        "Ich kann dir nicht helfen!"
    )
    st.write("[Learn More >]")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Bitte gergesche!
            """
        )
        st.write("https://www.instagram.com/tuv_se/")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    #with image_column:
        #st.image(img_lottie_animation)
    with text_column:
        st.subheader("FAVORITE ANIME")
        st.write(
            """
         HUNTER X HUNTER

            """
        )
        st.markdown("https://www.instagram.com/tuv_se/")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("FAVORITE GAMES")
        st.write(
            """
            
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("https://www.linkedin.com/in/tuvshin-s-ab74aa182/")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    #contact_form = """

    #"""
    #left_column, right_column = st.columns(2)
    #with left_column:
        #st.markdown(contact_form, unsafe_allow_html=True)
    #with right_column:
        #st.empty()