import spacy

def extract_skills(resume_text, skill_list):
    """
    Extract matching skills from resume text using spaCy and a predefined list.

    Args:
        resume_text (str): The plain text of the resume.
        skill_list (list): A list of predefined skills to match.

    Returns:
        list: A list of matched skills.
    """
    # Load spaCy's English model
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(resume_text)

    # Normalize skill list to lowercase for case-insensitive matching
    normalized_skills = [skill.lower() for skill in skill_list]

    # Extract tokens from the resume text
    matched_skills = set()
    for token in doc:
        if token.text.lower() in normalized_skills:
            matched_skills.add(token.text)

    return list(matched_skills)