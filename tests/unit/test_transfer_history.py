from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount


class TestTransferHistory:
    def test_valid_array_display(self):
        account = PersonalAccount("John", "Doe", "11111111111")
        account.incoming_transfer(500)
        account.outgoing_transfer_express(300)
        assert account.historia[0] == 500
        assert account.historia[1] == -300
        assert account.historia[2] == -1


class TestTransferExpress:
    def test_express_transfer_takes_1_pln_from_balance_for_personal_account(self):
        account = PersonalAccount("John", "Doe", "11111111111")
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
