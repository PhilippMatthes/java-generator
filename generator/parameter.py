import random
import string

from generator.type import RandomRandomizedType


class Parameter:
    def __init__(self, type, name, final=False):
        self._type = type
        self._name = name
        self._final = final

    def __str__(self):
        return "{final}{type} {name}".format(
            final="final " if self._final else "",
            type=self._type,
            name=self._name
        )


class RandomizedParameter(Parameter):
    def __init__(self):
        type = RandomRandomizedType()
        name = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        final = bool(random.getrandbits(1))
        super().__init__(type, name, final)


class RandomizedNonFinalParameter(Parameter):
    def __init__(self):
        type = RandomRandomizedType()
        name = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        final = False
        super().__init__(type, name, final)


if __name__ == "__main__":
    parameter = RandomizedParameter()
    print(parameter)
