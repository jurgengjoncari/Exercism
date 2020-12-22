import re


class PhoneNumber:
    def __init__(self, number):
        self.number = number
        self.number = ''.join(re.findall(r'\d', self.number))
        if len(self.number) not in {10, 11}:
            raise ValueError("Wrong length")
        else:
            if len(self.number) == 11:
                if self.number[0] != "1":
                    raise ValueError("The country code is not 1")
                self.number = self.number.removeprefix("1")
            self.area_code = self.number[:3]
            self.exchange_code = self.number[3:6]
            if bool({self.area_code[0], self.exchange_code[0]} & {"0", "1"}):
                raise ValueError("Invalid Area / Exchange code")

    def pretty(self):
        return "({})-{}-{}".format(self.number[:3], self.number[3:6], self.number[6:])
