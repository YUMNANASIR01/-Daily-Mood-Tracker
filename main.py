import streamlit as st
import pandas as pd
import datetime
import csv
import os
import random

MOOD_FILE = "mood_log.csv"   

def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=["Date", "Mood"])
    try:
        return pd.read_csv(MOOD_FILE)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["Date", "Mood"])

def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Add animated background and modern styling
st.markdown("""
<style>
    body {
        margin: 0;
        padding: 0;
        min-height: 100vh;
       background: linear-gradient(-45deg, #6366f1, #8b5cf6, #ec4899, #6b7290);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white !important;
        overflow: hidden;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stApp {
        background-color: transparent !important;
    }
    
    .main-title {
        color: white !important;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 1.5rem;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
    }
    
    .sub-title {
        color: white !important;
        font-size: 1.25rem;
        margin-bottom: 1rem;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.2);
    }
    
    .stSelectbox > div {
        background: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(5px);
    }
    
    .stButton > button {
        background: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.5rem 2rem !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background: rgba(255, 255, 255, 0.25) !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.2);
    }
    
    .particle {
        position: fixed;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 50%;
        animation: float 20s infinite linear;
        pointer-events: none;
    }
    
    @keyframes float {
        0% { transform: translate(0, 0) scale(0); opacity: 0; }
        50% { opacity: 0.4; }
        100% { transform: translate(100vw, -100vh) scale(1); opacity: 0; }
    }
</style>
""", unsafe_allow_html=True)

# Add animated particles
particles_html = "<div>"
for _ in range(15):
    size = random.randint(2, 5)
    left = random.randint(0, 100)
    delay = random.uniform(0, 15)
    particles_html += f'<div class="particle" style="width: {size}px; height: {size}px; left: {left}%; animation-delay: {delay}s"></div>'
particles_html += "</div>"
st.markdown(particles_html, unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-title">🌤️ Daily Mood Tracker</h1>', unsafe_allow_html=True)

today = datetime.date.today()

# Mood Selection Section
st.markdown('<h2 class="sub-title">How are you feeling today? 🌈</h2>', unsafe_allow_html=True)
mood = st.selectbox("", ["😃 Happy", "😢 Sad", "😡 Angry", "😐 Neutral"], label_visibility="collapsed")

if st.button("Log My Mood"):
    save_mood_data(today, mood)
    st.success("🎉 Mood logged successfully!")

# Mood Trends Section
data = load_mood_data()
if not data.empty:
    st.markdown('<h2 class="sub-title">Mood Timeline 📅</h2>', unsafe_allow_html=True)
    data["Date"] = pd.to_datetime(data["Date"])
    mood_counts = data["Mood"].value_counts()
    
    # Styled chart container
    st.markdown('<div style="background: rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 1rem; backdrop-filter: blur(5px);">', unsafe_allow_html=True)
    st.bar_chart(mood_counts, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: center;">
        <p>Build with 💗 by <a href="https://github.com/YUMNANASIR01/-Daily-Mood-Tracker.git" target="_blank">Yumna Nasir</a></p>
    </div>
    """,
    unsafe_allow_html=True
)




































































































































































# import streamlit as st   # for creating web interface
# import pandas as pd   # for data manipulate
# import datetime   # for handling dates
# import csv   # for reading and writing csv files
# import os   # for file operations

# # define mood data
# MOOD_FILE = "mood_log.csv"   

# def load_mood_data():
#     # check file exits
#     if not os.path.exists(MOOD_FILE):
#         # if no file empty data with columns
#         return pd.DataFrame(columns=["Date", "Mood"])
#     # read and return mood data
#     return pd.read_csv(MOOD_FILE)

# def save_mood_data(date, mood):
#     # file open in append mood
#     with open(MOOD_FILE, "a") as file:

#         writer = csv.writer(file)
# # new mood entry in file data
#         writer.writerow([date,mood])

# st.title("Moood Tracker")  
# #  today data    
# today = datetime.date.today()

# st.subheader("How are you feeling today?")
# # drop down to mood select
# mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# if st.button("Log Mood"):
#     save_mood_data(today, mood)

#     st.success("Mood Logged SuccessFully!")

# data = load_mood_data()

# if not data.empty:
#     st.subheader("Mood Trends Over Time")

#     data["Date"] = pd.to_datetime(data["Date"])

#     mood_counts = data.groupby("Mood").count()["Date"]

#     st.bar_chart(mood_counts)

#     st.write("Built with 💗 by Yumna Nasir ")