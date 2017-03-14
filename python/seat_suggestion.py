import json


class SeatFinder:
    def __init__(self, theater):
        self.theater = theater

    def suggest(self, count):
        for label, row in self.theater._rows.items():
            if row.has_space(count):
                return "%s%d"%(
                    label,
                    row.middle_seats(count).number
                )

        return []


class Seat:
    booked = False

    def __init__(self, number, booked=False):
        self.number = number
        self.booked = booked

    def __repr__(self):
        return '<Seat num=%d, booked=%s>'%(
            self.number, self.booked
        )


class Row:
    seats = []
    name = None

    def __init__(self, name, seats):
        self.name = name
        self.seats = seats

    @property
    def _free_seats(self):
        return filter(lambda s: not s.booked, self.seats)

    def has_space(self, count):
        return len(self._free_seats) >= count

    def is_booked(self, label):
        return filter(lambda s: str(s.number) == label, self.seats)[0].booked

    def middle_seats(self, count):
        seats = self._free_seats
        offset = (len(seats) - count) / 2
        return seats[offset:].pop(count)

    def __repr__(self):
        return '<Row label=%s>' % self.name


class Theater:
    def __init__(self, rows, seats, booked):
        self._rows = {row: Row(name=row, seats=[
            Seat(s, "%s%d" % (row, s) in booked) for s in seats])
                    for row, seats in seats.items()
        }
        self.rows = rows
        self.seats = seats

    def is_booked(self, seat):
        rlabel, clabel = seat
        return self._rows[rlabel].is_booked(clabel)


def rows_and_seats_from_json(json_text):
    data = json.loads(json_text)
    rows = data["rows"]
    seats = data["seats"]
    return rows, seats


def theater_from_json(filename, booked):
    with open(filename) as f:
        rows, seats = rows_and_seats_from_json(f.read())
    return Theater(rows, seats, booked)