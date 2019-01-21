import random
import string

from generator.attribute import RandomAttribute
from generator.function import RandomFunction


class Class:
    def __init__(self, attributes, name, functions):
        self._attributes = [str(a) for a in attributes]
        self._name = name
        self._functions = [str(f) for f in functions]

    @property
    def name(self):
        return self._name

    def __str__(self):
        formatted_attributes = "\n".join(self._attributes)
        formatted_functions = "\n".join(self._functions)
        return """
        class {name} {{
        
            {formatted_attributes}
            
            {formatted_functions}
            
        }}
        
        """.format(
            name=self._name,
            formatted_attributes=formatted_attributes,
            formatted_functions=formatted_functions
        )


class RandomClass(Class):
    def __init__(
            self,
            min_num_functions=0,
            max_num_functions=10,
            min_num_attribs=0,
            max_num_attribs=10
    ):
        attributes = [RandomAttribute()
                      for _ in range(random.randint(min_num_attribs, max_num_attribs))]
        name = "".join(
            random.choice(string.ascii_uppercase) for _ in range(10)
        )
        functions = [RandomFunction()
                     for _ in range(random.randint(min_num_functions, max_num_functions))]
        super().__init__(attributes, name, functions)


if __name__ == "__main__":
    c = RandomClass()
    print(c)