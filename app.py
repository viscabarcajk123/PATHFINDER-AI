from pathlib import Path
import html
import json
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from streams import STREAMS
from courses import COURSES

ROOT = Path(__file__).resolve().parent
MODEL_DIR = ROOT / "models"

st.set_page_config(page_title="PATHFINDER AI", page_icon="🧭", layout="wide")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
:root { --cream:#F7F1E7; --paper:#FFFCF6; --navy:#302820; --terracotta:#B96545; --sage:#6D7D63; --gold:#D6AC62; }
.stApp { background:var(--cream); color:var(--navy); font-family:'DM Sans',sans-serif; }
[data-testid="stSidebar"] { background:#EDE2D1; }
h1,h2,h3 { color:var(--navy)!important; font-family:'Playfair Display',serif!important; }
p, label, .stMarkdown, [data-testid="stCaptionContainer"] { color:var(--navy); }
div.stButton > button, div.stFormSubmitButton > button { background:var(--terracotta); color:#fffaf3; border:0; border-radius:12px; padding:.65rem 1.15rem; font-weight:700; }
div.stButton > button:hover, div.stFormSubmitButton > button:hover { background:#965039; color:white; border:0; }
[data-testid="stMetric"] { background:var(--paper); border:1px solid #E5D8C5; padding:16px; border-radius:14px; }
.pathfinder-hero { background:#302820; color:#FFF4E5; padding:28px; border-radius:20px; margin-bottom:18px; }
.pathfinder-hero h1 { color:#FFF4E5!important; margin-bottom:5px; }
.pathfinder-hero p { color:#E7D8C7!important; }
.result-card { background:#FFFCF6; border:1px solid #E5D8C5; border-radius:16px; padding:18px; margin:8px 0; }
.course-card { background:#FFFCF6; border:1px solid #E5D8C5; border-top:4px solid #B96545; border-radius:14px; padding:16px; height:100%; }
.course-rank { color:#B96545; font-weight:700; letter-spacing:1.5px; font-size:12px; margin:0 0 4px 0; }
.course-name { font-family:'Playfair Display',serif; font-weight:700; font-size:17px; margin:0 0 6px 0; color:#302820; }
.course-where { font-size:14px; margin:0; color:#5a4d40; }
hr { border-color:#DFD2C0; }
</style>
""", unsafe_allow_html=True)


def show_top_courses(field_name):
    """Show the top 3 courses for a field as three cards."""
    courses = COURSES.get(field_name, [])
    if not courses:
        st.info("Course suggestions for this field are not available yet.")
        return
    cols = st.columns(len(courses))
    for i, (col, (course, where)) in enumerate(zip(cols, courses), start=1):
        col.markdown(
            f'<div class="course-card"><p class="course-rank">COURSE {i}</p>'
            f'<p class="course-name">{html.escape(course)}</p>'
            f'<p class="course-where">{html.escape(where)}</p></div>',
            unsafe_allow_html=True,
        )


stream_names = list(STREAMS.keys())
with st.sidebar:
    st.markdown("## 🧭 PATHFINDER AI")
    st.caption("Your career compass")
    st.divider()
    stream = st.radio("CHOOSE YOUR STREAM", stream_names, format_func=lambda s: f"{STREAMS[s]['icon']}  {s}")
    st.divider()
    page = st.radio("VIEW", ["Career Finder", "Model Evaluation"])
    st.divider()
    st.caption(f"{stream.upper()} STREAM")
    st.caption(f"{len(STREAMS[stream]['questions'])} questions · {len(STREAMS[stream]['fields'])} fields")

cfg = STREAMS[stream]
slug, FIELDS, QUESTIONS = cfg["slug"], cfg["fields"], cfg["questions"]
MODEL_PATH = MODEL_DIR / f"{slug}_model.pkl"
METRICS_PATH = MODEL_DIR / f"{slug}_metrics.json"

if page == "Career Finder":
    st.markdown(f"""
    <div class="pathfinder-hero">
      <p style="letter-spacing:2px;font-size:12px;font-weight:700;">DISCOVER YOUR DIRECTION</p>
      <h1>Find your {stream} pathway.</h1>
      <p>Answer honestly. Pathfinder estimates which fields best align with your interests and preferences.</p>
    </div>""", unsafe_allow_html=True)
    if not MODEL_PATH.exists():
        st.error("The trained model was not found. Run `py train_model.py` in the project folder first.")
        st.stop()
    model = joblib.load(MODEL_PATH)
    with st.form(f"assessment_form_{slug}"):
        st.markdown("### Your assessment")
        st.caption("Rate each statement from 1 to 5. There are no right or wrong answers.")
        answers = {}
        for i, (col, question) in enumerate(QUESTIONS):
            answers[col] = st.slider(f"{i+1}. {question}", 1, 5, 3, key=f"{slug}_answer_{col}")
        submitted = st.form_submit_button("Discover my best-fit fields", use_container_width=True)
    if submitted:
        input_df = pd.DataFrame([[answers[col] for col, _ in QUESTIONS]], columns=[col for col, _ in QUESTIONS])
        predictions = np.clip(np.asarray(model.predict(input_df)).reshape(1, -1)[0], 0, 100)
        ranked = sorted(zip(FIELDS, predictions), key=lambda item: item[1], reverse=True)
        best, best_score = ranked[0]
        st.markdown("---")
        st.markdown("### Your Pathfinder results")
        st.markdown(f'<div class="result-card"><p style="color:#B96545;font-weight:700;letter-spacing:1.5px;font-size:12px;">YOUR TOP MATCH</p><h2 style="margin-top:0;">{best[0]}</h2><p>{best[2]}</p></div>', unsafe_allow_html=True)
        st.metric("Estimated compatibility score", f"{best_score:.0f}/100")
        st.caption("This score is a model-generated estimate, not a probability of success, an admission prediction, or a validated career assessment.")

        st.markdown(f"### Top 3 courses in {best[0]}")
        show_top_courses(best[0])
        st.caption("Course names, institutions and entrance exams are indicative. Admission rules and availability change every year, so always confirm on the official websites.")

        st.markdown("### Your other matches")
        for (name, col, desc), score in ranked[1:]:
            with st.expander(f"{name} · {score:.0f}/100"):
                st.write(desc)
                st.markdown("**Top 3 courses**")
                show_top_courses(name)
        st.markdown("### Your score overview")
        st.bar_chart(pd.DataFrame({"Estimated compatibility":[round(float(item[1]),1) for item in ranked]}, index=[item[0][0] for item in ranked]))
else:
    st.markdown(f"""
    <div class="pathfinder-hero">
      <p style="letter-spacing:2px;font-size:12px;font-weight:700;">MODEL TRANSPARENCY · {stream.upper()}</p>
      <h1>Model Evaluation</h1>
      <p>Inspect performance on held-out synthetic records.</p>
    </div>""", unsafe_allow_html=True)
    if not METRICS_PATH.exists():
        st.warning("Evaluation metrics are not available yet. Run `py train_model.py` first.")
        st.stop()
    metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    st.markdown("### Compatibility-score prediction · Regression")
    c1,c2,c3 = st.columns(3)
    c1.metric("MAE", f"{metrics['regression']['mae']:.2f}")
    c2.metric("R²", f"{metrics['regression']['r2']:.3f}")
    c3.metric("Test records", f"{metrics['test_records']:,}")
    st.caption("MAE is the average absolute difference between predicted and target scores on a 0–100 scale; lower is better. R² compares predictions with a test-set mean baseline; closer to 1 is generally better.")
    st.markdown("### Top-field prediction · Classification")
    c1,c2,c3 = st.columns(3)
    c1.metric("Weighted precision", f"{metrics['classification']['precision_weighted']:.3f}")
    c2.metric("Weighted recall", f"{metrics['classification']['recall_weighted']:.3f}")
    c3.metric("Weighted F1-score", f"{metrics['classification']['f1_weighted']:.3f}")
    st.metric("Top-field accuracy", f"{metrics['classification']['accuracy']:.3f}")
    st.caption("These metrics compare the predicted top field with the top field implied by synthetic target scores. They do not establish real-world career guidance accuracy.")
    st.markdown("### Per-field regression performance")
    per_field = pd.DataFrame(metrics["per_field"]).rename(columns={"field":"Field","mae":"MAE","r2":"R²"})
    st.dataframe(per_field, use_container_width=True, hide_index=True)
    st.markdown("### Important limitation")
    st.write("The dataset is synthetic and its scores are generated from a designed rubric. Strong metrics mainly indicate how well the model learns that rubric. Real-world usefulness would require validation with student feedback and suitable outcome data.")
