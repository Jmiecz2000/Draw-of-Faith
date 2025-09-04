"""Card models for Draw of Faith game."""


class Card:
    """Base card class representing a standard playing card."""
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.position = 'attack'

    def value(self):
        """Return the numerical value of the card for comparison."""
        hierarchy = {
            'A': 14, 'K': 13, 'Q': 12, 'J': 11,
            '10': 10, '9': 9, '8': 8, '7': 7,
            '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
        }
        return hierarchy[self.rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"


class FusionCard(Card):
    """Special fusion card created by combining multiple cards."""
    
    def __init__(self, name, base_cards, bonus=2):
        super().__init__(rank="Fusion", suit="★")
        self.name = name
        self.base_cards = base_cards
        self.bonus = bonus

    def value(self):
        """Return the value of the strongest base card plus bonus."""
        return max(card.value() for card in self.base_cards) + self.bonus

    def __str__(self):
        return f"{self.name}★"

    def __repr__(self):
        return f"FusionCard({self.name}, {len(self.base_cards)} cards)"
