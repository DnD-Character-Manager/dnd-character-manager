class AbilityScore:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            self._value = value
        else:
            raise ValueError("Ability score must be an integer.")

    def get_modifier(self):
        return (self.value - 10) // 2


class AbilityScores:
    def __init__(self, strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10):
        self.strength = AbilityScore(strength)
        self.dexterity = AbilityScore(dexterity)
        self.constitution = AbilityScore(constitution)
        self.intelligence = AbilityScore(intelligence)
        self.wisdom = AbilityScore(wisdom)
        self.charisma = AbilityScore(charisma)

    def __str__(self):
        return (
            f"Strength: {self.strength.value} (Modifier: {self.strength.get_modifier()}), "
            f"Dexterity: {self.dexterity.value} (Modifier: {self.dexterity.get_modifier()}), "
            f"Constitution: {self.constitution.value} (Modifier: {self.constitution.get_modifier()}), "
            f"Intelligence: {self.intelligence.value} (Modifier: {self.intelligence.get_modifier()}), "
            f"Wisdom: {self.wisdom.value} (Modifier: {self.wisdom.get_modifier()}), "
            f"Charisma: {self.charisma.value} (Modifier: {self.charisma.get_modifier()})"
        )

    def get_abilities(self):
        return {
            'Strength': {'score': self.strength.value, 'modifier': self.strength.get_modifier()},
            'Dexterity': {'score': self.dexterity.value, 'modifier': self.dexterity.get_modifier()},
            'Constitution': {'score': self.constitution.value, 'modifier': self.constitution.get_modifier()},
            'Intelligence': {'score': self.intelligence.value, 'modifier': self.intelligence.get_modifier()},
            'Wisdom': {'score': self.wisdom.value, 'modifier': self.wisdom.get_modifier()},
            'Charisma': {'score': self.charisma.value, 'modifier': self.charisma.get_modifier()}
        }
