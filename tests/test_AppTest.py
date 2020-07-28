import unittest
import requests
import sys
import os
from unittest.mock import patch
sys.path.append(os.path.abspath('./vk'))
from vk.vk_api import VkApi

class AppTest(unittest.TestCase):
    def setUp(self):
        self.token = 'f839fd74f1ba06f8e74a820ddbd216666045a136230ff5e040266dff0afbdad18c87a2e0ba7df4d6a1fff'
        self.test = VkApi(self.token)

    def test_token_valid_and_info_taked(self):
        result = self.test.reqGet('account.getProfileInfo')
        self.assertGreater(result['response']['id'], 0)

    def test_create_file(self):
        directory = './'
        files = os.listdir(directory)
        json = [i for i in files if i.endswith('.json')] 
        if json[0] in files:
            result = True
        else:
            result = False
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()