class Athlete:
    def __init__(self, id, index, date, first_name, last_name, age, gender, address, sport, club, email, affiliated, result):
        self.id = id
        self.index = index
        self.date = date
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address
        self.sport = sport
        self.club = club
        self.email = email
        self.affiliated = affiliated
        self.result = result

    def __str__(self):
        return f"Athlete(id={self.id}, index={self.index}, date={self.date}, first_name={self.first_name}, last_name={self.last_name}, age={self.age}, gender={self.gender}, address={self.address}, sport={self.sport}, club={self.club}, email={self.email}, affiliated={self.affiliated}, result={self.result})"
