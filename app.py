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
/* full app animated gradient background with shimmer */
.stApp {
    background: linear-gradient(270deg, #0f2027, #203a43, #2c5364);
    background-size: 600% 600%;
    animation: gradientAnimation 45s ease infinite;
    color: #e6eef8;
    min-height: 100vh;
    position: relative;
    overflow: hidden;
}

@keyframes gradientAnimation {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* subtle noise grain overlay */
.stApp::before {
    content: "";
    pointer-events: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: url("https://grainy-gradients.vercel.app/noise.svg");
    opacity: 0.15;
    z-index: 0;
    mix-blend-mode: soft-light;
}

/* floating colorful blobs with smooth animation */
.blob {
    position: absolute;
    border-radius: 50%;
    filter: blur(120px);
    opacity: 0.2;
    animation-timing-function: ease-in-out;
    animation-iteration-count: infinite;
}

.blob.one {
    width: 400px;
    height: 400px;
    background: #ff0080;
    top: -120px;
    left: -100px;
    animation-name: blobMoveOne;
    animation-duration: 16s;
}

.blob.two {
    width: 360px;
    height: 360px;
    background: #00bfff;
    bottom: -130px;
    right: -90px;
    animation-name: blobMoveTwo;
    animation-duration: 21s;
}

@keyframes blobMoveOne {
    0%, 100% { transform: translateY(0) translateX(0) scale(1);}
    50% { transform: translateY(20px) translateX(30px) scale(1.1);}
}

@keyframes blobMoveTwo {
    0%, 100% { transform: translateY(0) translateX(0) scale(1);}
    50% { transform: translateY(-20px) translateX(-30px) scale(0.85);}
}

/* glass card with glowing edges and smooth shadow */
.main-card {
    position: relative;
    z-index: 1;
    padding: 28px 30px;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.04);
    box-shadow: 0 8px 40px rgba(0, 0, 0, 0.7), 0 0 10px 1px #0ff;
    backdrop-filter: blur(14px) saturate(150%);
    border: 1px solid rgba(0, 255, 255, 0.3);
    transition: all 0.35s ease;
}

.main-card:hover {
    box-shadow: 0 16px 60px rgba(0,255,255,0.9), 0 0 20px 3px #0ff;
    transform: translateY(-10px) scale(1.03);
}

/* header fonts */
.app-title {
    font-size: 26px;
    font-weight: 900;
    letter-spacing: 0.5px;
    text-shadow: 0 0 5px #0ff;
}

.app-sub {
    font-size: 14px;
    color: rgba(230, 238, 248, 0.9);
}

/* modern gradient buttons with smooth hover */
.stButton > button {
    background: linear-gradient(45deg, #00f, #0ff);
    color: white;
    border-radius: 9999px;
    padding: 10px 22px;
    font-weight: 700;
    border: none;
    box-shadow: 0 8px 28px rgba(0, 255, 255, 0.7);
    cursor: pointer;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(45deg, #0ff, #00f);
    box-shadow: 0 14px 44px rgba(0, 255, 255, 1);
    transform: translateY(-2px) scale(1.05);
}

/* sidebar with transparent dark blur */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.85);
    border-right: 1px solid rgba(0, 255, 255, 0.25);
    backdrop-filter: blur(14px);
    color: #aaddff;
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
