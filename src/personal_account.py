from src.account import BaseAccount


class PersonalAccount(BaseAccount):
    def __init__(self, first_name, last_name, pesel, promo_code=None):
        super().__init__(balance=0, express_fee=1)
        self.first_name = first_name
        self.last_name = last_name
        if len(pesel) != 11:
            self.pesel = "Invalid"
        else:
            self.pesel = pesel

        if promo_code is not None and "PROM" in promo_code:
            if self.is_promo_age_eligible():
                self.balance += 50

    def checking_age(self):
        """
        Extract birth year from PESEL.
        Returns int year (e.g. 1985) or None if PESEL invalid / cannot determine.
        """
        if (
            not isinstance(self.pesel, str)
            or len(self.pesel) != 11
            or not self.pesel.isdigit()
        ):
            return None
        yy = int(self.pesel[0:2])
        mm = int(self.pesel[2:4])

        # determine century from month encoding per PESEL rules
        if 1 <= mm <= 12:
            year = 1900 + yy
        elif 21 <= mm <= 32:
            year = 2000 + yy
        elif 41 <= mm <= 52:
            year = 2100 + yy
        elif 61 <= mm <= 72:
            year = 2200 + yy
        elif 81 <= mm <= 92:
            year = 1800 + yy
        else:
            return None

        return year

    def is_promo_age_eligible(self):
        # Promo eligibility: born after 1960.
        birth_year = self.checking_age()
        if birth_year is None:
            return False
        return birth_year > 1960

    def submit_for_loan(self, amount):
        if len(self.historia) < 5:
            return False

        if self.historia[-1] >= 0 and self.historia[-2] >= 0 and self.historia[-3] >= 0:
            self.balance += amount
            return True
        else:
            sum = self.historia[-1]
            +self.historia[-2]
            +self.historia[-3]
            +self.historia[-4]
            +self.historia[-5]
            if sum > amount:
                self.balance += amount
                return True
            else:
                return False
