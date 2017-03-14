from seat_suggestion import *
import unittest


class TestSeatSuggestion(unittest.TestCase):
    theater_json = ''
    rows = 0
    seats = 0
    booked = []
    theater = None
    seat_finder = None

    def setUp(self):
        self.theater_json = """{"rows" : ["A", "B"],
                    "seats": {"A": [1,2,3,4,5,6,7,8,9,10],
                              "B": [1,2,3,4,5,6,7,8,9,10]}} """
        self.rows, self.seats = rows_and_seats_from_json(self.theater_json)
        self.booked = ["B2", "B3", "B4", "B5"]
        self.theater = Theater(self.rows, self.seats, self.booked)
        self.seat_finder = SeatFinder(self.theater)

    def test_one_seat_is_allocated_near_the_front(self):
        self.assertTrue(self.seat_finder.suggest(1) in ["A5", "A6"])

    def test_theater_seat_is_booked(self):
        self.assertTrue(self.theater.is_booked('B3'))


if __name__ == '__main__':
    unittest.main()