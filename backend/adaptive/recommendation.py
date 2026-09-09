import random
from adaptive.question_bank import load_questions

masteries = {
    "linear_regression": 0.85,
    "gradient_descent": 0.35,
    "neural_networks": 0.60
}


def recommend_question(masteries: dict, seen_questions=None) -> dict:
    questions = load_questions()
    concept = select_concept(masteries)
    difficulty = select_difficulty(masteries[concept])

    return select_question(
        questions,
        concept,
        difficulty,
        seen_questions
    )


def select_question(
    questions: list[dict],
    concept: str,
    difficulty: str,
    seen_questions=None
) -> dict:
    if seen_questions is None:
        seen_questions = set()

    for fallback_difficulty in get_difficulty_fallbacks(difficulty):
        matching_questions = [
            question
            for question in questions
            if question["concept"] == concept
            and question["difficulty"] == fallback_difficulty
            and question["id"] not in seen_questions
        ]

        if matching_questions:
            return random.choice(matching_questions)

    raise ValueError(
        f"No questions found for {concept} at any available difficulty."
    )


def select_concept(masteries: dict) -> str:
    return min(masteries, key=masteries.get)


def select_difficulty(mastery: float) -> str:
    if mastery < 0.40:
        return "easy"
    elif mastery < 0.70:
        return "medium"
    else:
        return "hard"
    
def get_difficulty_fallbacks(difficulty: str) -> list:
    if difficulty == "easy":
        return ["easy", "medium", "hard"]
    elif difficulty == "medium":
        return ["medium", "easy", "hard"]
    else:
        return ["hard", "medium", "easy"]