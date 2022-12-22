class Request:
    def __init__(self, str_request):
        self._from = str_request.split(" ")[4]
        self._to = str_request.split(" ")[6]
        self._amount = str_request.split(" ")[1]
        self._product = str_request.split(" ")[2]

    def __repr__(self):
        return f"""from = {self._from},\nto = {self._to},\namount = {self._amount},\nproduct = {self._product}"""

    def from_(self):
        return self._from

    def to(self):
        return self._to

    def amount(self):
        return int(self._amount)

    def product(self):
        return self._product
