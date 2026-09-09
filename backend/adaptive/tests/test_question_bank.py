from adaptive.question_bank import load_questions


def test_load_questions():
    questions = load_questions()

    assert len(questions) == 27


def test_question_has_required_fields():
    questions = load_questions()

    required_fields = {
        "id",
        "concept",
        "difficulty",
        "question",
        "choices",
        "answer"
    }

    for question in questions:
        assert required_fields.issubset(question.keys())


def test_question_has_four_choices():
    questions = load_questions()

    for question in questions:
        assert len(question["choices"]) == 4


def test_answer_is_valid_choice_index():
    questions = load_questions()

    for question in questions:
        assert 0 <= question["answer"] < len(question["choices"])


def test_question_metadata_is_valid():
    questions = load_questions()

    valid_difficulties = {"easy", "medium", "hard"}
    valid_concepts = {
        "linear_regression",
        "gradient_descent",
        "neural_networks"
    }

    for question in questions:
        assert question["difficulty"] in valid_difficulties
        assert question["concept"] in valid_concepts

def test_three_questions_per_concept_and_difficulty():
    questions = load_questions()

    concepts = {
        "linear_regression",
        "gradient_descent",
        "neural_networks"
    }

    difficulties = {"easy", "medium", "hard"}

    for concept in concepts:
        for difficulty in difficulties:
            matching = [
                q for q in questions
                if q["concept"] == concept
                and q["difficulty"] == difficulty
            ]

            assert len(matching) == 3

def test_question_ids_are_unique():
    questions = load_questions()

    ids = [question["id"] for question in questions]

    assert len(ids) == len(set(ids))