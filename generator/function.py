import random
import string

from generator.parameter import RandomizedParameter
from generator.type import RandomRandomizedType
from generator.visibility import RandomVisibility


class Function:
    def __init__(self, visibility, name, return_type, parameters):
        self._visibility = visibility
        self._name = name
        self._return_type = return_type
        self._parameters = parameters

    def __str__(self):
        formatted_parameters = ", ".join([str(p) for p in self._parameters])
        return """
        {visibility} {return_type} {name} ({formatted_parameters}) {{
            {return_statement}
        }}
        """.format(
            visibility=self._visibility,
            return_type=self._return_type,
            name=self._name,
            formatted_parameters=formatted_parameters,
            return_statement=self._return_type.return_statement,
        )


class RandomFunction(Function):
    def __init__(self, min_parameters=0, max_parameters=10):
        visibility = RandomVisibility()
        name = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        return_type = RandomRandomizedType()
        num_parameters = random.randint(min_parameters, max_parameters)
        parameters = [RandomizedParameter() for _ in range(num_parameters)]
        super().__init__(visibility, name, return_type, parameters)


if __name__ == "__main__":
    f = RandomFunction()
    print(f)
