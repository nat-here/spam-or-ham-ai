import streamlit as st
import pickle

# 1. Page Configuration (Sets title, icon, and layout)
st.set_page_config(
    page_title="Spam Or Ham AI",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to elevate styling (adds soft gradients & shadow borders)
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #6B7280;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Modern Header
st.markdown('<div class="main-title">🛡️ Spam Or Ham AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Instant intelligent classification for suspicious SMS and email messages</div>', unsafe_allow_html=True)
st.divider()

# 3. Sidebar for model info or instructions
with st.sidebar:
    st.header("⚙️ App Information")
    st.info("This application uses a trained Machine Learning model (`model.pkl`) to analyze text patterns and flag potential security risks.")
    st.caption("v1.0.0 • Developed with Streamlit")

# 4. Content Container & Input Field
with st.container():
    # Using text_area for better text visibility instead of text_input
    message = st.text_area(
        "📩 Paste the message you want to check:",
        placeholder="Type or paste message text here...",
        height=150,
        help="Provide the complete message for a more accurate prediction."
    )
    
    # Styled columns to align button nicely
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Full width primary button
        submit = st.button('✨ Analyze Message', use_container_width=True, type="primary")

# 5. Prediction Logic and Enhanced Feedback
if submit:
    if not message.strip():
        st.warning("⚠️ Please enter a message before running the analysis.")
    else:
        with st.spinner('Analyzing textual patterns...'):
            try:
                # Load the model safely inside the block or globally
                with open('model.pkl', 'rb') as f:
                    model = pickle.load(f)
                
                prediction = model.predict([message])
                
                # Smooth transition layout for results
                st.subheader("Analysis Result")
                
                if prediction[0].lower() == 'spam':
                    st.error("🚨 **Danger: This message looks like SPAM!**")
                else:
                    st.success("✅ **Safe: This message appears to be LEGIT (Ham).**")
                    
            except FileNotFoundError:
                st.error("❌ `model.pkl` could not be found. Please ensure the model file is in the same directory.")
