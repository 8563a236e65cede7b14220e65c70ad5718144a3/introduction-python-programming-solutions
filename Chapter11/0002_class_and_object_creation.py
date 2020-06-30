"""
Program 11.1
Illustrate Class and Object Creation
"""


class Mobile:
    def __init__(self):
        print("This message is from Constructor Method")

    def receive_message(self):
        self.do_nothing()
        print("Receive message using Mobile")
        
    def send_message(self):
        self.do_nothing()
        print("Send message using Mobile")

    def do_nothing(self):
        pass


def main():
    nokia = Mobile()
    nokia.receive_message()
    nokia.send_message()


if __name__ == "__main__":
    main()
