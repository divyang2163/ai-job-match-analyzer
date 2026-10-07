# 🤖 AI Job Match Analyzer

A Python-based job analysis tool that compares a user's technical skills with a job description and identifies matched skills, missing skills, and an overall match score.

The project includes both a command-line version and an interactive Streamlit web application.

## 🚀 Features

- Paste your current technical skills
- Paste a full job description
- Automatically detect technical skills
- Calculate a job match percentage
- Identify matched skills
- Identify missing skills
- Generate a recommendation based on the match score
- Interactive web interface using Streamlit
- Supports common skill aliases such as ML, JavaScript/JS, AWS, and REST APIs

## 🛠️ Technologies Used

- Python
- Streamlit
- Regular Expressions
- Dictionaries
- Functions
- Conditional Logic
- String Processing

## 📁 Project Structure

```text
ai-job-match-analyzer/
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

### `app.py`
Runs the interactive Streamlit web application.

### `main.py`
Runs the command-line version of the analyzer.

### `requirements.txt`
Contains the Python packages needed to run the web application.

## ▶️ Run the Web Application

### 1. Install the required package

```bash
python3 -m pip install -r requirements.txt
```

### 2. Start the Streamlit application

```bash
python3 -m streamlit run app.py
```

The application will open in your web browser.

## 💻 Run the Command-Line Version

```bash
python3 main.py
```

## 🧠 How It Works

The analyzer uses a predefined skill dictionary and common aliases to identify technical skills mentioned in both the user's skill list and the job description.

It then compares the detected skills and calculates:

```text
Match Score = Matched Skills / Detected Job Skills × 100
```

The results are separated into matched and missing skills to make skill gaps easy to identify.

## ⚠️ Current Version

The current version uses rule-based skill matching and regular expressions rather than a machine-learning model or external AI API.

This makes the application fast, transparent, and easy to run locally.

## 🔮 Future Improvements

- Add NLP-based skill extraction
- Add AI-generated job-fit explanations
- Analyze uploaded resumes
- Add weighted scoring for required vs. preferred skills
- Detect education and experience requirements
- Add resume improvement suggestions
- Deploy the application online

## 👤 Author

**Divyang Parikh**