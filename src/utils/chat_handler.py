import streamlit as st
import time
import random


def get_bot_response(message):
    """Generate mock bot responses"""
    responses = [
        f"I understand you said: '{message}'. How can I help you further?",
        f"That's interesting! You mentioned '{message}'. Tell me more.",
        f"Thanks for sharing about '{message}'. What would you like to know?",
        "I'm here to help! What specific information are you looking for?",
        "Great question! Let me think about that...",
        "I appreciate your input. Could you provide more details?",
    ]

    # Simulate processing time
    time.sleep(1)
    return random.choice(responses)


def send_message(message, message_type="text"):
    """Process and send a message"""
    if message.strip():
        # Add user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": message,
                "type": message_type,
                "timestamp": time.time(),
            }
        )

        # Get bot response
        bot_response = get_bot_response(message)

        # Add bot response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": bot_response,
                "type": "text",
                "timestamp": time.time(),
            }
        )

        return True
    return False


def process_audio(audio_data):
    """Mock audio processing via WebSocket"""
    # In production, send audio_data via WebSocket to speech-to-text service
    # For demo, return mock transcription
    return "This is a mock transcription of your audio message"
