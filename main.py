from vk.vk_api import VkApi
from vk.get_token import get_token_link

if __name__ == "__main__":
    print('-'*20)
    token_link = get_token_link()
    print('-'*20)

    result = VkApi(
        'eshmargunov', '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008')

    result.app()
