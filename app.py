import re
import streamlit as st


SKILL_ALIASES = {
    "Python": ["python"],
    "SQL": ["sql"],
    "JavaScript": ["javascript", "java script", "js"],
    "HTML": ["html", "html5"],
    "CSS": ["css", "css3"],
    "Git": ["git"],
    "GitHub": ["github"],
    "Docker": ["docker"],
    "Linux": ["linux"],
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure", "microsoft azure"],
    "Google Cloud": ["google cloud", "gcp"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Matplotlib": ["matplotlib"],
    "Scikit-learn": ["scikit-learn", "scikit learn", "sklearn"],
    "Machine Learning": ["machine learning", "machine-learning", "ml"],
    "Deep Learning": ["deep learning", "deep-learning"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "Data Analysis": ["data analysis", "data analytics", "data analyst"],
    "Excel": ["excel", "microsoft excel"],
    "REST API": ["rest api", "restful api", "restful services"],
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql", "postgres"],
    "MongoDB": ["mongodb"],
    "Power BI": ["power bi", "powerbi"],
    "Tableau": ["tableau"]
}


def contains_phrase(text, phrase):
    pattern = r"(?<!\w)" + re.escape(phrase.lower()) + r"(?!\w)"
    return re.search(pattern, text.lower()) is not None


def detect_skills(text):
    detected_skills = []

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if contains_phrase(text, alias):
                detected_skills.append(skill)
                break

    return detected_skills


def compare_skills(user_skills, job_skills):
    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in user_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills


def calculate_match_score(matched_skills, job_skills):
    if not job_skills:
        return 0

    return round((len(matched_skills) / len(job_skills)) * 100)


def get_recommendation(score):
    if score >= 80:
        return "Strong match — this position looks worth applying for."
    elif score >= 60:
        return "Good match — consider applying and review the missing skills."
    elif score >= 40:
        return "Moderate match — you have relevant skills, but there are some important gaps."
    else:
        return "Low match — review the missing skills and determine whether the role fits your current experience."


st.set_page_config(
    page_title="AI Job Match Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Job Match Analyzer")

st.write(
    "Compare your current technical skills with a job description "
    "and identify your match score, strengths, and skill gaps."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    user_input = st.text_area(
        "Your Skills",
        placeholder="Example: Python, SQL, GitHub, Excel, Data Analysis",
        height=220
    )

with col2:
    job_description = st.text_area(
        "Job Description",
        placeholder="Paste the full job description here...",
        height=220
    )

analyze_button = st.button(
    "Analyze Job Match",
    type="primary",
    use_container_width=True
)

if analyze_button:

    if not user_input.strip() or not job_description.strip():
        st.warning("Please enter your skills and paste a job description.")

    else:
        user_skills = detect_skills(user_input)
        job_skills = detect_skills(job_description)

        matched_skills, missing_skills = compare_skills(
            user_skills,
            job_skills
        )

        score = calculate_match_score(
            matched_skills,
            job_skills
        )

        st.divider()

        st.subheader("Job Match Results")

        score_col, detected_col, missing_col = st.columns(3)

        with score_col:
            st.metric(
                label="Match Score",
                value=f"{score}%"
            )

        with detected_col:
            st.metric(
                label="Detected Job Skills",
                value=len(job_skills)
            )

        with missing_col:
            st.metric(
                label="Missing Skills",
                value=len(missing_skills)
            )

        st.progress(score / 100)

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.subheader("✅ Matched Skills")

            if matched_skills:
                for skill in matched_skills:
                    st.success(skill)
            else:
                st.info("No matched skills detected.")

        with result_col2:
            st.subheader("❌ Missing Skills")

            if missing_skills:
                for skill in missing_skills:
                    st.error(skill)
            else:
                st.success("No missing skills detected.")

        st.subheader("🎯 Recommendation")
        st.info(get_recommendation(score))

        with st.expander("View all detected job skills"):
            if job_skills:
                for skill in job_skills:
                    st.write(f"• {skill}")
            else:
                st.write("No recognized technical skills were detected.")