import streamlit as st
from src.utils.chat_handler import send_message, process_audio
from src.utils.session import logout
from src.components.message import render_message


def render():
    """Render the chat interface"""
    # Header with user info and logout
    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.markdown(
            f"<p style='color: #9CA3AF;'>👤 {st.session_state.username}</p>",
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            "<h1 style='text-align: center; color: #8B5CF6;'>Chat Interface</h1>",
            unsafe_allow_html=True,
        )

    with col3:
        if st.button("Logout", key="logout_btn"):
            logout()
            st.rerun()

    st.markdown("---")

    # Chat messages container
    chat_container = st.container()

    with chat_container:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        # Display messages
        if not st.session_state.messages:
            st.markdown(
                """
            <div style='text-align: center; color: #9CA3AF; padding: 50px;'>
                <h3>Welcome to the chat!</h3>
                <p>Send a message to start the conversation</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            for message in st.session_state.messages:
                render_message(message)

        st.markdown("</div>", unsafe_allow_html=True)

    # Input area
    st.markdown("---")

    col1, col2 = st.columns([10, 1])

    with col1:
        user_input = st.text_input(
            "Message",
            placeholder="Type your message here...",
            key="chat_input",
            label_visibility="collapsed",
        )

    with col2:
        mic_button = st.button("🎤", key="mic_btn", help="Voice input (WebSocket)")

    # Handle text input
    if st.button("Send", use_container_width=True, key="send_btn") or (
        user_input and st.session_state.get("enter_pressed")
    ):
        if user_input:
            send_message(user_input, "text")
            st.rerun()

    # Handle voice input
    if mic_button:
        st.info("🎤 Voice recording would start here...")
        # In production, implement WebSocket connection for audio streaming
        # For demo, simulate audio transcription
        mock_transcription = process_audio(None)
        send_message(mock_transcription, "audio")
        st.rerun()

    # Instructions
    with st.expander("ℹ️ How to use"):
        st.markdown(
            """
        - **Text Input**: Type your message and click 'Send' or press Enter
        - **Voice Input**: Click the microphone button to record audio (WebSocket connection)
        - **Demo Credentials**: Use `demo@example.com` / `demo123` to test
        """
        )
