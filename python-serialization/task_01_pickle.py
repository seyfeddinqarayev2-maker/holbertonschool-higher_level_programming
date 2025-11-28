#!/usr/bin/python3
"""Script to test pickling and unpickling a CustomObject."""

import pickle


class CustomObject:
    """Custom class with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a pickle file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (OSError, pickle.PickleError, EOFError):
            return None


# -------------------------------
# Example usage as a script
# -------------------------------
if __name__ == "__main__":
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize to file
    obj.serialize("object.pkl")

    # Deserialize from file
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    if new_obj:
        new_obj.display()
    else:
        print("Failed to deserialize the object.")
