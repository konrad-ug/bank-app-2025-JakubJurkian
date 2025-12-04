import pytest
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount


class TestLoan:
    @pytest.fixture()
    def personalAccount(self):
        account = PersonalAccount("John", "Doe", "11111111111")
        return account

    @pytest.fixture()
    def companyAccount(self):
        account = CompanyAccount("Drutex", "0123456789")
        return account

    def test_submit_loan_failed_last_3_transfers_not_ingoing(self, personalAccount):
        for _ in range(5):
            personalAccount.incoming_transfer(1000)

        personalAccount.outgoing_transfer(1000)
        isLoanAccepted = personalAccount.submit_for_loan(10000)
        assert isLoanAccepted == False

    def test_submit_loan_failed_sum_of_latest_5_transactions_is_less_or_equal_than_submit_for_loan(
        self, personalAccount
    ):
        for _ in range(6):
            personalAccount.incoming_transfer(1000)
        personalAccount.outgoing_transfer(1000)

        isLoanAccepted = personalAccount.submit_for_loan(5000)
        assert isLoanAccepted == False
