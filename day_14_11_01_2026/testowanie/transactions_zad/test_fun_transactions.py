import fun_transactions as ft


def test_map_transactions_usd():
    result = [1000, 200, 500, 300, 700, 0, 0]
    assert ft.map_transactions(ft.transactions, "USD") == result
    # test_fun_transactions.py::test_map_transactions_usd PASSED


# test_reduce
def test_reduce_transactions():
    assert ft.reduce_transactions([1000, 500, 700, 0]) == 2200
    # test_fun_transactions.py::test_reduce_transactions PASSED


def test_filter_transactions_income():
    expected_list = [
        {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
        {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
        {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
        {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
    ]

