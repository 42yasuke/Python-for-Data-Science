from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """"Representing a King, inheriting from Baratheon and Lannister."""
    def __init__(self, first_name: str, is_alive=True):
        """Init a King"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, value):
        """Set the eyes of the King"""
        self.eyes = value

    def get_eyes(self):
        """Get the eyes of the King"""
        return self.eyes

    def set_hairs(self, value):
        """Set the hairs of the King"""
        self.hairs = value

    def get_hairs(self):
        """Get the hairs of the King"""
        return self.hairs


def main():
    try:
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)
    except TypeError as te:
        print(f"TypeError: {te}")


if __name__ == "__main__":
    main()
