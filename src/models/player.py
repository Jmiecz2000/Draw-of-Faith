"""Player model for Draw of Faith game."""

from .card import FusionCard


class Player:
    """Represents a player in the Draw of Faith game."""
    
    def __init__(self, name, is_ai=False):
        self.name = name
        self.hand = []
        self.field = []
        self.graveyard = []
        self.points = 0
        self.is_ai = is_ai

    def draw_card(self, deck):
        """Draw a card from the deck to the player's hand."""
        if deck:
            self.hand.append(deck.pop())

    def summon(self):
        """
        Attempt to summon a card or fusion combination.
        Returns tuple of (action_name, cards_summoned).
        """
        if not self.hand:
            return "None", []

        ranks = [card.rank for card in self.hand]
        suits = [card.suit for card in self.hand]
        values = sorted([card.value() for card in self.hand])

        # Royal Fusion - King, Queen, Jack combo
        if all(r in ranks for r in ['K', 'Q', 'J']):
            fusion_cards = [card for card in self.hand if card.rank in ['K', 'Q', 'J']]
            for card in fusion_cards:
                self.hand.remove(card)
            fusion = FusionCard("Royal Knight", fusion_cards)
            self.field.append(fusion)
            return "Royal Fusion", [fusion]

        # Five of a Kind - All same suit, 5+ cards
        if len(set(suits)) == 1 and len(self.hand) >= 5:
            fusion_cards = self.hand[:5]
            for card in fusion_cards:
                self.hand.remove(card)
            fusion = FusionCard("Elemental Avatar", fusion_cards)
            self.field.append(fusion)
            return "Five of a Kind", [fusion]

        # Straight Flush - Same suit, consecutive values
        if len(set(suits)) == 1 and len(values) >= 5:
            consecutive = self._find_consecutive_sequence(values, 5)
            if consecutive:
                fusion_cards = self.hand[:5]
                for card in fusion_cards:
                    self.hand.remove(card)
                fusion = FusionCard("Chrono Blade", fusion_cards)
                self.field.append(fusion)
                return "Straight Flush", [fusion]

        # Regular summon - play one card
        card = self.hand.pop(0)
        self.field.append(card)
        return "Summon", [card]

    def _find_consecutive_sequence(self, values, length):
        """Check if there's a consecutive sequence of given length in values."""
        if len(values) < length:
            return False
        return values[:length] == list(range(values[0], values[0] + length))

    def battle(self, opponent):
        """
        Battle against opponent's front card.
        Winner gains a point and sends loser's card to graveyard.
        """
        if not (self.field and opponent.field):
            return "No battle occurred."
        
        my_card = self.field[0]
        opp_card = opponent.field[0]
        
        if my_card.value() > opp_card.value():
            self.points += 1
            defeated = opponent.field.pop(0)
            opponent.graveyard.append(defeated)
            return f"{self.name} wins!"
        else:
            defeated = self.field.pop(0)
            self.graveyard.append(defeated)
            return f"{opponent.name} wins!"

    def __str__(self):
        return f"{self.name} (Points: {self.points})"

    def __repr__(self):
        return f"Player({self.name}, AI: {self.is_ai}, Points: {self.points})"
