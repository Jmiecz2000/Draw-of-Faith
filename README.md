# Draw of Faith

A strategic card fusion battle game built with Python and Tkinter.

## 🎮 Game Overview

Draw of Faith is a unique card game where players battle using standard playing cards with special fusion mechanics. Players can combine cards to create powerful Fusion Cards with enhanced abilities.

## ✨ Features

- **Fusion Mechanics**: Combine cards to create powerful fusion combinations
- **Multiple Fusion Types**: 
  - Royal Fusion (King, Queen, Jack)
  - Five of a Kind (5+ cards of same suit)
  - Straight Flush (5+ consecutive cards of same suit)
- **AI Opponent**: Play against an intelligent computer opponent
- **Turn-based Combat**: Strategic battle system
- **Beautiful GUI**: Clean, intuitive interface built with Tkinter

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually included with Python)

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/draw-of-faith.git
   cd draw-of-faith
   ```

2. **Run the game**:
   ```bash
   python src/main.py
   ```

### Alternative Installation

If you prefer to install as a package:

```bash
pip install -e .
```

Then run:
```bash
python -m draw_of_faith
```

## 🎯 How to Play

### Basic Rules

1. **Starting Hand**: Each player starts with 5 cards
2. **Turn Structure**: 
   - Summon a card or fusion to your field
   - Battle phase (automatic)
   - Draw new cards if available

3. **Winning**: Player with the most points when all cards are played wins

### Fusion Combinations

- **Royal Fusion**: Combine King, Queen, and Jack for "Royal Knight" fusion
- **Five of a Kind**: Combine 5+ cards of the same suit for "Elemental Avatar" fusion  
- **Straight Flush**: Combine 5+ consecutive cards of same suit for "Chrono Blade" fusion

### Combat

Cards battle automatically based on their values:
- Ace = 14, King = 13, Queen = 12, Jack = 11, 10 = 10... 2 = 2
- Fusion cards get bonus points added to their strongest component card
- Winner gains 1 point, loser's card goes to graveyard

## 🏗️ Project Structure

```
draw-of-faith/
├── src/
│   ├── main.py              # Entry point
│   ├── models/
│   │   ├── card.py          # Card and FusionCard classes
│   │   └── player.py        # Player class and game logic
│   ├── game/
│   │   └── deck.py          # Deck management
│   └── gui/
│       └── interface.py     # GUI implementation
├── tests/                   # Unit tests
├── README.md
└── requirements.txt
```

## 🧪 Development

### Running Tests

```bash
python -m pytest tests/
```

### Code Style

This project follows PEP 8 style guidelines. Format code with:

```bash
black src/
flake8 src/
```

## 🛠️ Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 Future Features

- [ ] Multiplayer support
- [ ] Custom card designs
- [ ] More fusion combinations
- [ ] Difficulty levels for AI
- [ ] Tournament mode
- [ ] Save/load game state
- [ ] Sound effects and animations
- [ ] Deck customization

## 🐛 Known Issues

- AI strategy could be more sophisticated
- Limited fusion combinations currently available
- No save/load functionality yet

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic card games and modern fusion mechanics
- Built with Python's excellent Tkinter library
- Thanks to the Python community for excellent documentation

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/draw-of-faith/issues) page
2. Create a new issue if your problem isn't already reported
3. Include your Python version and operating system in bug reports

---

**Have fun playing Draw of Faith! May the cards be ever in your favor! 🃏✨**
