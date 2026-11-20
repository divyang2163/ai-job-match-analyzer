import re
import streamlit as st

# ----------------------------------------
# SKILL DATABASE
# ----------------------------------------

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

# ----------------------------------------
# NEW FEATURE: SKILLS LEARNING ROADMAP
# ----------------------------------------

LEARNING_ROADMAP = {
    "Python": (
        "Practice functions, dictionaries, files, and error handling.",
        "Build a Python data-processing application."
    ),
    "SQL": (
        "Learn SELECT, JOIN, GROUP BY, and subqueries.",
        "Analyze a sample database using SQL queries."
    ),
    "JavaScript": (
        "Learn variables, functions, DOM manipulation, and fetch.",
        "Build an interactive web application."
    ),
    "HTML": (
        "Learn semantic HTML, forms, and page structure.",
        "Create a personal portfolio webpage."
    ),
    "CSS": (
        "Study responsive design, Flexbox, and Grid.",
        "Style a responsive portfolio website."
    ),
    "Git": (
        "Learn commits, branches, merging, and version control.",
        "Manage a coding project using Git."
    ),
    "GitHub": (
        "Learn repositories, pull requests, and GitHub workflows.",
        "Publish a documented project on GitHub."
    ),
    "Docker": (
        "Study containers, images, and Dockerfiles.",
        "Containerize a Python application."
    ),
    "Linux": (
        "Practice terminal commands, permissions, and processes.",
        "Create a shell script to automate a task."
    ),
    "AWS": (
        "Learn IAM, S3, EC2, and cloud fundamentals.",
        "Deploy a small application using AWS."
    ),
    "Azure": (
        "Study Azure compute, storage, and identity services.",
        "Deploy a simple application on Azure."
    ),
    "Google Cloud": (
        "Learn cloud storage, compute, and IAM fundamentals.",
        "Deploy a basic application on Google Cloud."
    ),
    "Pandas": (
        "Practice DataFrames, filtering, grouping, and cleaning.",
        "Analyze a CSV dataset using Pandas."
    ),
    "NumPy": (
        "Learn arrays, indexing, broadcasting, and calculations.",
        "Build a numerical analysis notebook."
    ),
    "Matplotlib": (
        "Learn line, bar, scatter, and histogram plots.",
        "Create a data visualization report."
    ),
    "Scikit-learn": (
        "Study preprocessing, model training, and evaluation.",
        "Train and evaluate a classification model."
    ),
    "Machine Learning": (
        "Learn supervised learning, validation, and evaluation metrics.",
        "Build a machine learning prediction project."
    ),
    "Deep Learning": (
        "Understand neural networks and backpropagation.",
        "Train a simple neural network."
    ),
    "TensorFlow": (
        "Learn tensors, Keras, and neural network training.",
        "Build a neural network using TensorFlow."
    ),
    "PyTorch": (
        "Learn tensors, autograd, and training loops.",
        "Train a classifier using PyTorch."
    ),
    "Data Analysis": (
        "Practice cleaning, exploration, and summarizing datasets.",
        "Create an exploratory data analysis report."
    ),
    "Excel": (
        "Practice formulas, pivot tables, and data visualization.",
        "Build an interactive Excel dashboard."
    ),
    "REST API": (
        "Study HTTP requests, JSON, endpoints, and status codes.",
        "Build a Python application using a public API."
    ),
    "MySQL": (
        "Learn schema design, queries, joins, and indexing.",
        "Create a small relational database."
    ),
    "PostgreSQL": (
        "Study PostgreSQL queries, constraints, and indexing.",
        "Build a database-backed Python project."
    ),
    "MongoDB": (
        "Learn document databases, collections, and CRUD operations.",
        "Create a document-based application."
    ),
    "Power BI": (
        "Learn Power Query, DAX basics, and data modeling.",
        "Build an interactive business dashboard."
    ),
    "Tableau": (
        "Practice calculated fields, charts, and dashboards.",
        "Create a visualization dashboard."
    )
}

# ----------------------------------------
# EXISTING MATCHING FUNCTIONS
# ----------------------------------------


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
        return "Strong technical skill overlap. Review the full job requirements."
    elif score >= 60:
        return "Good technical skill overlap. Consider applying and reviewing gaps."
    elif score >= 40:
        return "Moderate technical skill overlap. Focus on relevant missing skills."
    else:
        return "Low detected technical skill overlap. Review the role requirements."


# ----------------------------------------
# STREAMLIT APPLICATION
# ----------------------------------------

st.set_page_config(
    page_title="AI Job Match Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Job Match Analyzer")

st.write(
    "Compare your technical skills with a job description, "
    "identify skill gaps, and discover what to learn next."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    user_input = st.text_area(
        "Your Skills",
        placeholder="Example: Python, SQL, GitHub, Excel",
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
        st.warning("Please enter your skills and a job description.")

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

        if not job_skills:
            st.warning(
                "No recognized technical skills were found in "
                "the job description. A match score cannot be calculated."
            )

        else:
            st.subheader("📊 Job Match Results")

            score_col, detected_col, missing_col = st.columns(3)

            with score_col:
                st.metric("Match Score", f"{score}%")

            with detected_col:
                st.metric("Detected Job Skills", len(job_skills))

            with missing_col:
                st.metric("Missing Skills", len(missing_skills))

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

            # ----------------------------------------
            # NEW: PERSONALIZED LEARNING ROADMAP
            # ----------------------------------------

            st.divider()
            st.subheader("📚 Your Skills Learning Roadmap")

            if missing_skills:

                st.write(
                    "Based on the missing skills detected, "
                    "here are suggested learning activities and projects."
                )

                for number, skill in enumerate(missing_skills, start=1):

                    study_topic, practice_project = LEARNING_ROADMAP.get(
                        skill,
                        (
                            f"Study the fundamentals of {skill}.",
                            f"Build a beginner project using {skill}."
                        )
                    )

                    with st.expander(
                        f"Step {number}: Learn {skill}",
                        expanded=False
                    ):
                        st.markdown("**What to learn:**")
                        st.write(study_topic)

                        st.markdown("**Practice project:**")
                        st.write(practice_project)

            else:
                st.success(
                    "All detected job skills are matched. "
                    "Continue building practical experience."
                )

            st.caption(
                "This roadmap is based on detected skill keywords. "
                "It is a suggested study checklist, not a verified "
                "assessment of proficiency or job eligibility."
            )

            with st.expander("View all detected job skills"):
                for skill in job_skills:
                    st.write(f"• {skill}")
