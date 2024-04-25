from pathlib import Path

import streamlit as st
from PIL import Image


THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "style"
CSS_FILE = STYLES_DIR / "main.css"

# --- GENERAL SETTINGS ---
STRIPE_CHECKOUT = "https://donate.stripe.com/test_8wM16N2af1vZ3FSbIL"
CONTACT_EMAIL = "karsree29@gmail.com"
PRODUCT_NAME = "Cypress Ranch Key Club"
PRODUCT_TAGLINE = "Build character with Key Club through service and leadership"

def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    


# Define function to render different pages
def render_home_page():
    st.title("Home Page")
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/281260/pexels-photo-281260.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    }
    [data-testid="stSidebar"] {
    background-color: #0250cf; /* Navy Blue */
    }
    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown("""
    <body>
    <section>
    <h1 align="center">
    <span>C</span>
    <span>Y</span>
    <span>-</span>
    <span>R</span>
    <span>A</span>
    <span>N</span>
    <span>C</span>
    <span>H</span>
    <span> </span>  
    <span>K</span>
    <span>E</span>
    <span>Y</span>
    <span>-</span>
    <span>C</span>
    <span>L</span>
    <span>U</span>
    <span>B</span>          
    </h1> 
    </section>
    <style>
    body {
      margin: 0;
      padding: 0;
      background: #000;
    }
    section {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      position: relative;
    }
    h1 {
      margin: 0px;
      padding: 0px;
      color: #000;
      font-size: min(2vw, 2rem);
      font-family: sans-serif;
    }
    h1 span {
       display: inline-block;
       animation: letterAnimation 1s linear 1 forwards;
       border:0px solid white;
       border-radius: 1px;
       padding: 0.25rem;
       padding-bottom: 0;
    }
    @keyframes letterAnimation {
      100% {
        opacity: 1;
        color: white;
        padding: 0.25rem;
        padding-bottom: 0;
        border: 0px solid red;
        border-radius: 4px;
        text-shadow: -1px 1px black, 1px 1px black, 1px 1px black, 1px 1px black;
        box-sizing: 10;
      }
    }
    h1 span:nth-child(1) {
      animation-delay: 0.5s;
    }
    h1 span:nth-child(2) {
      animation-delay: 1.5s;
    }
    h1 span:nth-child(3) {
      animation-delay: 2.5s;
    }
    h1 span:nth-child(4) {
      animation-delay: 3.5s;
    }
    h1 span:nth-child(5) {
      animation-delay: 4.5s;
    }
    h1 span:nth-child(6) {
      animation-delay: 5.5s;
    }
    h1 span:nth-child(7) {
      animation-delay: 6.5s;
    }
    h1 span:nth-child(8) {
      animation-delay: 7.5s;
    }
    h1 span:nth-child(9) {
      animation-delay: 8.5s;
    }
    h1 span:nth-child(10) {
      animation-delay: 9.5s;
    }
    h1 span:nth-child(11) {
      animation-delay: 10.5s;
    }
    h1 span:nth-child(12) {
      animation-delay: 11.5s;
    }
    h1 span:nth-child(13) {
      animation-delay: 12.5s;
    }
    h1 span:nth-child(14) {
      animation-delay: 13.5s;
    }
    h1 span:nth-child(15) {
      animation-delay: 14.5s;
    }
    h1 span:nth-child(16) {
      animation-delay: 15.5s;
    }
    h1 span:nth-child(17) {
      animation-delay: 16.5s;
    }
    </style>
    </body>
    """, unsafe_allow_html=True)

def render_about_page():
    st.title("About")
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/281260/pexels-photo-281260.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    }
    [data-testid="stSidebar"] {
    background-color: #0250cf; /* Navy Blue */
    }
    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    features = {
        "Meeting2.png": [
            "Meetings",
            "Meetings capture the spirit of excited students with fun after school activities, hints of team-building, and laughter of content children enjoying their time together, Cy-Ranch Key Club is all about fun and team-building.",
        ],
        "RollerRink.png": [
            "Socials",
            "Socials provide a vibrant platform for fostering connections and enjoying memorable moments filled with laughter and joy. They are the heartbeat of our community, where friendships flourish and memories are made.",
        ],
        "food.png": [
            "Food Drives & Fundraisers",
            "Key Club prioritizes food drives and fundraisers as crucial avenues for not only addressing hunger but also for raising awareness about food insecurity within our communities. By organizing these events, Key Club not only collects vital resources but also sparks meaningful conversations and educates others about the importance of combating hunger.",
        ],
    }
    for image, description in features.items():
        image = Image.open(ASSETS_DIR / image)
        st.write("")
        left_col, right_col = st.columns(2)
        left_col.image(image, use_column_width=True)
        right_col.write(f"**{description[0]}**")
        right_col.write(description[1])
    st.markdown(
        f'<a href={STRIPE_CHECKOUT} class="button">Donate To Key-Club💖</a>',
        unsafe_allow_html=True,
    )

    st.write("Key Club DW is a service organization for high school students, which operates under school regulations and draws its membership from the student body. Key Club differs from other organizations in many ways. Key Club is unique because it is sponsored by a local Kiwanis Club, composed of the leading business and professional people of the community. Key Club's objective is the development of initiative, leadership ability, and good citizenship practices. Key Club functions not only on the local level but on a district and international level. This highly developed structure provides programs, literature, and the opportunity to relate to teenagers from countries all around the world. Key Club is the largest high school service organization of its kind in the world! We are Key Club, and you can be too!")

