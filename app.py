import streamlit as st
from pages import login, signup, chat

# Sidebar router
PAGES = {
    "Login": login.show,
    "Sign Up": signup.show,
    "Chat": chat.show,
}

st.set_page_config(page_title="Beacon Chat — Streamlit", layout="wide")

st.sidebar.title("Beacon")
page = st.sidebar.radio("Go to", list(PAGES.keys()))

PAGES[page]()
