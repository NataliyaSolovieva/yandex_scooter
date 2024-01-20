# Наталья Соловьева, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_get_order():
    order = sender_stand_request.get_order(sender_stand_request.track)
    assert order.status_code == 200


