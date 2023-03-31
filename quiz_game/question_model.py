""" BELOW: Model of a question. Using self method, that contains two parameter, text and answer."""
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
