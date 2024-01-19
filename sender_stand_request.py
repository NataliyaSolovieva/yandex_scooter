import config
import requests
import data


def post_new_order():
    user_body = data.user_body
    return requests.post(config.URL_SERVICE + config.ORDER_CREATION,  # подставляем полный url
                         json=user_body)  # тут тело


track = post_new_order().json()
print(track)


def get_order():
    global track
    t = track
    return (requests.getcd
            (config.URL_SERVICE + config.RECEIVING_ORDER, params=t))


res = get_order()
print(res.status_code)
print(res.json())
