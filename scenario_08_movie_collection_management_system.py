class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def get_category(self):
        if self.rating >= 8.5:
            return "Hit"
        elif self.rating >= 6:
            return "Average"
        return "Flop"

    def __str__(self):
        return (
            f"Movie Name: {self.movie_name}, "
            f"Rating: {self.rating}, "
            f"Ticket Price: ₹{self.ticket_price}, "
            f"Category: {self.get_category()}"
        )


class Cinema:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print(f"\nMovies at {self.name}:\n")
        if not self.movies:
            print("No movies available.")
            return
        for movie in self.movies:
            print(movie)


def main():
    cinema = Cinema("CineWorld")

    cinema.add_movie(Movie("Inception", 8.8, 280))
    cinema.add_movie(Movie("The Avengers", 7.9, 240))
    cinema.add_movie(Movie("The Last Stand", 5.6, 180))
    cinema.add_movie(Movie("Interstellar", 9.2, 320))

    cinema.display_movies()


if __name__ == "__main__":
    main()
