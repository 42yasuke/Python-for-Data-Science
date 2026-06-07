import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random string to be used as a student ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    """Generates a login name for the student."""
    return name[0].upper() + surname.lower()


@dataclass
class Student:
    """Student is a dataclass that represents a student with a name,
    surname, active status, login, and ID."""
    name: str
    surname: str
    active: bool = field(default=True, init=False)
    login: str = field(default="", init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Called after the dataclass initializer."""
        self.login = generate_login(self.name, self.surname)


def main():
    """Main function to create a student and print its details."""
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == "__main__":
    main()
