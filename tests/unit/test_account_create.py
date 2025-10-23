from src.account import Account


class TestAccount:
    def test_init_sets_first_and_last_name(self):
        account = Account("John", "Doe", "11111111111")
        assert account.first_name == "John"
        assert account.last_name == "Doe"

    def test_initial_balance_is_zero(self):
        account = Account("John", "Doe", "11111111111")
        assert account.balance == 0

    def test_pesel_length_is_11_for_valid_pesel(self):
        account = Account("John", "Doe", "11111111111")
        assert len(account.pesel) == 11

    def test_invalid_pesel_sets_pesel_to_invalid(self):
        account = Account("John", "Doe", "11111")
        assert account.pesel == "Invalid"

    def test_balance_updated_when_promo_code_applied(self):
        account = Account("John", "Doe", "03211111111", "PROM_AZA")
        assert account.balance == 50

    def test_promo_age_doesnt_work_when_age_not_eligible(self):
        account = Account("John", "Doe", "59111111111", "PROM_AZA")
        assert account.balance == 0