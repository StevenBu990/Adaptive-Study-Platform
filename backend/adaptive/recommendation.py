
masteries = {
    "linear_regression" : 0.85,
    "gradient_descent" : 0.35,
    "neural_networks" : 0.60
}

def recommend_question(masteries: dict) -> tuple[str, str]:
    concept = select_concept(masteries)
    difficulty = select_difficulty(masteries[concept])

    return concept, difficulty

def select_concept(masteries: dict) -> str:
    return min(masteries, key=masteries.get)

def select_difficulty(mastery: float) -> str:
    if mastery < 0.40:
        return "easy"
    elif mastery < 0.70:
        return "medium"
    else:
        return "hard"