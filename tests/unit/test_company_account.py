import pytest
from src.company_account import CompanyAccount

@pytest.fixture()
def account():
    account = CompanyAccount("Drutex", "0123456789")
    return account

class TestCompanyAccount:    
    def test_init_sets_company_name(self, account):
        assert account.company_name == "Drutex"

    def test_initial_balance_is_zero(self, account):
        assert account.balance == 0

    def test_nip_length_is_10_for_valid_nip(self, account):
        assert len(account.nip) == 10

    def test_invalid_nip_sets_nip_to_invalid(self, account):
        account = CompanyAccount("Drutex", "01234")
        assert account.nip == "Invalid"
        

class TestCompanyTransfer:
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