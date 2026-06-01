from unittest.mock import patch

def test_MainShouldExecuteUseCase():
    with (
        patch("transactions_ms.app.main.RabbitMQTransactionPublisher") as publisher_cls,
        patch("transactions_ms.app.main.RegisterTransaction") as use_case_cls,
        patch("transactions_ms.app.main.Transaction") as transaction_cls,
    ):
        use_case = use_case_cls.return_value
        from transactions_ms.app.main import main
        main()
        use_case.execute.assert_called_once()
