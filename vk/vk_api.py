import requests
import time
import json
from user_data.data_from_user import *
from .menu import *
from dbase.db import add_result

class VkApi:

    def __init__(self, token):
        self.token = token

    def reqGet(self, method, params=None, reply=0):
        _params = {'v': 5.21, 'access_token': self.token}
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

    def where_are_looking(self):
        about_city()
        choice = input('-> ')
        if choice == '0':
            city_number = self.reqGet('users.get', params={'fields': 'city'})[
                'response'][0]['city']['id']
            city_name = self.reqGet('users.get', params={'fields': 'city'})[
                'response'][0]['city']['title']
            print(f'поиск по городу {city_name}')
        elif choice == '1':
            city_number = None
            print('поиск без ограничений')
        elif choice == 'q':
            print('выход')
            raise SystemExit
        else:
            print('введено неправильное значение, попробуйте еще раз')
            return self.where_are_looking()
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

    def get_photo_links(self, applicant_id):
        photos_data = self.reqGet('photos.get', params={
            'owner_id': applicant_id, 'album_id': 'profile', 'extended': '1', 'photo_sizes': '1'})
        prof_photos = {}
        for photo in photos_data['response']['items']:
            link_and_likes = {photo['sizes'][0]
                              ['src']: photo['likes']['count']}
            prof_photos.update(link_and_likes)
        sorted_by_likes = [i for i in sorted(
            prof_photos.items(), key=lambda item: item[1], reverse=True)]
        photos_links = []
        for index, link in enumerate(sorted_by_likes):
            if index < 3:
                photos_links.append(link[0])
            else:
                break
        return photos_links

    def get_result(self, all_ids, data_search, to_json):
        ids_count = 0
        ids_10 = []
        for i in all_ids:
            if ids_count < 10:
                if i not in data_search:
                    ids_count += 1
                    data_search.append(i)
                    ids_10.append(i)
                elif i in data_search:
                    continue
            else:
                break
        for i in ids_10:
            to_json.update({f'https://vk.com/id{i}': self.get_photo_links(i)})
        about_json()
        choice = input('-> ')
        with open(f'{choice}.json', 'w') as f:
            json.dump(to_json, f)
        with open(f'{choice}.json') as f:
            result = json.load(f)
        return result

    def result(self, data_search):
        all_ids = self.applicants()
        to_json = {}
        result = self.get_result(all_ids, data_search, to_json)
        about_result()
        choice = choise()
        if choice == '0':
            return self.result(data_search)
        elif choice == '1':
            about_name()
            name = name_for_db()
            add_result(name, result)

    def app(self):
        welcome()
        data_search = []
        result = self.result(data_search)
        return result
