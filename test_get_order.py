import sender_stand_request


def test_get_order():
    order = sender_stand_request.get_order()
    assert order.status_code == 200


