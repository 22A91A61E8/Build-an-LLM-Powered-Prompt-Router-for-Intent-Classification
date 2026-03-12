def classify_intent(text):

    text = text.lower()

    code_keywords = ["python", "sql", "bug", "function", "code", "program"]
    data_keywords = ["average", "pivot", "data", "numbers", "analysis"]
    writing_keywords = ["rewrite", "paragraph", "professional", "writing"]
    career_keywords = ["career", "resume", "job", "interview", "cover letter"]

    for word in code_keywords:
        if word in text:
            return "code", 0.90

    for word in data_keywords:
        if word in text:
            return "data", 0.88

    for word in writing_keywords:
        if word in text:
            return "writing", 0.87

    for word in career_keywords:
        if word in text:
            return "career", 0.89

    return "unclear", 0.50

