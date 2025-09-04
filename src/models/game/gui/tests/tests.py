# tests/test_card.py
"""Tests for card models."""

import unittest
from src.models.card import Card, FusionCard


class TestCard(unittest.TestCase):
    """Test cases for the Card class."""
    
    def test_card_creation(self):
        """Test basic card creation."""
        card = Card('A', '♠')
        self.assertEqual(card.rank, 'A')
        self.assertEqual(card.suit, '♠')
        self.assertEqual(card.position, 'attack')
    
    def test_card_value(self):
        """Test card value calculation."""
        ace = Card('A', '♠')
        king = Card('K', '♠')
        two = Card('2', '♠')
        
        self.assertEqual(ace.value(), 14)
        self.assertEqual(king.value(), 13)
        self.assertEqual(two.value(), 2)
    
    def test_card_str(self):
        """Test string representation."""
        card = Card('Q', '♥')
        self.assertEqual(str(card), 'Q♥')


class TestFusionCard(unittest.TestCase):
    """Test cases for the FusionCard class."""
    
    def test_fusion_card_creation(self):
        """Test fusion card creation."""
        base_cards = [Card('K', '♠'), Card('Q', '♠'), Card('J', '♠')]
        fusion = FusionCard("Royal Knight", base_cards)
        
        self.assertEqual(fusion.name, "Royal Knight")
        self.assertEqual(len(fusion.base_cards), 3)
        self.assertEqual(fusion.bonus, 2)
    
    def test_fusion_card_value(self):
        """Test fusion card value calculation."""
        base_cards = [Card('K', '♠'), Card('Q', '♠'), Card('J', '♠')]
        fusion = FusionCard("Royal Knight", base_cards)
        
        # Should be max value (13) + bonus (2) = 15
        self.assertEqual(fusion.value(), 15)


if __name__ == '__main__':
    unittest.main()


# tests/test_player.py
"""Tests for player model."""

import unittest
from src.models.player import Player
from src.models.card import Card
from src.game.deck import create_deck


class TestPlayer(unittest.TestCase):
    """Test cases for the Player class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.player = Player("Test Player")
        self.ai = Player("AI", is_ai=True)
        self.deck = create_deck()
    
    def
