
from adaptive.question_bank import load_questions

masteries = {
    "linear_regression" : 0.85,
    "gradient_descent" : 0.35,
    "neural_networks" : 0.60
}

def recommend_question(masteries: dict) -> tuple[str, str]:
    concept = select_concept(masteries)
    difficulty = select_difficulty(masteries[concept])
    questions = load_questions()

    return select_question(questions, concept, difficulty)

def select_question(questions: list[dict], concept: str, difficulty: str) -> dict:
    matching_questions = [
        question
        for question in questions
        if question["concept"] == concept
        and question["difficulty"] == difficulty
    ]

    if not matching_questions:
        raise ValueError(
            f"No questions found for {concept} at {difficulty} difficulty."
        )

    return matching_questions[0]

def select_concept(masteries: dict) -> str:
    return min(masteries, key=masteries.get)

def select_difficulty(mastery: float) -> str:
    if mastery < 0.40:
        return "easy"
    elif mastery < 0.70:
        return "medium"
    else:
        return "hard"