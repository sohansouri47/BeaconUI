import streamlit as st


def apply_dark_theme():
    """Apply custom dark theme CSS"""
    st.markdown(
        """
    <style>
    /* Main container */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        background-color: #1E1E2E;
        color: #FAFAFA;
        border: 1px solid #2A2A3E;
        border-radius: 8px;
        padding: 10px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8B5CF6;
        box-shadow: 0 0 0 1px #8B5CF6;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #8B5CF6;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        background-color: #7C3AED;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
    }
    
    /* Secondary button */
    .secondary-button > button {
        background-color: transparent;
        color: #8B5CF6;
        border: 1px solid #8B5CF6;
    }
    
    .secondary-button > button:hover {
        background-color: rgba(139, 92, 246, 0.1);
    }
    
    /* Chat messages */
    .user-message {
        background-color: #8B5CF6;
        color: white;
        padding: 12px 16px;
        border-radius: 18px;
        margin: 8px 0;
        max-width: 70%;
        margin-left: auto;
        word-wrap: break-word;
    }
    
    .bot-message {
        background-color: #1E1E2E;
        color: #FAFAFA;
        padding: 12px 16px;
        border-radius: 18px;
        margin: 8mysterious 0;
        max-width: 70%;
        margin-right: auto;
        word-wrap: break-word;
    }
    
    /* Chat container */
    .chat-container {
        height: 500px;
        overflow-y: auto;
        padding: 20px;
        background-color: #0E1117;
        border-radius: 12px;
    }
    
    /* Form container */
    .form-container {
        max-width: 400px;
        margin: auto;
        padding: 40px;
        background-color: #1E1E2E;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    
    /* Links */
    a {
        color: #8B5CF6;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1E1E2E;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #8B5CF6;
        border-radius: 4px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
