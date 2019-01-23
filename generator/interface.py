
from generator.function import Function
from generator.parameter import Parameter
from generator.type import NonNullableIntegerType, ObjectType
from generator.visibility import PublicVisibility


class Interface:
    def __init__(self, name, needed_functions, import_statement):
        self.name = name
        self.needed_functions = needed_functions
        self.import_statement = import_statement

    @property
    def implements_statement(self):
        return "implements {}".format(self.name)

    @property
    def implementation(self):
        return "\n".join(
            ["@Override {}".format(f) for f in self.needed_functions]
        )


class ComparableInterface(Interface):
    def __init__(self):
        name = "Comparable"
        return_type = NonNullableIntegerType()
        needed_functions = [
            Function(
                visibility=PublicVisibility(),
                name="compareTo",
                return_type=return_type,
                parameters=[Parameter(name="o", datatype=ObjectType())],
                body=return_type.return_statement
            ),
        ]
        super().__init__(name, needed_functions, "import java.lang.Comparable;")
