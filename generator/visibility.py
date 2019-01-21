import random


class Visibility:
    def __init__(self):
        self._visibility = None

    def __str__(self):
        return self._visibility


class PublicVisibility(Visibility):
    def __init__(self):
        super().__init__()
        self._visibility = "public"


class PrivateVisibility(Visibility):
    def __init__(self):
        super().__init__()
        self._visibility = "private"


class NoVisibility(Visibility):
    def __init__(self):
        super().__init__()
        self._visibility = ""


class ProtectedVisibility(Visibility):
    def __init__(self):
        super().__init__()
        self._visibility = "protected"


class RandomVisibility(Visibility):
    def __init__(self):
        super().__init__()
        visibilities = [PublicVisibility, PrivateVisibility, NoVisibility, ProtectedVisibility]
        random.shuffle(visibilities)
        random_visibility = visibilities[0]()
        self._visibility = random_visibility._visibility


if __name__ == "__main__":
    random_vis = RandomVisibility()
    print(random_vis._visibility)

