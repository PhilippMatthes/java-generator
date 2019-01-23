import random
import string


class Type:
    def __init__(self, return_statement, return_type):
        self.return_statement = return_statement
        self.return_type = return_type

    def __str__(self):
        return self.return_type


class RandomizedType(Type):
    def __init__(self, return_statement, return_type, randomized_value):
        self.randomized_value = randomized_value
        super().__init__(return_statement, return_type)


class VoidType(Type):
    def __init__(self):
        super().__init__("return;", "void")


class StringType(RandomizedType):
    def __init__(self):
        randomized_value = ''.join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        return_statement = "return \"{}\";".format(randomized_value)
        return_type = "String"
        super().__init__(return_statement, return_type, randomized_value)


class IntegerType(RandomizedType):
    def __init__(self):
        randomized_value = random.randint(0, 1337)
        return_statement = "return {};".format(randomized_value)
        return_type = "Integer"
        super().__init__(return_statement, return_type, randomized_value)


class RandomType(Type):
    def __init__(self):
        types = [VoidType, StringType, IntegerType]
        random.shuffle(types)
        random_type = types[0]()
        return_statement = random_type.return_statement
        return_type = str(random_type)
        super().__init__(return_statement, return_type)


class RandomRandomizedType(Type):
    def __init__(self):
        types = [StringType, IntegerType]
        random.shuffle(types)
        random_type = types[0]()
        return_statement = random_type.return_statement
        return_type = str(random_type)
        super().__init__(return_statement, return_type)


if __name__ == "__main__":
    r = RandomType()
    print(r)
    print(r.return_statement)

