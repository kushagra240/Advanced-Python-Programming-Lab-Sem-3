class Player:
    def __init__(self, player_name, jersey_number, runs):
        self.player_name = player_name
        self.jersey_number = jersey_number
        self.runs = runs

    def get_category(self):
        if self.runs >= 50:
            return "Excellent"
        elif self.runs >= 30:
            return "Good"
        return "Average"

    def __str__(self):
        return (
            f"Player Name: {self.player_name}, "
            f"Jersey Number: {self.jersey_number}, "
            f"Runs: {self.runs}, "
            f"Category: {self.get_category()}"
        )


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_players(self):
        print(f"\nPlayers in {self.name}:\n")
        if not self.players:
            print("No players added yet.")
            return
        for player in self.players:
            print(player)


def main():
    team = Team("Royal Strikers")

    team.add_player(Player("Aman", 7, 62))
    team.add_player(Player("Ravi", 18, 45))
    team.add_player(Player("Suhail", 11, 28))
    team.add_player(Player("Karan", 24, 54))

    team.display_players()


if __name__ == "__main__":
    main()
