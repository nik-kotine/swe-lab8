from rewards_ms.app.domain.TransactionReceived import TransactionReceived

def test_TransactionReceivedShouldStoreFields():
    transaction = TransactionReceived(amount = 100, user_id = "JOHNID")

    assert transaction.amount == 100
    assert transaction.user_id == "JOHNID"
