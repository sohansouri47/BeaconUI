import streamlit as st
import time


def authenticate_user(email, password):
    """Mock authentication function"""
    users = st.session_state.users

    if email in users and users[email]["password"] == password:
        st.session_state.authenticated = True
        st.session_state.username = users[email]["username"]
        st.session_state.email = email
        return True
    return False


def register_user(username, email, password):
    """Mock user registration"""
    if email not in st.session_state.users:
        st.session_state.users[email] = {"username": username, "password": password}
        return True
    return False


def reset_password(email):
    """Mock password reset"""
    # In production, send reset email
    return email in st.session_state.users
