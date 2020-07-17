import sys
import os
sys.path.append(os.path('./user_data'))
sys.path.append(os.path('./dbase'))
sys.path.append(os.path('./vk'))
from vk.vk_api import VkApi
from vk.get_token import get_token_link

if __name__ == "__main__":
    print('-'*20)
    token_link = get_token_link()
    print(token_link)
    print('-'*20)

    result = VkApi(
        1102558, 'f839fd74f1ba06f8e74a820ddbd216666045a136230ff5e040266dff0afbdad18c87a2e0ba7df4d6a1fff')

    result.app()
