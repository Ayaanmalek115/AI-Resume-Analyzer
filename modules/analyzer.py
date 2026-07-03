def analyze_resume(resume_text):

    text = resume_text.lower()

    skills_list = [
        "python",
        "java",
        "c++",
        "sql",
        "html",
        "css",
        "javascript",
        "react",
        "flask",
        "django",
        "git",
        "machine learning",
        "artificial intelligence",
        "data science"
    ]

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    score = 0

    # Skills (30 Marks)
    score += min(len(found_skills) * 5, 30)

    # Education
    education_keywords = [
        "b.tech",
        "bachelor",
        "degree",
        "college",
        "university"
    ]

    if any(word in text for word in education_keywords):
        score += 15

    # Projects
    if "project" in text:
        score += 15

    # Experience
    if "experience" in text or "internship" in text:
        score += 10

    # Certifications
    if "certificate" in text or "certification" in text:
        score += 10

    suggestions = []

    if score < 30:
        suggestions.append("Add more technical skills.")

    if "project" not in text:
        suggestions.append("Add your academic or personal projects.")

    if "experience" not in text and "internship" not in text:
        suggestions.append("Include internships or work experience.")

    if "certificate" not in text:
        suggestions.append("Add certifications.")

    if len(found_skills) < 5:
        suggestions.append("Mention more relevant technical skills.")

    return found_skills, suggestions, score