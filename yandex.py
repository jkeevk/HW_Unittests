import requests

class YandexDisk():
    def __init__(self, token):
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "OAuth " + token
        }

    def create_folder(self, folder_name):
        params = {"path": folder_name}
        response = requests.put(self.base_url, headers=self.headers, params=params)
        return response

    def delete_folder(self, folder_name):
        params = {"path": folder_name}
        response = requests.delete(self.base_url, headers=self.headers, params=params)
        return response

    def check_folder(self, folder_name):
        params = {"path": folder_name}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        return response

