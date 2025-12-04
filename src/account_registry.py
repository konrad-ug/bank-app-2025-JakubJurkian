# nowy plik
from typing import List, Optional

class AccountRegistry:
    """
    Prosty rejestr kont osobistych (in-memory).
    Przechowuje dowolne obiekty posiadające atrybut 'pesel'.
    """
    def __init__(self):
        self._accounts: List[object] = []

    def add_account(self, account) -> None:
        """Dodaje konto do rejestru."""
        self._accounts.append(account)

    def find_by_pesel(self, pesel: str) -> Optional[object]:
        """Zwraca pierwsze konto o podanym peselu lub None."""
        for acct in self._accounts:
            if getattr(acct, "pesel", None) == pesel:
                return acct
        return None

    def all_accounts(self) -> List[object]:
        """Zwraca listę wszystkich kont (referencję do listy)."""
        return list(self._accounts)

    def count(self) -> int:
        """Zwraca liczbę kont w rejestrze."""
        return len(self._accounts)