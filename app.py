import streamlit as st
from src.utils.styles import apply_dark_theme
from src.utils.session import initialize_session_state
from src.pages import login, signup, chat

# Page configuration
st.set_page_config(
    page_title="Dark Chat App",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Initialize session state
initialize_session_state()

# Apply dark theme
apply_dark_theme()


# Navigation logic
def main():
    if not st.session_state.authenticated:
        if st.session_state.page == "signup":
            signup.render()
        else:
            login.render()
    else:
        chat.render()


if __name__ == "__main__":
    main()
