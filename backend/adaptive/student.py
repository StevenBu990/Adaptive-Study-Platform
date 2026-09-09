
class StudentState:
    def __init__(self, mastery: dict[str, float]):
        self.mastery = mastery
        self.seen_questions = set()

    def mark_question_seen(self, question_id: int):
        self.seen_questions.add(question_id)

    def has_seen_question(self, question_id: int) -> bool:
        return question_id in self.seen_questions