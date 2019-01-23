import random
import string

from generator.type import RandomRandomizedType


class Parameter:
    def __init__(self, datatype, name, final=False):
        self.datatype = datatype
        self.name = name
        self.final = final

    def __str__(self):
        return "{final}{datatype} {name}".format(
            final="final " if self.final else "",
            datatype=self.datatype,
            name=self.name
        )


class RandomizedParameter(Parameter):
    def __init__(self):
        datatype = RandomRandomizedType()
        name = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        final = bool(random.getrandbits(1))
        super().__init__(datatype, name, final)


class RandomizedNonFinalParameter(Parameter):
    def __init__(self):
        datatype = RandomRandomizedType()
        name = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        final = False
        super().__init__(datatype, name, final)


if __name__ == "__main__":
    parameter = RandomizedParameter()
    print(parameter)
