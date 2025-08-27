import streamlit as st
from src.utils.auth import register_user


def render():
    """Render the signup page"""
    st.markdown(
        "<h1 style='text-align: center; color: #8B5CF6;'>Create Account</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; color: #9CA3AF;'>Join us to start chatting</p>",
        unsafe_allow_html=True,
    )

    # Center the form
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.container():
            st.markdown('<div class="form-container">', unsafe_allow_html=True)

            username = st.text_input(
                "Username", placeholder="Choose a username", key="signup_username"
            )
            email = st.text_input(
                "Email", placeholder="Enter your email", key="signup_email"
            )
            password = st.text_input(
                "Password",
                placeholder="Create a password",
                type="password",
                key="signup_password",
            )
            confirm_password = st.text_input(
                "Confirm Password",
                placeholder="Confirm your password",
                type="password",
                key="signup_confirm",
            )

            if st.button("Sign Up", use_container_width=True, key="signup_btn"):
                if username and email and password and confirm_password:
                    if password != confirm_password:
                        st.error("Passwords do not match!")
                    elif len(password) < 6:
                        st.error("Password must be at least 6 characters long")
                    else:
                        if register_user(username, email, password):
                            st.success("Account created successfully! Please login.")
                            st.session_state.page = "login"
                            st.rerun()
                        else:
                            st.error("Email already registered!")
                else:
                    st.warning("Please fill in all fields")

            st.markdown("---")

            st.markdown(
                "<p style='text-align: center;'>Already have an account?</p>",
                unsafe_allow_html=True,
            )

            if st.button("Back to Login", use_container_width=True, key="goto_login"):
                st.session_state.page = "login"
                st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)
