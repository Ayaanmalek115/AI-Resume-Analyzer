def generate_questions(skills):

    questions = []


    question_bank = {


        "python":
        [
        "What are Python data types?",
        "Explain list vs tuple in Python.",
        "What is OOP in Python?"
        ],


        "java":
        [
        "Explain JVM, JRE and JDK.",
        "What are OOP concepts?",
        "What is inheritance in Java?"
        ],


        "sql":
        [
        "What is a primary key?",
        "Explain different types of joins.",
        "Difference between DELETE and TRUNCATE."
        ],


        "machine learning":
        [
        "What is Machine Learning?",
        "Explain supervised vs unsupervised learning.",
        "What is overfitting?"
        ],


        "html":
        [
        "What are HTML tags?",
        "Difference between div and span?"
        ],


        "css":
        [
        "Explain CSS selectors.",
        "What is Flexbox?"
        ]

    }



    for skill in skills:


        if skill in question_bank:


            questions.extend(
                question_bank[skill]
            )


    return questions
def check_answer(answer):


    keywords = [
        "data",
        "algorithm",
        "program",
        "object",
        "class",
        "database",
        "model",
        "learning",
        "function",
        "method"
    ]


    answer = answer.lower()


    count = 0


    for word in keywords:


        if word in answer:

            count = count + 1



    score = count * 20



    if score > 100:

        score = 100



    if score >= 70:

        feedback = "Excellent Answer"


    elif score >= 40:

        feedback = "Good Answer but add more details"


    else:

        feedback = "Need Improvement"


    return score, feedback