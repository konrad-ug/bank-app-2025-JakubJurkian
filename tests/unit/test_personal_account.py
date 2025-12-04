import pytest
from src.personal_account import PersonalAccount

@pytest.fixture()
def account():
    account = PersonalAccount("John", "Doe", "11111111111")
    return account

class TestAccount:    
    
    def test_init_sets_first_and_last_name(self, account):
        assert account.first_name == "John"
        assert account.last_name == "Doe"

    def test_initial_balance_is_zero(self, account):
        assert account.balance == 0

    def test_pesel_length_is_11_for_valid_pesel(self, account):
        assert len(account.pesel) == 11

    def test_invalid_pesel_sets_pesel_to_invalid(self):
        account = PersonalAccount("John", "Doe", "11111")
        assert account.pesel == "Invalid"

    def test_balance_updated_when_promo_code_applied(self):
        account = PersonalAccount("John", "Doe", "03211111111", "PROM_AZA")
        assert account.balance == 50

    def test_promo_age_doesnt_work_when_age_not_eligible(self):
        account = PersonalAccount("John", "Doe", "59111111111", "PROM_AZA")
        assert account.balance == 0

    def test_promo_age_doesnt_work_when_age_not_valid(self):
        account = PersonalAccount("John", "Doe", "9111111111", "PROM_AZA")
        assert account.balance == 0

    def test_promo_age_doesnt_work_when_pesel_not_valid(self):
        account = PersonalAccount("John", "Doe", "59001111111", "PROM_AZA")
        assert account.balance == 0


class TestTransfer:
    def test_receive_correct_amount(self, account):
        old_balance = account.balance
        x = 1000
        account.incoming_transfer(x)
        new_balance = account.balance
        assert (new_balance - old_balance) == x

    def test_send_correct_amount(self, account):
        x = 1000
        account.incoming_transfer(x)
        old_balance = account.balance
        account.outgoing_transfer(x)
        new_balance = account.balance
        assert (old_balance - x) == new_balance

    def test_cant_send_money_when_balance_not_enough(self, account):
        x = 1000
        account.incoming_transfer(x)
        expected_balance = account.balance

        account.outgoing_transfer(x + 1)

        assert account.balance == expected_balance