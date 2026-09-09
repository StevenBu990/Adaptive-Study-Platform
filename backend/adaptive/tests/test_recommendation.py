from adaptive.recommendation import (
    select_concept,
    select_difficulty,
    recommend_question,
    select_question,
    get_difficulty_fallbacks
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


def test_select_question_avoids_seen_questions():
    questions = [
        {
            "id": 1,
            "concept": "linear_regression",
            "difficulty": "medium",
            "question": "Question 1",
            "choices": ["A", "B", "C", "D"],
            "answer": 0
        },
        {
            "id": 2,
            "concept": "linear_regression",
            "difficulty": "medium",
            "question": "Question 2",
            "choices": ["A", "B", "C", "D"],
            "answer": 0
        }
    ]

    result = select_question(
        questions,
        "linear_regression",
        "medium",
        seen_questions={1}
    )

    assert result["id"] == 2

def test_select_question_fails_when_all_questions_seen():
    questions = [
        {
            "id": 1,
            "concept": "linear_regression",
            "difficulty": "medium",
            "question": "Question 1",
            "choices": ["A", "B", "C", "D"],
            "answer": 0
        }
    ]

    try:
        select_question(
            questions,
            "linear_regression",
            "medium",
            seen_questions={1}
        )
        assert False
    except ValueError:
        assert True


def test_recommend_question_avoids_seen_questions():
    masteries = {
        "linear_regression": 0.50,
        "gradient_descent": 0.50,
        "neural_networks": 0.50
    }

    seen_questions = {1, 2, 3}

    question = recommend_question(
        masteries,
        seen_questions
    )

    assert question["id"] not in seen_questions

def test_difficulty_fallbacks():
    assert get_difficulty_fallbacks("easy") == ["easy", "medium", "hard"]
    assert get_difficulty_fallbacks("medium") == ["medium", "easy", "hard"]
    assert get_difficulty_fallbacks("hard") == ["hard", "medium", "easy"]


def test_select_question_falls_back_to_next_difficulty():
    questions = [
        {
            "id": 1,
            "concept": "gradient_descent",
            "difficulty": "easy",
            "question": "Easy question",
            "choices": ["A", "B", "C", "D"],
            "answer": 0
        },
        {
            "id": 2,
            "concept": "gradient_descent",
            "difficulty": "medium",
            "question": "Medium question",
            "choices": ["A", "B", "C", "D"],
            "answer": 0
        }
    ]

    result = select_question(
        questions,
        "gradient_descent",
        "easy",
        seen_questions={1}
    )

    assert result["id"] == 2


def test_select_question_falls_back_to_hard():
    questions = [
        {
            "id": 1,
            "concept": "gradient_descent",
            "difficulty": "easy",
            "question": "Easy question",
            "choices": ["A", "B", "C", "D"],
            "answer": 0
        },
        {
            "id": 2,
            "concept": "gradient_descent",
            "difficulty": "medium",
            "question": "Medium question",
            "choices": ["A", "B", "C", "D"],
            "answer": 0
        },
        {
            "id": 3,
            "concept": "gradient_descent",
            "difficulty": "hard",
            "question": "Hard question",
            "choices": ["A", "B", "C", "D"],
            "answer": 0
        }
    ]

    result = select_question(
        questions,
        "gradient_descent",
        "easy",
        seen_questions={1, 2}
    )

    assert result["id"] == 3