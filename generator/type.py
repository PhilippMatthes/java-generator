import random
import string


class Type:
    def __init__(self):
        self._return_statement = None
        self._return_type = None

    @property
    def return_statement(self):
        return self._return_statement

    def __str__(self):
        return self._return_type


class RandomizedType(Type):
    def __init__(self):
        super().__init__()
        self._randomized_value = None

    @property
    def randomized_value(self):
        return self._randomized_value


class VoidType(Type):
    def __init__(self):
        super().__init__()
        self._return_statement = "return;"
        self._return_type = "void"


class StringType(RandomizedType):
    def __init__(self):
        super().__init__()
        self._randomized_value = ''.join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        self._return_statement = "return \"{}\";".format(self._randomized_value)
        self._return_type = "String"


class IntegerType(RandomizedType):
    def __init__(self):
        super().__init__()
        self._randomized_value = random.randint(0, 1337)
        self._return_statement = "return {};".format(self._randomized_value)
        self._return_type = "Integer"


class RandomType(Type):
    def __init__(self):
        super().__init__()
        types = [VoidType, StringType, IntegerType]
        random.shuffle(types)
        random_type = types[0]()
        self._return_statement = random_type.return_statement
        self._return_type = str(random_type)


class RandomRandomizedType(Type):
    def __init__(self):
        super().__init__()
        types = [StringType, IntegerType]
        random.shuffle(types)
        random_type = types[0]()
        self._return_statement = random_type.return_statement
        self._return_type = str(random_type)


if __name__ == "__main__":
    r = RandomType()
    print(r)
    print(r.return_statement)

