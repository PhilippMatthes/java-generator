import random

from generator.parameter import RandomizedNonFinalParameter
from generator.visibility import RandomVisibility


class Attribute:
    def __init__(self, visibility, static, parameter):
        self._visibility = visibility
        self._static = static
        self._parameter = parameter

    def __str__(self):
        return "{visibility} {static}{parameter};".format(
            visibility=self._visibility,
            static="static " if self._static else "",
            parameter=self._parameter
        )


class RandomAttribute(Attribute):
    def __init__(self):
        visibility = RandomVisibility()
        static = bool(random.getrandbits(1))
        parameter = RandomizedNonFinalParameter()
        super().__init__(visibility, static, parameter)


if __name__ == "__main__":
    a = RandomAttribute()
    print(a)