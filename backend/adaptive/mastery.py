
"""
Used to update the mastery function in the adaptive learning
"""


"""
Meanings
Guess: If the student doesn't know the concept, there's a 25% chance they guess correctly.
Slip: If the student does know the concept, there's a 10% chance they accidentally get it wrong.
LEARNING_PROBABILITY: 10% chance the interaction causes the student to learn the concept.
"""
# Initial heuristic parameters for MVP.
# Values should eventually be tuned using student performance data.
DIFFICULTY_PARAMETERS = {"easy" : {
                            "guess" : 0.30,
                            "slip" : 0.05
                            },
                        "medium" : {
                            "guess" : 0.25,
                            "slip" : 0.10,
                            },
                        "hard" : {
                            "guess" : 0.15,
                            "slip" : 0.15
                            }
                        }
LEARNING_PROBABILITY = 0.10

def update_mastery(current_mastery: float, correct: bool, difficulty: str) -> float:
    # Obtain difficulty parameters
    parameters = DIFFICULTY_PARAMETERS[difficulty]

    guess = parameters["guess"]
    slip = parameters["slip"]

    # Determine the probability of the observed answer
    if correct:
        p_answer_given_mastery = 1 - slip
        p_answer_given_no_mastery = guess
    else:
        p_answer_given_mastery = slip
        p_answer_given_no_mastery = 1 - guess

    # Calculate the probability of observing the answer
    # EQ: P(answer) = P(answer | mastered) * P(mastered) + P(answer | not mastered) * P(not mastered)
    p_answer = (p_answer_given_mastery * current_mastery + p_answer_given_no_mastery * (1 - current_mastery))

    # Bayes theorem: P(mastered | answer)
    posterior_mastery = (p_answer_given_mastery * current_mastery) / p_answer

    # Apply the learning
    updated_mastery = (posterior_mastery + (1 - posterior_mastery) * LEARNING_PROBABILITY)

    return updated_mastery
