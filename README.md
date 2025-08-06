# AI-Based Resume Screener

An AI-powered tool designed to streamline the recruitment process by parsing resumes, extracting relevant skills, and matching them against predefined skill sets. This project leverages natural language processing (NLP) and machine learning to automate resume screening, saving time and improving efficiency.

---

## 🚀 Project Overview

The **AI-Based Resume Screener** processes resumes in PDF and DOCX formats, extracts plain text, and identifies relevant skills using a predefined list. It uses libraries like `spaCy`, `pdfminer.six`, and `docx2txt` for text processing and skill extraction. The tool is ideal for recruiters and HR professionals looking to automate the initial stages of candidate screening.

---

## ✨ Features

- **Resume Parsing**: Supports PDF and DOCX formats for extracting plain text.
- **Skill Extraction**: Identifies relevant skills from resumes using NLP and a predefined skill list.
- **Dataset Exploration**: Analyze and visualize resume datasets using `pandas` and `matplotlib`.
- **Customizable Skill List**: Easily update the predefined skill list to match job requirements.
- **Scalable**: Designed to handle large datasets of resumes efficiently.

---

## 🛠️ Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/resume-screener.git
   cd resume-screener
2. Set Up a Virtual Environment:
3. Install Dependencies:
   pip install -r requirements.txt
4. Download spaCy Language Model:
   python -m spacy download en_core_web_sm

🧰 Technologies Used
Python: Core programming language.
spaCy: NLP library for skill extraction.
pdfminer.six: PDF parsing.
docx2txt: DOCX parsing.
pandas: Data manipulation and analysis.
matplotlib & seaborn: Data visualization.
scikit-learn: (Optional) For advanced machine learning tasks.


### Notes:
- Replace `your-username` and `your-email@example.com` with your GitHub username and email.