"""
Tp 4
Polashi Dey
Excercice 1

Cette code est pour faire une classe et le modifier le message

"""


class Stringfoo:

    def __init__(self, message):
        self.message = message

    def set_string(self, sms):
        self.message = sms

    def print_string(self):
        print(self.message.upper())


stringfoo = Stringfoo("bébé")
stringfoo.set_string("enfant")
stringfoo.print_string()
