# AI Job Match Analyzer
# Author: Divyang Parikh

import re


# --------------------------------------------------
# SKILL DATABASE
# Each skill includes common names/variations that
# may appear in a job description.
# --------------------------------------------------

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

    "Machine Learning": [
        "machine learning",
        "machine-learning",
        "ml"
    ],

    "Deep Learning": [
        "deep learning",
        "deep-learning"
    ],

    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],

    "Data Analysis": [
        "data analysis",
        "data analytics",
        "data analyst"
    ],

    "Excel": [
        "excel",
        "microsoft excel"
    ],

    "REST API": [
        "rest api",
        "restful api",
        "restful services"
    ],

    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql", "postgres"],
    "MongoDB": ["mongodb"],

    "Power BI": ["power bi", "powerbi"],
    "Tableau": ["tableau"]
}


def contains_phrase(text, phrase):
    """
    Check whether a skill or alias appears as a complete
    word/phrase instead of accidentally matching part
    of another word.

    Example:
    'git' will not automatically match 'github'.
    """

    pattern = r"(?<!\w)" + re.escape(phrase.lower()) + r"(?!\w)"

    return re.search(pattern, text.lower()) is not None


def detect_skills(text):
    """
    Detect recognized technical skills in text.
    """

    detected_skills = []

    for skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            if contains_phrase(text, alias):
                detected_skills.append(skill)
                break

    return detected_skills


def get_user_skills():
    """
    Ask the user to enter their skills.
    """

    print("\nEnter your skills separated by commas:")
    user_input = input("> ")

    return detect_skills(user_input)


def get_job_description():
    """
    Allow the user to paste a multi-line job description.
    """

    print("\nPaste the job description below.")
    print("When finished, type DONE on a new line and press Enter.\n")

    lines = []

    while True:

        line = input()

        if line.strip().lower() == "done":
            break

        lines.append(line)

    return " ".join(lines)


def compare_skills(user_skills, job_skills):
    """
    Compare the user's skills with skills detected
    in the job description.
    """

    matched_skills = []
    missing_skills = []

    for skill in job_skills:

        if skill in user_skills:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills


def calculate_match_score(matched_skills, job_skills):
    """
    Calculate the percentage of detected job skills
    that the user already has.
    """

    if not job_skills:
        return 0

    score = (len(matched_skills) / len(job_skills)) * 100

    return round(score)


def get_recommendation(score):
    """
    Generate a simple recommendation based on
    the calculated match score.
    """

    if score >= 80:
        return "Strong match — this position looks worth applying for."

    elif score >= 60:
        return (
            "Good match — consider applying and review the "
            "missing skills before an interview."
        )

    elif score >= 40:
        return (
            "Moderate match — you have relevant skills, "
            "but there are some important gaps."
        )

    else:
        return (
            "Low match — review the missing skills and determine "
            "whether the position fits your current experience."
        )


def display_results(job_skills, matched_skills, missing_skills, score):
    """
    Display the final analysis.
    """

    print("\n" + "=" * 60)
    print("AI JOB MATCH ANALYSIS")
    print("=" * 60)

    if not job_skills:

        print("\nNo recognized technical skills were found.")
        print("Try using a more detailed job description.")

        return

    print(f"\nMatch Score: {score}%")

    print("\nDetected Job Skills:")

    for skill in job_skills:
        print(f"• {skill}")

    print("\nMatched Skills:")

    if matched_skills:

        for skill in matched_skills:
            print(f"✓ {skill}")

    else:
        print("None")

    print("\nMissing Skills:")

    if missing_skills:

        for skill in missing_skills:
            print(f"✗ {skill}")

    else:
        print("None — all detected skills matched!")

    print("\nRecommendation:")
    print(get_recommendation(score))

    print("\n" + "=" * 60)


def main():

    print("=" * 60)
    print("AI JOB MATCH ANALYZER")
    print("=" * 60)

    user_skills = get_user_skills()

    job_description = get_job_description()

    job_skills = detect_skills(job_description)

    matched_skills, missing_skills = compare_skills(
        user_skills,
        job_skills
    )

    score = calculate_match_score(
        matched_skills,
        job_skills
    )

    display_results(
        job_skills,
        matched_skills,
        missing_skills,
        score
    )


if __name__ == "__main__":
    main()