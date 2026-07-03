import PyPDF2
import re


def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def extract_email(text):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):

    pattern = r"\+?\d[\d\s-]{8,}\d"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_name(text):

    lines = text.split("\n")

    ignore_words = [
        "page",
        "email",
        "phone",
        "address",
        "linkedin",
        "github",
        "resume",
        "curriculum",
        "vitae"
    ]

    for line in lines:

        line = line.strip()

        if len(line) < 3:
            continue

        if any(word in line.lower() for word in ignore_words):
            continue

        if len(line.split()) <= 4:
            return line

    return "Not Found"