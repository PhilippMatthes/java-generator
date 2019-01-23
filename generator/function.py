import random
import string

from generator.parameter import RandomizedParameter
from generator.type import RandomRandomizedType
from generator.visibility import RandomVisibility


class Function:
    def __init__(self, visibility, name, return_type, body, parameters):
        self.visibility = visibility
        self.name = name
        self.return_type = return_type
        self.body = body
        self.parameters = parameters

    def __str__(self):
        formatted_parameters = ", ".join([str(p) for p in self.parameters])
        return """
        {visibility} {return_type} {name} ({formatted_parameters}) {{
            {body}
        }}
        """.format(
            visibility=self.visibility,
            return_type=self.return_type.return_type,
            name=self.name,
            formatted_parameters=formatted_parameters,
            body=self.body,
        )


class RandomFunction(Function):
    def __init__(self, min_parameters=0, max_parameters=10):
        visibility = RandomVisibility()
        name = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        return_type = RandomRandomizedType()
        body = return_type.return_statement
        num_parameters = random.randint(min_parameters, max_parameters)
        parameters = [RandomizedParameter() for _ in range(num_parameters)]
        super().__init__(visibility, name, return_type, body, parameters)


if __name__ == "__main__":
    f = RandomFunction()
    print(f)
