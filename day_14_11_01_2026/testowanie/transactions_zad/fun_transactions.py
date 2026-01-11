# filtrowanie, mapowanie, sumowanie (reduce)

transactions = [
    {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
    {"id": 2, "type": "expense", "amount": 200, "currency": "USD"},
    {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
    {"id": 4, "type": "expense", "amount": 300, "currency": "USD"},
    {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
    {"id": 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
]


def filter_transactions(transactions, transaction_type):
    pass


def map_transactions(transactions, currency):
    pass


def reduce_transactions(transactions):
    pass


def process_transactions(transactions, transaction_type, currency):
    filtered = filter_transactions(transactions, transaction_type)
    mapped = map_transactions(filtered, currency)
    total = reduce_transactions(mapped)

    return total


if __name__ == '__main__':
    print(process_transactions(transactions, "expense", "EUR"))
