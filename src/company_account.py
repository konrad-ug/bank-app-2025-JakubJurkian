from src.account import BaseAccount


class CompanyAccount(BaseAccount):
    def __init__(self, company_name, nip):
        super().__init__(balance=0, express_fee=5)
        self.company_name = company_name
        self.nip = nip

        if len(nip) != 10:
            self.nip = "Invalid"

    def take_loan(self, amount):
        """
        Przyznaje kredyt firmowy jeśli:
        - saldo >= 2 * amount
        - w historii operacji istnieje przynajmniej jedna wychodząca operacja o wartości -1775
        Zwraca True jeśli przyznano kredyt i aktualizuje saldo, wpp. False.
        """
        # zabezpieczenie jeśli nie ma historii lub balance
        history = getattr(self, "history", [])
        balance = getattr(self, "balance", 0)

        has_zus_payment = any(op == -1775 for op in history)
        if balance >= 2 * amount and has_zus_payment:
            # Zwiększ saldo o kwotę kredytu
            self.balance = balance + amount
            return True
        return False