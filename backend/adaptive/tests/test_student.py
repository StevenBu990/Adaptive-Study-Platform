from adaptive.student import StudentState


def test_student_starts_with_mastery():
    mastery = {
        "linear_regression": 0.5,
        "gradient_descent": 0.5,
        "neural_networks": 0.5
    }

    student = StudentState(mastery)

    assert student.mastery == mastery


def test_student_starts_with_no_seen_questions():
    student = StudentState({})

    assert len(student.seen_questions) == 0


def test_mark_question_seen():
    student = StudentState({})

    student.mark_question_seen(5)

    assert 5 in student.seen_questions


def test_has_seen_question():
    student = StudentState({})

    student.mark_question_seen(5)

    assert student.has_seen_question(5)
    assert not student.has_seen_question(6)