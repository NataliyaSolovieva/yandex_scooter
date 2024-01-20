import config
import requests
import data


def post_new_order():
    user_body = data.user_body
    return requests.post(config.URL_SERVICE + config.ORDER_CREATION,  # подставляем полный url
                         json=user_body)  # тут тело


track = post_new_order().json()
print(track)


def get_order(params):
    params = {"t": track["track"]}
    return requests.get(config.URL_SERVICE + config.RECEIVING_ORDER, params=params)


res = get_order(track)
print(res.status_code)
print(res.json())
