"""
Program 11.2
Illustrate Multiple Parameters in __init__() Method
"""


class Mobile:
    def __init__(self, name):
        self.mobile_name = name

    def receive_message(self):
        print(f"Receive message using {self.mobile_name} Mobile")

    def send_message(self):
        print(f"Send message using {self.mobile_name} Mobile")

    def do_nothing(self):
        pass


def main():
    nokia = Mobile("Nokia")
    nokia.receive_message()
    nokia.send_message()


if __name__ == "__main__":
    main()
