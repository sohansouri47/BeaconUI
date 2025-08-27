import streamlit as st


def initialize_session_state():
    """Initialize session state variables"""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = None
    if "email" not in st.session_state:
        st.session_state.email = None
    if "page" not in st.session_state:
        st.session_state.page = "login"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "users" not in st.session_state:
        # Mock user database
        st.session_state.users = {
            "demo@example.com": {
                "username": "demo_user",
                "password": "demo123",  # In production, use hashed passwords
            }
        }


def logout():
    """Clear session state for logout"""
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.email = None
    st.session_state.messages = []
    st.session_state.page = "login"
