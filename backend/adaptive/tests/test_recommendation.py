from adaptive.recommendation import (
    select_concept,
    select_difficulty,
    select_question,
    recommend_question
)


def test_selects_weakest_concept():
    masteries = {
        "linear_regression": 0.85,
        "gradient_descent": 0.35,
        "neural_networks": 0.60
    }

    assert select_concept(masteries) == "gradient_descent"


def test_easy_difficulty():
    assert select_difficulty(0.30) == "easy"


def test_medium_difficulty():
    assert select_difficulty(0.50) == "medium"


def test_hard_difficulty():
    assert select_difficulty(0.80) == "hard"


def test_recommend_question():
    masteries = {
        "linear_regression": 0.85,
        "gradient_descent": 0.35,
        "neural_networks": 0.60
    }

    question = recommend_question(masteries)

    assert question["concept"] == "gradient_descent"
    assert question["difficulty"] == "easy"

def test_select_question():
    questions = [
        {
            "id": 1,
            "concept": "gradient_descent",
            "difficulty": "easy",
            "question": "Test question",
            "choices": ["A", "B", "C", "D"],
            "answer": 0
        }
    ]

    question = select_question(
        questions,
        "gradient_descent",
        "easy"
    )

    assert question["id"] == 1