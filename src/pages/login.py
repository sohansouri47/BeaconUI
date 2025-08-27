import streamlit as st
from src.utils.auth import authenticate_user


def render():
    """Render the login page"""
    st.markdown(
        "<h1 style='text-align: center; color: #8B5CF6;'>Welcome Back</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; color: #9CA3AF;'>Sign in to continue to your chat</p>",
        unsafe_allow_html=True,
    )

    # Center the form
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.container():
            st.markdown('<div class="form-container">', unsafe_allow_html=True)

            email = st.text_input(
                "Email", placeholder="Enter your email", key="login_email"
            )
            password = st.text_input(
                "Password",
                placeholder="Enter your password",
                type="password",
                key="login_password",
            )

            col_btn1, col_btn2 = st.columns(2)

            with col_btn1:
                if st.button("Sign In", use_container_width=True, key="signin_btn"):
                    if email and password:
                        if authenticate_user(email, password):
                            st.success("Login successful!")
                            st.rerun()
                        else:
                            st.error(
                                "Invalid credentials. Try demo@example.com / demo123"
                            )
                    else:
                        st.warning("Please fill in all fields")

            with col_btn2:
                if st.button(
                    "Forgot Password?", use_container_width=True, key="forgot_btn"
                ):
                    st.info("Password reset functionality coming soon!")

            st.markdown("---")

            st.markdown(
                "<p style='text-align: center;'>Don't have an account?</p>",
                unsafe_allow_html=True,
            )

            if st.button("Create Account", use_container_width=True, key="goto_signup"):
                st.session_state.page = "signup"
                st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)
