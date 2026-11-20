# 🤖 AI Job Match Analyzer

A Python-based job analysis tool that helps users compare their technical skills with job descriptions, identify skill gaps, and discover what to learn next.

The application analyzes recognized technical skills, calculates a match percentage, and generates a personalized learning roadmap with suggested topics and hands-on projects.

Built using **Python and Streamlit**, the project includes both an interactive web application and a command-line version.

## 🌐 Live Application

**Try the application here:**

https://divyang-ai-job-match-analyzer.streamlit.app/

No installation is required to use the online version.

## 🚀 Features

- Compare your technical skills with a job description
- Automatically identify recognized technical skills
- Calculate a technical skill match percentage
- Display matched and missing skills
- Generate recommendations based on the match score
- Create a personalized learning roadmap for missing skills
- Suggest learning topics and practical projects
- Interactive web interface built with Streamlit
- Support common skill aliases such as ML, JS, AWS, and GCP
- Command-line version for local use

## 📚 Personalized Skills Learning Roadmap

The Skills Learning Roadmap helps users understand what they could study next based on the technical skills identified as missing from a job description.

For each missing skill, the application provides:

1. A recommended learning topic
2. A suggested hands-on practice project

### Example

**Your Skills:**
Python, SQL, GitHub, Excel

**Job Requirements:**
Python, SQL, Docker, AWS, Machine Learning

**Match Results:**

- Match Score: 40%
- Matched Skills: Python, SQL
- Missing Skills: Docker, AWS, Machine Learning

**Suggested Learning Roadmap:**

| Missing Skill | What to Learn | Practice Project |
|---|---|---|
| Docker | Containers, images, Dockerfiles | Containerize a Python application |
| AWS | IAM, S3, EC2, cloud fundamentals | Deploy a small application |
| Machine Learning | Supervised learning, validation, evaluation | Build a prediction model |

The roadmap uses predefined recommendations and is intended as a learning guide rather than a verified assessment of job eligibility.

## 🛠️ Technologies Used

- Python
- Streamlit
- Regular Expressions (Regex)
- Python Dictionaries and Lists
- Functions and Conditional Logic
- String Processing
- Git and GitHub

## 📁 Project Structure

```text
ai-job-match-analyzer/
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

### app.py

Runs the interactive Streamlit application, including job matching and the personalized learning roadmap.

### main.py

Runs the command-line version of the job analyzer.

### requirements.txt

Contains the packages required to run the web application.

## ▶️ Run the Web Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/divyang2163/ai-job-match-analyzer.git
cd ai-job-match-analyzer
```

### 2. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 3. Start Streamlit

```bash
python3 -m streamlit run app.py
```

The application will open in your web browser.

## 💻 Run the Command-Line Version

```bash
python3 main.py
```

Enter your technical skills and paste a job description to receive the analysis.

The command-line version provides skill matching and score-based recommendations. The personalized learning roadmap is currently available in the Streamlit application.

## 🧠 How It Works

### Step 1: Skill Detection

The application uses a predefined dictionary of technical skills and aliases.

Regular expressions identify recognized skills in the user's input and job description.

### Step 2: Skill Comparison

Detected job skills are compared against the user's recognized skills.

The application separates them into:

- Matched Skills
- Missing Skills

### Step 3: Match Score Calculation

```text
Match Score = (Matched Skills / Detected Job Skills) × 100
```

The calculation considers recognized technical skills only. All detected job skills currently have equal weight.

### Step 4: Recommendation

The application generates a recommendation based on the calculated match score.

### Step 5: Personalized Learning Roadmap

For each missing skill, the application retrieves a predefined learning topic and practice project from its learning roadmap database.

These recommendations help users identify potential areas for technical improvement.

## ⚠️ Current Limitations

- Uses rule-based skill detection rather than a trained machine-learning model
- Recognizes skills included in its predefined database
- Does not currently analyze uploaded resumes
- Does not evaluate years of experience, education, or certifications
- Does not distinguish required skills from preferred skills
- Match scores are indicators of detected skill overlap, not hiring predictions

## 🔮 Future Improvements

- Add NLP-based skill extraction
- Support PDF and DOCX resume uploads
- Introduce AI-generated job-fit explanations
- Add weighted scoring for required and preferred skills
- Detect education and experience requirements
- Provide resume improvement suggestions
- Add relevant learning resources to the roadmap
- Expand the technical skills database

## 🎯 Project Purpose

I built this project to strengthen my Python programming skills and apply what I have learned about data processing, conditional logic, dictionaries, and application development.

The goal is to create a practical tool that helps students and job seekers understand technical skill requirements and identify opportunities for improvement.

I plan to continue expanding the project as I develop my knowledge of machine learning, natural language processing, and AI application development.

## 👤 Author

**Divyang Parikh**

Computer Science & Information Systems Student | AI Concentration

[GitHub](https://github.com/divyang2163) | [LinkedIn](https://www.linkedin.com/in/divyang-parikh-2ba4411b7/)
