import AbilityScores

class Character:
    def __init__(self, name):
        self.name = name
        self.ability_scores = AbilityScores()

    def set_ability_scores(self, ability_scores):
        if isinstance(ability_scores, AbilityScores):
            self.ability_scores = ability_scores
        else:
            raise TypeError("Only AbilityScores instances can be assigned.")

 