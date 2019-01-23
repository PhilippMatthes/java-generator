import random


class Visibility:
    def __init__(self, visibility):
        self.visibility = visibility

    def __str__(self):
        return self.visibility


class PublicVisibility(Visibility):
    def __init__(self):
        super().__init__("public")


class PrivateVisibility(Visibility):
    def __init__(self):
        super().__init__("private")


class NoVisibility(Visibility):
    def __init__(self):
        super().__init__("")


class ProtectedVisibility(Visibility):
    def __init__(self):
        super().__init__("protected")


class RandomVisibility(Visibility):
    def __init__(self):
        visibilities = [PublicVisibility, PrivateVisibility, NoVisibility, ProtectedVisibility]
        random.shuffle(visibilities)
        random_visibility = visibilities[0]()
        visibility = random_visibility.visibility
        super().__init__(visibility)


if __name__ == "__main__":
    random_vis = RandomVisibility()
    print(random_vis.visibility)

