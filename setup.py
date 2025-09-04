import tkinter as tk
from tkinter import messagebox
import random

# --- Card Classes ---
class Card:
    def init(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.position = 'attack'

    def value(self):
        hierarchy = {'A':14, 'K':13, 'Q':12, 'J':11,
                     '10':10, '9':9, '8':8, '7':7,
                     '6':6, '5':5, '4':4, '3':3, '2':2}
        return hierarchy[self.rank]

    def str(self):
        return f"{self.rank}{self.suit}"

class FusionCard(Card):
    def init(self, name, base_cards, bonus=2):
        super().init(rank="Fusion", suit="★")
        self.name = name
        self.base_cards = base_cards
        self.bonus = bonus

    def value(self):
        return max(card.value() for card in self.base_cards) + self.bonus

    def str(self):
        return f"{self.name}★"

# --- Player Class ---
class Player:
    def init(self, name, is_ai=False):
        self.name = name
        self.hand = []
        self.field = []
        self.graveyard = []
        self.points = 0
        self.is_ai = is_ai

    def draw_card(self, deck):
        if deck:
            self.hand.append(deck.pop())

    def summon(self):
        if not self.hand:
            return "None", []

        ranks = [card.rank for card in self.hand]
        suits = [card.suit for card in self.hand]
        values = sorted([card.value() for card in self.hand])

        # Royal Fusion
        if all(r in ranks for r in ['K', 'Q', 'J']):
            fusion_cards = [card for card in self.hand if card.rank in ['K', 'Q', 'J']]
            for card in fusion_cards:
                self.hand.remove(card)
            fusion = FusionCard("Royal Knight", fusion_cards)
            self.field.append(fusion)
            return "Royal Fusion", [fusion]

        # Five of a Kind
        if len(set(suits)) == 1 and len(self.hand) >= 5:
            fusion_cards = self.hand[:5]
            for card in fusion_cards:
                self.hand.remove(card)
            fusion = FusionCard("Elemental Avatar", fusion_cards)
            self.field.append(fusion)
            return "Five of a Kind", [fusion]

        # Straight Flush
        if len(set(suits)) == 1 and values[:5] == list(range(values[0], values[0]+5)):
            fusion_cards = self.hand[:5]
            for card in fusion_cards:
                self.hand.remove(card)
            fusion = FusionCard("Chrono Blade", fusion_cards)
            self.field.append(fusion)
            return "Straight Flush", [fusion]

        # Regular summon
        card = self.hand.pop(0)
        self.field.append(card)
        return "Summon", [card]

    def battle(self, opponent):
        if self.field and opponent.field:
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
        return "No battle occurred."

# --- Deck Creation ---
def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    deck = [Card(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# --- GUI Class ---
class DrawOfFaithGUI:
    def init(self, root):
        self.root = root
        self.root.title("Draw of Faith")
        self.deck = create_deck()
        self.player = Player("Jakub")
        self.ai = Player("AI", is_ai=True)
        self.turn = 1

        for _ in range(5):
            self.player.draw_card(self.deck)
            self.ai.draw_card(self.deck)

        self.build_layout()
        self.render_all()

    def build_layout(self):
        self.ai_field_frame = tk.LabelFrame(self.root, text="AI Field", padx=10, pady=5)
        self.ai_field_frame.pack(pady=5)

        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.pack()

        self.fusion_frame = tk.LabelFrame(self.middle_frame, text="Fusion Zone", padx=10, pady=5)
        self.fusion_frame.grid(row=0, column=0, padx=10)

        self.ai_graveyard_frame = tk.LabelFrame(self.middle_frame, text="AI Graveyard", padx=10, pady=5)
        self.ai_graveyard_frame.grid(row=0, column=1, padx=10)

        self.player_graveyard_frame = tk.LabelFrame(self.middle_frame, text="Player Graveyard", padx=10, pady=5)
        self.player_graveyard_frame.grid(row=0, column=2, padx=10)

        self.player_field_frame = tk.LabelFrame(self.root, text="Player Field", padx=10, pady=5)
        self.player_field_frame.pack(pady=5)

        self.hand_frame = tk.LabelFrame(self.root, text="Your Hand", padx=10, pady=5)
        self.hand_frame.pack(pady=5)

        self.status = tk.Label(self.root, text="Your Turn", font=("Arial", 14))
        self.status.pack()

        self.score_label = tk.Label(self.root, text="Score: Jakub 0 - AI 0", font=("Arial", 12))
        self.score_label.pack()

        self.turn_label = tk.Label(self.root, text="Turn: 1", font=("Arial", 12))
        self.turn_label.pack()

        self.combo_log = tk.Text(self.root, height=6, width=60, state='disabled', bg="
#f0f0f0")
        self.combo_log.pack(pady=10)

    def render_all(self):
        self.render_zone(self.ai_field_frame, self.ai.field, "red")
        self.render_zone(self.player_field_frame, self.player.field, "blue")
        self.render_zone(self.hand_frame, self.player.hand, "white", clickable=True)
        self.render_zone(self.ai_graveyard_frame, self.ai.graveyard, "gray")
        self.render_zone(self.player_graveyard_frame, self.player.graveyard, "gray")

    def render_zone(self, frame, cards, color, clickable=False):
        for widget in frame.winfo_children():
            widget.destroy()
        for i, card in enumerate(cards):
            bg = "gold" if isinstance(card, FusionCard) else color
            lbl = tk.Label(frame, text=str(card), bg=bg, fg="black", font=("Arial", 12), width=10)
            if clickable:
                lbl.bind("<Button-1>", lambda e, i=i: self.summon_card(i))
            lbl.pack(side=tk.LEFT, padx=5)

    def summon_card(self, index):
        card = self.player.hand.pop(index)
        self.player.field.append(card)
        self.status.config(text=f"You summoned {card}")
        self.render_all()
        self.root.after(1000, self.ai_turn)

    def ai_turn(self):
        action, cards = self.ai.summon()
        self.status.config(text=f"AI performed {action}!")
        self.log_combo("AI", action, cards)
        self.render_all()
        self.root.after(1500, self.battle)

    def log_combo(self, player_name, fusion_type, cards):
        self.combo_log.config(state='normal')
        card_names = ', '.join(str(c) for c in cards)
        self.combo_log.insert(tk.END, f"Turn {self.turn}: {player_name} activated {fusion_type} with {card_names}\n")
        self.combo_log.config(state='disabled')

    def battle(self):
        result = self.player.battle(self.ai)
        self.score_label.config(text=f"Score: Jakub {self.player.points} - AI {self.ai.points}")
        self.turn += 1
        self.turn_label.config(text=f"Turn: {self.turn}")
        messagebox.showinfo("Battle", result)
        self.render_all()
        self.check_game_end()

    def check_game_end(self):
        if not self.player.hand and not self.ai.hand:
            winner = "Jakub" if self.player.points > self.ai.points else "AI"
            messagebox.showinfo("Game Over", f"{winner} wins the duel!")
            self.root.quit()

# --- Run the Game ---
if name == "main":
    root = tk.Tk()
    app = DrawOfFaithGUI(root)
    root.mainloop()
