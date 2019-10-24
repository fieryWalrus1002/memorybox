class Memory_Card:
    def __init__(self, question, answer, hint, rank):
        self.question = question
        self.answer = answer
        self.hint = hint
        self.rank = rank

        @property
        def print_question(question):
            return 'Q. {}'.format(self.question)

        @property
        def print_answer(answer):
            return 'A. {}'.format(self.answer)

        def __repr__(self):
            return "Q: {}, A: {}, Hint: {}, Rank: {}".format(self.question, self.answer, self.hint, self.rank)
