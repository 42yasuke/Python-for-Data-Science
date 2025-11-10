from abc import ABC, abstractmethod


class Character(ABC):
    """A Character base class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Character"""
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be a boolean")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """The Character die"""
        pass


class Stark(Character):
    """A Stark class inheriting from Character"""

    def die(self):
        """The Stark die"""
        self.is_alive = False


def main():
    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)
    except TypeError as te:
        print(f"TypeError: {te}")


if __name__ == "__main__":
    main()
