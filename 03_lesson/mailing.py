from address import Address

class Mailing:

    def __init__(self, to_address: Address, from_address: Address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return f"Отправление {self.track} из {self.from_address}, в {self.to_address}, стоимость {self.cost} рублей"