# https://docs.circuitpython.org/en/latest/shared-bindings/canio/index.html#canio.BusState
class BusState:
    pass  # TODO: enum?

# TODO: create CAN mock
# class CAN:
#     def __init__(self) -> None:
#         pass

# class Match(id: int, ...)

class Message:
    def __init__(self, id: int, data: bytes, extended: bool = False) -> None:
        self.id = id
        self.data = data
        self.extended = extended
