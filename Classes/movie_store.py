# Movie Store
# Manage video rentals and controls when videos are checked out, due to return,
# overdue fees and for added complexity create a summary of those accounts
# which are overdue for contact.

class Movie(object):
    
    current_id = 0

    def __init__(self, title, year, num_copies=0):
        Movie.current_id += 1
        self.id = Movie.current_id
        self.title = title
        self.year = year
        self.num_copies = num_copies

    def add_num_copies(self, num):
        self.num_copies += num

    def remove_num_copies(self, num):
        self.num_copies = max(0, self.num_copies - num)

class Rental(object):
    
    def __init__(self, movie, customer):
        self.movie = movie
        self.start_date = None
        self.end_date = None


class Customer(object):
    
    current_id = 0

    def __init__(self, name):
        Customer.current_id += 1
        self.id = Customer.current_id
        self.name = name
        self.active_rentals = []
        self.past_rentals = []

    def rent_movie(self, rental):
        self.active_rentals.append(rental)

    def deliver_movie(self, movie_id):
        for rental in self.active_rentals:
            if rental.movie.id == movie_id:
                self.past_rentals.append(rental)
                self.active_rentals.remove(rental)
                break


class MovieStore(object):

    def __init__(self):
        self.movies = []
        self.active_rentals = []
        self.past_rentals = []
        self.customers = []


