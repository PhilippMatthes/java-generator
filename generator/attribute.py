import random

from generator.parameter import RandomizedNonFinalParameter, Parameter
from generator.visibility import RandomVisibility


class Attribute:
    def __init__(self, visibility, is_static, parameter):
        self.visibility = visibility
        self.is_static = is_static
        self.parameter = parameter

    def __str__(self):
        return "{visibility} {static}{parameter};".format(
            visibility=self.visibility,
            static="static " if self.is_static else "",
            parameter=self.parameter
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