from app.resume_parser import parse_resume
from app.skill_extractor import extract_skills

# Define the file path to the sample resume and the predefined skill list
file_path = "data/resumes/sample_resume.pdf"  # Replace with the actual path to your resume file
skills = ["Python", "Machine Learning", "Data Analysis", "SQL", "Java", "Communication"]

def main():
    try:
        # Parse the resume to extract plain text
        resume_text = parse_resume(file_path)
        print("Resume Text Extracted Successfully!")

        # Extract matched skills from the resume text
        matched_skills = extract_skills(resume_text, skills)
        print("\nMatched Skills:")
        print(matched_skills)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()