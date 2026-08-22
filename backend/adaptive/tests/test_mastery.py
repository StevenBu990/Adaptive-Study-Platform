from adaptive.mastery import update_mastery

def test_correct_answer_increases_mastery():
    result = update_mastery(0.5, True, "medium")
    assert result > 0.5

def test_incorrect_answer_decreases_mastery():
    result = update_mastery(0.5, False, "medium")
    assert result < 0.5

def test_harder_question_provides_more_evidence():
    easy = update_mastery(0.5, True, "easy")
    hard = update_mastery(0.5, True, "hard")

    assert hard > easy