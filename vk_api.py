import requests
import time

class VkApi:

    def __init__(self, ids, token):
        self.id = ids
        self.token = token


    def reqGet(self, method, params=None, reply=0):
        _params = {'v': 5.120, 'access_token': self.token}
        if params:
            _params.update(params)
        time.sleep(0.4)
        resp = requests.get(
            f'https://api.vk.com/method/{method}', params=_params)
        if resp.status_code != 200:
            return
        if 'error' in resp.json():
            data = resp.json()['error']
            if data['error_code'] == 30 or data['error_code'] == 18:
                return
            if data['error_code'] == 6:
                if reply > 3:
                    return
                time.sleep(2)
                res = self.reqGet(method, params, reply + 1)
                return res.json()
        return resp.json()
    

    def get_id(self):
        try:
            if self.id >= 0:
                user_id = self.id
        except TypeError:
            user_id = self.reqGet('utils.resolveScreenName', params={
                'screen_name': self.id})['response']['object_id']
        return user_id

    def where_are_looking(self):
        choice = input('-> ')
        if choice == '0':
            uid = self.get_id()
            city_number = self.reqGet('users.get', params={'fields': 'city', 'user_ids': uid})['response'][0]['city']['id']
            city_name = self.reqGet('users.get', params={'fields': 'city'})['response'][0]['city']['title']
            print(f'поиск по городу {city_name}')
        elif choice == '1':
            city_number = None
            print('поиск без ограничений')
        elif choice == 'q':
            print('выход')
            exit(0)
        else:
            print('введено неправильное значение, попробуйте еще раз')
            self.where_are_looking()
        return city_number