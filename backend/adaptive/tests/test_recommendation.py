from adaptive.recommendation import (
    select_concept,
    select_difficulty,
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

    concept, difficulty = recommend_question(masteries)

    assert concept == "gradient_descent"
    assert difficulty == "easy"