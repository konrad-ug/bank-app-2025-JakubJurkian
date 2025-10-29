from src.account import Account
from src.account import CompanyAccount


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


class TestTransfer:
    def test_receive_correct_amount(self):
        account = Account("John", "Doe", "03211111111")
        old_balance = account.balance
        x = 1000
        account.incoming_transfer(x)
        new_balance = account.balance
        assert (new_balance - old_balance) == x

    def test_send_correct_amount(self):
        account = Account("John", "Doe", "03211111111")
        x = 1000
        account.incoming_transfer(x)
        old_balance = account.balance
        account.outgoing_transfer(x)
        new_balance = account.balance
        assert (old_balance - x) == new_balance

    def test_cant_send_money_when_balance_not_enough(self):
        account = Account("John", "Doe", "03211111111")
        x = 1000
        account.incoming_transfer(x)
        expected_balance = account.balance

        account.outgoing_transfer(x + 1)

        assert account.balance == expected_balance


class TestCompanyAccount:
    def test_init_sets_company_name(self):
        account = CompanyAccount("Drutex", "0123456789")
        assert account.company_name == "Drutex"

    def test_initial_balance_is_zero(self):
        account = CompanyAccount("Drutex", "0123456789")
        assert account.balance == 0

    def test_nip_length_is_10_for_valid_nip(self):
        account = CompanyAccount("Drutex", "0123456789")
        assert len(account.nip) == 10

    def test_invalid_nip_sets_nip_to_invalid(self):
        account = CompanyAccount("Drutex", "01234")
        assert account.nip == "Invalid"


class TestCompanyTransfer:
    def test_receive_correct_amount(self):
        account = CompanyAccount("Drutex", "0123456789")
        old_balance = account.balance
        x = 1000
        account.incoming_transfer(x)
        new_balance = account.balance
        assert (new_balance - old_balance) == x

    def test_send_correct_amount(self):
        account = CompanyAccount("Drutex", "0123456789")
        x = 1000
        account.incoming_transfer(x)
        old_balance = account.balance
        account.outgoing_transfer(x)
        new_balance = account.balance
        assert (old_balance - x) == new_balance

    def test_cant_send_money_when_balance_not_enough(self):
        account = CompanyAccount("Drutex", "0123456789")
        x = 1000
        account.incoming_transfer(x)
        expected_balance = account.balance

        account.outgoing_transfer(x + 1)

        assert account.balance == expected_balance


class TestTransferExpress:
    def test_express_transfer_takes_1_pln_from_balance_for_personal_account(self):
        account = Account("John", "Doe", "11111111111")
        old_balance = account.balance
        x = 1000
        account.incoming_transfer(x)
        account.outgoing_transfer_express(x)
        new_balance = account.balance
        assert new_balance == (old_balance - 1)

    def test_express_transfer_takes_5_pln_from_balance_for_company_account(self):
        account = CompanyAccount("Drutex", "0123456789")
        old_balance = account.balance
        x = 1000
        account.incoming_transfer(x)
        account.outgoing_transfer_express(x)
        new_balance = account.balance
        assert new_balance == (old_balance - 5)
