from adaptive.mastery import update_mastery
from adaptive.recommendation import recommend_question
from adaptive.student import StudentState


student = StudentState({
    "linear_regression": 0.50,
    "gradient_descent": 0.50,
    "neural_networks": 0.50
})


answers = [
    True,
    True,
    False,
    True,
    False,
    True,
    True,
    False,
    True,
    True
]


for correct in answers:
    question = recommend_question(student.mastery)

    concept = question["concept"]
    difficulty = question["difficulty"]

    old_mastery = student.mastery[concept]

    new_mastery = update_mastery(
        old_mastery,
        correct,
        difficulty
    )

    student.mastery[concept] = new_mastery
    student.mark_question_seen(question["id"])

    print(
        f"Question #{question['id']} | "
        f"Concept: {concept} | "
        f"Difficulty: {difficulty}"
    )

    print(
        f"Question: {question['question']}"
    )

    print(
        f"Correct: {correct} | "
        f"Mastery: {old_mastery:.2f} -> {new_mastery:.2f}"
    )