import pytest
from types import SimpleNamespace
from src.account_registry import AccountsRegistry

@pytest.fixture
def registry():
    return AccountsRegistry()

@pytest.mark.parametrize("pesel", ["11111111111", "22222222222", "33333333333"])
def test_add_and_find_by_pesel(registry, pesel):
    acct = SimpleNamespace(pesel=pesel, owner="Test")
    registry.add_account(acct)
    found = registry.find_by_pesel(pesel)
    assert found is acct

def test_all_accounts_and_count(registry):
    a1 = SimpleNamespace(pesel="100", owner="A")
    a2 = SimpleNamespace(pesel="200", owner="B")
    registry.add_account(a1)
    registry.add_account(a2)

    all_accts = registry.all_accounts()
    assert len(all_accts) == 2
    assert registry.count() == 2
    assert a1 in all_accts and a2 in all_accts

def test_find_by_pesel_not_found(registry):
    registry.add_account(SimpleNamespace(pesel="999", owner="X"))
    assert registry.find_by_pesel("no-such-pesel") is None