def render_join_page():
    st.markdown("<h1 style='text-align: center; color: white;'>Join</h1>", unsafe_allow_html=True)
    st.subheader("Unfortunately, the deadline to join Key Club for the 23-24 school year has passed. Don't worry, there's always next year!")
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/281260/pexels-photo-281260.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    }
    [data-testid="stSidebar"] {
    background-color: #0250cf; /* Navy Blue */
    }
    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)


def render_games_page():
    tasks = [
    "Organize a fundraising event",
    "Volunteer at a local shelter",
    "Collect donations for a food drive",
    "Plan a community cleanup day",
    "Create care packages for the elderly",
]
    completed_tasks = []
    st.title("Key Club Quest")
    st.write("Welcome to Key Club Quest! Your mission is to complete various service tasks.")
    
    for i, task in enumerate(tasks, start=1):
        if st.checkbox(f"Task {i}: {task}"):
            completed_tasks.append(task)
            
            if len(completed_tasks) == len(tasks):
                st.balloons()


    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/281260/pexels-photo-281260.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    }
    [data-testid="stSidebar"] {
    background-color: #0250cf; /* Navy Blue */
    }
    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)








def render_events_page():
    st.markdown("<h1 style='text-align: center; color: white;'>Events</h1>", unsafe_allow_html=True)
    st.subheader("Make sure to download Hourify to track your volunteering hours!")
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/281260/pexels-photo-281260.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    }
    [data-testid="stSidebar"] {
    background-color: #0250cf; /* Navy Blue */
    }
    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def render_news_page():
    st.markdown("<h1 style='text-align: center; color: white;'>News</h1>", unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
             st.subheader("Cy-Ranch News")
             st.write("Finals Week coming up in 2 weeks.")
             st.write("Last Staar test of the week is algebra")
             
    with right_column:
        st.subheader("Key-Club News")
        st.write("Interviews are now open. Sign Up to get your officer position!!")
        st.write("Who will be the next officers for Key-Club next year. DUN DUN DUNNNN")
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/281260/pexels-photo-281260.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    }
    [data-testid="stSidebar"] {
    background-color: #0250cf; /* Navy Blue */
    }
    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def render_contact_page():
    st.markdown("<h1 style='text-align: center; color: white;'>Contact</h1>", unsafe_allow_html=True)
    with st.container():
        st.header("Have any questions?")
        st.write("If you have any questions feel free to submit them here!")
        st.write("##")
        
        preferred_email = "Constanza1072@aol.com"  # Change this to your preferred email
        preferref_email = "domilowe123@gmail.com"  # Change this to your preferred email
        preferree_email = "lindsaynguyen9306@gmail.com"  # Change this to your preferred email
        preferrer_email = "averyr121@gmail.com"  # Change this to your preferred email
        
        col1, col2, col3, col4 = st.columns(4)
        
        if col1.button("Contact the President", key="president"):
            st.markdown(f"Click [here](mailto:{preferred_email}) to send an email to your President.", unsafe_allow_html=True)
            
        if col2.button("Contact the Vice-President", key="vice_president"):
            st.markdown(f"Click [here](mailto:{preferref_email}) to send an email to your Vice-President.", unsafe_allow_html=True)
            
        if col3.button("Contact the Secretary", key="secretary"):
            st.markdown(f"Click [here](mailto:{preferree_email}) to send an email to your Secretary.", unsafe_allow_html=True)
            
        if col4.button("Contact the Officer Supervisor", key="officer_supervisor"):
            st.markdown(f"Click [here](mailto:{preferrer_email}) to send an email to your Officer Supervisor.", unsafe_allow_html=True)
            
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/281260/pexels-photo-281260.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    }
    [data-testid="stSidebar"] {
    background-color: #0250cf; /* Navy Blue */
    }
    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/281260/pexels-photo-281260.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    }
    [data-testid="stSidebar"] {
    background-color: #0250cf; /* Navy Blue */
    }
    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Page config
st.set_page_config(page_title="Cy-Ranch Key Club", page_icon="https://www.keyclub.org/wp-content/uploads/sites/19/2017/08/KEY-CLUB-SEAL-Color-1-150x150.png", layout="centered", initial_sidebar_state="collapsed")

with st.sidebar:
    image_html = '<a href="https://www.keyclub.org/"><img src="https://www.keyclub.org/wp-content/uploads/sites/19/2017/08/KEY-CLUB-SEAL-Color-1-150x150.png" width="50" height="50"></a>'
    st.markdown(image_html, unsafe_allow_html=True)
# Custom CSS for navigation
load_css_file(CSS_FILE)

# Sidebar options
options = ["Home", "About", "Join", "Games", "Events",  "News", "Contact"]

# Render sidebar
selected = st.sidebar.radio("Cypress Ranch Key Club", options)

# Render selected page
if selected == "Home":
    render_home_page()
if selected == "About":
    render_about_page()
if selected == "Join":
    render_join_page()
if selected == "Games":
    render_games_page()
if selected == "Events":
    render_events_page()
if selected == "News":
    render_news_page()
if selected == "Contact":
    render_contact_page()
