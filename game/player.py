class Player:
    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name

    def to_dict(self):
        return {
            "card_id": self.card_id,
            "name": self.name
        }