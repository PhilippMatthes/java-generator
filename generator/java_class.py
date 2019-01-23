import random
import string

from generator.attribute import RandomAttribute
from generator.function import RandomFunction


class Class:
    def __init__(self, attributes, name, functions):
        self.attributes = attributes
        self.name = name
        self.functions = functions

    @property
    def constructor(self):
        non_static_attribs = [a for a in self.attributes if not a.is_static]
        constructor_params = ", ".join([str(a.parameter) for a in non_static_attribs])
        constructor_assignments = "\n".join([
            "this.{attribute_name} = {attribute_name};".format(
                attribute_name=a.parameter.name
            ) for a in non_static_attribs
        ])
        return """
        {name} ({constructor_params}) {{
            {constructor_assignments}
        }}
        """.format(
            name=self.name,
            constructor_params=constructor_params,
            constructor_assignments=constructor_assignments
        )

    def __str__(self):
        formatted_attributes = "\n".join([str(a) for a in self.attributes])
        formatted_functions = "\n".join([str(f) for f in self.functions])
        return """
        class {name} {{
            {formatted_attributes}
            
            {constructor}
            
            {formatted_functions}
        }}
        
        """.format(
            name=self.name,
            formatted_attributes=formatted_attributes,
            constructor=self.constructor,
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