import requests
import time
from data_from_user import from_ages, to_ages, status, gender
from menu import about_city, about_status, about_fromAges, about_gender, about_toAges, about_counts, about_not_10_counts

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
            raise SystemExit
        else:
            print('введено неправильное значение, попробуйте еще раз')
            self.where_are_looking()
        return city_number

    def pair_search(self):
        params = {}
        about_gender()
        gender_data = gender()
        gender_dict = dict(sex=gender_data)
        params.update(gender_dict)
        about_fromAges()
        from_ages_data = from_ages()
        from_ages_dict = dict(age_from=from_ages_data)
        params.update(from_ages_dict)
        about_toAges()
        to_ages_data = to_ages()
        to_ages_dict = dict(age_to=to_ages_data)
        params.update(to_ages_dict)
        photo_data = dict(has_photo=1)
        params.update(photo_data)
        city_number = self.where_are_looking()
        city_dict = dict(city=city_number)
        about_status()
        status_data = status()
        if status_data == '0':
            status_dict = dict(status=1)
            params.update(status_dict)
            if city_number == None:
                not_married = self.reqGet('users.search', params=params)
                return not_married
            else:
                params.update(city_dict)
                not_married = self.reqGet('users.search', params=params)
                return not_married
        elif status_data == '1':
            status_dict = dict(status=6)
            params.update(status_dict)
            if city_number == None:
                actively_looking = self.reqGet('users.search', params=params)
                return actively_looking
            else:
                params.update(city_dict)
                actively_looking = self.reqGet('users.search', params=params)
                return actively_looking
        elif status_data == 'q':
            print('выход')
            raise SystemExit


    def applicants(self):
        applicants_data = self.pair_search()
        print(applicants_data)
        if applicants_data['response']['count'] == 0:
            about_counts()
            return self.applicants()
        elif applicants_data['response']['count'] < 10:
            about_not_10_counts(), print(applicants_data['response']['count'])
            applicants_ids_data = []
            for index, applicant_info in enumerate(applicants_data['response']['items']):
                if index != applicants_data['response']['count']:
                    applicants_ids_data.append(applicant_info['id'])
                elif index == applicants_data['response']['count']:
                    break
            if applicants_ids_data == []:
                about_counts()
                return self.applicants()
            else:
                return applicants_ids_data
        else:
            applicants_ids_data = []
            for index, applicant_info in enumerate(applicants_data['response']['items']):
                if index != 10:
                    applicants_ids_data.append(applicant_info['id'])
                elif index == 10:
                    break
            if applicants_ids_data == []:
                about_counts()
                return self.applicants()
            else:
                return applicants_ids_data