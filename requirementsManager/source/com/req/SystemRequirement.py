class SystemRequirement:
    def __init__(self, id: int, text: str):
        # Unique number identifying a particular requirement
        self.id = id

        # The actual shall statement for the requirement.
        self.text = text



if __name__ == "__main__":
    print("Running SystemRequirement.py")