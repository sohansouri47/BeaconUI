import streamlit as st


def render_message(message):
    """Render a single chat message"""
    if message["role"] == "user":
        st.markdown(
            f"""
        <div style="display: flex; justify-content: flex-end; margin: 10px 0;">
            <div class="user-message">
                {message["content"]}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
        <div style="display: flex; justify-content: flex-start; margin: 10px 0;">
            <div class="bot-message">
                {message["content"]}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
