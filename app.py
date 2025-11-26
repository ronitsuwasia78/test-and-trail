# app.py  -- Creative UI + Contact + Doctor Page
import os
import pickle
import pandas as pd
import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")

# -------------------------
# CSS — animated background + glass card styling
# -------------------------
CUSTOM_CSS = """
/* full app animated gradient */
.stApp {
    background: linear-gradient(120deg, #050816 0%, #0b1220 35%, #0f766e 70%, #7c3aed 100%);
    background-size: 300% 300%;
    animation: gradientShift 18s ease infinite;
    color: #e6eef8;
    min-height: 100vh;
    position: relative;
    overflow: hidden;
}

/* animated gradient */
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* grain / noise texture overlay */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    opacity: 0.13;
    mix-blend-mode: soft-light;
    background-image:
      url("https://grainy-gradients.vercel.app/noise.svg");
    background-size: 300px 300px;
    z-index: 0;
}

/* soft blobs */
.blob {
    position: absolute;
    width: 360px;
    height: 360px;
    border-radius: 50%;
    filter: blur(100px);
    opacity: 0.18;
    z-index: 0;
    pointer-events: none;
}
.blob.one {
    background: rgba(236, 252, 203, 0.25);
    top: -120px;
    left: -80px;
}
.blob.two {
    background: rgba(244, 114, 182, 0.22);
    bottom: -140px;
    right: -100px;
}

/* main glass card */
.main-card {
    position: relative;
    z-index: 1;
    padding: 28px 24px;
    border-radius: 18px;
    background: radial-gradient(circle at top left, rgba(248,250,252,0.12), rgba(15,23,42,0.92));
    box-shadow:
        0 18px 40px rgba(15,23,42,0.75),
        0 0 0 1px rgba(148,163,184,0.22);
    backdrop-filter: blur(14px) saturate(130%);
    border: 1px solid rgba(148,163,184,0.28);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}

/* small hover lift when card is in focus area */
.main-card:hover {
    transform: translateY(-3px);
    box-shadow:
        0 26px 60px rgba(15,23,42,0.9),
        0 0 0 1px rgba(248,250,252,0.25);
    border-color: rgba(248,250,252,0.42);
}

/* headings */
.app-title {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: 0.4px;
}
.app-sub {
    font-size: 13px;
    color: rgba(226,232,240,0.82);
}

/* buttons */
.stButton > button {
    background: linear-gradient(120deg,#06b6d4,#22c55e);
    color: white;
    border-radius: 999px;
    padding: 8px 18px;
    font-weight: 600;
    border: none;
    box-shadow: 0 10px 30px rgba(15,23,42,0.7);
    cursor: pointer;
    transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease;
}
.stButton > button:hover {
    transform: translateY(-1px) scale(1.01);
    box-shadow: 0 14px 40px rgba(15,23,42,0.9);
    filter: brightness(1.05);
}

/* sidebar */
[data-testid="stSidebar"] {
    background: radial-gradient(circle at top, rgba(15,23,42,0.95), rgba(15,23,42,0.98));
    border-right: 1px solid rgba(148,163,184,0.35);
    backdrop-filter: blur(18px) saturate(140%);
}

/* sidebar text tweaks */
[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

/* make selectbox & inputs a bit glassy */
div[data-baseweb="select"],
.stNumberInput input,
.stTextInput input {
    background: rgba(15,23,42,0.9);
    border-radius: 999px;
    border: 1px solid rgba(148,163,184,0.65);
    color: #e5e7eb;
}

"""

st.markdown(f"<style>{CUSTOM_CSS}</style>", unsafe_allow_html=True)

# floating blobs
st.markdown(
    """
    <div class="blob one"></div>
    <div class="blob two"></div>
    """,
    unsafe_allow_html=True,
)


# -------------------------
# Load model (kept same as original)
# -------------------------
st.header("Heart Disease Prediction Using Machine Learning")

