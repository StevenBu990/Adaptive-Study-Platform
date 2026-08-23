from adaptive.mastery import update_mastery
from adaptive.recommendation import recommend_question

student_mastery = {
    "linear_regression" : 0.50,
    "gradient descent" : 0.50,
    "neural_networks" : 0.50
}

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
    concept, difficulty = recommend_question(student_mastery)

    old_mastery = student_mastery[concept]

    new_mastery = update_mastery(old_mastery, correct, difficulty)

    student_mastery[concept] = new_mastery

    print(
        f"Concept: {concept} | "
        f"Difficulty: {difficulty} | "
        f"Correct: {correct} | "
        f"Mastery: {old_mastery:.2f} -> {new_mastery:.2f}"
    )