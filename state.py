class Replacement:
    def __init__(self):
        self.approved = False
        self.state = Design()
        print(self, "initial_state")

    @property
    def get_state(self):
        return self.state

    @get_state.setter
    def set_state(self, state):
        self.state = state

    def approve(self, approved):
        self.state.approve(self, approved)


class ReplacementState:
    def approve(self, replacement, approved):
        pass


class Design(ReplacementState):
    def approve(self, replacement, approved):
        replacement.approved = approved
        if approved:
            replacement.set_state = Review()
            print(replacement, "design_approved")
        if not approved:
            print(replacement, "design_not_approved")


class Review(ReplacementState):
    def approve(self, replacement, approved):
        replacement.approved = approved
        if approved:
            replacement.set_state = Construction()
            print(replacement, "review_approved")
        if not approved:
            replacement.set_state = Design()
            print(replacement, "review_not_approved_back_to_design")


class Construction(ReplacementState):
    def approve(self, replacement, approved):
        replacement.approved = approved
        if approved:
            replacement.set_state = Finished()
            print(replacement, "construction_approved")


class Finished(ReplacementState):
    def approve(self, replacement, approved):
        pass


replacement = Replacement()
replacement.approve(True)
replacement.approve(True)
replacement.approve(True)
replacement.approve(True)