data = '''Project Objective
Heart Disease Prediction using Machine Learning
Heart disease prevention is critical, and data-driven prediction systems can significantly aid in early diagnosis and treatment. Machine Learning offers accurate prediction capabilities, enhancing healthcare outcomes.
In this project, I analyzed a heart disease dataset with appropriate preprocessing. Multiple classification algorithms were implemented in Python using Scikit-learn and Keras to predict the presence of heart disease.

Most Common Heart Diseases
1. Coronary Artery Disease (CAD) / Heart Attack Risk

Main cause: plaque buildup blocking heart arteries/
Predictors: cholesterol, blood pressure, age, chest pain, ECG, exercise results

2. Heart Failure

The heart becomes too weak to pump blood properly/
Predictors: ejection fraction, serum sodium, serum creatinine, anemia, age

3. Arrhythmia (Irregular Heartbeat)

Issues with heartbeat rhythm/
Predictors: ECG signals, heart rate variability

4. Hypertension (High Blood Pressure)

Very common and easy for college-level prediction/
Predictors: BMI, age, sodium intake, lifestyle, stress

5. Stroke Prediction

Not exactly a heart disease, but related to cardiovascular health/
Predictors: heart disease history, blood pressure, lifestyle, glucose, BMI'''

model_path = os.path.join(os.path.dirname(__file__), "MODEL", "Heart_disease_pred.pkl")

with open(model_path, "rb") as f:
    chatgpt = pickle.load(f)

st.subheader(data)
st.image('https://t-shikuro.github.io/images/heart/heart.gif')


# -------------------------
# Sidebar: NOW WITH DOCTOR PAGE
# -------------------------
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Navigation", ["Predict", "Contact Us"])


# -------------------------
# Contact Page
# -------------------------
FORM_EMBED_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfLwo3-ETSS-JYSgGhKKxqluSBisCIg5bfHYYvOaT6w8uG3hg/viewform?embedded=true%22"

if page == "Contact Us":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("## Contact Us")
    st.markdown("Use the form below to reach out to us!")

    iframe = f"""
        <iframe src="{FORM_EMBED_URL}" width="700" height="900" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    """
    st.markdown(iframe, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(
        "If the form above doesn't load, click here: "
        "[Open Contact Form](https://docs.google.com/forms/d/e/1FAIpQLSfLwo3-ETSS-JYSgGhKKxqluSBisCIg5bfHYYvOaT6w8uG3hg/viewform)"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()


# -------------------------
# Home Page (Prediction UI)
# -------------------------
csv_path = os.path.join(os.path.dirname(__file__), "heart.csv")
df = pd.read_csv(csv_path)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown(
    """
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
      <div style="font-size:34px">❤️</div>
      <div>
        <div class="app-title">Heart Disease Predictor</div>
        <div class="app-sub">Fast predictions using pre-trained models — keep your doctor informed.</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

left_col, right_col = st.columns([1, 1.2], gap="large")

with left_col:
    st.subheader("Inputs")
    st.image("https://tse4.mm.bing.net/th/id/OIP.7LA1z7w-drtQmnFmC0KBNAHaE7?cb=thfvnext&pid=ImgDet&w=201&h=134&c=7&o=7&rm=3", width=200)
    all_values = []
    random.seed(11)
    for i in df.iloc[:, :-1]:
        min_value, max_value = df[i].agg(['min', 'max'])
        var = st.slider(f'Select {i} value', int(min_value), int(max_value),
                        random.randint(int(min_value), int(max_value)))
        all_values.append(var)

    final_value = [all_values]
    run = st.button("Run Model")

with right_col:
    st.subheader("Result")
    result_placeholder = st.empty()
    anim_placeholder = st.empty()

    if run:
        progress_bar = st.progress(0)
        anim_placeholder.image('https://media1.tenor.com/m/LLlSFiqwJGMAAAAC/beating-heart-gif.gif', width=200)
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)

        ans = chatgpt.predict(final_value)[0]

        anim_placeholder.empty()
        progress_bar.empty()

        if ans == 0:
            result_placeholder.success("No Heart Disease Detected ✅\n\nNote: This is a prediction — consult a doctor for diagnosis.")
        else:
            result_placeholder.warning("Heart Disease Found ⚠️\n\nThis prediction suggests possible heart disease — seek medical advice.")
    else:
        st.info("Set the input sliders and press **Run Model** to predict.")

st.markdown('</div>', unsafe_allow_html=True)
